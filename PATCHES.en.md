# PATCHES — what this fork changes

English documentation for this fork of
[maunium/stickerpicker](https://github.com/maunium/stickerpicker). The fork adds
**Telegram animated sticker import**, **upload resilience** against homeserver
rate limits and media quotas, and **concurrent importing**. Behavior for static
stickers is unchanged from upstream.

Contents:

1. [What this fork changes](#what-this-fork-changes)
2. [The GIF decision (why animated stickers are GIFs)](#the-gif-decision-why-animated-stickers-are-gifs)
3. [Dependencies and build notes](#dependencies-and-build-notes)
4. [Quota-aware retry design](#quota-aware-retry-design)
5. [Helper scripts manual](#helper-scripts-manual)
6. [Adding new packs day-to-day](#adding-new-packs-day-to-day)

## What this fork changes

### 1. Animated sticker conversion — `sticker/lib/util.py`

- `.tgs` stickers (Telegram animated stickers are gzipped Lottie animations) are
  converted to looping GIFs with
  [LottieConverter](https://github.com/sot-tech/LottieConverter), which renders
  through [rlottie](https://github.com/Samsung/rlottie) — the same rendering
  library Telegram itself uses, so fidelity is high. Output is capped at 256 px
  on the longest side and 25 fps; transparency is preserved. The converter
  binary is located via the `LOTTIECONVERTER` environment variable, then `PATH`,
  then `~/.local/bin/lottieconverter`.
- Video stickers (WebM, detected by EBML magic bytes) are re-uploaded as-is.
  The local thumbnail is the first frame extracted with `ffmpeg`; if `ffmpeg`
  is not installed, a 128x128 transparent PNG placeholder is written instead of
  crashing.
- `make_sticker()` accepts a custom mimetype, so GIF and WebM uploads are no
  longer labelled `image/png`. The upstream Element iOS compatibility hack
  (`thumbnail_url` = sticker URL) is kept.
- `add_thumbnails()` tolerates re-runs: stickers that were already uploaded in a
  previous run have no local image data and are skipped; a WebM sticker whose
  thumbnail cannot be produced falls back to the placeholder.

### 2. Upload resilience — `sticker/lib/matrix.py`

`upload()` retries transparently instead of dropping stickers. The full retry
matrix is documented in [Quota-aware retry design](#quota-aware-retry-design)
below. Attempts are configurable via the `STICKER_UPLOAD_ATTEMPTS` environment
variable (default 6).

### 3. Concurrent import — `sticker/stickerimport.py`

- Rewritten around asyncio semaphores: `STICKER_JOBS` (default 6) stickers move
  through download → convert → upload concurrently, and `STICKER_PACK_JOBS`
  (default 3) packs are processed in parallel. All tasks share a single Telethon
  connection, which is safe for this pattern and keeps one MTProto session.
- Failure isolation: a failed sticker is skipped (logged, the pack still
  completes); a failed pack prints a traceback and the batch continues with the
  next pack.
- Resume works as upstream: an existing pack JSON is indexed by Telegram
  document ID (`net.maunium.telegram.sticker.id`) and matching documents are not
  re-downloaded.
- Two upstream bugs fixed while rewriting:
  1. On re-runs, already-uploaded (skipped) stickers hit an unbound `data`
     variable when thumbnails were generated. Now `stickers_data` only contains
     freshly uploaded stickers and `add_thumbnails()` skips the rest.
  2. Resume parsing crashed with `KeyError` on pack entries lacking Telegram
     metadata (e.g. packs produced by other tools). `KeyError`, `TypeError` and
     `ValueError` are now caught; such entries are simply replaced by the
     freshly imported sticker.

### 4. Operations tooling — `scripts/` and `probe_and_resume.sh`

- `scripts/audit.py` — offline audit of the generated pack data.
- `scripts/resume_holes.sh` — re-imports only packs with holes or that failed
  wholesale.
- `scripts/set_sticker_widget.py` — registers the picker widget account-data
  event without touching `/devtools`.
- `probe_and_resume.sh` — double-gate auto-resume for scheduled (hourly) or
  manual operation.

## The GIF decision (why animated stickers are GIFs)

Telegram animated stickers are `.tgs` files; they must be converted to something
a Matrix client can render. The three candidate formats:

| Format | Verdict |
| --- | --- |
| Animated WebP | Element Android does not animate it — stickers arrive as static frames ([element-android#2695](https://github.com/vector-im/element-android/issues/2695)). Rejected. |
| Transparent WebM (VP8/VP9 alpha) | Encode and decode paths are both broken in practice (details below). Rejected. |
| **GIF** | Plays animated, with transparency, on every platform the widget runs on (Element Web/Desktop/Android/iOS). **Chosen.** |

Why transparent WebM is a dead end:

- The default VP8 alpha encode simply fails. `ffmpeg -c:v libvpx -pix_fmt
  yuva420p` refuses to open the encoder with `Transparency encoding with
  auto_alt_ref does not work` unless `-auto-alt-ref 0` is passed. Upstream
  FFmpeg never actually removed VP8 alpha encoding — current FFmpeg 9 still
  lists `yuva420p` for `libvpx` — but the out-of-the-box encode fails hard,
  which in practice looks exactly like "VP8 alpha encoding is gone".
- Even when encoded, WebM alpha lives in Matroska `BlockAdditional` and is
  widely ignored: FFmpeg's own native VP8/VP9 decoders skip it (upstream added a
  warning about exactly this: [commit
  2ae24134889e](https://github.com/FFmpeg/FFmpeg/commit/2ae24134889e)), and
  browser support is only solid for 4:2:0 alpha ([commit
  33b215d1554a](https://github.com/FFmpeg/FFmpeg/commit/33b215d1554a), which
  marks everything beyond 4:2:0 as experimental).
- GIF has no such support matrix: it animates with 1-bit transparency
  everywhere. The costs — binary transparency instead of full alpha, larger
  files — are acceptable and mitigated by the 256 px / 25 fps caps.

Video stickers are a different case: Telegram's video stickers are already
WebM, Element plays them natively, so they are re-uploaded untouched and only
their thumbnails depend on `ffmpeg`.

## Dependencies and build notes

- `lottieconverter` — required for animated (`.tgs`) stickers.
- `ffmpeg` — needed only for WebM video-sticker thumbnails.
- Python dependencies are unchanged from upstream (Telethon, aiohttp, yarl,
  Pillow).

### Building LottieConverter on Arch-family systems (no sudo)

Install everything into `~/.local`; `find_lottieconverter()` picks up
`~/.local/bin/lottieconverter` automatically.

1. Build [rlottie](https://github.com/Samsung/rlottie) first:

   ```bash
   git clone --recursive https://github.com/Samsung/rlottie
   cmake -S rlottie -B rlottie/build -DCMAKE_BUILD_TYPE=Release \
         -DCMAKE_INSTALL_PREFIX="$HOME/.local" \
         -DCMAKE_POLICY_VERSION_MINIMUM=3.5
   cmake --build rlottie/build -j"$(nproc)"
   cmake --install rlottie/build
   ```

   The `-DCMAKE_POLICY_VERSION_MINIMUM=3.5` flag is mandatory with CMake >= 4.0:
   rlottie's `CMakeLists.txt` declares `cmake_minimum_required(VERSION 3.3)`,
   which modern CMake refuses to configure otherwise. Afterwards make sure the
   rlottie headers landed in `~/.local/include` — LottieConverter compiles
   against them.

2. Build [LottieConverter](https://github.com/sot-tech/LottieConverter):

   ```bash
   git clone https://github.com/sot-tech/LottieConverter
   cmake -S LottieConverter -B LottieConverter/build \
         -DCMAKE_PREFIX_PATH="$HOME/.local" \
         -DCMAKE_INSTALL_RPATH="$HOME/.local/lib"
   cmake --build LottieConverter/build -j"$(nproc)"
   install -Dm755 LottieConverter/build/lottieconverter \
           "$HOME/.local/bin/lottieconverter"
   ```

   `-DCMAKE_INSTALL_RPATH` is what lets the binary find `librlottie.so` in
   `~/.local/lib` without touching `LD_LIBRARY_PATH`.

### Upstream resolution-parsing bug (patched locally)

Upstream (release 0.2 and current master) has a bug in the resolution argument
parsing (`lottie_export.cpp`): after splitting `WxH`, the height is parsed with

```c
h = strtoul(argv[argi], nullptr, 10);
```

which re-parses the full `256x384` string from the beginning, so `h` always ends
up equal to `w` and non-square stickers are stretched into squares. The one-line
fix is to parse the already-prepared buffer that holds the substring after `x`:

```c
h = strtoul(res, nullptr, 10);
```

The local binary carries this fix; unpatched upstream builds will distort any
non-square animated sticker.

## Quota-aware retry design

### The problem: matrix.org media quotas

Free matrix.org accounts are subject to a fair-use media quota: **500 MB per
24-hour period and 2 GB per 28 days** for accounts without a paid plan
([matrix.org homeserver pricing](https://matrix.org/homeserver/pricing/)).
During bulk import the observed effective window was closer to ~300 MB/day.
Large sticker packs blow through this in minutes; the quota exhaustion surfaces
as `403 M_USER_LIMIT_EXCEEDED` from `/_matrix/media/v3/upload`. Dropping
stickers on that error is not acceptable, so `upload()` treats it as a signal to
slow down and let the window refill.

### Retry matrix (`sticker/lib/matrix.py`)

Each upload gets up to `STICKER_UPLOAD_ATTEMPTS` attempts (default 6; each
attempt uses a fresh `aiohttp` session):

| Outcome | Action |
| --- | --- |
| `content_uri` in response | Success, the mxc URI is returned. |
| HTTP 429 / `M_LIMIT_EXCEEDED` | Sleep `retry_after_ms` as provided by the server (fallback 1000 ms), clamped to 1–120 s. |
| `M_USER_LIMIT_EXCEEDED` (media quota) | Hard exponential backoff: `min(30 * 2**attempt, 300)` — 30 s, 60 s, 120 s, 240 s, then a 300 s cap — riding out the refill window instead of failing. |
| HTTP >= 500 | Exponential backoff starting at 2 s, doubling, capped at 60 s. |
| Network error / non-JSON body | Same exponential backoff as 5xx. |
| Any other 4xx | Immediate failure — a bad token or request should not retry-loop. |

When all attempts are exhausted, a `RuntimeError` is raised with the attempt
count and the last error; the concurrent importer turns that into a per-sticker
skip (or per-pack failure), so one exhausted quota never loses the whole batch.

The scheduled worker started by `probe_and_resume.sh` runs with
`STICKER_UPLOAD_ATTEMPTS=20 STICKER_JOBS=10 STICKER_PACK_JOBS=3` — more
patience per upload, more parallelism — because it only launches after both
gates below have confirmed there is quota headroom.

## Helper scripts manual

All scripts run from the repo root. `audit.py` and `resume_holes.sh` parse the
import logs `20260830.1459.log` and `20260830-mopup.log` (hardcoded: the `LOGS`
list at the top of `scripts/audit.py`, and the inline list in
`scripts/resume_holes.sh` — edit those when the log filename changes).

### `scripts/audit.py`

```bash
.venv/bin/python scripts/audit.py            # local audit
.venv/bin/python scripts/audit.py --media 20 # also fetch 20 random stickers and verify
```

Local audit checks, over every pack JSON in `web/packs/` (except `index.json`):

- JSON parse failures, non-`mxc://` sticker URLs, missing/incomplete `info`
  blocks, malformed stickers (zero width/height or size < 500 B).
- Empty packs: the frontend guards against them, but `index.json` should not be
  pushed until they are backfilled.
- Mimetype composition of the corpus.
- Thumbnail coverage in `web/packs/thumbnails/`: missing vs orphaned
  thumbnails, plus a PNG-magic spot check of up to 60 random thumbnail files.
- `index.json` consistency: files listed in the index vs pack files on disk.
- Holes: the sticker count declared in the import logs (`Reuploading ... with N
  stickers and writing output to web/packs/X.json`) versus the count actually
  present in `X.json`.

`--media N` additionally downloads N random stickers from the homeserver via
`/_matrix/client/v1/media/download/matrix.org/{media id}` (authenticated with
`config.json`) and verifies the magic bytes against the declared mimetype (PNG,
GIF, or WebM EBML).

### `scripts/resume_holes.sh`

```bash
bash scripts/resume_holes.sh
```

Parses the same import logs and re-imports only what is incomplete: packs whose
declared sticker count exceeds the actual count (holes), plus packs that failed
wholesale (`Failed to import X,`). If there is nothing to do it prints so and
exits 0; otherwise it lists the packs and runs:

```bash
.venv/bin/sticker-import <packs> 2>&1 | tee -a 20260830-mopup.log
```

### `scripts/set_sticker_widget.py`

```bash
python scripts/set_sticker_widget.py
python scripts/set_sticker_widget.py --url 'https://example.org/stickerpicker/web/?theme=$theme'
```

Writes the global `m.widgets` account-data event directly, so the sticker button
appears in every Element room without editing state via `/devtools`. It reads
`config.json`, resolves the user ID via `/_matrix/client/v3/account/whoami`,
then PUTs an `m.stickerpicker` widget to
`/_matrix/client/v3/user/{user_id}/account_data/m.widgets`. The default widget
URL is `https://capricornus007.github.io/stickerpicker/web/?theme=$theme` —
Element substitutes `$theme`. Reload Element afterwards.

### `probe_and_resume.sh`

```bash
bash probe_and_resume.sh   # manual run; normally invoked by an hourly schedule
```

Starts the mop-up import only when it can actually make progress. Statuses it
prints: `IMPORT_RUNNING` (a worker is already active), `TG_STALLED`,
`STILL_LIMITED`, `RESUMED`.

1. Lock check: an import worker already running (matched via
   `pgrep -f 'xargs -n 8 .venv/bin/sticker-[i]mport'`) → exit without
   duplicating work.
2. Telegram gate: `timeout 40 .venv/bin/sticker-import --list` must list at
   least one pack. A throttled MTProto connection hangs the handshake, so 40 s
   without output means Telegram is not usable this round.
3. Matrix quota gate: uploads a 75 KB random probe file
   (`/tmp/quota-probe.bin`) to
   `https://matrix.org/_matrix/media/v3/upload?filename=quota-probe.bin` using
   the `config.json` token. Anything other than HTTP 200 means the quota has not
   refilled yet (the HTTP status and the first 150 bytes of the response are
   printed).
4. Both gates open → starts a detached worker (`setsid nohup`) with
   `STICKER_UPLOAD_ATTEMPTS=20 STICKER_JOBS=10 STICKER_PACK_JOBS=3` that
   enumerates all saved sticker packs (`sticker-import --list`), imports them in
   batches of 8 (`xargs -n 8`), and appends all output to
   `20260830-mopup.log`. It also opens an alacritty window tailing the log;
   closing that window does not affect the import, which is detached from the
   session.

## Adding new packs day-to-day

```bash
cd ~/Downloads/stickerpicker   # or your repo path
.venv/bin/sticker-import https://t.me/addstickers/PackName   # animated/static/video all accepted
git add web/packs && git commit -m "add pack" && git push
```

- Multiple pack URLs per invocation work, as do bare pack short names; the URL
  forms `t.me/addstickers/NAME`, `telegram.me/addstickers/NAME` and
  `telegram.dog/addstickers/NAME` are all accepted (upstream regex).
- `--list` shows the packs saved on the Telegram account.
- After large imports, run `scripts/audit.py` and then `scripts/resume_holes.sh`
  until it reports no holes; only push `index.json` once packs are complete.
- Concurrency is tuned with `STICKER_JOBS` and `STICKER_PACK_JOBS`. On free
  matrix.org accounts a bulk import will hit the fair-use window (500 MB/24 h,
  2 GB/28 days); the retry logic self-throttles through it, and the hourly
  `probe_and_resume.sh` drains whatever is left once quota returns.
