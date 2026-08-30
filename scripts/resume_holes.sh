#!/usr/bin/env bash
# 補洞:比對 log 宣告的包張數與實際 JSON,只重新匯入缺張數與曾整包失敗的包。
# 用法:bash scripts/resume_holes.sh   (在 repo 根目錄)
cd "$(dirname "$0")/.." || exit 1

HOLES=$(.venv/bin/python - <<'EOF'
import glob, json, os, re
SP = 'web/packs'
holes, failed = {}, set()
for lp in ['20260830.1459.log', '20260830-mopup.log']:
    if not os.path.exists(lp):
        continue
    text = open(lp, errors='ignore').read()
    for m in re.finditer(r'Reuploading (?:.+?) with (\d+) stickers and writing output to web/packs/(\S+?)\.json', text):
        want, short = int(m.group(1)), m.group(2)
        pf = os.path.join(SP, short + '.json')
        have = len(json.load(open(pf)).get('stickers', [])) if os.path.exists(pf) else 0
        if have < want:
            holes[short] = want
    for m in re.finditer(r'Failed to import (\S+),', text):
        failed.add(m.group(1))
for short in sorted(holes) + sorted(failed - set(holes)):
    # Quarantine: b675aff8 (Strongh♂lds) downloads have twice killed the Telethon
    # connection mid-pack; run it alone in a dedicated process, never in a batch.
    if short == 'b675aff8_by_fStikBot':
        continue
    print(short, end='\n')
EOF
)
HOLES=$(echo "$HOLES" | sed '/^$/d')

if [ -z "$HOLES" ]; then
  echo "沒有洞，全部完整。"
  exit 0
fi
echo "需要補的包:"
echo "$HOLES"
.venv/bin/sticker-import $HOLES 2>&1 | tee -a 20260830-mopup.log
