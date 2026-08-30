#!/usr/bin/env bash
# 雙門閘自動續跑探測:Matrix 媒體配額有餘裕、且 Telegram 連線通暢時,
# 才啟動補齊匯入(由每小時排程呼叫,亦可手動執行)。
cd /home/avatar/Downloads/stickerpicker || exit 1

if pgrep -f 'xargs -n 8 .venv/bin/sticker-[i]mport' >/dev/null 2>&1; then
  echo "IMPORT_RUNNING（匯入已在跑，不重複啟動）"
  exit 0
fi

# 閘門一:Telegram MTProto 連通(被節流時握手會吊著,40 秒無清單即判定)
TG=$(timeout 40 .venv/bin/sticker-import --list 2>/dev/null | grep -c 'addstickers')
if [ "$TG" -eq 0 ] 2>/dev/null; then
  echo "TG_STALLED（Telegram 連線仍被節流，等下一輪）"
  exit 0
fi

# 閘門二:Matrix token 有效性 → 媒體配額
TOKEN=$(python3 -c "import json;print(json.load(open('config.json'))['access_token'])")
WHO=$(curl -s -o /tmp/whoami-resp.json -w '%{http_code}' --max-time 30 \
  "https://matrix.org/_matrix/client/v3/account/whoami" -H "Authorization: Bearer $TOKEN")
if [ "$WHO" != "200" ]; then
  echo "TOKEN_DEAD（access token 失效，HTTP $WHO — 需要使用者提供新 token）"
  exit 0
fi
head -c 76800 /dev/urandom > /tmp/quota-probe.bin
CODE=$(curl -s -o /tmp/quota-probe-resp.json -w '%{http_code}' --max-time 60 -X POST \
  "https://matrix.org/_matrix/media/v3/upload?filename=quota-probe.bin" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/octet-stream" \
  --data-binary @/tmp/quota-probe.bin)
if [ "$CODE" != "200" ]; then
  echo "STILL_LIMITED（Matrix 配額未回，HTTP $CODE：$(head -c 150 /tmp/quota-probe-resp.json 2>/dev/null)）"
  exit 0
fi

# 兩閘全開 → 啟動分離式工人 + 桌面觀景窗
setsid nohup bash -c 'export STICKER_UPLOAD_ATTEMPTS=20 STICKER_JOBS=10 STICKER_PACK_JOBS=3; cd /home/avatar/Downloads/stickerpicker && .venv/bin/sticker-import --list 2>/dev/null | grep -oP "(?<=addstickers/)[A-Za-z0-9_-]+" | xargs -n 8 .venv/bin/sticker-import 2>&1 | tee -a 20260830-mopup.log' >/dev/null 2>&1 &
DISPLAY=:0 nohup alacritty --title 'sticker-import-viewer' -e bash -c 'echo "== 觀景窗：收割機即時輸出（關掉此視窗不影響匯入）=="; tail -f /home/avatar/Downloads/stickerpicker/20260830-mopup.log' >/dev/null 2>&1 &
echo "RESUMED（兩閘全開，已啟動匯入工人與桌面觀景窗）"
