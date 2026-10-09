"""Migrasi: perbaiki karakter/produk tersimpan yang fotonya masih CHARACTER SHEET.

Karakter lama (disimpan sebelum sensor `sheetfix` dipasang 9 Okt 16:xx) bisa berupa character sheet
15 panel. Kalau sheet ini dipakai sebagai "Karakter Saya", SEMUA render berikutnya menghadapi masalah
identitas: model harus mengarang wajah dari kolase (ada panel samping/belakang) → wajah tidak identik.

Script ini: unduh foto tiap karakter/produk → deteksi sheet → potong panel orangnya → unggah ulang
(dikirim ke chat user → dapat file_id baru) → update DB. Sekali jalan, aman diulang (idempoten).

Pakai:  ./.venv/bin/python tools/fix_saved_chars.py            # semua
        ./.venv/bin/python tools/fix_saved_chars.py Arunika    # pilih nama
"""
from __future__ import annotations

import asyncio
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import sheetfix                                    # noqa: E402
from aiogram import Bot                            # noqa: E402
from aiogram.client.default import DefaultBotProperties  # noqa: E402
from aiogram.enums import ParseMode                # noqa: E402
from aiogram.types import FSInputFile              # noqa: E402
from config import settings                        # noqa: E402
from db import Database                            # noqa: E402

db = Database(settings.db_path)                    # noqa: E402

WORK = Path(settings.work_dir) / "inventory_fix"


async def fix_one(bot: Bot, row: dict) -> str:
    name, fid = row["name"], row["file_id"]
    if not WORK.exists():
        WORK.mkdir(parents=True, exist_ok=True)
    src = WORK / f"{row['id']}_{name}.jpg"
    tg = await bot.get_file(fid)
    await bot.download_file(tg.file_path, src)      # type: ignore[arg-type]
    info = await asyncio.to_thread(sheetfix.analyze_sync, src, settings.promptsmith_base,
                                   settings.promptsmith_key, settings.promptsmith_model)
    if not (info.get("sheet") and info.get("box")):
        return f"✅ {name}: sudah foto biasa (bukan sheet) — tidak perlu diubah"
    panel = await asyncio.to_thread(sheetfix.crop_panel, src, info["box"], src.with_name(src.stem + "_panel.jpg"))
    if not panel:
        return f"⚠️  {name}: terdeteksi sheet tapi panel gagal dipotong — dilewati"
    sent = await bot.send_photo(
        row["telegram_id"], FSInputFile(panel),
        caption=(f"🔧 <b>Karakter \"{name}\" diperbaiki</b>\n\n"
                 f"Foto yang tersimpan ternyata <b>character sheet</b> (banyak panel), jadi setiap render "
                 f"harus mengarang wajah → hasilnya tidak identik. Bot sudah mengambil <b>panel wajahnya</b> "
                 f"dan ini yang sekarang dipakai untuk render. ✅"),
        parse_mode=ParseMode.HTML)
    new_fid = sent.photo[-1].file_id
    ok_set = db.char_set_file_id(int(row["id"]), new_fid)
    tanda = "OK" if ok_set else "GAGAL SIMPAN"
    return f"🔧 {name}: sheet → panel dipotong, file_id diperbarui ({tanda}) {new_fid[:24]}…"


async def main() -> None:
    only = sys.argv[1] if len(sys.argv) > 1 else None
    bot = Bot(settings.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    try:
        rows = [dict(r) for r in db.char_list_all()]        # semua user
        if only:
            rows = [r for r in rows if only.lower() in (r["name"] or "").lower()]
        if not rows:
            print("tidak ada karakter/produk tersimpan yang cocok")
            return
        for r in rows:
            try:
                print(await fix_one(bot, r))
            except Exception as e:                          # noqa: BLE001
                print(f"❌ {r['name']}: {type(e).__name__}: {e}")
    finally:
        await bot.session.close()


if __name__ == "__main__":
    os.chdir(Path(__file__).resolve().parent.parent)
    asyncio.run(main())