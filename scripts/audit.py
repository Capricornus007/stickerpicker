#!/usr/bin/env python3
"""Audit the local sticker pack data: pack JSON structure, thumbnail coverage,
index consistency, holes (declared vs actual sticker counts), and optionally
spot-check real media on the homeserver.

Usage:
    python scripts/audit.py            # local audit
    python scripts/audit.py --media 20 # also fetch N random stickers and verify
"""
import argparse
import collections
import glob
import json
import os
import random
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SP = os.path.join(ROOT, 'web', 'packs')
LOGS = [os.path.join(ROOT, '20260830.1459.log'), os.path.join(ROOT, '20260830-mopup.log')]
MAGIC = {'image/png': b'\x89PNG', 'image/gif': b'GIF8', 'video/webm': b'\x1aE\xdf\xa3'}


def local_audit():
    issues = []
    all_media = {}
    mimetypes = collections.Counter()
    packs = sorted(f for f in glob.glob(os.path.join(SP, '*.json'))
                   if os.path.basename(f) != 'index.json')
    for pf in packs:
        short = os.path.basename(pf)[:-5]
        try:
            d = json.load(open(pf))
        except Exception as e:
            issues.append((short, 'JSON 解析失敗', repr(e)))
            continue
        for s in d.get('stickers', []):
            url = s.get('url', '')
            if url.startswith('mxc://'):
                all_media[url.rsplit('/', 1)[-1]] = s.get('info', {}).get('mimetype', '?')
            else:
                issues.append((short, '非 mxc url', url[:50]))
            if not isinstance(s.get('info'), dict) or 'mimetype' not in s['info']:
                issues.append((short, 'info 殘缺', s.get('id', '?')))
            mimetypes[s.get('info', {}).get('mimetype', '?')] += 1
            info = s.get('info', {})
            if info.get('h', 1) == 0 or info.get('w', 1) == 0 or info.get('size', 999) < 500:
                issues.append((short, '畸形貼圖(零尺寸/過小)', s.get('id', '?')))

    empty = [os.path.basename(f) for f in packs
             if not json.load(open(f)).get('stickers')]
    if empty:
        print(f'⚠ 空包(前端已防護,但補完前不建議 push index):{empty}')
    print(f'包數: {len(packs)} | 貼圖: {sum(mimetypes.values())} | 構成: {dict(mimetypes)}')

    tdir = os.path.join(SP, 'thumbnails')
    thumbs = set(os.listdir(tdir)) if os.path.isdir(tdir) else set()
    referenced = set(all_media)
    print(f'縮圖: {len(thumbs)} | 被引用: {len(referenced)} | '
          f'缺縮圖: {len(referenced - thumbs)} | 孤立縮圖: {len(thumbs - referenced)}')

    bad = [t for t in random.sample(sorted(thumbs), min(60, len(thumbs)))
           if open(os.path.join(tdir, t), 'rb').read(4) != b'\x89PNG'] if thumbs else []
    print(f'縮圖 PNG 抽查 60: 不合格 {len(bad)}')

    idx = set(json.load(open(os.path.join(SP, 'index.json')))['packs'])
    files = {os.path.basename(p) for p in packs}
    print(f'index 有檔無: {len(idx - files)} | 有檔無 index: {len(files - idx)}')

    holes = {}
    for lp in LOGS:
        if not os.path.exists(lp):
            continue
        for m in re.finditer(r'Reuploading (?:.+?) with (\d+) stickers and '
                             r'writing output to web/packs/(\S+?)\.json',
                             open(lp, errors='ignore').read()):
            want, short = int(m.group(1)), m.group(2)
            pf = os.path.join(SP, short + '.json')
            have = len(json.load(open(pf)).get('stickers', [])) if os.path.exists(pf) else 0
            if have < want:
                holes[short] = (have, want)
    print(f'有洞的包: {len(holes)}')
    for k, v in sorted(holes.items(), key=lambda x: x[1][0] - x[1][1]):
        print(f'  {k}: {v[0]}/{v[1]}')

    print(f'結構問題: {len(issues)}')
    for i in issues[:10]:
        print(' ', i)
    return all_media


def media_audit(all_media, count):
    cfg = json.load(open(os.path.join(os.path.dirname(SP), 'config.json')))
    hs = cfg['homeserver'].rstrip('/')
    sample = random.sample(sorted(all_media.items()), min(count, len(all_media)))
    import urllib.request
    bad = 0
    for mid, mt in sample:
        url = f'{hs}/_matrix/client/v1/media/download/matrix.org/{mid}'
        req = urllib.request.Request(url, headers={'Authorization': 'Bearer ' + cfg['access_token']})
        try:
            data = urllib.request.urlopen(req, timeout=30).read()
            ok = data[:4] == MAGIC.get(mt, b'') or (mt == 'image/gif' and data[:4] == b'GIF8')
            if not ok:
                bad += 1
                print(f'  魔數不符: {mid} ({mt})')
        except Exception as e:
            bad += 1
            print(f'  抓取失敗: {mid} {e!r}')
    print(f'媒體抽查 {len(sample)}: 異常 {bad}')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--media', type=int, default=0, help='抽查 N 張真實媒體')
    args = ap.parse_args()
    media = local_audit()
    if args.media:
        media_audit(media, args.media)
