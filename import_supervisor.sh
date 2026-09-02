#!/usr/bin/env bash
# Detached quota-aware supervisor: resumes the Telegram→Matrix sticker import
# whenever matrix.org's media-upload quota is back, syncs the room (both
# im.ponies + m.image_pack) after each batch, and stops once nothing is missing.
cd /home/avatar/Downloads/stickerpicker || exit 1
LOG=import-supervisor.log
echo "[$(date '+%F %T')] supervisor started (waits for matrix media quota to reset, then auto-resumes)" >> "$LOG"

while :; do
  # done? holes.py exit 0 == every pack complete
  if .venv/bin/python scripts/holes.py >/dev/null 2>&1; then
    echo "[$(date '+%F %T')] no holes left — final room sync + exit" >> "$LOG"
    .venv/bin/python scripts/msc2545_room_sync.py --force >> "$LOG" 2>&1
    break
  fi

  # probe_and_resume gates on Telegram connectivity + matrix media quota;
  # only launches the (detached) import worker when both are open.
  status=$(bash probe_and_resume.sh 2>&1)
  echo "[$(date '+%F %T')] probe: $status" >> "$LOG"

  if printf '%s' "$status" | grep -q RESUMED; then
    # wait for the detached worker to finish (absent for 3 consecutive checks)
    idle=0
    while :; do
      if pgrep -f '\.venv/bin/sticker-import' >/dev/null 2>&1; then
        idle=0
      else
        idle=$((idle+1)); [ "$idle" -ge 3 ] && break
      fi
      sleep 120
    done
    echo "[$(date '+%F %T')] import batch finished — syncing room" >> "$LOG"
    .venv/bin/python scripts/msc2545_room_sync.py --force >> "$LOG" 2>&1
    echo "[$(date '+%F %T')] room now: $(ls web/packs/*.json 2>/dev/null | wc -l) packs" >> "$LOG"
  else
    # STILL_LIMITED / TG_STALLED / TOKEN_DEAD → wait an hour, retry
    sleep 3600
  fi
done
echo "[$(date '+%F %T')] supervisor done — all packs imported & published" >> "$LOG"
