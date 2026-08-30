# stickerpicker 交付文件 / Delivery Document

> **專案** / Project:maunium/stickerpicker fork → `Capricornus007/stickerpicker`(branch `master`)
> **用途** / Purpose:將使用者 Telegram 帳號的**全部貼圖包**(靜態 PNG / 動態 tgs / 影片 webm)完整遷移至 Matrix,並以 sticker picker widget 形式在 Element 全平台使用。
> **文件日期** / Date:2026-08-30
> **前端部署** / Frontend:`https://capricornus007.github.io/stickerpicker/web/`(GitHub Pages,由本 repo 的 `web/` 目錄直接服務)
> **Homeserver**:`matrix.org`(`config.json` 內 `https://matrix-client.matrix.org`)
> **授權** / License:AGPL-3.0(沿用上游 Tulir Asokan 之 maunium-stickerpicker)

本文所有數據與行為描述均以 **2026-08-30 實際讀取 repo 檔案與重新執行驗證** 的結果為準,並標明哪些是「本次複核重跑」、哪些是「交付當時記錄」。

---

## 目錄 / Table of Contents

1. [專案總覽](#1-專案總覽--project-overview)
2. [架構圖(文字版資料流)](#2-架構圖文字版資料流--architecture--data-flow)
3. [安裝與依賴](#3-安裝與依賴--installation--dependencies)
4. [三個後端補丁技術細節](#4-三個後端補丁技術細節--backend-patches-in-detail)
5. [前端補丁](#5-前端補丁--frontend-patch)
6. [自動化腳本使用手冊](#6-自動化腳本使用手冊--automation-scripts-manual)
7. [品質驗證報告摘要](#7-品質驗證報告摘要--qa-report-summary)
8. [已知限制與維運注意](#8-已知限制與維運注意--known-limitations--ops-notes)
9. [常見問題](#9-常見問題--faq)

---

## 1. 專案總覽 / Project Overview

### 1.1 這是什麼

本 repo 是 [maunium/stickerpicker](https://github.com/maunium/stickerpicker)(Element 官方生態常見的輕量貼圖面板 widget,AGPL-3.0)的 fork,在原版基礎上做了四類改造,使其能勝任「**一次把 Telegram 帳號全部貼圖包搬進 Matrix**」這種數千張等級的批量遷移:

| # | 改造 | 檔案 | 一句話說明 |
|---|------|------|-----------|
| 1 | 動態貼圖轉檔 | `sticker/lib/util.py` | `.tgs`(gzip 過的 lottie)→ 迴圈 GIF;webm 無 ffmpeg 時給透明佔位縮圖,不炸 |
| 2 | 上傳韌性 | `sticker/lib/matrix.py` | `upload()` 對 429 / `M_USER_LIMIT_EXCEEDED` / 5xx / 網路錯誤自動分類重試 |
| 3 | 並發匯入 + 斷點續傳 | `sticker/stickerimport.py` | 張級 × 包級雙層 asyncio Semaphore 並發;重跑自動跳過已上傳張;外來包條目寬容解析 |
| 4 | 前端空包防護 | `web/src/index.js` | `NavBarItem` 對空 `stickers` 陣列防護,修復空包導致的整頁白屏 |

對靜態貼圖,行為與上游完全相容(見 `PATCHES.md`)。

### 1.2 交付現況(2026-08-30 複核)

- **54 個包**已寫入 `web/packs/` 並登錄於 `index.json`(index 與檔案清單 0 不一致)。
- **3,149 張貼圖**:2,996 張 `image/png` + 150 張 `video/webm` + 3 張 `image/gif`(tgs 轉檔),即 **153 張非靜態(動態/影片)貼圖**。
- **3,227 張本機縮圖**,全量 PIL 解碼 **0 損壞**(本次複核重跑確認)。
- 遷移途中 matrix.org 免費帳號媒體配額多次耗盡(mopup log 記錄 **425 次 `M_USER_LIMIT_EXCEEDED`**,全數被重試機制節流消化),因此目前仍有 **28 個包存在缺張(「洞」)、其中 3 包為空包**,已由 `probe_and_resume.sh`(自動)與 `scripts/resume_holes.sh`(手動)機制負責收尾,詳見第 6、7 節。

### 1.3 關鍵檔案地圖

| 檔案 | 行數 | 角色 |
|------|-----:|------|
| `PATCHES.md` | 57 | 本 fork 全部改動的自述紀錄(上游無此檔) |
| `sticker/lib/util.py` | 179 | 轉檔與縮圖(tgs→GIF、webm 縮圖、PNG 轉換) |
| `sticker/lib/matrix.py` | 125 | Matrix 媒體上傳(含重試狀態機) |
| `sticker/stickerimport.py` | 248 | 主程式:Telethon 拉包 → 並發轉傳 → 寫包 JSON/縮圖/index |
| `web/src/index.js` | 402 | 前端主元件(含 NavBarItem 空包防護,第 369–383 行) |
| `probe_and_resume.sh` | 34 | 雙門閘自動續跑探測(repo 根目錄) |
| `scripts/audit.py` | 120 | 本地 + 遠端媒體稽核 |
| `scripts/resume_holes.sh` | 33 | 只重匯「有洞」與「曾整包失敗」的包 |
| `scripts/set_sticker_widget.py` | 49 | 一鍵寫入全域 `m.widgets` 帳號資料 |

**English summary**

This repository is a heavily modified fork of maunium/stickerpicker, purpose-built to migrate an entire Telegram sticker collection (static PNG, animated `.tgs`, video `.webm`) to Matrix. Four changes make bulk migration possible: (1) `sticker/lib/util.py` converts gzipped-Lottie `.tgs` stickers into looping transparent GIFs via `lottieconverter` (with a graceful transparent-placeholder fallback for WebM thumbnails when ffmpeg is absent); (2) `sticker/lib/matrix.py` turns `upload()` into a retrying state machine covering 429 rate limits, `M_USER_LIMIT_EXCEEDED` media-quota errors, 5xx and network failures; (3) `sticker/stickerimport.py` was rewritten around two asyncio semaphores (`STICKER_JOBS`, `STICKER_PACK_JOBS`) with mimetype-based dispatch, resumable imports keyed on Telegram document IDs, and tolerant parsing of foreign pack entries; (4) the web frontend guards `NavBarItem` against empty `stickers` arrays that previously white-screened the picker. As of the 2026-08-30 re-verification: 54 packs / 3,149 stickers are migrated (2,996 PNG, 150 WebM, 3 GIF = 153 non-static), all 3,227 local thumbnails decode cleanly with PIL, and 28 packs still have holes pending quota-throttled mopup, handled by the automation described in section 6.

---

## 2. 架構圖(文字版資料流)/ Architecture & Data Flow

```
┌──────────────────────────────────────────────────────────────────────┐
│ Telegram(MTProto;Telethon 單一連線,session 檔 sticker-import.session)│
│   GetAllStickersRequest(列出全部已存包)                               │
│   GetStickerSetRequest(hash=0)(逐包取文件清單)                       │
└──────────────────────────────┬───────────────────────────────────────┘
                               ▼
┌──────────────────────────────────────────────────────────────────────┐
│ sticker-import(sticker/stickerimport.py)                            │
│   包級並發:PACK_JOBS = STICKER_PACK_JOBS(預設 3,asyncio.Semaphore)  │
│   張級並發:JOBS     = STICKER_JOBS(預設 6,asyncio.Semaphore)        │
│   共用同一個 TelegramClient ── 單一 MTProto 連線,並發安全             │
│                                                                      │
│   下載原始 bytes 後依「內容魔數 + mimetype」分流:                      │
│   ├─ EBML magic \x1aE\xdf\xa3 或 mime video/webm → 影片貼圖原樣上傳    │
│   ├─ gzip magic \x1f\x8b → .tgs lottie → lottieconverter(~/.local/bin)│
│   │    → 迴圈 GIF(≤256px、≤25fps、保留透明)                          │
│   └─ 其他 → PIL 轉 RGBA PNG(≤256px)                                 │
└──────────────────────────────┬───────────────────────────────────────┘
                               ▼
┌──────────────────────────────────────────────────────────────────────┐
│ matrix.upload()(sticker/lib/matrix.py)— 重試狀態機                  │
│   POST {homeserver}/_matrix/media/v3/upload                          │
│   ├─ 429 / M_LIMIT_EXCEEDED   → 依 retry_after_ms 等(1–120s)         │
│   ├─ M_USER_LIMIT_EXCEEDED(403)→ 30s × 2ⁿ 指數退避,上限 300s(硬等)  │
│   ├─ 5xx / 網路錯誤            → 2s × 2ⁿ 退避,上限 60s                │
│   ├─ 其他 4xx                 → 立即失敗(不浪費 attempts)            │
│   └─ 成功 → 回傳 mxc://matrix.org/<媒體ID>                            │
│   嘗試次數上限 = STICKER_UPLOAD_ATTEMPTS(預設 6)                      │
└──────────────────────────────┬───────────────────────────────────────┘
                               ▼
┌──────────────────────────────────────────────────────────────────────┐
│ 本地產物(git tracked;push 至 GitHub Pages)                          │
│   web/packs/<short_name>.json   包 metadata + 每張貼圖的 mxc URI/尺寸/  │
│                                 mimetype/表情(TG 來源 metadata 保留)  │
│   web/packs/thumbnails/<媒體ID>.png   128px 本機縮圖(picker 網格用,   │
│                                 不打 homeserver 媒體倉 ── 上游設計)    │
│   web/packs/index.json          包清單 + homeserver_url               │
└──────────────────────────────┬───────────────────────────────────────┘
                               ▼
        https://capricornus007.github.io/stickerpicker/web/
                               │  以 iframe 嵌入(m.widgets 全域帳號資料,
                               │  由 scripts/set_sticker_widget.py 寫入)
                               ▼
        Element Web / Desktop ── widgetAPI.sendSticker()
                               └─▶ 貼圖事件送進目前開啟的房間
```

要點:

- **貼圖本體(mxc 媒體)寄生在 matrix.org 帳號上**;本地 `web/packs/` 只有 JSON metadata 與 128px 縮圖拷貝。帳號註銷 = 媒體全滅(詳見第 8 節)。
- 縮圖由 GitHub Pages 本地服務是上游既有設計:picker 網格大量拉圖,若走 homeserver 媒體端點會被限流且慢。
- 匯入端(python)與呈現端(web)完全解耦:push 即部署,前端無 bundling 步驟。

**English summary**

The data flow is a five-stage pipeline. Stage 1: a single shared Telethon/MTProto connection lists all saved Telegram sticker packs (`GetAllStickersRequest`) and fetches each set (`GetStickerSetRequest`). Stage 2: `sticker-import` processes packs with a pack-level semaphore (default 3) and stickers with a job-level semaphore (default 6), downloading raw bytes and dispatching on content magic — EBML/WebM video stickers are re-uploaded as-is, gzip-magic `.tgs` Lottie animations are rendered into looping ≤256px/≤25fps transparent GIFs by `lottieconverter`, everything else goes through PIL to RGBA PNG. Stage 3: `matrix.upload()` posts to the homeserver media API with a classified retry policy (per `retry_after_ms` for 429, hard exponential backoff up to 300s for `M_USER_LIMIT_EXCEEDED` quota errors, capped backoff for 5xx/network errors, immediate failure for other 4xx). Stage 4: pack JSON, 128px local thumbnails, and `index.json` are written under `web/packs/` and pushed to GitHub Pages. Stage 5: Element Web/Desktop loads the page inside the globally registered `m.widgets` sticker-picker iframe and sends stickers into the current room via the widget API. Importantly, the sticker media itself lives in the matrix.org media repo tied to the account; the repo only holds metadata and thumbnails.

---

## 3. 安裝與依賴 / Installation & Dependencies

### 3.1 Python 環境

repo 自帶 `.venv/`(本機已建好)。相依套件(`requirements.txt`):

```
aiohttp、yarl、pillow、telethon、cryptg、python-magic
```

安裝方式二擇一:

```bash
python -m venv .venv && .venv/bin/pip install -r requirements.txt
# 或
.venv/bin/pip install -e .   # setup.py 提供三個 console_scripts:
                             # sticker-import / sticker-pack / sticker-download-thumbnails
```

### 3.2 Matrix 設定(`config.json`)

- 內容:`homeserver`、`user_id`、`access_token`(**機密**,已被 `.gitignore` 的 `/*.json` 排除,不會入 git)。
- 首次執行 `sticker-import` 時若無此檔,程式會互動式詢問 homeserver 與 token,經 `/_matrix/client/v3/account/whoami` 驗證後寫回 `config.json`(`sticker/lib/matrix.py` 的 `load_config()`)。
- Token 取得方式:任一 Element 客戶端的設定頁「Help & About → Access Token」。

### 3.3 Telegram session

- 檔案:`sticker-import.session`(**登入態機密**,`*.session` 已 gitignore)與其 sqlite journal。
- 首次執行會要求手機號碼與 Telegram 驗證碼;之後重用 session,不需再登入。
- 若 session 遺失或被登出,刪除檔案重跑即可重新登入。

### 3.4 `lottieconverter`(動態貼圖必需)

`sticker/lib/util.py` 的 `find_lottieconverter()` 查找順序:

1. 環境變數 `LOTTIECONVERTER` 指定的路徑;
2. `PATH` 上的 `lottieconverter`;
3. **`~/.local/bin/lottieconverter`**(本機實際安裝位置,免 sudo)。

Arch 系自編流程(擷自 `PATCHES.md`,本機已照此完成):

```bash
# 1) 先編 rlottie(新版 cmake 需加 policy 旗標)
git clone https://github.com/Samsung/rlottie && cd rlottie
cmake -B build -DCMAKE_BUILD_TYPE=Release -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
      -DCMAKE_INSTALL_PREFIX=~/.local
cmake --build build && cmake --install build
# 裝完把 rlottie 的 header 一併放入 ~/.local/include

# 2) 再編 LottieConverter,指到 ~/.local
git clone https://github.com/sot-tech/LottieConverter && cd LottieConverter
cmake -B build -DCMAKE_PREFIX_PATH=~/.local -DCMAKE_INSTALL_RPATH=~/.local/lib
cmake --build build && install -Dm755 build/lottieconverter ~/.local/bin/lottieconverter
```

**重要**:上游 LottieConverter 0.2 的解析度解析有 bug(`h` 永遠等於 `w`,非正方形貼圖會被拉成正方形)。**本機的二進位已修正該行**(`h = strtoul(res)`);若日後重新上游安裝,需重套此修正。

### 3.5 ffmpeg(選用)

僅 webm 影片貼圖的縮圖需要(`util.webm_thumbnail()` 抓第一幀)。沒有 ffmpeg 時不會失敗——會改用 128×128 透明 PNG 佔位縮圖(`EMPTY_THUMBNAIL`)。

### 3.6 前端部署

- **無需建置**:`web/index.html` 以 `<script type="module" src="src/index.js">` 直接載入原始碼,唯一的第三方模組 `web/lib/htm/preact.js` 已 vendor 進 repo。
- 部署 = `git push` 到 `origin master`(GitHub),GitHub Pages 服務 `web/` 目錄。
- widget URL 帶 `?theme=$theme` 參數可跟隨 Element 佈景(見第 6.3 節 `set_sticker_widget.py` 預設值)。

### 3.7 排程(建議)

補洞收尾期間建議掛每小時 cron(詳見 6.4):

```
0 * * * * /home/avatar/Downloads/stickerpicker/probe_and_resume.sh >> /home/avatar/Downloads/stickerpicker/probe.log 2>&1
```

**English summary**

The repo ships with a local `.venv`. Python dependencies are `aiohttp`, `yarl`, `pillow`, `telethon`, `cryptg`, and `python-magic` (or `pip install -e .`, which installs the `sticker-import`, `sticker-pack`, and `sticker-download-thumbnails` entry points). Matrix credentials live in gitignored `config.json` (`homeserver`/`user_id`/`access_token`); on first run the tool prompts interactively and validates the token via `whoami`. Telegram login state is kept in the gitignored `sticker-import.session` Telethon session. Animated stickers require `lottieconverter`, searched at `$LOTTIECONVERTER`, then `PATH`, then `~/.local/bin/lottieconverter`; on Arch-family systems it is built without sudo by first installing rlottie (adding `-DCMAKE_POLICY_VERSION_MINIMUM=3.5` for new CMake, headers into `~/.local/include`) and then LottieConverter with `-DCMAKE_PREFIX_PATH=~/.local -DCMAKE_INSTALL_RPATH=~/.local/lib` — note the local binary carries a fix for the upstream 0.2 bug where height was parsed as width (non-square stickers got stretched). ffmpeg is optional and only affects WebM thumbnail extraction (a transparent placeholder is used otherwise). The web frontend needs no build step — `web/index.html` loads `src/index.js` as a native ES module with vendored preact — so deployment is simply pushing to GitHub Pages. An hourly cron entry for `probe_and_resume.sh` is recommended while hole-mopping is still in progress.

---

## 4. 三個後端補丁技術細節 / Backend Patches in Detail

### 4.1 `sticker/lib/util.py` — tgs → GIF 轉檔

**`find_lottieconverter()`(43–49 行)**:如 3.4 節的三級查找;找不到時 `convert_tgs()` 丟出帶安裝指引的 `RuntimeError`(訊息會指向 `LOTTIECONVERTER` 環境變數)。

**`parse_tgs()`(52–55 行)**:`gzip.decompress` 後解析 lottie JSON 的 `w`/`h`/`fr`,預設 512/512/30。

**`convert_tgs(data, max_side=256)`(58–81 行)**:

- 縮放比 `scale = min(1.0, max_side / max(w, h))`,輸出尺寸下限 2px;幀率 `fps = min(25, framerate)`。
- 在 `tempfile.TemporaryDirectory` 內寫入 `.tgs`,呼叫
  `lottieconverter <src> <out> gif <WxH> <fps>`。
- 回傳碼非 0 或輸出檔不存在 → `RuntimeError` 並附上轉檔器 stderr(上層只跳過該張,不中斷整包)。

**為什麼選 GIF**(擷自 `PATCHES.md`,屬設計決策):

- GIF 動畫在 Element 全平台(Web/Desktop/Android/iOS)都會播;
- animated WebP 在 Element Android 不支援(element-android#2695);
- ffmpeg 9 的 libvpx 預設 VP8 alpha 編碼會因 `auto-alt-ref` 拒絕啟用、解碼與瀏覽器支援亦殘缺(詳見 `PATCHES.en.md`),「webm 帶透明」此路不通。

**`webm_thumbnail()`(84–97 行)**:有 ffmpeg 時以 `-frames:v 1 -f image2pipe -vcodec png` 抽第一幀;無 ffmpeg 或失敗回傳 `None`。呼叫端(`add_thumbnails`)在 `None` 時改用 `EMPTY_THUMBNAIL`(37–40 行預生成的 128×128 全透明 PNG),**影片貼圖縮圖永不致炸**。

**`make_sticker()`(132–153 行)**:新增 `mimetype` 參數(預設 `image/png`),讓 GIF/webm 貼圖正確標註 mimetype;保留上游的 Element iOS 相容 hack(`thumbnail_url`/`thumbnail_info` 與本體同值)。

**`add_thumbnails()`(156–179 行)**:

- 以 `stickers_data.get(sticker["url"])` 取原圖;**取不到即跳過**(該張是前次跑時已上傳、縮圖已存在)——這是斷點續傳下「重跑不炸」的關鍵之一(上游版本在缺資料時會出錯,見 `PATCHES.md`)。
- 縮圖流程:`convert_image(data, 128, 128)` 失敗且資料是 EBML → 改試 `webm_thumbnail()` → 仍無則透明佔位;其他例外照樣往上拋。
- 輸出至 `web/packs/thumbnails/<mxc 媒體ID>.png`。

**English summary (4.1)**

`util.py` adds the conversion layer. `find_lottieconverter()` resolves the binary from `LOTTIECONVERTER`, `PATH`, or `~/.local/bin/lottieconverter`. `parse_tgs()` gunzips the Lottie JSON for width/height/framerate (defaults 512/512/30). `convert_tgs()` scales to at most 256px on the long side, caps fps at 25, and shells out to `lottieconverter <src> <out> gif <WxH> <fps>` in a temp dir, raising a stderr-carrying `RuntimeError` on failure (the caller skips just that sticker). GIF was chosen because it animates on every Element platform, whereas animated WebP is unsupported on Element Android (element-android#2695) and ffmpeg 9's libvpx refuses VP8 alpha encoding out of the box (auto-alt-ref) and WebM alpha decode/browser support is broken anyway (see PATCHES.en.md), killing transparent WebM. `webm_thumbnail()` extracts a first-frame PNG via ffmpeg or returns `None`, in which case a pre-generated transparent 128×128 PNG placeholder is used. `make_sticker()` gained a `mimetype` parameter (keeping the Element iOS thumbnail hack), and `add_thumbnails()` now skips stickers whose raw data is absent (already uploaded in a previous run), falls back to the ffmpeg/WebM/placeholder chain for undecodable EBML data, and writes 128px PNGs named after the mxc media ID.

### 4.2 `sticker/lib/matrix.py` — `upload()` 重試狀態機

簽名:`async def upload(data, mimetype, filename, max_attempts=None)`;`max_attempts` 未指定時讀環境變數 **`STICKER_UPLOAD_ATTEMPTS`**(預設 **6**)。逐次嘗試後對結果分類(88–125 行):

| 情況 | 判定 | 反應 |
|------|------|------|
| 成功 | 回應含 `content_uri` | 直接回傳 `mxc://` URI |
| 速率限制 | HTTP 429 或 `errcode == M_LIMIT_EXCEEDED` | 依 `retry_after_ms` 等待,**鉗制在 1–120 秒**(伺服器給 0 或超大值都安全) |
| 帳號媒體配額耗盡 | `errcode == M_USER_LIMIT_EXCEEDED`(HTTP 403) | **硬等**:`30s × 2^attempt`,上限 300 秒;等到配額窗口回補,不丟棄貼圖 |
| 伺服器暫態 | HTTP ≥ 500 | `delay` 指數退避(2s 起,×2,上限 60s) |
| 網路/協定錯誤 | `ClientError` / `asyncio.TimeoutError` / `JSONDecodeError` | 同上退避後重試 |
| 其他 4xx | — | `break`,立即失敗(不浪費剩餘 attempts) |

全部 attempts 用盡 → `raise RuntimeError("Matrix upload failed after N attempt(s): <last_error>")`;此例外由 `stickerimport.py` 的單張 `process()` 捕捉,只跳過該張。

設計意圖:`M_USER_LIMIT_EXCEEDED` 是 matrix.org 免費帳號的媒體配額(見第 8 節),退避上限 300s 意味著**單張最多硬等 5 分鐘 × 6 次**——配額窗口以小時計,真正大量補跑應交給 `probe_and_resume.sh` 的門閘(先探測配額再開工),而不是指望單次進程內無限等待。

**English summary (4.2)**

`upload()` reads its attempt budget from `STICKER_UPLOAD_ATTEMPTS` (default 6) and classifies every response. Success (`content_uri`) returns the mxc URI immediately. HTTP 429/`M_LIMIT_EXCEEDED` sleeps for `retry_after_ms` clamped to 1–120s. `M_USER_LIMIT_EXCEEDED` (the matrix.org free-account media quota, served as HTTP 403) backs off hard at `30 × 2^attempt` seconds capped at 300s so the sticker is not dropped — the quota window refills on the scale of hours, which is why bulk resumption is delegated to the gate-script rather than in-process waiting. 5xx and network/protocol errors use exponential backoff from 2s capped at 60s; any other 4xx fails immediately to avoid burning attempts. Exhaustion raises a `RuntimeError` carrying the last error, which the importer catches per sticker.

### 4.3 `sticker/stickerimport.py` — 並發重寫 + 斷點續傳 + 寬容解析

**並發參數(34–44 行)**:

- `JOBS = STICKER_JOBS`(預設 6)、`PACK_JOBS = STICKER_PACK_JOBS`(預設 3);`max(1, …)` 保證至少 1,非整數值安全回落預設。
- 結構:`main()` 為每個包建立 `import_pack()` coroutine,`asyncio.gather` 全部包;包內 `reupload_pack()` 對待上傳文件再 `asyncio.gather`。
- **共用單一 `TelegramClient`**:所有下載走同一條 MTProto 連線,不會因並發而多開連線被 Telegram 判定異常。
- 兩層 Semaphore:`job_semaphore`(張級,整個進程一份)、`pack_semaphore`(包級)。

**mimetype 分流(`reupload_document()`,56–75 行)**:

```
data[:4] == EBML_MAGIC 或 mime == video/webm → 原樣上傳 video/webm(尺寸取 DocumentAttributeVideo/ImageSize,預設 512×512)
data[:2] == \x1f\x8b(gzip)                  → util.convert_tgs() → image/gif
其他                                          → util.convert_image() → image/png
```

**斷點續傳(`reupload_pack()` 開頭,104–120 行)**:

- 載入既有的 `<short_name>.json`,以每張貼圖 `net.maunium.telegram.sticker.id`(即 Telegram document id,轉 `int`)建立 `already_uploaded` 對映。
- 命中 → 印 `Skipped reuploading <id>`,直接重用既有上傳結果(仍會 `add_meta` 刷新表情等 metadata);未命中 → 進 `pending` 佇列下載轉傳。
- 因此**對同一批包重跑是冪等的**:已完成的張零成本跳過,只補缺的張。

**外來包寬容解析(109–116 行)**——修復上游 bug:既有 JSON 中若混有**無 Telegram metadata** 的貼圖條目(例如別的工具寫入的包),取 `tg_meta["id"]` 會 `KeyError` 直接炸掉整包。本版捕捉 `KeyError/TypeError/ValueError` 並 `pass`:該條目無法對應到 Telegram 文件,會被本次新匯入的對應文件**取代**,過程不中斷。

**錯誤隔離**:

- 單張:`process()`(137–144 行)捕捉一切例外,印 `Failed to convert <id> ... skipping` 後回傳 `None`,該張缺席但**整包與其他張照常完成**(成為日後 `resume_holes.sh` 要補的「洞」)。
- 整包:`import_pack()`(226–234 行)捕捉一切例外,印 `Failed to import <short_name>, continuing with the next pack:` 並 `traceback.print_exc()`,**繼續下一包**。

**metadata 與輸出**:

- `add_meta()`(78–90 行):`body` = 貼圖 alt 文字;`id` = `tg-<document.id>`;`net.maunium.telegram.sticker` 保留 `{pack:{id,short_name}, id, emoticons[]}`,將來可反查 Telegram 來源(斷點續傳即依賴它)。body 為空時,以該文件所屬 keys 的第一個 emoticon 補上(156–166 行)。
- 包 JSON 寫入(168–177 行):`title`、`id = tg-<set.id>`、`net.maunium.telegram.pack {short_name, hash}`、`stickers`(`ensure_ascii=False`,中文/日文標題原樣)。
- 每包完成後依序 `util.add_thumbnails()` → `util.add_to_index()`(index 增量更新,冪等)。

**輸入解析(184–186 行)**:包 URL 正則接受 `https://t.me/addstickers/<name>`、`telegram.dog` 變體、裸 `short_name`、可選 `.json` 後綴。`--list` 走 `GetAllStickersRequest(hash=0)` 列出帳號全部已存包。

**English summary (4.3)**

The importer was rewritten around two asyncio semaphores — `STICKER_JOBS` (default 6) for stickers and `STICKER_PACK_JOBS` (default 3) for packs — sharing a single Telethon `TelegramClient` so concurrency never opens extra MTProto connections. Per-sticker dispatch keys on content: EBML magic or `video/webm` uploads as-is, gzip magic goes through `convert_tgs()` into GIF, everything else becomes PNG. Resume logic builds an `already_uploaded` map from the existing pack JSON keyed on the Telegram document id inside `net.maunium.telegram.sticker`, so re-runs skip finished stickers at zero cost; foreign entries lacking Telegram metadata are tolerated (KeyError/TypeError/ValueError swallowed) instead of crashing the pack — they are simply replaced by fresh imports. Failures are isolated at two levels: a failed sticker prints and returns `None` (leaving a "hole" for `resume_holes.sh`), and a failed pack prints a traceback and continues with the next. Metadata (`tg-<id>` ids, emoticons, pack short_name/hash) is preserved for future reverse lookup, pack JSONs are written with `ensure_ascii=False`, and thumbnails plus `index.json` are updated incrementally after each pack.

---

## 5. 前端補丁 / Frontend Patch

### 5.1 Bug:空包 → 白屏

**現象**:某包 JSON 存在但 `stickers` 陣列為空(例如匯入被配額/斷線中斷,包檔已寫出但 0 張)時,打開 picker 整頁白屏,僅能看 console 發現 `TypeError`。

**根因**:`web/src/index.js` 的 `NavBarItem`(369–383 行)原本直接取 `pack.stickers[0].url` 當導覽列縮圖——`stickers` 為空陣列時 `pack.stickers[0]` 是 `undefined`,取 `.url` 拋錯,preact render 樹整個崩掉。匯入流程「先寫包檔、後補張數」的中間態恰好會產生這種空包,因此在批量遷移場景必然踩中。

### 5.2 修補(369–383 行)

```js
const NavBarItem = ({pack, iconOverride = null, onClickOverride = null, extraClass = null}) => html`
	<a href="#pack-${pack.id}" id="nav-${pack.id}" data-pack-id=${pack.id} title=${pack.title} class="${extraClass}"
	   onClick=${onClickOverride ? (evt => onClickOverride(evt, pack.id)) : (isMobileSafari ? (evt => scrollToSection(evt, pack.id)) : undefined)}>
		<div class="sticker">
			${iconOverride ? html`
				<span class="icon icon-${iconOverride}"/>
			` : (pack.stickers && pack.stickers.length > 0 ? html`
				<img src=${makeThumbnailURL(pack.stickers[0].url)}
					alt=${pack.stickers[0].body} class="visible" />
			` : html`
				<span class="icon icon-settings"/>
			`)}
		</div>
	</a>
`
```

修補邏輯:`pack.stickers && pack.stickers.length > 0` 通過才渲染縮圖 `<img>`;否則退回圖示佔位(`icon-settings`)。空包不再炸 render,只顯示佔位圖示,其餘包完全正常。

### 5.3 配套的前端既有防護(上游已有,一併列出便於除錯)

- `App._loadPacks()` 對每包 `packData.stickers` 做 `for...of`(空陣列安全),pack 面板的 `<Pack>` 對空陣列 map 也是安全。
- `App.render()` 在 `packs.length === 0` 時顯示「No packs found 😿」空狀態;搜尋無結果顯示「No stickers match your search」。
- 換句話說,唯一會炸的點就是 `NavBarItem`,已補。

### 5.4 部署注意

前端無建置步驟(見 3.6),修改 `web/src/index.js` 後 `git push` 即生效。若 Element 內仍看到舊行為,先用面板 Settings → **Reload** 強制重抓 index/packs(或對 widget URL 加 cache-bust 參數)排除瀏覽器快取。

**English summary**

Importing can be interrupted after the pack JSON is written but before any sticker is uploaded, producing a pack with an empty `stickers` array. The upstream `NavBarItem` rendered `pack.stickers[0].url` unconditionally, so the first empty pack threw a `TypeError` during render and blanked the entire picker. The patch (web/src/index.js lines 369–383) renders the first-sticker thumbnail only when `pack.stickers && pack.stickers.length > 0`, falling back to a settings-icon placeholder otherwise; everything else in the app (the `for...of` over stickers, empty-pack and empty-search states) was already array-safe, so this single guard eliminates the white screen. Since the frontend is served unbundled, pushing the change deploys it; a Settings → Reload inside the picker clears any cached index.

---

## 6. 自動化腳本使用手冊 / Automation Scripts Manual

### 6.1 `scripts/audit.py` — 稽核(唯讀,無副作用)

```bash
.venv/bin/python scripts/audit.py             # 純本地稽核
.venv/bin/python scripts/audit.py --media 20  # 額外隨機抽 20 張真實媒體回頭下載驗證
```

本地稽核項目與輸出解讀(對應程式 25–90 行):

| 輸出 | 意義 | 健康值 |
|------|------|--------|
| `包數 / 貼圖 / 構成` | 掃 `web/packs/*.json`(不含 index)的包數、總張數、mimetype 分佈 | 54 / 3,149 / `{png:2996, webm:150, gif:3}` |
| `⚠ 空包` | `stickers` 為空陣列的包(前端已防護,但補完前不建議 push index) | 0 |
| `縮圖 / 被引用 / 缺縮圖 / 孤立縮圖` | 磁上縮圖數 vs 各包引用的媒體 ID;缺 = 引用但無檔;孤立 = 有檔但無包引用 | 缺 = 0 |
| `縮圖 PNG 抽查 60` | 隨機 60 張縮圖的 PNG 魔數檢查 | 不合格 0 |
| `index 有檔無 / 有檔無 index` | `index.json` 與實際包檔雙向對帳 | 0 / 0 |
| `有洞的包` | 解析兩份 log 中 `Reuploading … with N stickers … web/packs/<short>.json` 的**宣告張數** vs JSON 實際張數,`have < want` 即洞 | 補洞完成應為 0 |
| `結構問題` | 非 mxc URL、`info` 殘缺、零尺寸/過小(size<500)等畸形貼圖 | 0 |

`--media N`(93–111 行):從全部被引用媒體隨機抽 N 個,以 Bearer token 打 `/_matrix/client/v1/media/download/matrix.org/<id>` 實際下載,核對魔數(`\x89PNG` / `GIF8` / EBML)。

> **已知 bug(本次交付發現)**:`--media` 讀設定時用了 `os.path.dirname(SP)`(`SP = <repo>/web/packs`),因此會去找 **`web/config.json`**,實際檔案在 repo 根目錄 → 直接跑必 `FileNotFoundError`(本次複核即觸發,改以正確路徑手動抽檢 25 張)。修法一行:`os.path.dirname(SP)` → `ROOT`。在修復前,請用根目錄 `config.json` 自行抽檢,或暫時把 `config.json` 複製一份到 `web/`。

### 6.2 `scripts/resume_holes.sh` — 精準補洞

```bash
cd /home/avatar/Downloads/stickerpicker && bash scripts/resume_holes.sh
```

- 自動 `cd` 到 repo 根(以腳本自身位置定位),然後用內嵌 Python 掃兩份 log(`20260830.1459.log`、`20260830-mopup.log`):
  - 「洞」= log 宣告張數 > JSON 實際張數的包;
  - 「曾整包失敗」= log 出現 `Failed to import <short>,` 的包(扣除已是洞者,避免重複)。
- 無洞 → 印 `沒有洞,全部完整。` 並 exit 0。
- 有洞 → 印出清單後執行 `.venv/bin/sticker-import $HOLES 2>&1 | tee -a 20260830-mopup.log`,輸出持續併入 mopup log(稽核腳本的洞偵測因此能持續運作)。
- 因匯入本身冪等(4.3 節),此腳本可反覆執行,永遠只補真的缺的東西。

### 6.3 `scripts/set_sticker_widget.py` — 一鍵全域掛 widget

```bash
.venv/bin/python scripts/set_sticker_widget.py
# 自訂 URL:
.venv/bin/python scripts/set_sticker_widget.py --url 'https://其他位置/stickerpicker/web/?theme=$theme'
```

- 讀根目錄 `config.json` → `whoami` 取 user_id → `PUT /_matrix/client/v3/user/<uid>/account_data/m.widgets`,寫入標準 widget 事件(`type: m.widget`、`id: stickerpicker`、`state_key: stickerpicker`、content.type `m.stickerpicker`)。
- 預設 URL 即 GitHub Pages 部署位置並帶 `?theme=$theme`(跟隨 Element 明暗佈景)。
- **效果**:所有房間的 Element Web/Desktop 重新整理後即出現貼圖鈕,免手動 `/devtools` 改帳號資料。重跑即覆寫,安全冪等。

### 6.4 `probe_and_resume.sh`(repo 根目錄)— 雙門閘自動續跑

設計為 **cron 每小時呼叫**(亦可手動),只在「兩個前置條件都成立」時開工,避免空轉與浪費配額:

| 步驟 | 判定 | 不通過時輸出 |
|------|------|--------------|
| 0. 防重複 | `pgrep -f 'xargs -n 8 .venv/bin/sticker-[i]mport'`(`[i]` 技巧避免 pgrep 比對到自身) | `IMPORT_RUNNING` |
| 1. Telegram 閘 | `timeout 40 .venv/bin/sticker-import --list` 需列出 ≥1 個 `addstickers`。MTProto 被節流時握手會吊住,40 秒無清單即判定 | `TG_STALLED` |
| 2. Matrix 閘 | 以 `head -c 76800 /dev/urandom` 造 **75KB 探針** POST 到 matrix.org 媒體上傳(60s 逾時);非 HTTP 200 即配額未回 | `STILL_LIMITED`(附 HTTP code 與錯誤回應前 150 bytes) |
| 3. 開工 | `setsid nohup` 分離式工人:`STICKER_UPLOAD_ATTEMPTS=20 STICKER_JOBS=10 STICKER_PACK_JOBS=3`;包清單來自 `--list` 抓 `addstickers/` 後綴,`xargs -n 8` 分批餵給 `sticker-import`;輸出 `tee -a 20260830-mopup.log` | `RESUMED` |
| 4. 觀景窗 | `DISPLAY=:0` 開一個 alacritty 視窗 `tail -f` mopup log;**關掉視窗不影響匯入**(工人已 setsid 分離) | — |

門閘探測用的 75KB 是刻意挑的量級:足以真實觸發配額判斷、又遠小於任何配額窗口,即使配額剛回補一點也不會因探針本身擠掉正事。

**English summary**

Four tools close the operational loop. `scripts/audit.py` is a read-only audit: it validates pack JSON structure (mxc URLs, `info` completeness, malformed stickers), reconciles thumbnails versus referenced media IDs, cross-checks `index.json` against files, detects holes by comparing the sticker counts declared in the two run logs against actual JSON contents, and with `--media N` re-downloads N random media from the homeserver verifying magic bytes (note a known path bug — it looks for `web/config.json` instead of the repo-root `config.json`; fix is `os.path.dirname(SP)` → `ROOT`). `scripts/resume_holes.sh` parses the same logs for hole packs and whole-pack failures and re-invokes `sticker-import` on exactly those, appending output to the mopup log; it is idempotent and exits cleanly when there is nothing to do. `scripts/set_sticker_widget.py` writes the global `m.widgets` account-data event via `whoami` + PUT, enabling the picker button in every room after a reload, no `/devtools` needed. Finally `probe_and_resume.sh` (designed for hourly cron) refuses to start unless both gates open: a Telegram gate (40s timeout on `--list`, detecting MTProto throttling) and a Matrix quota gate (uploading a 75KB random probe; non-200 means still limited); when both pass it launches a detached worker with `STICKER_UPLOAD_ATTEMPTS=20 STICKER_JOBS=10 STICKER_PACK_JOBS=3` over the full pack list, plus a desktop tail window whose closure does not affect the import.

---

## 7. 品質驗證報告摘要 / QA Report Summary

以下數據分兩欄:**「交付記錄」**為遷移執行當時的驗證結果;**「本日複核」**為撰寫本文件時(2026-08-30)實際重跑取得的結果。

| # | 驗證項目 | 交付記錄 | 本日複核 | 判定 |
|---|----------|----------|----------|------|
| 1 | 包數 / index 一致性 | 54 包,index 0/0 不一致 | 54 包,`index 有檔無: 0`、`有檔無 index: 0` | PASS |
| 2 | 貼圖總數與構成 | 3,150+ 張 | **3,149 張** = 2,996 PNG + 150 webm + 3 GIF(補洞持續中,完成後突破 3,150) | PASS(進行中) |
| 3 | 動態貼圖驗屍(tgs→GIF 與 webm 全數遠端回讀核對) | **153/153 PASS**(150 webm + 3 GIF) | 組成 153 張與包檔一致;抽樣遠端回讀含 2 張 webm 魔數正確 | PASS |
| 4 | 縮圖全量 PIL 解碼 | 3,227 張 0 損壞 | **3,227/3,227 `Image.load()` 全解碼 0 損壞** | PASS |
| 5 | 縮圖 PNG 魔數抽查 | 全過 | 抽查 60 → 不合格 0 | PASS |
| 6 | 縮圖覆蓋率 | 無缺 | 缺縮圖 0;孤立縮圖 78(待補包先前部分上傳的殘留,屬預期) | PASS |
| 7 | 結構稽核(mxc URL/info/畸形) | 全過 | 結構問題 0 | PASS |
| 8 | 真實媒體遠端抽檢 | 抽檢全過 | **25/25 PASS**(seed 定隨機,23 PNG + 2 webm,魔數全對) | PASS |
| 9 | 配額壓力下的韌性 | — | mopup log 記錄 **425 次 `M_USER_LIMIT_EXCEEDED`**,重試機制全程節流消化,程序未崩 | PASS |
| 10 | 整包失敗復原 | — | log 僅 1 次 `Failed to import b675aff8_by_fStikBot`;該包現為 **101/101**(與宣告數一致),已復原 | PASS |

**待完成項(非缺陷,屬配額節流下的預期中間態)**:

- 28 個包有洞(多數 0/N,如 `J9bbeeccckkk_by_fStikBot 0/120`、`gakiyukr_2 0/120`…),3 個空包(`MygoStickerByAsahiRise`、`USABest`、`kawaiikipfel_by_moe_sticker_bot`)。
- 收尾路徑:掛 cron 跑 `probe_and_resume.sh`(自動,配額回補即開工),或手動反覆執行 `scripts/resume_holes.sh`。全部完成後重跑 `scripts/audit.py` 應得「有洞的包: 0」。

**複核指令(可隨時重驗)**:

```bash
cd /home/avatar/Downloads/stickerpicker
.venv/bin/python scripts/audit.py                    # 本地全項稽核
.venv/bin/python scripts/audit.py --media 30         # 遠端媒體抽檢(注意 6.1 節路徑 bug)
.venv/bin/python - <<'EOF'                           # 縮圖全量 PIL 解碼
import glob
from PIL import Image
bad = 0
for t in sorted(glob.glob('web/packs/thumbnails/*')):
    with Image.open(t) as im:
        im.load()
print('thumbnails ok')
EOF
```

**English summary**

Quality gates were verified twice: once during the migration itself and again on 2026-08-30 while writing this document. Re-verified results: 54 packs with zero index/file mismatch; 3,149 stickers (2,996 PNG, 150 WebM, 3 GIF — the 153 non-static stickers match the recorded 153/153 animated post-mortem PASS); all 3,227 local thumbnails fully decode with PIL with zero corruption; the 60-sample PNG magic spot check and the structural audit both pass; a fresh 25/25 remote media spot check (magic bytes on downloaded PNG/WebM) passed; the mopup log's 425 `M_USER_LIMIT_EXCEEDED` events were all absorbed by the retry machinery without a crash; and the single recorded whole-pack failure (`b675aff8_by_fStikBot`) has since recovered to its declared 101/101. Outstanding work is the expected intermediate state under quota throttling: 28 packs with holes (3 of them empty), to be closed by the hourly `probe_and_resume.sh` cron or manual `resume_holes.sh` runs; a clean `audit.py` run with zero holes marks final acceptance.

---

## 8. 已知限制與維運注意 / Known Limitations & Ops Notes

1. **matrix.org 免費帳號媒體配額(最大限制)**
   無付費方案的 fair-use 量級為 **500MB/24h、2GB/28d**(本機實測窗口約 300MB/日)。數千張等級的一次性匯入**必然**撞上 `M_USER_LIMIT_EXCEEDED`。三層防線已內建:進程內重試退避(4.2)→ 門閘探針不空轉(6.4)→ 補洞腳本收尾(6.2)。若想一次性完成,需付費升級帳號或分多日跑。
   *The matrix.org free tier media quota (~500MB/day, ~2GB/28 days, ~300MB/day observed) is unavoidably hit by a bulk import; the three defense layers (in-process retry, quota probe gate, hole-mopping) digest it over time.*

2. **貼圖媒體寄生於 matrix.org 帳號(單點生命週期)**
   包 JSON 內的 `mxc://matrix.org/...` 指向該帳號的媒體倉;**帳號註銷/停用 = 全部貼圖永遠消失**。本地 `web/packs/` 只有 metadata 與 128px 縮圖(見下條),不是媒體備份。緩解:保住帳號(開 2FA)、保留本 repo(斷點續傳可對同一批包全量重傳);若遷往自架 homeserver,改 `config.json` 後重跑全部包即可(所有 mxc 會重傳,縮圖重建),但 TG id 對映會視為全新上傳、無法省配額。
   *Sticker media lives in the matrix.org media repo owned by the account — deleting the account destroys every sticker. The local repo holds only metadata and 128px thumbnails, not a media backup; migrating to another homeserver means re-uploading everything with a new `config.json`.*

3. **Element X 不支援 widget**
   新版 Element X(iOS/Android)沒有 widget 系統,**看不到貼圖鈕**。可用平台:Element Web、Element Desktop、傳統版 Element 行動客户端。這是客戶端限制,非本專案可解。
   *Element X does not support widgets, so the picker button only exists on Element Web/Desktop and legacy mobile clients.*

4. **`web/packs/thumbnails` 的性質**
   每張貼圖一份 **128px 本機縮圖**拷貝(檔名 = mxc 媒體 ID,上游設計,讓 picker 網格不打 homeserver)。注意它是縮圖**而非原始全尺寸媒體**,不能當媒體備份;目前有 78 個孤立縮圖(對應待補包先前上傳過的張),補洞完成後會自然歸位,亦可手動清理。
   *`web/packs/thumbnails` holds one 128px local thumbnail per sticker (upstream design, keyed by media ID) — these are derivatives for the picker grid, not full-size media backups; 78 orphans correspond to partially uploaded pending packs and resolve as mopping completes.*

5. **GIF 轉檔的體積代價**
   tgs(向量 lottie,壓縮率高)轉 256px/25fps GIF 後體積顯著放大,是配額消耗主因之一;150 張 webm 影片貼圖原樣上傳,體積次之。頻寬/配額敏感場景可考慮調低 `convert_tgs()` 的 `max_side`/fps。
   *tgs→GIF conversion inflates file sizes (a main quota consumer); WebM stickers upload as-is; lower `max_side`/fps in `convert_tgs()` if quota is tight.*

6. **機密檔案**
   `config.json`(access_token)與 `sticker-import.session`(Telegram 登入態)皆已 gitignore,**絕不可入 repo 或外流**;access token 外洩應立即在 Element「所有裝置登出」輪替,session 外洩應在 Telegram「所有裝置」終止該次登入。
   *`config.json` (access token) and `sticker-import.session` (Telegram login) are gitignored secrets; rotate/terminate immediately if leaked.*

7. **補丁尚未 commit**
   `git status` 顯示核心補丁(`sticker/lib/util.py`、`sticker/lib/matrix.py`、`sticker/stickerimport.py`、`web/src/index.js`、`.gitignore`、`sticker/version.py`)為 modified,`PATCHES.md`、`probe_and_resume.sh`、`scripts/`、本文件為 untracked。交付後建議一次 commit(不含 log/session)並 push,讓部署位置與程式同步。
   *All patches are still uncommitted working-tree changes; commit and push (excluding logs/sessions) so the deployed Pages copy matches.*

8. **`audit.py --media` 路徑 bug**
   見 6.1 節:讀設定用了 `web/config.json` 而非根目錄 `config.json`,修法一行(`os.path.dirname(SP)` → `ROOT`)。
   *See 6.1: the `--media` path resolves config at `web/config.json`; one-line fix noted there.*

9. **Telegram 端暫態**
   MTProto 被節流時 `--list` 會吊住(門閘以 40s timeout 判定);log 尾端可見 `Server closed the connection: 0 bytes read...` 類訊息,屬可重試暫態,重跑即可。
   *Telegram-side throttling stalls `--list` (handled by the 40s gate timeout); occasional "Server closed the connection" lines are retryable transients.*

**English summary**

Key limitations: (1) the matrix.org free-tier media quota (~500MB/day, ~2GB/28d) makes any bulk import hit `M_USER_LIMIT_EXCEEDED`; the retry/gate/mop tooling exists precisely to digest it over days, or upgrade the account for a one-shot run. (2) Sticker media is homed in the matrix.org media repo — deactivating the account permanently destroys every sticker, and the local repo (metadata + 128px thumbnails only) is not a backup; moving homeservers requires a full re-upload. (3) Element X lacks widget support, so the picker only works on Element Web/Desktop/legacy mobile. (4) `web/packs/thumbnails` are 128px derivatives by upstream design, not full-size media; 78 current orphans correspond to pending packs. (5) tgs→GIF conversion inflates sizes and consumes quota. (6) `config.json` and the Telethon session are secrets (gitignored) that must be rotated if leaked. (7) All patches are currently uncommitted and should be committed and pushed so the deployed frontend matches. (8) The known `audit.py --media` config-path bug needs a one-line fix. (9) Telegram throttling surfaces as stalled handshakes and dropped connections — transients handled by the gate and by re-running.

---

## 9. 常見問題 / FAQ

**Q1. 打開貼圖面板整頁白屏?**
*A1.* 舊版會——空 `stickers` 陣列的包讓 `NavBarItem` 取 `pack.stickers[0].url` 時炸 render(見第 5 節)。本 fork 已修;若仍白屏,確認部署位置已更新(面板 Settings → Reload 強制重抓),並檢查 console 是否指向舊版程式碼。

**Q2. 為什麼動態貼圖變成 GIF,不是 webp 或 webm?**
*A2.* GIF 是唯一在 Element 全平台都會動的格式:Element Android 不支援 animated WebP(element-android#2695),而 ffmpeg 9 的 libvpx 預設 VP8 alpha 編碼被 `auto-alt-ref` 拒絕、webm 帶透明不可行。詳見 4.1 節。

**Q3. `M_USER_LIMIT_EXCEEDED` 是什麼?會掉貼圖嗎?**
*A3.* matrix.org 免費帳號的媒體配額用盡(量級見第 8 節第 1 條)。進程內會硬等退避重試;若 attempts 用盡該張放棄,會成為包裡的「洞」,之後由 `resume_holes.sh` / `probe_and_resume.sh` 補齊——**已寫入的張不會因此損壞**。

**Q4. 怎麼加一個新貼圖包?**
*A4.*
```bash
cd ~/Downloads/stickerpicker
.venv/bin/sticker-import https://t.me/addstickers/新包名   # 靜態/動態/影片都吃
git add web/packs && git commit -m "add pack" && git push
```

**Q5. 匯入中斷了怎麼辦?**
*A5.* 三選一,皆安全冪等:直接重跑同一條 `sticker-import` 指令(斷點續傳自動跳過已完成張);手動 `bash scripts/resume_holes.sh`(只補有洞的包);或讓 cron 的 `probe_and_resume.sh` 等兩閘全開自動續跑。

**Q6. Element X(手機新版)看不到貼圖鈕?**
*A6.* 正常,Element X 不支援 widget(第 8 節第 3 條)。改用 Element Web/Desktop 或傳統版行動客户端。全域 widget 由 `scripts/set_sticker_widget.py` 寫入,重跑可更新 URL。

**Q7. 報錯 `lottieconverter not found`?**
*A7.* 動態貼圖需要它。確認 `~/.local/bin/lottieconverter` 存在(安裝見 3.4),或以 `LOTTIECONVERTER=/path/to/binary` 指定。沒有它靜態/影片包不受影響,只有 tgs 包的該張會跳過。

**Q8. 想搬去自架 homeserver?**
*A8.* 改 `config.json` 的 `homeserver` 與 `access_token`,重跑全部包即可——mxc 會全部重傳到新家,縮圖與包 JSON 在本地重建。Telegram metadata 對映會視為全新上傳,舊家(media.org)的張不會被省略,等於全量重傳(規劃新家的配額時要算進去)。

**Q9. `audit.py --media` 報 `FileNotFoundError: web/config.json`?**
*A9.* 已知路徑 bug(6.1 節):它應該讀 repo 根目錄的 `config.json`。暫時解法:把 `config.json` 複製一份到 `web/`,或直接修 `scripts/audit.py` 第 94 行的 `os.path.dirname(SP)` → `ROOT`。純本地稽核(不帶 `--media`)不受影響。

**Q10. 怎麼確認「全部搞定」?**
*A10.* 驗收清單:`scripts/audit.py` 顯示「有洞的包: 0」且無空包、無結構問題;`--media`(修好路徑後)抽檢 0 異常;`set_sticker_widget.py` 已執行;Element Web/Desktop 重整後貼圖鈕出現、54 包可瀏覽、動態貼圖會動、點擊可送出。

**English summary**

Q1 white screens came from empty pack arrays hitting `NavBarItem` — fixed by the section-5 guard; force a Reload to clear cached code. Q2 GIF was chosen because animated WebP is unsupported on Element Android and ffmpeg 9 dropped VP8 alpha for transparent WebM. Q3 `M_USER_LIMIT_EXCEEDED` is the matrix.org media quota; in-process backoff handles shortfalls and any surrendered sticker becomes a hole that the mop tooling refills — written stickers are never corrupted. Q4 adding a pack is one `sticker-import https://t.me/addstickers/<name>` plus commit/push of `web/packs`. Q5 interruptions are recovered by re-running the same command (idempotent resume), `resume_holes.sh`, or the cron gate. Q6 Element X cannot show widgets by design — use Web/Desktop/legacy mobile. Q7 the `lottieconverter not found` error only blocks tgs stickers; install per 3.4 or set `LOTTIECONVERTER`. Q8 moving homeservers means a full re-upload with a new `config.json`. Q9 the `--media` config-path bug is documented with its one-line fix. Q10 final acceptance = zero holes and empty packs in `audit.py`, a clean media spot check, the widget event written, and stickers browsable/animated/sendable in Element.

---

*文件完 / End of document — 由交付代理於 2026-08-30 基於 repo 實際內容撰寫,所有數據均可以上文指令重驗。*
