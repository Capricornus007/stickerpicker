#!/usr/bin/env python3
"""Report which local packs are incomplete relative to the Telegram account.

Source of truth is the live Telegram snapshot written by
verify_against_telegram.py (scripts/tg-live-state.json); it falls back to the
run logs if the snapshot is missing.

Usage: .venv/bin/python scripts/holes.py
Exit codes: 0 = everything complete, 1 = holes present, 3 = no data source.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SP = os.path.join(ROOT, "web", "packs")
LIVE = os.path.join(ROOT, "scripts", "tg-live-state.json")
LOGS = ["20260830.1459.log", "20260830-mopup.log"]


def local_doc_ids(short: str) -> set:
    path = os.path.join(SP, short + ".json")
    ids = set()
    if not os.path.exists(path):
        return ids
    with open(path, encoding="utf-8") as f:
        pack = json.load(f)
    for st in pack.get("stickers", []):
        tg = st.get("net.maunium.telegram.sticker") or {}
        try:
            ids.add(int(tg["id"]))
        except (KeyError, TypeError, ValueError):
            pass
    return ids


def from_live():
    with open(LIVE, encoding="utf-8") as f:
        return json.load(f)


def from_logs():
    """Fallback: declared counts from the import logs (doc-level diff impossible)."""
    declared = {}
    for lp in LOGS:
        p = os.path.join(ROOT, lp)
        if not os.path.exists(p):
            continue
        with open(p, errors="ignore") as f:
            text = f.read()
        for m in re.finditer(r"Reuploading (?:.+?) with (\d+) stickers and writing "
                             r"output to web/packs/(\S+?)\.json", text):
            short, want = m.group(2), int(m.group(1))
            if short not in declared or want > declared[short]:
                declared[short] = want
    return {s: {"count": want, "doc_ids": None}
            for s, want in declared.items()}


def main() -> int:
    try:
        live = from_live()
        source = "tg-live-state.json"
    except FileNotFoundError:
        if not any(os.path.exists(os.path.join(ROOT, lp)) for lp in LOGS):
            print("沒有 tg-live-state.json 也沒有 log,無法判斷(先跑 verify_against_telegram.py)")
            return 3
        live = from_logs()
        source = "logs(僅包級張數,以 log 宣告為準)"

    holes, missing_total, tg_total = {}, 0, 0
    missing_files = []
    for short, info in live.items():
        if "error" in info:
            holes[short] = (0, info.get("count", 0), "TG 取得失敗")
            continue
        tg_total += info["count"]
        want_ids = set(info["doc_ids"]) if info.get("doc_ids") is not None else None
        have = local_doc_ids(short)
        path = os.path.join(SP, short + ".json")
        if not os.path.exists(path):
            missing_files.append(short)
        if want_ids is None:
            have_count = len(have)
            if have_count < info["count"]:
                holes[short] = (have_count, info["count"], "缺張(log 口徑)")
                missing_total += info["count"] - have_count
        else:
            miss = len(want_ids - have)
            extra = len(have - want_ids)
            if miss or extra:
                holes[short] = (info["count"] - miss, info["count"],
                                f"缺 {miss}" + (f",多餘 {extra}" if extra else ""))
                missing_total += miss

    print(f"資料來源: {source}")
    print(f"TG 帳號 {len(live)} 包 / {tg_total} 張;缺張總計 {missing_total};"
          f"有問題的包 {len(holes)} 個(其中整包缺檔 {len(missing_files)})")
    for short in sorted(holes):
        have, want, note = holes[short]
        print(f"  {short}: {have}/{want} ({note})")
    return 1 if holes else 0


if __name__ == "__main__":
    sys.exit(main())
