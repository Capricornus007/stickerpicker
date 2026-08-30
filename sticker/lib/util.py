# maunium-stickerpicker - A fast and simple Matrix sticker picker widget.
# Copyright (C) 2020 Tulir Asokan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
from functools import partial
from io import BytesIO
import gzip
import json
import os
import os.path
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from PIL import Image

from . import matrix

open_utf8 = partial(open, encoding='UTF-8')

# The magic bytes of EBML containers (Matroska/WebM)
EBML_MAGIC = b"\x1a\x45\xdf\xa3"

_empty_thumbnail = BytesIO()
Image.new("RGBA", (128, 128), (0, 0, 0, 0)).save(_empty_thumbnail, "PNG")
# Transparent placeholder for stickers that can't be thumbnailed (e.g. video without ffmpeg)
EMPTY_THUMBNAIL = _empty_thumbnail.getvalue()


def find_lottieconverter() -> Optional[str]:
    path = os.environ.get("LOTTIECONVERTER") or shutil.which("lottieconverter")
    if not path:
        local = os.path.expanduser("~/.local/bin/lottieconverter")
        if os.path.isfile(local):
            path = local
    return path


def parse_tgs(data: bytes) -> Tuple[int, int, int]:
    """Parse a .tgs (gzipped lottie) sticker and return its width, height and framerate."""
    meta = json.loads(gzip.decompress(data))
    return int(meta.get("w", 512)), int(meta.get("h", 512)), int(float(meta.get("fr", 30)))


def convert_tgs(data: bytes, max_side: int = 256) -> Tuple[bytes, int, int]:
    """Convert an animated .tgs (gzipped lottie) sticker into a looping transparent GIF
    using lottieconverter (https://github.com/sot-tech/LottieConverter)."""
    converter = find_lottieconverter()
    if not converter:
        raise RuntimeError("lottieconverter not found. It is required to import animated "
                           "stickers. Install it or point the LOTTIECONVERTER environment "
                           "variable at the binary.")
    width, height, framerate = parse_tgs(data)
    scale = min(1.0, max_side / max(width, height))
    out_w, out_h = max(2, int(width * scale)), max(2, int(height * scale))
    fps = min(25, framerate)
    with tempfile.TemporaryDirectory() as tmp:
        src_path = os.path.join(tmp, "sticker.tgs")
        out_path = os.path.join(tmp, "sticker.gif")
        with open(src_path, "wb") as src_file:
            src_file.write(data)
        proc = subprocess.run([converter, src_path, out_path, "gif",
                               f"{out_w}x{out_h}", str(fps)], capture_output=True)
        if proc.returncode != 0 or not os.path.isfile(out_path):
            stderr = proc.stderr.decode("utf-8", errors="replace").strip()
            raise RuntimeError(f"lottieconverter failed: {stderr}")
        with open(out_path, "rb") as out_file:
            return out_file.read(), out_w, out_h


def webm_thumbnail(data: bytes) -> Optional[bytes]:
    """Extract the first frame of a WebM video sticker as PNG data using ffmpeg."""
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        return None
    with tempfile.TemporaryDirectory() as tmp:
        src_path = os.path.join(tmp, "sticker.webm")
        with open(src_path, "wb") as src_file:
            src_file.write(data)
        proc = subprocess.run([ffmpeg, "-loglevel", "error", "-i", src_path, "-frames:v", "1",
                               "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True)
        if proc.returncode == 0 and proc.stdout:
            return proc.stdout
    return None


def convert_image(data: bytes, max_w=256, max_h=256) -> (bytes, int, int):
    image: Image.Image = Image.open(BytesIO(data)).convert("RGBA")
    new_file = BytesIO()
    image.save(new_file, "png")
    w, h = image.size
    if w > max_w or h > max_h:
        # Set the width and height to lower values so clients wouldn't show them as huge images
        if w > h:
            h = int(h / (w / max_w))
            w = max_w
        else:
            w = int(w / (h / max_h))
            h = max_h
    return new_file.getvalue(), w, h


def add_to_index(name: str, output_dir: str) -> None:
    index_path = os.path.join(output_dir, "index.json")
    try:
        with open_utf8(index_path) as index_file:
            index_data = json.load(index_file)
    except (FileNotFoundError, json.JSONDecodeError):
        index_data = {"packs": []}
    if "homeserver_url" not in index_data and matrix.homeserver_url:
        index_data["homeserver_url"] = matrix.homeserver_url
    if name not in index_data["packs"]:
        index_data["packs"].append(name)
        with open_utf8(index_path, "w") as index_file:
            json.dump(index_data, index_file, indent="  ")
        print(f"Added {name} to {index_path}")


def make_sticker(mxc: str, width: int, height: int, size: int,
                 body: str = "", mimetype: str = "image/png") -> matrix.StickerInfo:
    return {
        "body": body,
        "url": mxc,
        "info": {
            "w": width,
            "h": height,
            "size": size,
            "mimetype": mimetype,

            # Element iOS compatibility hack
            "thumbnail_url": mxc,
            "thumbnail_info": {
                "w": width,
                "h": height,
                "size": size,
                "mimetype": mimetype,
            },
        },
        "msgtype": "m.sticker",
    }


def add_thumbnails(stickers: List[matrix.StickerInfo], stickers_data: Dict[str, bytes], output_dir: str) -> None:
    thumbnails = Path(output_dir, "thumbnails")
    thumbnails.mkdir(parents=True, exist_ok=True)

    for sticker in stickers:
        data = stickers_data.get(sticker["url"])
        if data is None:
            # Sticker was already uploaded in a previous run, its thumbnail already exists
            continue
        try:
            image_data, _, _ = convert_image(data, 128, 128)
        except Exception:
            if data[:4] == EBML_MAGIC:
                frame = webm_thumbnail(data)
                if frame:
                    image_data, _, _ = convert_image(frame, 128, 128)
                else:
                    image_data = EMPTY_THUMBNAIL
            else:
                raise

        name = sticker["url"].split("/")[-1]
        thumbnail_path = thumbnails / name
        thumbnail_path.write_bytes(image_data)
