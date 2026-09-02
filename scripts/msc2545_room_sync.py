#!/usr/bin/env python3
"""Publish local sticker packs into a dedicated Matrix room as MSC2545 image
packs, the format Cinny / Nheko / FluffyChat (and every matrix-dart-sdk client)
actually read.

Mechanism (route A, cross-client-native):
  * one `im.ponies.room_emotes` STATE event per pack (state_key = pack short
    name) inside a dedicated, unencrypted "sticker vault" room;
  * one `im.ponies.emote_rooms` ACCOUNT-DATA event pointing at that room so the
    packs are enabled globally in every room.

The room is created once and reused (its id + per-pack hashes are cached in
scripts/msc2545-room-state.json). Idempotent: only packs whose content changed
are re-PUT; packs removed locally get an empty state event and are dropped from
emote_rooms.

Usage:
  .venv/bin/python scripts/msc2545_room_sync.py [--dry-run] [--force] \
      [--room-name NAME]
Exit codes: 0 ok / 1 partial or full failure / 2 token dead.
"""
import argparse
import asyncio
import hashlib
import json
import os
import sys
from urllib.parse import quote

from aiohttp import ClientError, ClientSession
from yarl import URL

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SP = os.path.join(ROOT, "web", "packs")
STATE_PATH = os.path.join(ROOT, "scripts", "msc2545-room-state.json")
CONFIG_PATH = os.path.join(ROOT, "config.json")

ROOM_EMOTES_TYPE = "im.ponies.room_emotes"      # MSC2545 m.room.image_pack (state)
EMOTE_ROOMS_TYPE = "im.ponies.emote_rooms"      # MSC2545 m.image_pack.rooms (account data)
ROOM_IMAGE_PACK_TYPE = "m.room.image_pack"      # MSC2545 stable state (v1.19)
IMAGE_PACK_ROOMS_TYPE = "m.image_pack.rooms"    # MSC2545 stable account data (v1.19)
DEFAULT_ROOM_NAME = "貼圖包倉庫 · Sticker Vault"


def q(s):
    return quote(str(s), safe="")


def load_config():
    with open(CONFIG_PATH, encoding="utf-8") as f:
        cfg = json.load(f)
    return cfg["homeserver"], cfg["user_id"], cfg["access_token"]


def build_pack_content(short: str, pack: dict) -> tuple[dict, int]:
    """Build one MSC2545 image-pack event content from a maunium pack JSON."""
    images = {}
    bad = 0
    for i, st in enumerate(pack.get("stickers", [])):
        url = st.get("url") or ""
        if not url.startswith("mxc://"):
            bad += 1
            continue
        tg = st.get("net.maunium.telegram.sticker") or {}
        key = str(tg.get("id") or st.get("id") or f"s{i}")
        info = {}
        src_info = st.get("info") or {}
        for field in ("mimetype", "w", "h", "size"):
            if src_info.get(field) is not None:
                info[field] = src_info[field]
        img = {"url": url}
        if st.get("body"):
            img["body"] = st["body"]
        if info:
            img["info"] = info
        images[key] = img
    first_url = next(iter(images.values()))["url"] if images else None
    content = {
        "pack": {"display_name": pack.get("title") or short, "usage": ["sticker"]},
        "images": images,
    }
    if first_url:
        content["pack"]["avatar_url"] = first_url
    return content, bad


def collect_packs() -> dict:
    packs = {}
    for fn in sorted(os.listdir(SP)):
        if not fn.endswith(".json") or fn == "index.json":
            continue
        short = fn[:-5]
        try:
            with open(os.path.join(SP, fn), encoding="utf-8") as f:
                pack = json.load(f)
            content, bad = build_pack_content(short, pack)
        except (json.JSONDecodeError, OSError, ValueError):
            continue  # skip a pack mid-write by the concurrent importer
        if not content["images"]:
            packs[short] = None  # empty pack: nothing to publish
            continue
        content_bytes = json.dumps(content, ensure_ascii=False,
                                   separators=(",", ":")).encode("utf-8")
        packs[short] = {"content": content, "bytes": content_bytes, "bad": bad}
    return packs


class MatrixClient:
    def __init__(self, base: URL, token: str):
        self.base = base
        self.token = token
        self.failed = 0

    def _headers(self):
        return {"Authorization": f"Bearer {self.token}"}

    async def request(self, sess, method, path, payload=None):
        url = URL(f"{str(self.base).rstrip('/')}/{path.lstrip('/')}", encoded=True)
        for _attempt in range(6):
            async with sess.request(method, url, json=payload,
                                    headers=self._headers()) as resp:
                body = await resp.json(content_type=None)
                body = body if isinstance(body, dict) else {}
                if resp.status == 429 or body.get("errcode") == "M_LIMIT_EXCEEDED":
                    delay = min(max((body.get("retry_after_ms") or 1000) / 1000, 1), 30)
                    await asyncio.sleep(delay)
                    continue
                return resp.status, body
        return 429, {"errcode": "M_LIMIT_EXCEEDED"}

    async def whoami(self, sess):
        status, body = await self.request(
            sess, "GET", "_matrix/client/v3/account/whoami")
        if status == 200:
            return body.get("user_id"), "ok"
        return None, f"{status} {body.get('errcode', 'M_UNKNOWN')}"

    async def create_room(self, sess, name):
        status, body = await self.request(
            sess, "POST", "_matrix/client/v3/createRoom",
            {
                "name": name,
                "topic": "Telegram → Matrix sticker packs (MSC2545 im.ponies.room_emotes). "
                         "Enabled globally via im.ponies.emote_rooms.",
                "preset": "private_chat",
                "visibility": "private",
                "creation_content": {"type": None},
            })
        if status == 200:
            return body["room_id"], "ok"
        return None, f"{status} {body.get('errcode', 'M_UNKNOWN')}: {body.get('error','')[:120]}"

    async def room_alive(self, sess, room_id):
        status, _ = await self.request(
            sess, "GET",
            f"_matrix/client/v3/rooms/{q(room_id)}/state/m.room.create/")
        return status == 200

    async def put_state(self, sess, room_id, ev_type, state_key, content):
        status, body = await self.request(
            sess, "PUT",
            f"_matrix/client/v3/rooms/{q(room_id)}/state/{q(ev_type)}/{q(state_key)}",
            content)
        if status == 200:
            return "ok"
        self.failed += 1
        return f"{status} {body.get('errcode', 'M_UNKNOWN')}: {body.get('error','')[:100]}"

    async def put_account_data(self, sess, user_id, ev_type, content):
        status, body = await self.request(
            sess, "PUT",
            f"_matrix/client/v3/user/{q(user_id)}/account_data/{q(ev_type)}", content)
        if status == 200:
            return "ok"
        self.failed += 1
        return f"{status} {body.get('errcode', 'M_UNKNOWN')}: {body.get('error','')[:100]}"


def load_state():
    if os.path.exists(STATE_PATH):
        with open(STATE_PATH, encoding="utf-8") as f:
            return json.load(f)
    return {"room_id": None, "packs": {}}


def save_state(state):
    with open(STATE_PATH, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=1, sort_keys=True)


async def run(dry_run: bool, force: bool, room_name: str) -> int:
    homeserver, user_id, token = load_config()
    base = URL(homeserver)
    packs = collect_packs()

    empty = sorted(s for s, v in packs.items() if v is None)
    publishable = {s: v for s, v in packs.items() if v is not None}
    total = sum(len(v["content"]["images"]) for v in publishable.values())
    sizes = sorted(len(v["bytes"]) for v in publishable.values())
    oversized = [s for s, v in publishable.items() if len(v["bytes"]) > 60000]
    print(f"本地包 {len(packs)}(空包跳過 {len(empty)})|可發佈 {len(publishable)} 包 / {total} 張|"
          f"payload 最大 {sizes[-1] if sizes else 0}、中位 {sizes[len(sizes)//2] if sizes else 0} bytes|"
          f"超大(>60KB): {oversized or '無'}")

    if dry_run:
        for s in sorted(publishable):
            v = publishable[s]
            print(f"  would PUT state {ROOM_EMOTES_TYPE}/{s}: "
                  f"{len(v['content']['images'])} stickers, {len(v['bytes'])} bytes")
        print("dry-run:未接觸網路")
        return 0

    state = load_state()
    async with ClientSession() as sess:
        mc = MatrixClient(base, token)
        uid, err = await mc.whoami(sess)
        if not uid:
            print(f"TOKEN_DEAD({err})— 請更新 config.json 的 access_token 後重試")
            return 2
        if uid != user_id:
            print(f"警告:token 屬於 {uid},config 記錄 {user_id},以 token 為準")

        room_id = state.get("room_id")
        if room_id and not await mc.room_alive(sess, room_id):
            print(f"快取房間 {room_id} 已失效,重建")
            room_id = None
        if not room_id:
            room_id, err = await mc.create_room(sess, room_name)
            if not room_id:
                print(f"建房失敗:{err}")
                return 1
            print(f"已建立貼圖房間:{room_id}")
            state["room_id"] = room_id
            state["packs"] = {}
            save_state(state)
        else:
            print(f"沿用既有貼圖房間:{room_id}")

        todo = {s: v for s, v in publishable.items()
                if force or state["packs"].get(s) != hashlib.sha256(v["bytes"]).hexdigest()}
        stale = sorted(set(state["packs"]) - set(publishable))
        print(f"待寫入 {len(todo)} 包(內容有變)|待移除 {len(stale)} 包 {stale or ''}")

        for n, short in enumerate(sorted(todo), 1):
            v = publishable[short]
            e1 = await mc.put_state(sess, room_id, ROOM_EMOTES_TYPE, short, v["content"])
            e2 = await mc.put_state(sess, room_id, ROOM_IMAGE_PACK_TYPE, short, v["content"])
            mark = "" if e1 == "ok" and e2 == "ok" else f"  !! {e1} / {e2}"
            print(f"[{n}/{len(todo)}] {short}: {len(v['content']['images'])} 張{mark}")
            if e1 == "ok" and e2 == "ok":
                state["packs"][short] = hashlib.sha256(v["bytes"]).hexdigest()
            await asyncio.sleep(0.2)

        for short in stale:
            e1 = await mc.put_state(sess, room_id, ROOM_EMOTES_TYPE, short, {})
            e2 = await mc.put_state(sess, room_id, ROOM_IMAGE_PACK_TYPE, short, {})
            print(f"移除 {short}: {e1} / {e2}")
            if e1 == "ok" and e2 == "ok":
                state["packs"].pop(short, None)

        # point account data at the room (read-modify-write), both unstable + stable (v1.19)
        for adtype in (EMOTE_ROOMS_TYPE, IMAGE_PACK_ROOMS_TYPE):
            status, cur = await mc.request(
                sess, "GET", f"_matrix/client/v3/user/{q(uid)}/account_data/{q(adtype)}")
            rooms = cur.get("rooms") if status == 200 and isinstance(cur.get("rooms"), dict) else {}
            rooms[room_id] = {s: {} for s in sorted(state["packs"])}
            err = await mc.put_account_data(sess, uid, adtype, {"rooms": rooms})
            print(f"{adtype}: {err}(啟用 {len(rooms[room_id])} 包)")

    save_state(state)
    print(f"完成:寫入/更新 {len(todo) - mc.failed} 包成功、{mc.failed} 失敗;"
          f"房間 {state['room_id']} 現有 {len(state['packs'])} 包")
    return 1 if mc.failed else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--room-name", default=DEFAULT_ROOM_NAME)
    args = ap.parse_args()
    try:
        return asyncio.run(run(args.dry_run, args.force, args.room_name))
    except (ClientError, asyncio.TimeoutError) as e:
        print(f"network error: {e!r}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
