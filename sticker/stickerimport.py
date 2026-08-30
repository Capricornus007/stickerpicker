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
from typing import Dict, Optional, Tuple
import argparse
import asyncio
import os
import os.path
import json
import re
import traceback

from telethon import TelegramClient
from telethon.tl.functions.messages import GetAllStickersRequest, GetStickerSetRequest
from telethon.tl.types.messages import AllStickers
from telethon.tl.types import (InputStickerSetShortName, Document, DocumentAttributeSticker,
                               DocumentAttributeVideo, DocumentAttributeImageSize)
from telethon.tl.types.messages import StickerSet as StickerSetFull

from .lib import matrix, util

# How many stickers are downloaded/converted/uploaded concurrently and how many packs
# are processed at the same time. Override with the STICKER_JOBS and STICKER_PACK_JOBS
# environment variables.
try:
    JOBS = max(1, int(os.environ.get("STICKER_JOBS", "6")))
except ValueError:
    JOBS = 6
try:
    PACK_JOBS = max(1, int(os.environ.get("STICKER_PACK_JOBS", "3")))
except ValueError:
    PACK_JOBS = 3


def get_document_dimensions(document: Document) -> Tuple[int, int]:
    for attr in document.attributes:
        if isinstance(attr, DocumentAttributeVideo) and attr.w and attr.h:
            return attr.w, attr.h
        elif isinstance(attr, DocumentAttributeImageSize) and attr.w and attr.h:
            return attr.w, attr.h
    return 512, 512


async def reupload_document(client: TelegramClient, document: Document) -> Tuple[matrix.StickerInfo, bytes]:
    """Download, convert and reupload a single sticker."""
    print(f"Reuploading {document.id}", end="", flush=True)
    data = await client.download_media(document, file=bytes)
    print(".", end="", flush=True)
    if data[:4] == util.EBML_MAGIC or document.mime_type == "video/webm":
        # Video stickers are reuploaded as-is
        width, height = get_document_dimensions(document)
        mimetype, filename = "video/webm", f"{document.id}.webm"
    elif data[:2] == b"\x1f\x8b":
        # Animated stickers are gzipped lottie animations, convert them to looping GIFs
        data, width, height = util.convert_tgs(data)
        mimetype, filename = "image/gif", f"{document.id}.gif"
    else:
        data, width, height = util.convert_image(data)
        mimetype, filename = "image/png", f"{document.id}.png"
    print(".", end="", flush=True)
    mxc = await matrix.upload(data, mimetype, filename)
    print(".", flush=True)
    return util.make_sticker(mxc, width, height, len(data), mimetype=mimetype), data


def add_meta(document: Document, info: matrix.StickerInfo, pack: StickerSetFull) -> None:
    for attr in document.attributes:
        if isinstance(attr, DocumentAttributeSticker):
            info["body"] = attr.alt
    info["id"] = f"tg-{document.id}"
    info["net.maunium.telegram.sticker"] = {
        "pack": {
            "id": str(pack.set.id),
            "short_name": pack.set.short_name,
        },
        "id": str(document.id),
        "emoticons": [],
    }


async def reupload_pack(client: TelegramClient, pack: StickerSetFull, output_dir: str,
                        job_semaphore: Optional[asyncio.Semaphore] = None) -> None:
    pack_path = os.path.join(output_dir, f"{pack.set.short_name}.json")
    try:
        os.mkdir(os.path.dirname(pack_path))
    except FileExistsError:
        pass

    print(f"Reuploading {pack.set.title} with {pack.set.count} stickers "
          f"and writing output to {pack_path}", flush=True)

    already_uploaded = {}
    try:
        with util.open_utf8(pack_path) as pack_file:
            existing_pack = json.load(pack_file)
            for sticker in existing_pack["stickers"]:
                tg_meta = sticker.get("net.maunium.telegram.sticker") or {}
                try:
                    already_uploaded[int(tg_meta["id"])] = sticker
                except (KeyError, TypeError, ValueError):
                    # Sticker without Telegram metadata (e.g. from another tool):
                    # it can't be matched to a Telegram document and will be
                    # replaced by the freshly imported one.
                    pass
            if already_uploaded:
                print(f"Found {len(already_uploaded)} already reuploaded stickers", flush=True)
    except FileNotFoundError:
        pass

    if job_semaphore is None:
        job_semaphore = asyncio.Semaphore(JOBS)

    stickers_data: Dict[str, bytes] = {}
    reuploaded_documents: Dict[int, matrix.StickerInfo] = {}
    pending: list = []
    for document in pack.documents:
        cached = already_uploaded.get(document.id)
        if cached is not None:
            reuploaded_documents[document.id] = cached
            add_meta(document, cached, pack)
            print(f"Skipped reuploading {document.id}", flush=True)
        else:
            pending.append(document)

    async def process(document: Document) -> Optional[Tuple[matrix.StickerInfo, bytes]]:
        async with job_semaphore:
            try:
                return await reupload_document(client, document)
            except Exception as e:
                print(f"\nFailed to convert {document.id} ({document.mime_type}): {e!r}, skipping",
                      flush=True)
                return None

    if pending:
        results = await asyncio.gather(*(process(document) for document in pending))
        for document, result in zip(pending, results):
            if result is None:
                continue
            info, data = result
            add_meta(document, info, pack)
            reuploaded_documents[document.id] = info
            stickers_data[info["url"]] = data

    for sticker in pack.packs:
        if not sticker.emoticon:
            continue
        for document_id in sticker.documents:
            doc = reuploaded_documents.get(document_id)
            if doc is None:
                continue
            # If there was no sticker metadata, use the first emoji we find
            if doc["body"] == "":
                doc["body"] = sticker.emoticon
            doc["net.maunium.telegram.sticker"]["emoticons"].append(sticker.emoticon)

    with util.open_utf8(pack_path, "w") as pack_file:
        json.dump({
            "title": pack.set.title,
            "id": f"tg-{pack.set.id}",
            "net.maunium.telegram.pack": {
                "short_name": pack.set.short_name,
                "hash": str(pack.set.hash),
            },
            "stickers": list(reuploaded_documents.values()),
        }, pack_file, ensure_ascii=False)
    print(f"Saved {pack.set.title} as {pack.set.short_name}.json", flush=True)

    util.add_thumbnails(list(reuploaded_documents.values()), stickers_data, output_dir)
    util.add_to_index(os.path.basename(pack_path), output_dir)


pack_url_regex = re.compile(r"^(?:(?:https?://)?(?:t|telegram)\.(?:me|dog)/addstickers/)?"
                            r"([A-Za-z0-9-_]+)"
                            r"(?:\.json)?$")

parser = argparse.ArgumentParser()

parser.add_argument("--list", help="List your saved sticker packs", action="store_true")
parser.add_argument("--session", help="Telethon session file name", default="sticker-import")
parser.add_argument("--config",
                    help="Path to JSON file with Matrix homeserver and access_token",
                    type=str, default="config.json")
parser.add_argument("--output-dir", help="Directory to write packs to", default="web/packs/",
                    type=str)
parser.add_argument("pack", help="Sticker pack URLs to import", action="append", nargs="*")


async def main(args: argparse.Namespace) -> None:
    await matrix.load_config(args.config)
    client = TelegramClient(args.session, 298751, "cb676d6bae20553c9996996a8f52b4d7")
    await client.start()

    if args.list:
        stickers: AllStickers = await client(GetAllStickersRequest(hash=0))
        index = 1
        width = len(str(len(stickers.sets)))
        print("Your saved sticker packs:")
        for saved_pack in stickers.sets:
            print(f"{index:>{width}}. {saved_pack.title} "
                  f"(t.me/addstickers/{saved_pack.short_name})")
            index += 1
    elif args.pack[0]:
        input_packs = []
        for pack_url in args.pack[0]:
            match = pack_url_regex.match(pack_url)
            if not match:
                print(f"'{pack_url}' doesn't look like a sticker pack URL")
                return
            input_packs.append(InputStickerSetShortName(short_name=match.group(1)))

        job_semaphore = asyncio.Semaphore(JOBS)
        pack_semaphore = asyncio.Semaphore(PACK_JOBS)

        async def import_pack(input_pack: InputStickerSetShortName) -> None:
            async with pack_semaphore:
                try:
                    pack: StickerSetFull = await client(GetStickerSetRequest(input_pack, hash=0))
                    await reupload_pack(client, pack, args.output_dir, job_semaphore)
                except Exception:
                    print(f"Failed to import {input_pack.short_name}, "
                          f"continuing with the next pack:", flush=True)
                    traceback.print_exc()

        await asyncio.gather(*(import_pack(input_pack) for input_pack in input_packs))
    else:
        parser.print_help()

    await client.disconnect()


def cmd() -> None:
    asyncio.run(main(parser.parse_args()))


if __name__ == "__main__":
    cmd()
