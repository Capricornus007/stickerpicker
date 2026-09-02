#!/usr/bin/env python3
"""Live-verify local pack JSONs against the Telegram account.

Fetches the full sticker-set document list for every saved pack and
compares document IDs with web/packs/<short_name>.json.  Also dumps the
live Telegram state to /tmp/tg_live_state.json for follow-up runs.
"""
import asyncio
import json
import os
import sys

from telethon import TelegramClient
from telethon.tl.functions.messages import GetAllStickersRequest, GetStickerSetRequest
from telethon.tl.types import InputStickerSetShortName
from telethon.tl.types.messages import StickerSet as StickerSetFull

SP = "web/packs"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "tg-live-state.json")


async def main() -> int:
    client = TelegramClient("sticker-import", 298751, "cb676d6bae20553c9996996a8f52b4d7")
    await client.start()

    all_stickers = await client(GetAllStickersRequest(hash=0))
    live = {}
    print(f"Telegram 帳號共有 {len(all_stickers.sets)} 個包,逐包核對文件清單…", flush=True)

    for saved in all_stickers.sets:
        short = saved.short_name
        try:
            full: StickerSetFull = await client(GetStickerSetRequest(
                InputStickerSetShortName(short_name=short), hash=0))
        except Exception as e:
            print(f"  !! {short}: 取得失敗 {e!r}", flush=True)
            live[short] = {"title": saved.title, "error": repr(e), "count": saved.count,
                           "doc_ids": []}
            continue
        doc_ids = [d.id for d in full.documents]
        live[short] = {"title": full.set.title, "count": full.set.count,
                       "hash": str(full.set.hash), "doc_ids": doc_ids}

        pack_path = os.path.join(SP, short + ".json")
        local_ids = []
        if os.path.exists(pack_path):
            with open(pack_path, encoding="utf-8") as f:
                local = json.load(f)
            for st in local.get("stickers", []):
                tg = st.get("net.maunium.telegram.sticker") or {}
                try:
                    local_ids.append(int(tg["id"]))
                except (KeyError, TypeError, ValueError):
                    local_ids.append(None)
        want, have = set(doc_ids), {i for i in local_ids if i is not None}
        missing = want - have
        extra = have - want
        status = "OK" if not missing and not extra else (
            f"缺 {len(missing)}/{len(doc_ids)}" + (f",多餘 {len(extra)}" if extra else ""))
        print(f"  {short}: TG {len(doc_ids)} 張 / 本地 {len(have)} 張 → {status}", flush=True)
        live[short]["missing_doc_ids"] = sorted(missing)
        live[short]["extra_doc_ids"] = [str(i) for i in extra]
        live[short]["local_count"] = len(have)

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(live, f, ensure_ascii=False, indent=1)
    print(f"\nlive 狀態已寫到 {OUT}", flush=True)

    total_missing = sum(len(v.get("missing_doc_ids", [])) for v in live.values())
    bad = [k for k, v in live.items() if "error" in v]
    missing_files = [k for k, v in live.items()
                     if "error" not in v and not os.path.exists(os.path.join(SP, k + ".json"))]
    print(f"結論:{len(live)} 包;缺張合計 {total_missing};整包缺檔 {len(missing_files)} {missing_files};"
          f"取得失敗 {len(bad)} {bad}", flush=True)
    await client.disconnect()
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
