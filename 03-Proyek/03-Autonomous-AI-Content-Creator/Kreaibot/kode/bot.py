#!/usr/bin/env python3
"""Kreaibot — bot Telegram studio konten AI (karakter konsisten → video).

Jalankan:  python3 bot.py            (produksi)
           python3 bot.py --check    (validasi konfigurasi + isi katalog, tanpa Telegram)
"""
from __future__ import annotations

import asyncio
import json
import logging
import sys
import time
from pathlib import Path

from aiogram import Bot, Dispatcher, F, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (CallbackQuery, FSInputFile, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message)

import catalog
from backends import GenRequest, GenStatus, make_backend
from config import settings
from db import Database

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(name)s: %(message)s")
log = logging.getLogger("kreaibot")

db = Database(settings.db_path)
backend = make_backend(settings.backend, api_key=settings.runninghub_api_key,
                       base=settings.runninghub_base, work_dir=settings.work_dir)
router = Router()
SEM = asyncio.Semaphore(settings.concurrency)

# ============================ util ============================

def bar(pct: int, n: int = 10) -> str:
    fill = max(0, min(n, round(pct / 100 * n)))
    return "🟩" * fill + "⬜" * (n - fill)


def saldo_txt(tid: int) -> str:
    return f"💰 Sisa saldo: <b>{db.balance(tid):.1f} Token</b>"


def main_menu_kb() -> InlineKeyboardMarkup:
    rows = []
    for f in catalog.FEATURES.values():
        rows.append([InlineKeyboardButton(text=f"{f.label} — {f.cost:g} Token",
                                          callback_data=f"m:feat:{f.key}")])
    rows.append([InlineKeyboardButton(text="⚡ Top Up Token", callback_data="m:topup"),
                 InlineKeyboardButton(text="💳 Saldo", callback_data="m:saldo")])
    rows.append([InlineKeyboardButton(text="📖 Panduan", callback_data="m:help"),
                 InlineKeyboardButton(text="👥 Referral", callback_data="m:ref")])
    return InlineKeyboardMarkup(inline_keyboard=rows)


def back_kb(extra: list[list[InlineKeyboardButton]] | None = None) -> InlineKeyboardMarkup:
    rows = list(extra or [])
    rows.append([InlineKeyboardButton(text="🔙 Menu Utama", callback_data="m:home")])
    return InlineKeyboardMarkup(inline_keyboard=rows)


class Flow(StatesGroup):
    photos = State()
    prompt = State()
    ratio = State()


# ============================ menu ============================

@router.message(CommandStart())
async def cmd_start(msg: Message, state: FSMContext):
    await state.clear()
    db.ensure_user(msg.from_user.id, msg.from_user.username or "",
                   msg.from_user.full_name or "", settings.signup_bonus)
    await msg.answer(
        f"👋 Selamat datang di <b>{settings.bot_name}</b> — studio konten AI!\n\n"
        f"Bikin video karakter yang <b>konsisten</b> dari foto kamu, ganti outfit/scene, "
        f"image→video, pose transfer, sampai lip-sync. Semua tanpa watermark.\n\n"
        f"{saldo_txt(msg.from_user.id)}\n\n"
        f"Pilih fitur 👇",
        reply_markup=main_menu_kb())


@router.callback_query(F.data == "m:home")
async def cb_home(cb: CallbackQuery, state: FSMContext):
    await state.clear()
    await cb.message.edit_text(
        f"🏠 <b>Menu Utama</b>\n\n{saldo_txt(cb.from_user.id)}\n\nPilih fitur 👇",
        reply_markup=main_menu_kb())
    await cb.answer()


@router.callback_query(F.data == "m:saldo")
async def cb_saldo(cb: CallbackQuery):
    rows = db.ledger(cb.from_user.id, 5)
    hist = "\n".join(f"  · {r['delta']:+.1f} — {r['reason']}" for r in rows) or "  · (belum ada)"
    await cb.message.edit_text(
        f"💳 <b>Saldo & Riwayat</b>\n\n{saldo_txt(cb.from_user.id)}\n\n"
        f"<b>5 transaksi terakhir:</b>\n{hist}\n\n"
        f"Top up: Rp{settings.harga_per_10k:,} = {settings.tokens_per_10k} Token".replace(",", "."),
        reply_markup=back_kb())
    await cb.answer()


@router.callback_query(F.data == "m:topup")
async def cb_topup(cb: CallbackQuery):
    await cb.message.edit_text(
        f"⚡ <b>Top Up Token</b>\n\n"
        f"Rp{settings.harga_per_10k:,} = {settings.tokens_per_10k} Token (1 Token = Rp{settings.harga_per_10k // max(1, settings.tokens_per_10k):,})".replace(",", ".") + "\n\n"
        f"Cara isi (sementara manual):\n"
        f"1. Transfer/QRIS ke admin\n"
        f"2. Kirim bukti + ID Telegram kamu\n"
        f"3. Admin isi token → langsung bisa dipakai\n\n"
        f"<i>Integrasi QRIS otomatis (Midtrans/Xendit) menyusul.</i>\n\n"
        f"ID kamu: <code>{cb.from_user.id}</code>",
        reply_markup=back_kb())
    await cb.answer()


@router.callback_query(F.data == "m:help")
async def cb_help(cb: CallbackQuery):
    await cb.message.edit_text(
        "📖 <b>Panduan</b>\n\n"
        "1. Pilih fitur → kirim foto referensi (1–6 sesuai fitur)\n"
        "2. Ketik prompt gerakan/adegan\n"
        "3. Pilih rasio → render (estimasi 2–5 menit)\n"
        "4. Hasil dikirim otomatis, tanpa watermark\n\n"
        "Perintah: /start · /saldo · /topup · /cancel · /help\n"
        "Ganti outfit: pakai fitur All-in-One, foto 3–6 = outfit/properti.\n"
        "Konsistensi wajah: kirim foto tajam, muka jelas, tanpa watermark.",
        reply_markup=back_kb())
    await cb.answer()


@router.callback_query(F.data == "m:ref")
async def cb_ref(cb: CallbackQuery):
    link = f"https://t.me/{(await cb.bot.me()).username}?start=ref{cb.from_user.id}"
    await cb.message.edit_text(
        f"👥 <b>Program Referral</b>\n\nBagikan link ini:\n<code>{link}</code>\n\n"
        f"Setiap teman yang daftar & first top-up, kamu dapat bonus token.",
        reply_markup=back_kb())
    await cb.answer()


# ============================ fitur: mulai ============================

@router.callback_query(F.data.startswith("m:feat:"))
async def cb_feature(cb: CallbackQuery, state: FSMContext):
    key = cb.data.split(":")[2]
    f = catalog.get(key)
    if not f:
        await cb.answer("Fitur tidak dikenal", show_alert=True)
        return
    await state.clear()
    harga = catalog.price_rp(f, settings.tokens_per_10k, settings.harga_per_10k)
    await cb.message.edit_text(
        f"{f.label}\n\n{f.desc}\n\n"
        f"💠 Biaya: <b>{f.cost:g} Token</b> (≈ Rp{harga:,})".replace(",", "."),
        reply_markup=back_kb([[InlineKeyboardButton(text="🚀 Mulai", callback_data=f"m:go:{key}")]]))
    await cb.answer()


@router.callback_query(F.data.startswith("m:go:"))
async def cb_go(cb: CallbackQuery, state: FSMContext):
    key = cb.data.split(":")[2]
    f = catalog.get(key)
    if not f:
        await cb.answer("Fitur tidak dikenal", show_alert=True)
        return
    await state.set_state(Flow.photos)
    await state.update_data(feature=key, photos=[])
    await cb.message.edit_text(
        f"{f.label}\n\n📸 <b>Langkah 1/3: kirim foto referensi</b>\n"
        f"Kirim {f.min_photos}–{f.max_photos} foto.\n"
        + ("· Foto 1 = frame awal · Foto 2 = frame akhir · Foto 3+ = elemen tambahan\n" if key == "allinone" else "")
        + "\nKalau sudah, tekan ✅ Lanjut.",
        reply_markup=back_kb([[InlineKeyboardButton(text="✅ Lanjut", callback_data="f:next")]]))
    await cb.answer()


@router.message(Flow.photos, F.photo | F.document | F.video)
async def on_photo(msg: Message, state: FSMContext):
    data = await state.get_data()
    f = catalog.get(data.get("feature", ""))
    photos: list[str] = data.get("photos", [])
    if f and len(photos) >= f.max_photos:
        await msg.answer(f"Sudah maksimal {f.max_photos} foto — tekan ✅ Lanjut.")
        return
    if msg.photo:
        photos.append(msg.photo[-1].file_id)
    elif msg.video:
        photos.append(msg.video.file_id)
    else:
        photos.append(msg.document.file_id)      # type: ignore[union-attr]
    await state.update_data(photos=photos)
    sisa = (f.max_photos - len(photos)) if f else 0
    await msg.answer(
        f"✅ Foto #{len(photos)} diterima ({len(photos)}/{f.max_photos if f else '?'}).\n"
        + (f"Boleh kirim {sisa} foto lagi, atau tekan ✅ Lanjut." if sisa > 0 else "Sudah cukup — tekan ✅ Lanjut."),
        reply_markup=back_kb([[InlineKeyboardButton(text="✅ Lanjut", callback_data="f:next")]]))


@router.callback_query(F.data == "f:next", Flow.photos)
async def cb_next(cb: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    f = catalog.get(data.get("feature", ""))
    photos = data.get("photos", [])
    if not f or len(photos) < f.min_photos:
        await cb.answer(f"Butuh minimal {f.min_photos if f else 1} foto", show_alert=True)
        return
    if f.need_prompt:
        await state.set_state(Flow.prompt)
        await cb.message.edit_text(
            f"{f.label}\n\n📝 <b>Langkah 2/3: ketik prompt</b>\n"
            f"Contoh: <i>sinematik, kamera push-in perlahan, tersenyum lalu bicara, "
            f"rambut tertiup angin, ultra realistic, wajah konsisten</i>",
            reply_markup=back_kb([[InlineKeyboardButton(text="❌ Batal", callback_data="f:cancel")]]))
    else:
        await _ask_ratio_or_confirm(cb, state)
    await cb.answer()


@router.message(Flow.prompt, F.text)
async def on_prompt(msg: Message, state: FSMContext):
    await state.update_data(prompt=msg.text.strip()[:1000])
    data = await state.get_data()
    f = catalog.get(data["feature"])
    if f and f.need_ratio:
        await state.set_state(Flow.ratio)
        rows = [[InlineKeyboardButton(text=v, callback_data=f"f:ratio:{k}")] for k, v in catalog.RATIOS.items()]
        await msg.answer(f"{f.label}\n\n📐 <b>Langkah 3/3: pilih rasio video</b>",
                         reply_markup=InlineKeyboardMarkup(inline_keyboard=rows +
                                                           [[InlineKeyboardButton(text="❌ Batal", callback_data="f:cancel")]]))
    else:
        await _confirm(msg, state)


@router.callback_query(F.data.startswith("f:ratio:"), Flow.ratio)
async def cb_ratio(cb: CallbackQuery, state: FSMContext):
    await state.update_data(ratio=cb.data.split(":")[2])
    await _confirm(cb.message, state, cb.from_user.id)
    await cb.answer()


async def _ask_ratio_or_confirm(cb: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    f = catalog.get(data["feature"])
    if f and f.need_ratio:
        await state.set_state(Flow.ratio)
        rows = [[InlineKeyboardButton(text=v, callback_data=f"f:ratio:{k}")] for k, v in catalog.RATIOS.items()]
        await cb.message.edit_text(f"{f.label}\n\n📐 <b>Langkah 3/3: pilih rasio video</b>",
                                   reply_markup=InlineKeyboardMarkup(inline_keyboard=rows +
                                     [[InlineKeyboardButton(text="❌ Batal", callback_data="f:cancel")]]))
    else:
        await _confirm(cb.message, state, cb.from_user.id)


async def _confirm(target: Message, state: FSMContext, uid: int):
    data = await state.get_data()
    f = catalog.get(data["feature"])
    assert f
    saldo = db.balance(uid)
    cukup = saldo >= f.cost
    teks = (f"{f.label}\n\n🖼 Foto: <b>{len(data.get('photos', []))}</b>\n"
            f"📝 Prompt: <i>{(data.get('prompt') or '-')[:200]}</i>\n"
            f"📐 Rasio: <b>{data.get('ratio', '-')}</b>\n\n"
            f"💠 Biaya: <b>{f.cost:g} Token</b>\n{saldo_txt(uid)}\n\n"
            + ("Tekan 🚀 Render untuk mulai." if cukup else "⚠️ Saldo kurang — silakan Top Up dulu."))
    rows = [[InlineKeyboardButton(text="🚀 Render", callback_data="f:render")]] if cukup else \
           [[InlineKeyboardButton(text="⚡ Top Up", callback_data="m:topup")]]
    await state.set_state(Flow.photos)  # state tetap; render lewat callback
    await target.answer(teks, reply_markup=back_kb(rows))


@router.callback_query(F.data == "f:cancel")
async def cb_cancel(cb: CallbackQuery, state: FSMContext):
    await state.clear()
    await cb.message.edit_text("❌ Dibatalkan.\n\n🏠 Menu Utama", reply_markup=main_menu_kb())
    await cb.answer()


@router.message(Command("cancel"))
async def cmd_cancel(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer("❌ Dibatalkan.\n\n🏠 /start untuk menu utama.")


# ============================ render ============================

@router.callback_query(F.data == "f:render")
async def cb_render(cb: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    f = catalog.get(data.get("feature", ""))
    photos = data.get("photos", [])
    if not f or not photos:
        await cb.answer("Sesi kadaluarsa — mulai ulang dari menu.", show_alert=True)
        return
    if db.balance(cb.from_user.id) < f.cost:
        await cb.answer("Saldo kurang", show_alert=True)
        return
    job_id = db.create_job(cb.from_user.id, f.key, f.cost, photos,
                           data.get("prompt", ""), data.get("ratio", "9:16"))
    db.ledger_add(cb.from_user.id, -f.cost, "render", ref=str(job_id))
    await state.clear()
    await cb.message.edit_text(
        f"🎬 <b>{f.label}</b> 🚀\n\n🆔 Job: <code>{job_id}</code>\n"
        f"{bar(2)} 2%\n💬 Status: menyerahkan tugas ke backend...\n"
        f"{saldo_txt(cb.from_user.id)}", parse_mode=ParseMode.HTML)
    asyncio.create_task(process_job(job_id, cb.bot, cb.message.chat.id, cb.message.message_id))
    await cb.answer("Render dimulai")


async def process_job(job_id: int, bot: Bot, chat_id: int, msg_id: int):
    async with SEM:
        job = db.get_job(job_id)
        if not job:
            return
        f = catalog.get(job["feature"])
        work = Path(settings.work_dir) / f"job_{job_id}"
        work.mkdir(parents=True, exist_ok=True)
        try:
            # 1) unduh aset referensi
            photos = json.loads(job["ref_photos"] or "[]")
            local: list[Path] = []
            video_in: Path | None = None
            for i, fid in enumerate(photos, 1):
                p = work / f"ref{i}.bin"
                tg = await bot.get_file(fid)
                await bot.download_file(tg.file_path, p)   # type: ignore[arg-type]
                local.append(p)
                if f and f.key == "faceswap" and i == 2:
                    video_in, local = local[-1], local[:-1]
            out = work / "hasil.mp4"

            # 2) submit ke backend + poll
            req = GenRequest(job_id=job_id, feature_key=job["feature"],
                             workflow=f.backend_workflow if f else "", photos=local,
                             video_in=video_in, prompt=job["prompt"] or "",
                             ratio=job["ratio"] or "9:16", out_path=out)
            task_id = await backend.submit(req)
            db.set_job(job_id, status="running", task_id=task_id)
            t0 = time.time()
            pct = 5
            while True:
                if time.time() - t0 > settings.job_timeout:
                    raise TimeoutError("melebihi batas waktu render")
                st: GenStatus = await backend.poll(task_id)
                if st.state == "failed":
                    raise RuntimeError(st.error or "backend gagal")
                if st.state == "done":
                    result = st.result_path if (st.result_path and Path(st.result_path).exists()) else out
                    break
                pct = min(95, max(pct + 7, st.progress))
                try:
                    await bot.edit_message_text(
                        f"🎬 <b>{f.label}</b> 🚀\n\n🆔 Job: <code>{job_id}</code>\n"
                        f"{bar(pct)} {pct}%\n💬 Status: {st.message or 'diproses...'}\n"
                        f"⏱ {int(time.time()-t0)}s", chat_id=chat_id, message_id=msg_id,
                        parse_mode=ParseMode.HTML)
                except Exception:
                    pass
                await asyncio.sleep(settings.poll_interval)

            db.set_job(job_id, status="done", result_path=str(result))
            await bot.send_video(chat_id, FSInputFile(result),
                                 caption=f"✨ <b>{f.label}</b> selesai tanpa watermark!\n"
                                         f"🆔 Job <code>{job_id}</code> · {saldo_txt(job['telegram_id'])}",
                                 parse_mode=ParseMode.HTML)
            try:
                await bot.delete_message(chat_id, msg_id)
            except Exception:
                pass
            log.info("job %s selesai", job_id)
        except Exception as e:  # refund otomatis
            log.exception("job %s gagal", job_id)
            db.set_job(job_id, status="failed", error=str(e)[:400])
            if f:
                db.ledger_add(job["telegram_id"], f.cost, "refund", ref=str(job_id))
            await bot.send_message(chat_id,
                f"❌ <b>Render gagal</b> (job <code>{job_id}</code>).\nToken kamu <b>dikembalikan</b>.\n"
                f"Alasan: <code>{str(e)[:200]}</code>", parse_mode=ParseMode.HTML)


# ============================ admin ============================

def is_admin(uid: int) -> bool:
    return uid in settings.admin_ids


@router.message(Command("admin"))
async def cmd_admin(msg: Message):
    if not is_admin(msg.from_user.id):
        return
    s = db.stats()
    await msg.answer(
        f"🛠 <b>Admin</b>\n\n👥 User: {s['users']}\n🎬 Job: {s['jobs']} (selesai {s['done']}, antre {s['queued']})\n"
        f"💸 Token terpakai: {s['tokens_spent']:.1f}\n\n"
        f"/give &lt;id&gt; &lt;token&gt; · /voucher &lt;code&gt; &lt;token&gt; [max]\n/cek",
        parse_mode=ParseMode.HTML)


@router.message(Command("give"))
async def cmd_give(msg: Message):
    if not is_admin(msg.from_user.id):
        return
    parts = (msg.text or "").split()
    if len(parts) != 3:
        await msg.answer("Format: /give <telegram_id> <token>")
        return
    uid, n = int(parts[1]), float(parts[2])
    db.ensure_user(uid)
    bal = db.ledger_add(uid, n, "admin_grant", ref=str(msg.from_user.id))
    await msg.answer(f"✅ {n:g} token → <code>{uid}</code>. Saldo sekarang {bal:.1f}", parse_mode=ParseMode.HTML)


@router.message(Command("voucher"))
async def cmd_voucher(msg: Message):
    parts = (msg.text or "").split()
    if is_admin(msg.from_user.id) and len(parts) >= 3:
        code, tokens = parts[1], float(parts[2])
        mx = int(parts[3]) if len(parts) > 3 else 1
        db.conn.execute("INSERT OR REPLACE INTO vouchers (code,tokens,max_uses,used,created_at)"
                        " VALUES (?,?,?,0,?)", (code.upper(), tokens, mx, int(time.time())))
        db.conn.commit()
        await msg.answer(f"🎁 Voucher <code>{code.upper()}</code> = {tokens:g} token, {mx}x pakai")
        return
    if len(parts) != 2:
        await msg.answer("Pakai: /voucher <KODE>")
        return
    code = parts[1].upper()
    row = db.conn.execute("SELECT * FROM vouchers WHERE code=?", (code,)).fetchone()
    if not row or row["used"] >= row["max_uses"]:
        await msg.answer("❌ Voucher tidak valid / habis.")
        return
    db.conn.execute("UPDATE vouchers SET used=used+1 WHERE code=?", (code,))
    db.conn.commit()
    bal = db.ledger_add(msg.from_user.id, float(row["tokens"]), "voucher", ref=code)
    await msg.answer(f"🎉 Voucher aktif! +{row['tokens']:g} token. Saldo: {bal:.1f}")


@router.message(Command("cek"))
async def cmd_cek(msg: Message):
    if not is_admin(msg.from_user.id):
        return
    users = db.all_users()[:10]
    top = "\n".join(f"  · <code>{u['telegram_id']}</code> — {u['tokens']:.1f}" for u in users) or "  · kosong"
    await msg.answer(f"👥 <b>10 user terbaru</b>\n{top}", parse_mode=ParseMode.HTML)


@router.message(Command("help"))
async def cmd_help(msg: Message):
    await msg.answer("📖 /start · /saldo · /topup · /cancel\nFitur: All-in-One, Image→Video, Face Swap, Pose, Lip Sync, Image Editor")


# ============================ entrypoint ============================

def check() -> int:
    errs = settings.validate()
    print("=== Kreaibot — pemeriksaan konfigurasi ===")
    print(f"backend  : {settings.backend}")
    print(f"db       : {settings.db_path}")
    print(f"work     : {settings.work_dir}")
    print(f"admin    : {settings.admin_ids}")
    print(f"harga    : Rp{settings.harga_per_10k} = {settings.tokens_per_10k} token")
    print("\n=== Katalog fitur ===")
    for f in catalog.FEATURES.values():
        print(f"  {f.label:34s} {f.cost:>4g} token  (Rp{catalog.price_rp(f, settings.tokens_per_10k, settings.harga_per_10k)})  "
              f"foto {f.min_photos}-{f.max_photos}")
    print("\n=== Statistik DB ===")
    print(f"  {db.stats()}")
    if errs:
        print("\n⚠️  Masalah:")
        for e in errs:
            print("  -", e)
        return 1
    print("\n✅ Konfigurasi OK.")
    return 0


async def main() -> None:
    if not settings.bot_token:
        print("❌ KREAIBOT_TOKEN kosong. Isi di .env dulu (dari @BotFather).")
        sys.exit(1)
    settings.ensure_dirs()
    bot = Bot(settings.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(router)
    me = await bot.get_me()
    log.info("Kreaibot jalan sebagai @%s (backend=%s)", me.username, settings.backend)
    await dp.start_polling(bot)


if __name__ == "__main__":
    if "--check" in sys.argv:
        sys.exit(check())
    asyncio.run(main())