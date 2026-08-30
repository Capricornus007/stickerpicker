#!/usr/bin/env python3
"""Enable the sticker picker in every Element room by writing the global
m.widgets account-data event directly (no /devtools editing needed).

Usage (from the repo root, where config.json lives):
    python scripts/set_sticker_widget.py
    python scripts/set_sticker_widget.py --url 'https://capricornus007.github.io/stickerpicker/web/?theme=$theme'
"""
import argparse
import json
import urllib.parse
import urllib.request

ap = argparse.ArgumentParser()
ap.add_argument('--url', default='https://capricornus007.github.io/stickerpicker/web/?theme=$theme')
args = ap.parse_args()

cfg = json.load(open('config.json'))
hs = cfg['homeserver'].rstrip('/')
tok = cfg['access_token']


def call(path, method='GET', body=None):
    req = urllib.request.Request(
        hs + path, method=method,
        data=json.dumps(body).encode() if body is not None else None,
        headers={'Authorization': 'Bearer ' + tok, 'Content-Type': 'application/json'})
    return json.load(urllib.request.urlopen(req))


user_id = call('/_matrix/client/v3/account/whoami')['user_id']
widget = {
    'stickerpicker': {
        'content': {
            'type': 'm.stickerpicker',
            'url': args.url,
            'name': 'Stickerpicker',
            'creatorUserId': user_id,
            'data': {},
        },
        'sender': user_id,
        'state_key': 'stickerpicker',
        'type': 'm.widget',
        'id': 'stickerpicker',
    }
}
call(f'/_matrix/client/v3/user/{urllib.parse.quote(user_id)}/account_data/m.widgets',
     'PUT', widget)
print(f'已設定全域貼圖面板 for {user_id}\nURL: {args.url}\n重新整理 Element 即可看到貼圖按鈕。')
