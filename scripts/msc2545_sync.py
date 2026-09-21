#!/usr/bin/env python3
"""Sync local sticker packs into Matrix account data as MSC2545 user packs.

Writes one `im.packs.user.<short_name>` account-data event per pack plus an
`im.packs.global` event pointing at the user's own packs (the format the
original MSC2545 draft defined and Nheko/Cinny/FluffyChat read).  Idempotent:
only packs whose generated content differs from the last successful sync are
PUT again (state tracked in scripts/msc2545-state.json); packs deleted locally
are DELETEd remotely.

Usage:
  .venv/bin/python scripts/msc2545_sync.py [--dry-run] [--force]
Exit codes: 0 ok / 1 partial or full failure / 2 token dead.
"""
import argparse
import asyncio
import hashlib
import json
import os
import sys

from aiohttp import ClientError, ClientSession
from yarl import URL

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SP = os.path.join(ROOT, "web", "packs")
STATE_PATH = os.path.join(ROOT, "scripts", "msc2545-state.json")
CONFIG_PATH = os.path.join(ROOT, "config.json")

GLOBAL_TYPE = "im.packs.global"
USER_TYPE_PREFIX = "im.packs.user."


def load_config():
    with open(CONFIG_PATH, encoding="utf-8") as f:
        cfg = json.load(f)
    return cfg["homeserver"], cfg["user_id"], cfg["access_token"]


def build_pack_content(short: str, pack: dict) -> tuple[dict, int]:
    """Build one MSC2545 pack event content from a maunium pack JSON."""
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
        "pack": {"display_name": pack.get("title") or short},
        "usage": ["sticker"],
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
        with open(os.path.join(SP, fn), encoding="utf-8") as f:
            pack = json.load(f)
        content, bad = build_pack_content(short, pack)
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

    async def request(self, sess: ClientSession, method: str, path: str,
                      payload=None) -> tuple[int, dict]:
        url = self.base / path
        async with sess.request(method, url, json=payload,
                                headers=self._headers()) as resp:
            body = await resp.json(content_type=None)
            return resp.status, (body if isinstance(body, dict) else {})

    async def put_account_data(self, sess: ClientSession, user_id: str,
                               ev_type: str, content: dict) -> str:
        for attempt in range(4):
            status, body = await self.request(
                sess, "PUT", f"_matrix/client/v3/user/{user_id}/account_data/{ev_type}",
                content)
            if status == 200:
                return "ok"
            if status == 429 or body.get("errcode") == "M_LIMIT_EXCEEDED":
                await asyncio.sleep(min(max((body.get("retry_after_ms") or 1000) / 1000, 1), 30))
                continue
            self.failed += 1
            return f"{status} {body.get('errcode', 'M_UNKNOWN')}: {body.get('error', '')[:100]}"
        self.failed += 1
        return "429 persisted after retries"

    async def delete_account_data(self, sess: ClientSession, user_id: str,
                                  ev_type: str) -> str:
        status, body = await self.request(
            sess, "DELETE", f"_matrix/client/v3/user/{user_id}/account_data/{ev_type}")
        if status in (200, 404):
            return "ok"
        self.failed += 1
        return f"{status} {body.get('errcode', 'M_UNKNOWN')}"


async def whoami(base: URL, token: str) -> tuple[str, str]:
    async with ClientSession() as sess:
        async with sess.get(base / "_matrix/client/v3/account/whoami",
                            headers={"Authorization": f"Bearer {token}"}) as resp:
            body = await resp.json(content_type=None)
            if resp.status == 200:
                return body["user_id"], "ok"
            err = body.get("errcode", "M_UNKNOWN") if isinstance(body, dict) else "M_UNKNOWN"
            return "", f"{resp.status} {err}"


async def run(dry_run: bool, force: bool) -> int:
    homeserver, user_id, token = load_config()
    base = URL(homeserver)
    packs = collect_packs()

    empty = sorted(s for s, v in packs.items() if v is None)
    publishable = {s: v for s, v in packs.items() if v is not None}
    total_stickers = sum(len(v["content"]["images"]) for v in publishable.values())
    sizes = sorted(len(v["bytes"]) for v in publishable.values())
    oversized = [s for s, v in publishable.items() if len(v["bytes"]) > 60000]

    print(f"本地包 {len(packs)}(空包跳過 {len(empty)})|可發佈 {len(publishable)} 包 "
          f"/ {total_stickers} 張|payload 最大 {sizes[-1]},中位 {sizes[len(sizes)//2]},"
          f"合計 {sum(sizes)} bytes|超大(>60KB): {oversized or '無'}")

    state = {}
    if os.path.exists(STATE_PATH):
        with open(STATE_PATH, encoding="utf-8") as f:
            state = json.load(f)

    todo = {s: v for s, v in publishable.items()
            if force or state.get(s) != hashlib.sha256(v["bytes"]).hexdigest()}
    stale = sorted(set(state) - set(publishable))
    print(f"待寫入 {len(todo)} 包(內容有變)|待刪除 {len(stale)} 包 {stale or ''}")

    if dry_run:
        for s in sorted(todo):
            v = publishable[s]
            print(f"  would PUT {USER_TYPE_PREFIX}{s}: "
                  f"{len(v['content']['images'])} stickers, {len(v['bytes'])} bytes")
        print("dry-run:未接觸網路")
        return 0

    uid, err = await whoami(base, token)
    if not uid:
        print(f"TOKEN_DEAD({err})— 請更新 config.json 的 access_token 後重試")
        return 2
    if uid != user_id:
        print(f"警告:token 屬於 {uid},config 記錄 {user_id},以 token 為準")

    mc = MatrixClient(base, token)
    async with ClientSession() as sess:
        # global event: read-modify-write so third-party user packs survive
        status, cur = await mc.request(
            sess, "GET", f"_matrix/client/v3/user/{uid}/account_data/{GLOBAL_TYPE}")
        entries = (cur.get("packs") if status == 200 and isinstance(cur.get("packs"), list)
                   else [])
        me = {"type": "users", "id": uid}
        if me not in entries:
            entries.append(me)
            err = await mc.put_account_data(sess, uid, GLOBAL_TYPE, {"packs": entries})
            print(f"im.packs.global: {err}")
        else:
            print("im.packs.global: 已含本帳號,不變")

        for n, short in enumerate(sorted(todo), 1):
            v = publishable[short]
            err = await mc.put_account_data(sess, uid, f"{USER_TYPE_PREFIX}{short}",
                                            v["content"])
            mark = "" if err == "ok" else f"  !! {err}"
            print(f"[{n}/{len(todo)}] {short}: {len(v['content']['images'])} 張{mark}")
            if err == "ok":
                state[short] = hashlib.sha256(v["bytes"]).hexdigest()
            await asyncio.sleep(0.25)

        for short in stale:
            err = await mc.delete_account_data(sess, uid, f"{USER_TYPE_PREFIX}{short}")
            print(f"DELETE {short}: {err}")
            if err == "ok":
                state.pop(short, None)

    with open(STATE_PATH, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=1, sort_keys=True)

    print(f"完成:寫入 {len(todo) - mc.failed} 包成功、{mc.failed} 包失敗,共 {len(publishable)} 包可發佈")
    return 1 if mc.failed else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="build payloads only, no network")
    ap.add_argument("--force", action="store_true", help="re-PUT every pack even if unchanged")
    args = ap.parse_args()
    try:
        return asyncio.run(run(args.dry_run, args.force))
    except (ClientError, asyncio.TimeoutError) as e:
        print(f"network error: {e!r}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
