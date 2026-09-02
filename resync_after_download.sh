#!/usr/bin/env bash
# Detached one-shot: wait until the Telegram sticker-import worker finishes,
# then publish the freshly-downloaded packs into the MSC2545 room. Idempotent.
cd /home/avatar/Downloads/stickerpicker || exit 1
LOG=resync-after-download.log
echo "[$(date '+%F %T')] watcher started; waiting for sticker-import to finish" >> "$LOG"

# require the importer to be absent for 3 consecutive checks (~6 min) before syncing,
# so a brief gap between packs doesn't trigger an early sync.
idle=0
while :; do
  if pgrep -f '\.venv/bin/sticker-import' >/dev/null 2>&1; then
    idle=0
  else
    idle=$((idle+1))
    [ "$idle" -ge 3 ] && break
  fi
  sleep 120
done

.venv/bin/python scripts/msc2545_room_sync.py --force >> "$LOG" 2>&1
.venv/bin/python scripts/msc2545_room_sync.py >> "$LOG" 2>&1
echo "[$(date '+%F %T')] room sync exit=$? ; local packs now: $(ls web/packs/*.json 2>/dev/null | wc -l)" >> "$LOG"
