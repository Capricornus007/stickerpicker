# 本 fork 的修改紀錄(PATCHES)

這是 maunium/stickerpicker 的 fork,在原版基礎上加了 **Telegram 動態貼圖搬運**、
**上傳韌性**與**並發匯入**。以下為所有改動,原始版行為對靜態貼圖完全相容。

## 改了什麼

### `sticker/lib/util.py`
- **`.tgs` 動態貼圖 → 迴圈 GIF**:tgs 是 gzip 過的 lottie 動畫,用
  [lottieconverter](https://github.com/sot-tech/LottieConverter)(底層 rlottie,
  與 Telegram 同款渲染器)轉成 256px 內、保留透明、最高 25fps 的 GIF。
  選 GIF 是因為它動畫在 Element 全平台(Web/Desktop/Android/iOS)都會播;
  animated WebP 在 Element Android 不支援(element-android#2695),
  而 ffmpeg 9 的 libvpx 已移除 VP8 alpha 編碼,webm 帶透明此路不通。
- **webm 影片貼圖縮圖**:無 ffmpeg 時以透明佔位圖代替,不會炸。
- `make_sticker()` 支援自訂 mimetype;`add_thumbnails()` 容忍重跑時缺資料的貼圖。

### `sticker/lib/matrix.py`
- `upload()` 自動重試:`429 M_LIMIT_EXCEEDED`(照 `retry_after_ms` 等)、
  `403 M_USER_LIMIT_EXCEEDED`(matrix.org 帳號媒體配額,30s→300s 指數退避硬等)、
  5xx 與網路錯誤(指數退避);其他 4xx 立即失敗。
  重試次數可用環境變數 `STICKER_UPLOAD_ATTEMPTS`(預設 6)調整。
- matrix.org 免費帳號媒體配額:無方案 fair-use 為 500MB/24h、2GB/28d
  (實測窗口 300MB/日),大量匯入必然會撞,重試邏輯會自動節流消化。

### `sticker/stickerimport.py`(並發重寫)
- `STICKER_JOBS`(預設 6)張貼圖同時「下載→轉檔→上傳」,
  `STICKER_PACK_JOBS`(預設 3)包同時處理;共用單一 Telethon 連線,安全。
- 單張失敗只跳過該張;整包失敗印 traceback 後繼續下一包;斷點續傳照舊。
- 修復原版兩個 bug:重跑時 skipped 路徑 `data` 未賦值會炸;
  resume 解析遇到無 Telegram metadata 的外來貼圖條目會 KeyError。

## 轉檔依賴

- `lottieconverter`:Arch 系可自編安裝到 `~/.local`(免 sudo):
  先編 [rlottie](https://github.com/Samsung/rlottie)(
  新版 cmake 需加 `-DCMAKE_POLICY_VERSION_MINIMUM=3.5`,裝完記得把 header 一併放入
  `~/.local/include`),再編 LottieConverter 並加
  `-DCMAKE_PREFIX_PATH=~/.local -DCMAKE_INSTALL_RPATH=~/.local/lib`。
  **注意**:上游 0.2 的解析度解析有 bug(`h` 永遠等於 `w`,非正方形貼圖會被拉成正方形),
  本機的二進位已修正(`h = strtoul(res)` 那行)。
- `ffmpeg`:僅 webm 縮圖需要。

## 附屬腳本(`scripts/`)

- `audit.py`:稽核本地包資料(結構/縮圖/index/洞),`--media N` 加抽真實媒體。
- `resume_holes.sh`:只重新匯入「有洞」與「曾整包失敗」的包。
- `set_sticker_widget.py`:一鍵寫入全域 `m.widgets`,Element 重新整理即有貼圖鈕,
  免手動 `/devtools`。

## 日常加新包

```bash
cd ~/Downloads/stickerpicker   # 或你的 repo 路徑
.venv/bin/sticker-import https://t.me/addstickers/新包名   # 動態/靜態/影片都吃
git add web/packs && git commit -m "add pack" && git push
```
