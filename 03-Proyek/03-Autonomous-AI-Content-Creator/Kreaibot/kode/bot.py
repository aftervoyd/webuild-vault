#!/usr/bin/env python3
"""KREE.AI (Kreaibot) — bot Telegram studio konten AI: karakter konsisten → video, plus UGC Ads.

Jalankan:  python3 bot.py            (produksi)
           python3 bot.py --check    (validasi konfigurasi + katalog, tanpa Telegram)
"""
from __future__ import annotations

import asyncio
import json
import re
import shutil
import subprocess
import logging
import sys
import time
from pathlib import Path

from aiogram import Bot, Dispatcher, F, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (BotCommand, CallbackQuery, FSInputFile, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message)

import catalog
import presets
import promptsmith
import storyboard
from aulaa import Aulaa, make_client
from backends import GenRequest, GenStatus, make_backend
from backends.mediafix import smooth_fps, unwrap_media
from config import settings
from db import Database

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(name)s: %(message)s")
log = logging.getLogger("kreaibot")

db = Database(settings.db_path)
backend = make_backend(settings.backend, api_key=settings.runninghub_api_key,
                       base=settings.runninghub_base, work_dir=settings.work_dir,
                       upload_key=settings.runninghub_upload_key)
router = Router()
pay_gw = make_client(settings)            # None kalau AULAA_API_KEY belum diisi
bot: Bot = None                            # type: ignore[assignment]  # di-set di main(), dipakai handler
SEM = asyncio.Semaphore(settings.concurrency)

# ============================ util ============================

def bar(pct: int, n: int = 10) -> str:
    fill = max(0, min(n, round(pct / 100 * n)))
    return "🟩" * fill + "⬜" * (n - fill)


def saldo_txt(tid: int) -> str:
    return f"💰 Sisa saldo: <b>{db.balance(tid):.1f} Token</b>"


def main_menu_kb(uid: int | None = None) -> InlineKeyboardMarkup:
    rows = []
    if uid:
        # INVENTORY DI PALING ATAS: karakter & produk tersimpan (sekali simpan, pakai selamanya)
        rows.append([InlineKeyboardButton(
            text=f"🧑\u200d🎨 Karakter Saya ({db.char_count(uid, 'char')})",
            callback_data="m:inv:char"),
            InlineKeyboardButton(
            text=f"🛍️ Produk Saya ({db.char_count(uid, 'produk')})",
            callback_data="m:inv:produk")])
    for f in catalog.enabled_features():
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


IMG_EXT = {".png", ".jpg", ".jpeg", ".webp"}


async def send_result(bot: Bot, chat_id: int, result, caption: str) -> None:
    """Kirim hasil render: berkas gambar → foto, selain itu → video.

    Fitur editor mengembalikan GAMBAR (bukan video) — send_video akan gagal.
    """
    ext = Path(str(result)).suffix.lower()
    if ext in IMG_EXT:
        await bot.send_photo(chat_id, FSInputFile(result), caption=caption,
                             parse_mode=ParseMode.HTML)
    else:
        await bot.send_video(chat_id, FSInputFile(result), caption=caption,
                             parse_mode=ParseMode.HTML)


def style_kb() -> InlineKeyboardMarkup:
    rows = [[InlineKeyboardButton(text=label, callback_data=f"u:style:{key}")]
            for key, label in promptsmith.style_list_kb_rows()]
    rows.append([InlineKeyboardButton(text="❌ Batal", callback_data="f:cancel")])
    return InlineKeyboardMarkup(inline_keyboard=rows)


def ratio_kb() -> InlineKeyboardMarkup:
    rows = [[InlineKeyboardButton(text=v, callback_data=f"f:ratio:{k}")] for k, v in catalog.RATIOS.items()]
    rows.append([InlineKeyboardButton(text="❌ Batal", callback_data="f:cancel")])
    return InlineKeyboardMarkup(inline_keyboard=rows)


class Flow(StatesGroup):
    photos = State()
    prompt = State()
    ratio = State()
    # --- alur UGC (bertingkat) ---
    ugc_char = State()      # 1/5 character sheet
    ugc_prod = State()      # 2/5 foto produk
    ugc_brief = State()     # 3/5 brief produk
    ugc_style = State()     # 4/5 pilih gaya
    # --- inventory: karakter & produk tersimpan ---
    inv_photo = State()     # kirim foto master
    inv_name = State()      # kasih nama (atau ganti nama)


# ============================ menu ============================

def _welcome(tid: int) -> str:
    return (f"👋 Selamat datang di <b>{settings.bot_name}</b> — studio konten AI!\n\n"
            f"Bikin video dari fotomu, cukup <b>3 langkah</b>: pilih fitur → kirim foto → "
            f"langsung ketik prompt-nya. Selesai 🎬\n"
            f"🆕 <b>UGC Video Iklan</b>: foto kamu + foto produk → video iklan siap posting.\n"
            f"· Image→Video mulai <b>0,5 Token</b> (5 dtk) · All-in-One mulai 1 Token (5 dtk)\n\n"
            f"🎁 <b>Program Referral</b>: ajak teman, kamu dapat <b>{settings.ref_inviter:g} Token</b> "
            f"per teman (menu 👥 Referral).\n\n"
            f"{saldo_txt(tid)}\n\nPilih fitur 👇")


@router.message(CommandStart(deep_link=True))
async def cmd_start_ref(msg: Message, command: CommandObject, state: FSMContext):
    """Pendaftaran lewat link referral: t.me/<bot>?start=ref_<id>"""
    await state.clear()
    u = msg.from_user
    payload = (command.args or "").strip()
    digits = (payload[4:] if payload.startswith("ref_")
              else payload[3:] if payload.startswith("ref") else "")
    inviter = int(digits) if digits.isdigit() else 0
    is_new = db.get_user(u.id) is None
    db.ensure_user(u.id, u.username or "", u.full_name or "", settings.signup_bonus,
                   referred_by=inviter or None)
    if inviter and inviter != u.id and is_new and db.ref_register(inviter, u.id):
        kode = await _claim_invitee(u.id)
        if kode == "ok":
            await msg.answer(
                f"🎉 <b>Selamat datang + bonus referral!</b>\n\n"
                f"<b>+{settings.ref_invitee:g} Token</b> sudah masuk ke akunmu.\n"
                f"{saldo_txt(u.id)}\n\nYuk bikin video pertamamu 👇",
                reply_markup=main_menu_kb(u.id))
            return
        await msg.answer(_join_txt("🎁 <b>Kamu dapat bonus referral!</b>"), reply_markup=_join_kb())
        return
    await msg.answer(_welcome(u.id), reply_markup=main_menu_kb(u.id))


@router.message(CommandStart(deep_link=False))
async def cmd_start(msg: Message, state: FSMContext):
    await state.clear()
    db.ensure_user(msg.from_user.id, msg.from_user.username or "",
                   msg.from_user.full_name or "", settings.signup_bonus)
    await msg.answer(_welcome(msg.from_user.id), reply_markup=main_menu_kb(msg.from_user.id))


@router.callback_query(F.data == "m:home")
async def cb_home(cb: CallbackQuery, state: FSMContext):
    await state.clear()
    await cb.message.edit_text(
        f"🏠 <b>Menu Utama</b>\n\n{saldo_txt(cb.from_user.id)}\n\nPilih fitur 👇",
        reply_markup=main_menu_kb(cb.from_user.id))
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
async def cb_topup(cb: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    rows: list[list[InlineKeyboardButton]] = []
    if data.get("feature"):
        rows.append([InlineKeyboardButton(text="🔁 Sudah Top Up — Lanjut Render", callback_data="f:recheck")])
    harga_token = max(1, settings.harga_per_10k // max(1, settings.tokens_per_10k))
    for rp in (10_000, 25_000, 50_000, 100_000):
        rows.append([InlineKeyboardButton(text=f"Rp{rp:,} → {rp // harga_token} Token".replace(",", "."),
                                          callback_data=f"t:paket:{rp}")])
    await cb.message.edit_text(
        (f"⚡ <b>Top Up Token</b>\n\n"
         f"1 Token = <b>Rp{harga_token:,}</b>\n"
         f"Pilih paket → bayar → tekan “✅ Sudah Bayar”. Token masuk setelah admin verifikasi.\n\n"
         f"<b>Cara bayar</b>\n{settings.pay_info}\n\n"
         f"ID kamu: <code>{cb.from_user.id}</code>").replace(",", "."),
        reply_markup=back_kb(rows))
    await cb.answer()


@router.callback_query(F.data.startswith("t:paket:"))
async def cb_paket(cb: CallbackQuery):
    rp = int(cb.data.split(":")[2])
    harga_token = max(1, settings.harga_per_10k // max(1, settings.tokens_per_10k))
    tok = rp // harga_token
    uid = cb.from_user.id
    manual_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Sudah Bayar — Minta Diisi", callback_data=f"t:klaim:{rp}")],
        [InlineKeyboardButton(text="⬅️ Kembali", callback_data="m:topup")]])

    if pay_gw is None:                      # AULAA_API_KEY belum diisi → alur manual
        await cb.message.edit_text(
            (f"💳 <b>Pembayaran Rp{rp:,}</b> → <b>{tok:g} Token</b>\n\n"
             f"{settings.pay_info}\n\n"
             f"Sudah bayar? Tekan tombol di bawah — admin dapat notifikasi & tinggal 1 klik.\n\n"
             f"ID kamu: <code>{uid}</code>").replace(",", "."),
            reply_markup=manual_kb)
        await cb.answer()
        return

    # ---- QRIS otomatis (Aulaa) ----
    order_id = f"KREE-{uid}-{int(time.time())}"
    db.pay_create(order_id, uid, rp, tok)
    await cb.answer("Membuat QRIS…")
    try:
        p = await pay_gw.create(order_id, rp, method=(settings.aulaa_method or "qris"),
                                redirect_url=(settings.aulaa_redirect or None))
    except Exception as e:                  # noqa: BLE001
        log.warning("aulaa create gagal: %s", e)
        db.pay_set(order_id, status="error", note=str(e)[:180])
        await cb.message.edit_text(
            (f"⚠️ <b>QRIS otomatis sedang gangguan.</b>\n\n"
             f"{settings.pay_info}\n\nNominal: <b>Rp{rp:,}</b> → {tok:g} Token\n"
             f"ID kamu: <code>{uid}</code>\n\nTransfer manual dulu, lalu tekan tombol di bawah.").replace(",", "."),
            reply_markup=manual_kb)
        return

    db.pay_set(order_id, payment_id=p.id, invoice=p.number, is_test=1 if p.is_test else 0)
    exp = f"\n⏳ Berlaku sampai: {p.expired_at}" if p.expired_at else ""
    sand = ""
    if p.is_test:                   # sandbox → sertakan kode (bisa disalin) untuk halaman simulasi
        sand = ("\n\n🧪 <b>MODE SANDBOX — uji coba, tidak ada uang sungguhan</b>\n"
                "Bayar lewat <a href=\"https://api.aulaa.co/payment-simulation\">halaman simulasi</a>, "
                "tempel kode ini di tab <b>QRIS Code</b>:\n"
                f"<code>{p.number}</code>")
    cap = ((f"💳 <b>Rp{rp:,}</b> → <b>{tok:g} Token</b>\n\n"
            f"Scan QR ini pakai <b>m-banking / e-wallet apa saja</b> (QRIS).\n"
            f"Token masuk <b>otomatis</b> begitu pembayaran berhasil — gak perlu kirim bukti.{exp}{sand}\n\n"
            f"ID kamu: <code>{uid}</code>").replace(",", "."))
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔔 Sudah Bayar — Cek Sekarang", callback_data=f"t:cek:{order_id}")],
        [InlineKeyboardButton(text="📄 Buka Halaman Bayar", url=pay_gw.pay_url(p.id))],
        [InlineKeyboardButton(text="⬅️ Menu Utama", callback_data="m:home")]])
    try:
        await cb.message.edit_text(f"💳 QRIS Rp{rp:,} — lihat pesan di bawah ⬇️".replace(",", "."))
    except Exception:                       # noqa: BLE001
        pass
    if p.number and len(p.number) > 24:     # QRIS = string panjang → render jadi gambar QR
        try:
            qp = Aulaa.qr_png(p.number, Path(settings.work_dir) / f"qr-{order_id}.png")
            m = await cb.message.answer_photo(FSInputFile(qp), caption=cap, reply_markup=kb)
            db.pay_set(order_id, msg_id=m.message_id, chat_id=m.chat.id)
            return
        except Exception as e:              # noqa: BLE001
            log.warning("render QR gagal: %s", e)
    m = await cb.message.answer(cap, reply_markup=kb)
    db.pay_set(order_id, msg_id=m.message_id, chat_id=m.chat.id)


@router.callback_query(F.data.startswith("t:klaim:"))
async def cb_klaim(cb: CallbackQuery):
    rp = int(cb.data.split(":")[2])
    harga_token = max(1, settings.harga_per_10k // max(1, settings.tokens_per_10k))
    tok = rp // harga_token
    u = cb.from_user
    kb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text=f"✅ Setujui {tok} token", callback_data=f"adm:ok:{u.id}:{tok}"),
        InlineKeyboardButton(text="❌ Tolak", callback_data=f"adm:no:{u.id}")]])
    for aid in settings.admin_ids:
        try:
            await bot.send_message(
                aid,
                (f"💰 <b>KLAIM TOP UP</b>\n\n"
                 f"User: <b>{u.full_name}</b> (@{u.username or '-'})\n"
                 f"ID: <code>{u.id}</code>\n"
                 f"Paket: <b>Rp{rp:,}</b> → {tok} Token\n\n"
                 f"Cek pembayaran (yang masuk Rp{rp:,}), lalu tekan ✅/❌.").replace(",", "."),
                reply_markup=kb)
        except Exception as e:                      # noqa: BLE001
            log.warning("gagal kirim notif topup ke admin %s: %s", aid, e)
    await cb.message.edit_text(
        f"✅ <b>Permintaan terkirim ke admin.</b>\n\n"
        f"Token masuk begitu pembayaran diverifikasi.\nSaldo sekarang: {saldo_txt(u.id)}",
        reply_markup=back_kb())
    await cb.answer("Terkirim ke admin")


# ============================ QRIS otomatis (Aulaa) ============================

_LAST_CHECK: dict[str, float] = {}          # jeda cek per-order (API Aulaa: maks 30x/menit)
CHECK_MIN_GAP = 5.0                         # detik antar-cek untuk order yang sama


async def _notify_expired(row) -> None:
    try:
        await bot.send_message(int(row["telegram_id"]),
                               "⌛ <b>Waktu pembayaran habis.</b>\n\nKalau kamu sudah bayar, hubungi admin ya.",
                               reply_markup=main_menu_kb(int(row["telegram_id"])))
    except Exception:                       # noqa: BLE001
        pass


async def _check_order(order_id: str, via: str = "poller") -> bool:
    """Cek 1 order ke gateway; kalau lunas → kredit token. True = lunas."""
    if pay_gw is None:
        return False
    row = db.pay_get(order_id)
    if not row:
        return False
    if row["status"] == "paid":
        return True
    if row["status"] != "pending" or not row["payment_id"]:
        return False
    now = time.time()
    if now - _LAST_CHECK.get(order_id, 0.0) < CHECK_MIN_GAP:
        return False
    _LAST_CHECK[order_id] = now
    try:
        p = await pay_gw.get(str(row["payment_id"]))
    except Exception as e:                      # noqa: BLE001
        log.debug("cek %s gagal: %s", order_id, e)
        return False
    if p.paid:
        await _credit_topup(order_id, via=via, p=p)
        return True
    if p.dead:
        db.pay_set(order_id, status="expired")
        await _notify_expired(row)
    return False


async def _credit_topup(order_id: str, via: str = "poller", p=None) -> float | None:
    """Kredit token setelah pembayaran Aulaa lunas. Idempoten (aman dipanggil berulang)."""
    row = db.pay_get(order_id)
    if not row or row["status"] == "paid":
        return None
    # 🔒 pengaman uang nyata: nominal dari gateway HARUS sama dengan yang kita tagih
    if p is not None and int(getattr(p, "amount", 0) or 0) not in (0, int(row["amount"])):
        log.error("NOMINAL BEDA! order=%s gateway=%s lokal=%s → TIDAK dikredit",
                  order_id, getattr(p, "amount", "?"), row["amount"])
        db.pay_set(order_id, note=f"nominal beda: gateway={getattr(p, 'amount', '?')} lokal={row['amount']}")
        for adm in settings.admin_ids:
            try:
                await bot.send_message(int(adm),
                                       f"🚨 <b>Nominal tidak cocok</b>\norder <code>{order_id}</code>\n"
                                       f"gateway={getattr(p, 'amount', '?')} · lokal={row['amount']}\n"
                                       f"Token TIDAK dikredit. Cek dashboard Aulaa.")
            except Exception:                   # noqa: BLE001
                pass
        return None
    uid, tok = int(row["telegram_id"]), float(row["tokens"])
    db.ledger_add(uid, tok, "topup_aulaa", ref=order_id)   # ledger dulu → baru tandai lunas
    db.pay_mark_paid(order_id)
    bal = db.balance(uid)
    try:
        await bot.send_message(
            uid,
            f"🎉 <b>Pembayaran diterima!</b>\n\n"
            f"💚 +{tok:g} Token masuk\nSaldo sekarang: <b>{bal:g} Token</b>\n\n"
            f"Langsung bikin video 👇",
            reply_markup=main_menu_kb(uid))
    except Exception as e:                      # noqa: BLE001
        log.warning("gagal kabari user %s: %s", uid, e)
    # pesan QR di chat user → otomatis berubah jadi "LUNAS"
    try:
        keys = row.keys()
        mid = row["msg_id"] if "msg_id" in keys else None
        if mid:
            await bot.edit_message_caption(
                chat_id=uid, message_id=int(mid),
                caption=(f"✅ <b>LUNAS</b> — +{tok:g} Token masuk!\n"
                         f"Saldo: <b>{bal:g} Token</b> 💚\n\n<i>Token siap dipakai.</i>"))
    except Exception as e:                      # noqa: BLE001
        log.debug("edit caption QR gagal: %s", e)
    log.info("topup lunas (via %s): order=%s user=%s token=+%s", via, order_id, uid, tok)
    await _ref_on_purchase(uid)                 # mode aman referral
    return bal


@router.callback_query(F.data.startswith("t:cek:"))
async def cb_cek(cb: CallbackQuery):
    """User menekan 'Sudah Bayar' → cek status ke Aulaa sekarang."""
    order_id = cb.data.split(":", 2)[2]
    row = db.pay_get(order_id)
    if not row:
        await cb.answer("Order tidak ditemukan 🙏", show_alert=True)
        return
    if row["status"] == "paid":
        await cb.answer("✅ Sudah lunas — token sudah masuk", show_alert=True)
        return
    if pay_gw is None or not row["payment_id"]:
        await cb.answer("Belum bisa dicek otomatis. Hubungi admin ya.", show_alert=True)
        return
    await cb.answer("Mengecek ke gateway…")
    _LAST_CHECK.pop(order_id, 0.0)              # tombol = cek paksa, abaikan jeda
    lunas = await _check_order(order_id, via="tombol")
    if not lunas:
        r2 = db.pay_get(order_id)
        if r2 and r2["status"] == "expired":
            await cb.answer("⌛ Sesi pembayaran sudah berakhir — buat QR baru ya", show_alert=True)
        else:
            await cb.answer("⏳ Belum masuk. Kalau baru bayar, tunggu ±10 detik lalu cek lagi.", show_alert=True)


async def poller_payments() -> None:
    """Cek status QRIS pending tiap 6 detik → token masuk otomatis (tanpa webhook publik)."""
    if pay_gw is None:
        log.info("poller pembayaran nonaktif (AULAA_API_KEY belum diisi)")
        return
    log.info("poller pembayaran Aulaa AKTIF (interval 6s)")
    while True:
        try:
            for row in db.pay_pending(20):
                await _check_order(str(row["order_id"]), via="poller")
        except Exception as e:                  # noqa: BLE001
            log.warning("poller pembayaran error: %s", e)
        await asyncio.sleep(6)


@router.callback_query(F.data.startswith("adm:ok:"))
async def cb_adm_ok(cb: CallbackQuery):
    if not is_admin(cb.from_user.id):
        await cb.answer("Khusus admin", show_alert=True)
        return
    _, _, uid, tok = cb.data.split(":")
    uid, tok = int(uid), int(tok)
    bal = db.ledger_add(uid, tok, "topup_approve", ref=str(cb.from_user.id))
    await _ref_on_purchase(uid)                     # mode aman: cairkan bonus pengundang
    try:
        await bot.send_message(uid, f"🎉 <b>Token masuk: {tok:g} Token</b>\n"
                                    f"Saldo sekarang: <b>{bal:g} Token</b>\n\nSelamat berkarya! 🚀")
    except Exception as e:                          # noqa: BLE001
        log.warning("gagal kabari user %s: %s", uid, e)
    await cb.message.edit_text(f"✅ Disetujui <b>{tok:g} token</b> untuk <code>{uid}</code>\n"
                               f"Saldo mereka: <b>{bal:g}</b>")
    await cb.answer("Tersimpan")


@router.callback_query(F.data.startswith("adm:no:"))
async def cb_adm_no(cb: CallbackQuery):
    if not is_admin(cb.from_user.id):
        await cb.answer("Khusus admin", show_alert=True)
        return
    uid = int(cb.data.split(":")[2])
    try:
        await bot.send_message(uid, "❌ Klaim top up belum bisa disetujui. Hubungi admin ya 🙏")
    except Exception as e:                          # noqa: BLE001
        log.warning("gagal kabari user %s: %s", uid, e)
    await cb.message.edit_text(f"❌ Ditolak untuk <code>{uid}</code>")
    await cb.answer("Ditolak")


@router.callback_query(F.data == "m:help")
async def cb_help(cb: CallbackQuery):
    await cb.message.edit_text(
        "📖 <b>Panduan</b>\n\n"
        "<b>Video karakter:</b>\n"
        "1. Pilih fitur → kirim foto referensi (1–6)\n"
        "2. Ketik prompt gerakan/adegan → pilih rasio → render\n\n"
        "<b>UGC Video Iklan (jualan produk):</b>\n"
        "1. Kirim <b>character sheet</b> (foto kamu / wajah brand)\n"
        "2. Kirim <b>foto produk</b> (1–3)\n"
        "3. Tulis <b>brief</b>: nama produk, harga, keunggulan, maunya video seperti apa\n"
        "4. Pilih <b>gaya</b>: review / unboxing / problem-solution / testimoni / promo / sinematik\n"
        "5. Pilih rasio → render\n"
        "<i>Prompt videonya dirakit otomatis & diperhalus sistem — kamu cukup kasih brief santai.</i>\n\n"
        "Perintah: /start · /saldo · /topup · /cancel · /help",
        reply_markup=back_kb())
    await cb.answer()


# ============================ referral (anti-farming) ============================
# Aturan anti-farming:
#   1) 1 akun Telegram = 1 invitee SEKALI seumur hidup (DB: invitee_id UNIQUE)
#   2) wajib join channel komunitas (Telegram = akun ber-nomor HP → bikin akun palsu mahal)
#   3) bonus pengundang dibatasi harian + bulanan (default 10/hari, 30/bulan)
#   4) tidak bisa mengundang diri sendiri
#   5) (opsional) bonus pengundang baru cair setelah invitee TOP UP pertama

async def _channel_ok(uid: int) -> bool:
    """True kalau user sudah join channel komunitas (bot WAJIB admin di channel itu)."""
    ch = settings.channel
    if not ch:
        return True                       # gate dimatikan (channel belum di-set)
    try:
        m = await bot.get_chat_member(chat_id=f"@{ch}", user_id=uid)
        return m.status in ("creator", "administrator", "member", "restricted")
    except Exception as e:                # noqa: BLE001
        log.warning("cek keanggotaan channel @%s gagal: %s", ch, e)
        return False


def _ref_link(username: str, uid: int) -> str:
    return f"https://t.me/{username}?start=ref_{uid}"


def _join_kb() -> InlineKeyboardMarkup:
    rows: list[list[InlineKeyboardButton]] = []
    if settings.channel_link:
        rows.append([InlineKeyboardButton(text=f"📢 Join {settings.channel_title}",
                                          url=settings.channel_link)])
    rows.append([InlineKeyboardButton(text="✅ Sudah Join — Klaim Bonus", callback_data="r:claim")])
    rows.append([InlineKeyboardButton(text="🔙 Menu Utama", callback_data="m:home")])
    return InlineKeyboardMarkup(inline_keyboard=rows)


def _join_txt(prefix: str) -> str:
    return (f"{prefix}\n\n"
            f"Yang kamu dapat: <b>+{settings.ref_invitee:g} Token</b> gratis\n\n"
            f"<b>Cara klaim (2 langkah)</b>\n"
            f"1. Masuk channel <b>{settings.channel_title}</b> — tekan tombol di bawah\n"
            f"2. Balik ke sini, tekan <b>✅ Sudah Join — Klaim Bonus</b>\n\n"
            f"<i>Wajib join supaya bonus tidak disalahgunakan, sekaligus biar kamu dapat "
            f"info promo & update konten di channel.</i>")


async def _give_inviter_bonus(inviter_id: int, invitee_id: int) -> None:
    """Bayar bonus pengundang (sekali saja; dibatasi harian/bulanan)."""
    r = db.ref_get(invitee_id)
    if not r or r["inviter_paid"]:
        return
    now = int(time.time())
    if (db.ref_count_since(inviter_id, now - 86_400) >= settings.ref_max_day
            or db.ref_count_since(inviter_id, now - 30 * 86_400) >= settings.ref_max_month):
        log.info("bonus pengundang %s ditahan (limit tercapai)", inviter_id)
        return
    db.ledger_add(inviter_id, settings.ref_inviter, "ref_bonus_inviter", ref=str(invitee_id))
    db.ref_mark(invitee_id, inviter_paid=1)
    try:
        await bot.send_message(
            inviter_id,
            f"🎉 <b>Bonus referral +{settings.ref_inviter:g} Token</b>\n"
            f"Teman yang kamu undang sudah bergabung.\n{saldo_txt(inviter_id)}",
            reply_markup=main_menu_kb(inviter_id))
    except Exception as e:                # noqa: BLE001
        log.warning("gagal kabari pengundang %s: %s", inviter_id, e)


async def _claim_invitee(uid: int) -> str:
    """Klaim bonus invitee → 'ok' | 'sudah' | 'bukan' | 'belum_join'."""
    r = db.ref_get(uid)
    if not r:
        return "bukan"
    if r["invitee_paid"]:
        return "sudah"
    if not await _channel_ok(uid):
        return "belum_join"
    db.ledger_add(uid, settings.ref_invitee, "ref_bonus_invitee", ref=str(r["inviter_id"]))
    db.ref_mark(uid, invitee_paid=1, status="paid")
    if not settings.ref_inviter_after_purchase:
        await _give_inviter_bonus(int(r["inviter_id"]), uid)
    return "ok"


async def _ref_on_purchase(uid: int) -> None:
    """Dipanggil setelah top up: mode aman → cairkan bonus pengundang di sini."""
    if not settings.ref_inviter_after_purchase:
        return
    inv = db.ref_pending_inviter(uid)
    if inv:
        await _give_inviter_bonus(inv, uid)


@router.callback_query(F.data == "m:ref")
async def cb_ref(cb: CallbackQuery):
    uid = cb.from_user.id
    me = await cb.bot.me()
    link = _ref_link(me.username or "kreeaibot", uid)
    st, r = db.ref_summary(uid), db.ref_get(uid)
    txt = (f"👥 <b>Program Referral {settings.bot_name}</b>\n\n"
           f"🎁 Temanmu dapat <b>{settings.ref_invitee:g} Token</b> gratis\n"
           f"💰 Kamu dapat <b>{settings.ref_inviter:g} Token</b> tiap teman yang ikut\n\n"
           f"<b>Link kamu</b> (tekan untuk salin):\n<code>{link}</code>\n\n"
           f"📊 Diundang: <b>{st['total']}</b> · berhasil: <b>{st['paid']}</b>\n"
           f"💰 Token dari referral: <b>{st['earned']:.1f}</b>\n"
           f"📅 Batas: {settings.ref_max_day}/hari · {settings.ref_max_month}/bulan\n\n"
           f"📢 Komunitas: <a href=\"{settings.channel_link}\">{settings.channel_title}</a>\n\n"
           f"<i>Syarat: teman harus akun Telegram yang belum pernah pakai bot ini dan wajib join "
           f"channel komunitas. 1 bonus per akun — jadi tidak bisa di-farming.</i>")
    rows: list[list[InlineKeyboardButton]] = []
    if r and not r["invitee_paid"]:
        rows.append([InlineKeyboardButton(
            text=f"🎁 Klaim bonus kamu (+{settings.ref_invitee:g} Token)", callback_data="r:claim")])
    share = (f"https://t.me/share/url?url={link}&text="
             f"Coba {settings.bot_name}! Bikin video iklan dari foto, langsung di Telegram")
    rows.append([InlineKeyboardButton(text="📤 Bagikan ke teman", url=share)])
    await cb.message.edit_text(txt, reply_markup=back_kb(rows))
    await cb.answer()


@router.callback_query(F.data == "r:claim")
async def cb_claim(cb: CallbackQuery):
    uid = cb.from_user.id
    kode = await _claim_invitee(uid)
    if kode == "ok":
        await cb.message.edit_text(
            f"🎉 <b>Bonus referral masuk: +{settings.ref_invitee:g} Token!</b>\n\n"
            f"{saldo_txt(uid)}\n\nLangsung coba fiturnya 👇",
            reply_markup=main_menu_kb(u.id))
        await cb.answer("Bonus masuk!")
    elif kode == "sudah":
        await cb.answer("Bonus referral kamu sudah pernah diklaim 🙂", show_alert=True)
    elif kode == "belum_join":
        await cb.message.edit_text(_join_txt("Sebentar lagi 🙂"), reply_markup=_join_kb())
        await cb.answer("Kamu belum join channel")
    else:
        await cb.message.edit_text(
            "ℹ️ Kamu belum terdaftar di program referral.\n\n"
            "Kalau ada teman mengundangmu, buka link undangannya ya.",
            reply_markup=back_kb())
        await cb.answer()


@router.message(Command("refstats"))
async def cmd_refstats(msg: Message):
    """Admin: rekap referral (deteksi farming)."""
    if not is_admin(msg.from_user.id):
        return
    rows = db.ref_top(10)
    total = sum(int(r["total"]) for r in rows)
    paid = sum(int(r["paid"] or 0) for r in rows)
    lines = ["👥 <b>Statistik Referral</b>",
             f"Tercatat: <b>{total}</b> · berhasil: <b>{paid}</b>", ""]
    for r in rows:
        lines.append(f"· <code>{r['inviter_id']}</code> — {int(r['total'])} undang · "
                     f"{int(r['paid'] or 0)} cair")
    lines.append(f"\nTotal user: {db.stats()['users']}")
    await msg.answer("\n".join(lines))


# ============================ detail fitur ============================

@router.callback_query(F.data.startswith("m:feat:"))
async def cb_feature(cb: CallbackQuery, state: FSMContext):
    key = cb.data.split(":")[2]
    f = catalog.get(key)
    if not f:
        await cb.answer("Fitur tidak dikenal", show_alert=True)
        return
    await state.clear()
    # Layar detail = tempat harga ditampilkan → durasi HARUS bisa dipilih di sini
    # (dulu cuma ada tombol "🚀 Mulai", user jadi ngetik "15 detik" tanpa tombol).
    rows: list[list[InlineKeyboardButton]] = []
    if len(f.durations) > 1:
        rows += [[InlineKeyboardButton(text=f"▶️ {d} detik · {catalog.cost_for(key, d):g} Token",
                                       callback_data=f"m:go:{key}:{d}")] for d in f.durations]
    else:
        rows.append([InlineKeyboardButton(text="🚀 Mulai", callback_data=f"m:go:{key}")])
    saldo = db.balance(cb.from_user.id)
    await cb.message.edit_text(
        f"{f.label}\n\n{f.desc}\n\n💰 Saldo kamu: <b>{saldo:g} Token</b>\n\n"
        + ("👇 Pilih durasi buat mulai:" if len(f.durations) > 1 else "👇 Tekan Mulai ya:"),
        reply_markup=back_kb(rows))
    await cb.answer()


@router.callback_query(F.data.startswith("m:go:"))
async def cb_go(cb: CallbackQuery, state: FSMContext):
    parts = cb.data.split(":")
    key = parts[2]
    f = catalog.get(key)
    if not f:
        await cb.answer("Fitur tidak dikenal", show_alert=True)
        return
    dur = f.duration
    if len(parts) > 3:                      # tombol durasi dari layar detail: m:go:<key>:<dur>
        try:
            d = int(parts[3])
            if d in f.durations:
                dur = d
        except ValueError:
            pass
    await state.update_data(feature=key, photos=[], ratio="9:16", duration=dur,
                            prompt="", brief="", prod_photos=[], char_photo="",
                            style="review" if f.kind == "ugc" else "")
    batal = back_kb([[InlineKeyboardButton(text="❌ Batal", callback_data="f:cancel")]])
    if f.kind == "ugc":
        await state.set_state(Flow.ugc_char)
        simpan = inv_use_rows(cb.from_user.id, "char", "u:ch")
        rows = simpan + [[InlineKeyboardButton(text="❌ Batal", callback_data="f:cancel")]]
        await cb.message.edit_text(
            f"{f.label}\n\n🖼 <b>Kirim FOTO KARAKTER</b>\n"
            f"Foto wajah/tubuh yang mau dipakai jadi kreator — tajam, wajah jelas, tanpa watermark.\n\n"
            + ("🧑\u200d🎨 <b>Atau pakai karakter tersimpan</b> (1 tap):\n" if simpan else "")
            + "<i>Habislah langsung kirim foto produk, terus langsung ketik brief-nya. "
              "Gak perlu tekan tombol apa pun.</i>",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=rows))
        await cb.answer()
        return

    hint = f.hint or f"Kirim {f.min_photos}–{f.max_photos} foto"
    await state.set_state(Flow.photos)
    simpan = inv_use_rows(cb.from_user.id, "char", "use:c")
    rows = list(batal.inline_keyboard)
    if simpan:
        rows = simpan + [[InlineKeyboardButton(text="❌ Batal", callback_data="f:cancel")]]
    await cb.message.edit_text(
        f"{f.label}\n\n📸 <b>{hint}</b>\n"
        + ("· Foto 1 = frame awal · Foto 2 = frame akhir · Foto 3+ = elemen tambahan\n" if key == "allinone" else "")
        + f"💠 Biaya: <b>{catalog.cost_for(key, dur):g} Token</b>"
        + ("\n\n🧑\u200d🎨 <b>Atau pakai karakter tersimpan</b> (1 tap, tanpa kirim foto):"
           if simpan else "")
        + "\n\n<i>Kalau foto sudah cukup, <b>langsung ketik prompt</b>-nya — gak perlu tekan tombol.</i>",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=rows))
    await cb.answer()


@router.callback_query(F.data.startswith("use:c:"))
async def cb_use_saved_char(cb: CallbackQuery, state: FSMContext):
    """Pakai karakter tersimpan sebagai foto referensi → lanjut pilih situasi (preset)."""
    r = db.char_get(cb.from_user.id, int(cb.data.split(":")[2]))
    if not r:
        await cb.answer("Karakter tidak ketemu", show_alert=True)
        return
    data = await state.get_data()
    f = catalog.get(data.get("feature", ""))
    if not f:
        await cb.answer("Sesi kadaluarsa — mulai dari menu.", show_alert=True)
        return
    await state.update_data(photos=[r["file_id"]], preset_sent=False)
    db.char_bump(r["id"])
    rows = presets.kb_rows(f.key, lambda feat, dur: catalog.cost_for(
        feat, dur or (catalog.get(feat).duration if catalog.get(feat) else 5)))
    rows.append([InlineKeyboardButton(text="✍️ Tulis sendiri", callback_data="p:sendiri")])
    rows.append([InlineKeyboardButton(text="⬅️ Menu Utama", callback_data="m:home")])
    await cb.message.edit_text(
        f"🧑\u200d🎨 Karakter <b>{r['name']}</b> dipakai.\n\n"
        f"👇 <b>Mau diapain?</b> Pilih satu — nggak perlu ngetik apa-apa.",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=rows))
    await cb.answer(f"Karakter {r['name']} dipakai")


@router.callback_query(F.data.startswith("u:ch:"))
async def cb_ugc_saved_char(cb: CallbackQuery, state: FSMContext):
    """UGC langkah 1: pakai karakter tersimpan."""
    r = db.char_get(cb.from_user.id, int(cb.data.split(":")[2]))
    if not r:
        await cb.answer("Tidak ketemu", show_alert=True)
        return
    await state.update_data(char_photo=r["file_id"])
    await state.set_state(Flow.ugc_prod)
    db.char_bump(r["id"])
    pr = inv_use_rows(cb.from_user.id, "produk", "u:pr")
    rows = pr + [[InlineKeyboardButton(text="❌ Batal", callback_data="f:cancel")]]
    await cb.message.edit_text(
        f"✅ Karakter: <b>{r['name']}</b>\n\n🛍 <b>Kirim FOTO PRODUK</b>\n"
        "Foto produk yang jelas (label terbaca, latar bersih). Boleh 1–3 foto.\n\n"
        + ("🛍️ <b>Atau pakai produk tersimpan:</b>\n" if pr else "")
        + "<i>Kalau sudah, <b>langsung ketik brief</b>-nya (nama produk, harga, keunggulan).</i>",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=rows))
    await cb.answer(f"Karakter {r['name']} dipakai")


@router.callback_query(F.data.startswith("u:pr:"))
async def cb_ugc_saved_prod(cb: CallbackQuery, state: FSMContext):
    """UGC langkah 2: pakai produk tersimpan."""
    r = db.char_get(cb.from_user.id, int(cb.data.split(":")[2]))
    if not r:
        await cb.answer("Tidak ketemu", show_alert=True)
        return
    data = await state.get_data()
    prod = data.get("prod_photos", [])
    if r["file_id"] not in prod:
        prod.append(r["file_id"])
    await state.update_data(prod_photos=prod)
    db.char_bump(r["id"])
    await cb.message.edit_text(
        f"✅ Produk: <b>{r['name']}</b> ({len(prod)} foto)\n\n"
        "✍️ <b>Sekarang ketik brief</b>-nya (nama produk, harga, keunggulan, target pembeli).\n"
        "<i>Bahasa Indonesia santai juga bisa.</i>",
        reply_markup=back_kb([[InlineKeyboardButton(text="❌ Batal", callback_data="f:cancel")]]))
    await cb.answer(f"Produk {r['name']} dipakai")


# ============================ alur UGC ============================

@router.message(Flow.ugc_char, F.photo | F.document)
async def ugc_char(msg: Message, state: FSMContext):
    fid = msg.photo[-1].file_id if msg.photo else msg.document.file_id  # type: ignore[union-attr]
    await state.update_data(char_photo=fid)
    await state.set_state(Flow.ugc_prod)
    pr = inv_use_rows(msg.from_user.id, "produk", "u:pr")
    await msg.answer(
        "✅ Foto karakter masuk.\n\n🛍 <b>Kirim FOTO PRODUK</b>\n"
        "Foto produk yang jelas (label terbaca, latar bersih). Boleh 1–3 foto.\n\n"
        + ("🛍️ <b>Atau pakai produk tersimpan:</b>\n" if pr else "")
        + "<i>Kalau sudah, <b>langsung ketik brief</b>-nya (nama produk, harga, keunggulan) — "
          "gak perlu tekan tombol.</i>",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=pr + [[InlineKeyboardButton(
            text="❌ Batal", callback_data="f:cancel")]]))


@router.message(Flow.ugc_prod, F.photo | F.document)
async def ugc_prod(msg: Message, state: FSMContext):
    data = await state.get_data()
    prod = data.get("prod_photos", [])
    if len(prod) >= 3:
        await msg.answer("Sudah 3 foto produk (maksimal) — <b>langsung ketik brief</b>-nya sekarang.")
        return
    prod.append(msg.photo[-1].file_id if msg.photo else msg.document.file_id)  # type: ignore[union-attr]
    await state.update_data(prod_photos=prod)
    await msg.answer(
        f"✅ Foto produk #{len(prod)} masuk ({len(prod)}/3).\n"
        + ("Kirim foto produk lain, atau <b>langsung ketik brief</b>-nya." if len(prod) < 3
           else "Sudah cukup — <b>sekarang ketik brief</b>-nya."))


@router.message(Flow.ugc_prod, F.text)
async def ugc_brief_text(msg: Message, state: FSMContext):
    """Teks saat tahap foto produk = BRIEF → langsung ke layar konfirmasi (tanpa tombol)."""
    data = await state.get_data()
    # "tinggal sebut namanya" untuk UGC: karakter & produk tersimpan otomatis dipakai
    if not data.get("char_photo"):
        rc = db.char_find_in_text(msg.from_user.id, msg.text, kind="char")
        if rc:
            await state.update_data(char_photo=rc["file_id"])
            db.char_bump(rc["id"])
            await msg.answer(f"🧑\u200d🎨 Pakai karakter tersimpan: <b>{rc['name']}</b>")
            data = await state.get_data()
    if not data.get("prod_photos"):
        rp = db.char_find_in_text(msg.from_user.id, msg.text, kind="produk")
        if rp:
            await state.update_data(prod_photos=[rp["file_id"]])
            db.char_bump(rp["id"])
            await msg.answer(f"🛍️ Pakai produk tersimpan: <b>{rp['name']}</b>")
            data = await state.get_data()
    if not data.get("prod_photos"):
        await msg.answer("Kirim minimal 1 <b>foto produk</b> dulu, baru ketik brief-nya ya.")
        return
    await state.update_data(brief=msg.text.strip()[:1500])
    await _confirm(msg, state, msg.from_user.id)


@router.callback_query(F.data == "u:prod:next")     # tombol lama → tetap didukung
async def ugc_to_brief(cb: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if not data.get("prod_photos"):
        await cb.answer("Kirim minimal 1 foto produk dulu", show_alert=True)
        return
    await cb.message.edit_text("📝 <b>Ketik brief</b>-nya sekarang (teks biasa) — nama produk, harga, keunggulan.")
    await cb.answer()


@router.callback_query(F.data == "u:stylemenu")
async def ugc_style_menu(cb: CallbackQuery, state: FSMContext):
    await cb.message.edit_text(
        "🎨 <b>Pilih gaya video</b>\nSistem bakal rakit prompt profesional dari brief kamu.",
        reply_markup=style_kb())
    await cb.answer()


@router.callback_query(F.data.startswith("u:style:"))
async def ugc_style(cb: CallbackQuery, state: FSMContext):
    key = cb.data.split(":")[2]
    if key not in promptsmith.STYLES:
        await cb.answer("Gaya tidak dikenal", show_alert=True)
        return
    await state.update_data(style=key)
    await _confirm(cb.message, state, cb.from_user.id, edit=True)
    await cb.answer(f"Gaya: {promptsmith.STYLES[key].label}")


# ============================ alur umum: foto → prompt → rasio ============================

# Nama bahan per fitur: aset ke-1 biasanya orangnya, ke-2 = video gerakan / suara.
ASSET_LABEL: dict[str, tuple[str, ...]] = {
    "motion": ("Foto orang", "Video gerakan"),
    "lipsync": ("Foto orang", "Suara"),
    "pose": ("Foto orang", "Foto pose"),
    "faceswap": ("Foto orang", "Foto wajah/model"),
}


def _asset_name(key: str, idx: int) -> str:
    labels = ASSET_LABEL.get(key) or ()
    return labels[idx] if 0 <= idx < len(labels) else f"Foto #{idx + 1}"


@router.message(Flow.photos, F.photo | F.document | F.video | F.audio | F.voice)
async def on_photo(msg: Message, state: FSMContext):
    data = await state.get_data()
    f = catalog.get(data.get("feature", ""))
    photos: list[str] = data.get("photos", [])
    if f and len(photos) >= f.max_photos:
        await msg.answer(f"Sudah maksimal {f.max_photos} foto — <b>langsung ketik prompt</b>-nya.")
        return
    if msg.photo:
        photos.append(msg.photo[-1].file_id)
    elif msg.video:
        photos.append(msg.video.file_id)
    elif msg.audio:
        photos.append(msg.audio.file_id)
    elif msg.voice:
        photos.append(msg.voice.file_id)
    else:
        photos.append(msg.document.file_id)      # type: ignore[union-attr]
    await state.update_data(photos=photos)
    fkey = f.key if f else ""
    sisa = (f.max_photos - len(photos)) if f else 0
    kurang = (f.min_photos - len(photos)) if f else 0
    t = f"✅ {_asset_name(fkey, len(photos) - 1)} masuk ({len(photos)}/{f.max_photos if f else '?'}).\n"
    if kurang > 0:
        t += f"Sekarang kirim <b>{_asset_name(fkey, len(photos))}</b>."
    elif sisa > 0:
        t += "Kirim tambahan kalau perlu" + (", atau <b>langsung ketik prompt</b>-nya."
                                             if (f and f.need_prompt) else ".")
    else:
        t += "<b>Sekarang ketik prompt</b>-nya." if (f and f.need_prompt) else "<b>Bahan sudah lengkap.</b>"
    await msg.answer(t)

    # ---- PRESET 1-TAP: user cukup tap satu tombol, tidak perlu ngetik prompt ----
    if f and len(photos) >= f.min_photos and not data.get("preset_sent"):
        if not f.need_prompt:          # motion / lipsync / faceswap → tak ada prompt, langsung konfirmasi
            await state.update_data(preset_sent=True)
            await _confirm(msg, state, msg.from_user.id)
            return
        rows = presets.kb_rows(f.key, lambda feat, dur: catalog.cost_for(
            feat, dur or (catalog.get(feat).duration if catalog.get(feat) else 5)))
        if rows:
            await state.update_data(preset_sent=True)
            rows.append([InlineKeyboardButton(text="🔙 Menu Utama", callback_data="m:home")])
            await msg.answer(
                "👇 <b>Mau diapain?</b>\n"
                "Pilih satu → langsung diproses. <i>(nggak perlu ngetik apa-apa)</i>",
                reply_markup=InlineKeyboardMarkup(inline_keyboard=rows))


@router.message(Flow.photos, F.text)
async def on_prompt_in_photos(msg: Message, state: FSMContext):
    """Teks saat tahap foto = PROMPT (alur tanpa tombol, seperti Kuzushi)."""
    data = await state.get_data()
    f = catalog.get(data.get("feature", ""))
    photos = data.get("photos", [])
    if f and len(photos) < f.min_photos:
        await msg.answer(f"Kirim minimal <b>{f.min_photos} foto</b> dulu ya, baru ketik prompt-nya.")
        return
    await state.update_data(prompt=msg.text.strip()[:1000])
    # "tinggal sebut namanya": kalau belum ada foto & user menyebut nama karakter tersimpan,
    # otomatis pakai character sheet itu (identik tiap kali).
    d2 = await state.get_data()
    if not d2.get("photos"):
        r = db.char_find_in_text(msg.from_user.id, msg.text, kind="char")
        if r:
            await state.update_data(photos=[r["file_id"]])
            db.char_bump(r["id"])
            await msg.answer(f"🧑\u200d🎨 Pakai karakter tersimpan: <b>{r['name']}</b>")
    await _confirm(msg, state, msg.from_user.id)


@router.callback_query(F.data.startswith("p:"))
async def cb_preset(cb: CallbackQuery, state: FSMContext):
    """Preset 1-TAP: pilih situasi → langsung masuk layar konfirmasi (harga tampil)."""
    key = cb.data[2:]
    data = await state.get_data()
    f = catalog.get(data.get("feature", ""))
    if not f:
        await cb.answer("Sesi kadaluarsa — mulai dari menu utama.", show_alert=True)
        return
    if key == "sendiri":
        await cb.message.edit_text(
            f"{f.label}\n\n✍️ <b>Ketik prompt kamu sekarang</b>\n"
            "<i>Teks biasa aja — bahasa Indonesia juga bisa, nanti dirapikan otomatis.</i>",
            reply_markup=back_kb([[InlineKeyboardButton(text="🎲 Kasih preset acak",
                                                        callback_data="p:kejutan")]]))
        await cb.answer()
        return
    pr = presets.resolve(key, twist=int(time.time()) % 997)
    if not pr:
        await cb.answer("Preset itu belum siap ya.", show_alert=True)
        return
    upd: dict = {"preset": pr.key, "prompt": pr.text()}
    if pr.feature:
        nf = catalog.get(pr.feature)
        if nf and nf.key in catalog.SIAP_JUAL:
            upd["feature"] = nf.key
            f = nf
    if pr.duration and pr.duration in f.durations:
        upd["duration"] = pr.duration
    await state.update_data(**upd)
    if not upd.get("prompt"):        # preset cerita: user tetap menulis ceritanya
        await cb.message.edit_text(
            f"{f.label}\n\n📖 <b>Tulis ceritanya sekarang</b>\n"
            "<i>Bebas & berantakan juga boleh — nanti bot yang mecah jadi beberapa adegan.</i>",
            reply_markup=back_kb([[InlineKeyboardButton(text="🎲 Kasih preset acak",
                                                        callback_data="p:kejutan")]]))
        await cb.answer(f"{pr.emoji} {pr.label}")
        return
    await _confirm(cb.message, state, cb.from_user.id, edit=True)
    await cb.answer(f"{pr.emoji} {pr.label} ✓")


@router.callback_query(F.data == "f:next")          # tombol lama → tetap didukung
async def cb_next(cb: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    f = catalog.get(data.get("feature", ""))
    if not f:
        await cb.answer("Sesi kadaluarsa — mulai dari menu.", show_alert=True)
        return
    photos = data.get("photos", [])
    if len(photos) < f.min_photos:
        await cb.answer(f"Butuh minimal {f.min_photos} foto", show_alert=True)
        return
    if f.need_prompt and not data.get("prompt"):
        await cb.message.edit_text(
            f"{f.label}\n\n📝 <b>Ketik prompt</b>-nya sekarang (teks biasa).",
            reply_markup=back_kb([[InlineKeyboardButton(text="❌ Batal", callback_data="f:cancel")]]))
    else:
        await _confirm(cb.message, state, cb.from_user.id, edit=True)
    await cb.answer()


@router.callback_query(F.data.startswith("a:ratio:"))
async def adj_ratio(cb: CallbackQuery, state: FSMContext):
    # ⚠️ rasio memuat titik dua ("9:16") → JANGAN pakai split(":")[2]
    await state.update_data(ratio=cb.data[len("a:ratio:"):])
    await _confirm(cb.message, state, cb.from_user.id, edit=True)
    await cb.answer(f"✅ Rasio {cb.data[len('a:ratio:'):]} dipilih — tekan 🚀 Render")


@router.callback_query(F.data.startswith("a:dur:"))
async def adj_duration(cb: CallbackQuery, state: FSMContext):
    try:
        await state.update_data(duration=int(cb.data.split(":")[2]))
    except (IndexError, ValueError):
        await cb.answer("Durasi tidak valid", show_alert=True)
        return
    d = int(cb.data.split(":")[2])
    f = catalog.get((await state.get_data()).get("feature", ""))
    await _confirm(cb.message, state, cb.from_user.id, edit=True)
    await cb.answer(f"✅ {d} detik · {catalog.cost_for(f.key, d) if f else 0:g} Token — tekan 🚀 Render kalau pas")


async def _confirm(target: Message, state: FSMContext, uid: int, edit: bool = False):
    data = await state.get_data()
    f = catalog.get(data.get("feature", ""))
    if not f:
        await target.answer("Sesi kadaluarsa — mulai ulang dari menu utama.")
        return
    dur = int(data.get("duration") or f.duration)
    cost = catalog.cost_for(f.key, dur)
    ratio = data.get("ratio", "9:16")
    saldo = db.balance(uid)
    cukup = saldo >= cost

    if f.kind == "ugc":
        # PENTING: prompt rakitan TIDAK ditampilkan — user hanya lihat pilihan & brief miliknya
        teks = (f"{f.label}\n\n🖼 Foto karakter: <b>✅</b>\n"
                f"🛍 Foto produk: <b>{len(data.get('prod_photos', []))}</b>\n"
                f"{promptsmith.summary_for_user(data.get('style', ''))}\n"
                f"📝 Brief kamu: <i>{(data.get('brief') or '-')[:160]}</i>\n"
                f"📐 Rasio: <b>{ratio}</b> · ⏱ Durasi: <b>{dur} dtk</b>\n\n"
                f"💠 Biaya: <b>{cost:g} Token</b>\n{saldo_txt(uid)}")
    else:
        teks = (f"{f.label}\n\n🖼 Foto: <b>{len(data.get('photos', []))}</b>\n"
                f"📝 Prompt: <i>{(data.get('prompt') or '-')[:200]}</i>\n"
                f"📐 Rasio: <b>{ratio}</b> · ⏱ Durasi: <b>{dur} dtk</b>\n\n"
                f"💠 Biaya: <b>{cost:g} Token</b>\n{saldo_txt(uid)}"
                + ("\n✨ Prompt kamu dirapikan otomatis biar hasilnya lebih rapi."
                   if settings.refine_video else ""))

    teks += "\n\n" + ("Tekan 🚀 Render kalau sudah pas (bisa ganti rasio/durasi di bawah)."
                      if cukup else "⚠️ Saldo kurang — Top Up dulu ya.")

    rows: list[list[InlineKeyboardButton]] = []
    if cukup:
        rows.append([InlineKeyboardButton(text=f"🚀 Render ({cost:g} Token)", callback_data="f:render")])
    else:
        rows.append([InlineKeyboardButton(text="⚡ Top Up", callback_data="m:topup")])
    if f.need_ratio:
        rows.append([InlineKeyboardButton(text=(("✅ " if k == ratio else "") + v.split(" (")[0]),
                                          callback_data=f"a:ratio:{k}")
                     for k, v in catalog.RATIOS.items()])
    if len(f.durations) > 1:
        rows.append([InlineKeyboardButton(
            text=(("✅ " if d == dur else "") + f"{d} dtk · {catalog.cost_for(f.key, d):g}T"),
            callback_data=f"a:dur:{d}") for d in f.durations])
    if f.kind == "ugc":
        rows.append([InlineKeyboardButton(text="🎨 Ganti gaya", callback_data="u:stylemenu")])
    rows.append([InlineKeyboardButton(text="❌ Batal", callback_data="f:cancel")])
    kb = back_kb(rows)
    if edit:
        # Ganti durasi/rasio = EDIT pesan yang sama, bukan kirim pesan baru.
        # (Bug sebelumnya: tiap tap muncul pesan baru → "muncul itu lagi itu lagi".)
        try:
            await target.edit_text(teks, reply_markup=kb)
            return
        except TelegramBadRequest as e:
            if "not modified" in str(e).lower():
                return                  # pilihan tidak berubah → jangan kirim pesan baru
        except Exception:               # noqa: BLE001
            pass
    await target.answer(teks, reply_markup=kb)


@router.callback_query(F.data == "f:recheck")
async def cb_recheck(cb: CallbackQuery, state: FSMContext):
    """Setelah top up: kembali ke halaman konfirmasi tanpa mengulang alur."""
    data = await state.get_data()
    if not data.get("feature"):
        await cb.answer("Tidak ada sesi aktif — mulai dari menu.", show_alert=True)
        return
    await _confirm(cb.message, state, cb.from_user.id)
    await cb.answer("Saldo diperbarui")


@router.callback_query(F.data == "f:cancel")
async def cb_cancel(cb: CallbackQuery, state: FSMContext):
    await state.clear()
    await cb.message.edit_text("❌ Dibatalkan.\n\n🏠 Menu Utama", reply_markup=main_menu_kb(cb.from_user.id))
    await cb.answer()


@router.message(Command("cancel"))
async def cmd_cancel(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer("❌ Dibatalkan.\n\n🏠 /start untuk menu utama.")


# ============================ render ============================

def collect_photos(data: dict, f) -> list[str]:
    """Ambil daftar file_id sesuai jenis fitur."""
    if f.kind == "ugc":
        return [p for p in [data.get("char_photo", "")] + list(data.get("prod_photos", [])) if p]
    return list(data.get("photos", []))


def build_final_prompt(data: dict, f, ratio: str) -> tuple[str, str, str]:
    """Kembalikan (prompt_final, brief, style). UGC → dirakit PromptSmith."""
    if f.kind == "ugc":
        brief = data.get("brief", "")
        style = data.get("style", "review")
        return promptsmith.build_ugc_prompt(brief, style, product_hint="", ratio=ratio), brief, style
    # Prompt user dikirim APA ADANYA (tanpa klausa tambahan) — sama seperti
    # @KuzushiGenBot. Menempel klausa karangan (mis. "LIVING BACKGROUND") terbukti
    # bikin model lebih agresif menggerakkan seluruh frame → wajah/badan ikut warp.
    return " ".join(str(data.get("prompt") or "").split()), "", ""


@router.callback_query(F.data == "f:render")
async def cb_render(cb: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    f = catalog.get(data.get("feature", ""))
    if not f:
        await cb.answer("Sesi kadaluarsa — mulai ulang dari menu.", show_alert=True)
        return
    photos = collect_photos(data, f)
    if not photos:
        await cb.answer("Sesi kadaluarsa — mulai ulang dari menu.", show_alert=True)
        return
    dur = int(data.get("duration") or f.duration)
    cost = catalog.cost_for(f.key, dur)
    if db.balance(cb.from_user.id) < cost:
        await cb.answer("Saldo kurang", show_alert=True)
        return

    ratio = data.get("ratio", "9:16")
    prompt, brief, style = build_final_prompt(data, f, ratio)
    job_id = db.create_job(cb.from_user.id, f.key, cost, photos, prompt, ratio,
                           brief=brief, style=style, duration=dur)
    db.ledger_add(cb.from_user.id, -cost, "render", ref=str(job_id))
    await state.clear()

    # prompt hanya untuk internal/admin — TIDAK pernah ditampilkan ke user
    log.info("job %s [%s] prompt internal (%d char): %s", job_id, f.key, len(prompt), prompt[:180])
    await cb.message.edit_text(
        f"🎬 <b>{f.label}</b> 🚀\n\n🆔 Job: <code>{job_id}</code>\n"
        f"{bar(2)} 2%\n💬 Status: menyerahkan tugas ke backend...\n"
        f"{saldo_txt(cb.from_user.id)}", parse_mode=ParseMode.HTML)
    asyncio.create_task(process_job(job_id, cb.bot, cb.message.chat.id, cb.message.message_id))
    await cb.answer("Render dimulai")


async def fetch_url(url: str, dest: Path) -> Path:
    """Unduh hasil dari backend cloud (RunningHub/fal balikin URL, bukan file lokal)."""
    def _dl() -> None:
        import urllib.request
        req = urllib.request.Request(url, headers={"User-Agent": "kreaibot/1.0"})
        with urllib.request.urlopen(req, timeout=900) as r, open(dest, "wb") as f:
            shutil.copyfileobj(r, f)

    dest.parent.mkdir(parents=True, exist_ok=True)
    await asyncio.to_thread(_dl)
    return dest


async def process_job(job_id: int, bot: Bot, chat_id: int, msg_id: int):
    async with SEM:
        job = db.get_job(job_id)
        if not job:
            return
        f = catalog.get(job["feature"])
        work = Path(settings.work_dir) / f"job_{job_id}"
        work.mkdir(parents=True, exist_ok=True)
        try:
            # 0) UGC: haluskan prompt lewat LLM (opsional; gagal → pakai template)
            if f and f.kind == "ugc":
                refined = await promptsmith.refine_with_llm(
                    job["prompt"] or "", job["brief"] or "", job["style"] or "review",
                    base_url=settings.promptsmith_base, api_key=settings.promptsmith_key,
                    model=settings.promptsmith_model)
                if refined and refined != job["prompt"]:
                    log.info("job %s prompt dihaluskan LLM (%d → %d char)", job_id,
                             len(job["prompt"] or ""), len(refined))
                    db.set_job(job_id, prompt=refined)
            elif f and settings.refine_video and (job["prompt"] or "").strip():
                # 0b) fitur video biasa (i2v/all-in-one): rapikan prompt user.
                #     Gagal / hasil aneh → refine_video_prompt mengembalikan prompt ASLI.
                refined = await promptsmith.refine_video_prompt(
                    job["prompt"] or "", ratio=job["ratio"] or "9:16",
                    duration=int(job["duration"] or f.duration),
                    base_url=settings.promptsmith_base, api_key=settings.promptsmith_key,
                    model=settings.promptsmith_model)
                if refined and refined != job["prompt"]:
                    log.info("job %s prompt video dirapikan LLM (%d → %d char)",
                             job_id, len(job["prompt"] or ""), len(refined))
                    db.set_job(job_id, prompt=refined)

            # 1) unduh aset referensi
            photos = json.loads(job["ref_photos"] or "[]")
            local: list[Path] = []
            video_in: Path | None = None
            for i, fid in enumerate(photos, 1):
                p = work / f"ref{i}.bin"
                tg = await bot.get_file(fid)
                await bot.download_file(tg.file_path, p)   # type: ignore[arg-type]
                local.append(p)
                if f and f.key in ("faceswap", "motion", "lipsync") and i == 2:
                    video_in, local = local[-1], local[:-1]
            out = work / "hasil.mp4"

            # 1b) MODE CERITA (multi-shot): skenario panjang → N klip pendek, frame terakhir
            #     disambung ke klip berikutnya, lalu dijahit jadi 1 video.
            if f and f.backend_workflow == "krea_story" and local:
                n_shots, per_shot = storyboard.plan_shots(int(job["duration"] or f.duration))
                shots = await promptsmith.split_story(
                    job["prompt"] or "", shots=n_shots, seconds_each=per_shot,
                    base_url=settings.promptsmith_base, api_key=settings.promptsmith_key,
                    model=settings.promptsmith_model)
                db.set_job(job_id, status="running", task_id=f"story:{len(shots)}x{per_shot}s")
                log.info("job %s mode CERITA: %d scene × %ds", job_id, len(shots), per_shot)

                async def _story_progress(i: int, total: int, msg: str, _c=chat_id, _m=msg_id):
                    try:
                        await bot.edit_message_text(
                            f"🎬 <b>{f.label}</b>\n\n🎞 Scene {i}/{total}\n"
                            f"✅ {i-1} scene selesai · ⏳ scene {i} sedang dirender\n"
                            f"💬 {msg}\n🆔 Job <code>{job_id}</code>",
                            chat_id=_c, message_id=_m, parse_mode=ParseMode.HTML)
                    except Exception:
                        pass

                result = await storyboard.render_story(
                    backend, photo=local[0], shots=shots, ratio=job["ratio"] or "9:16",
                    work=work, dur_each=per_shot, job_id=job_id,
                    poll_interval=settings.poll_interval, on_progress=_story_progress)
                result = await asyncio.to_thread(unwrap_media, result)
                result = await asyncio.to_thread(smooth_fps, result)
                db.set_job(job_id, status="done", result_path=str(result))
                await send_result(bot, chat_id, result,
                                  f"✨ <b>{f.label}</b> selesai — {len(shots)} scene disambung!\n"
                                  f"🆔 Job <code>{job_id}</code> · {saldo_txt(job['telegram_id'])}")
                try:
                    await bot.delete_message(chat_id, msg_id)
                except Exception:
                    pass
                log.info("job %s (cerita) selesai: %s", job_id, result)
                return

            # 1c) LIPSYNC: durasi = panjang suara yang dikirim (maks 10 dtk, sesuai harga 0,5T)
            if f and f.key == "lipsync" and video_in and Path(video_in).exists():
                try:
                    from backends.mock import ffmpeg_bin
                    fprobe = str(Path(ffmpeg_bin()).with_name("ffprobe"))
                    pr = subprocess.run([fprobe, "-v", "error", "-show_entries", "format=duration",
                                         "-of", "csv=p=0", str(video_in)],
                                        capture_output=True, text=True, timeout=30)
                    ln = float((pr.stdout or "0").strip() or 0)
                    if ln > 0:
                        job["duration"] = max(3, min(int(round(ln)), 10))
                        log.info("job %s lipsync: suara %.1f dtk → durasi %s dtk", job_id, ln, job["duration"])
                except Exception as e:                        # noqa: BLE001
                    log.warning("job %s gagal baca durasi suara: %s", job_id, e)

            # 2) submit ke backend + poll
            req = GenRequest(job_id=job_id, feature_key=job["feature"],
                             workflow=f.backend_workflow if f else "", photos=local,
                             video_in=video_in, prompt=job["prompt"] or "",
                             ratio=job["ratio"] or "9:16",
                             duration=(job["duration"] or (f.duration if f else 5)), out_path=out)
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
                    rp = str(st.result_path or "")
                    if rp.startswith("http"):
                        try:
                            result = await fetch_url(rp, out)     # cloud → unduh ke lokal
                        except Exception as dl_err:
                            log.warning("job %s gagal unduh hasil: %s", job_id, dl_err)
                            result = out
                    elif rp and Path(rp).exists():
                        result = Path(rp)
                    else:
                        result = out
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

            result = await asyncio.to_thread(unwrap_media, result)  # kalau ZIP, ambil media
            result = await asyncio.to_thread(smooth_fps, result)   # 16fps → 30fps halus
            db.set_job(job_id, status="done", result_path=str(result))
            await send_result(bot, chat_id, result,
                              f"✨ <b>{f.label}</b> selesai tanpa watermark!\n"
                              f"🆔 Job <code>{job_id}</code> · {saldo_txt(job['telegram_id'])}")
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
        f"/give &lt;id&gt; &lt;token&gt; · /voucher &lt;code&gt; &lt;token&gt; [max]\n"
        f"/prompt &lt;job_id&gt; (prompt internal) · /cek",
        parse_mode=ParseMode.HTML)


@router.message(Command("prompt"))
async def cmd_prompt(msg: Message):
    """Admin: lihat prompt internal hasil rakitan PromptSmith."""
    if not is_admin(msg.from_user.id):
        return
    parts = (msg.text or "").split()
    if len(parts) != 2:
        await msg.answer("Format: /prompt <job_id>")
        return
    job = db.get_job(int(parts[1]))
    if not job:
        await msg.answer("Job tidak ditemukan.")
        return
    await msg.answer(
        f"🧠 <b>Prompt internal job {job['id']}</b> ({job['feature']}, gaya: {job['style'] or '-'})\n\n"
        f"<code>{(job['prompt'] or '')[:3500]}</code>", parse_mode=ParseMode.HTML)


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
    await msg.answer(
        "📖 <b>Cara pakai KREE.AI</b>\n\n"
        "1️⃣ Buka menu (/start) → pilih fitur\n"
        "2️⃣ Pilih durasi lewat tombol (harga langsung kelihatan)\n"
        "3️⃣ Kirim foto → <b>pilih situasi (1 tap, nggak perlu ngetik prompt)</b> → tekan 🚀 Render\n\n"
        f"Fitur siap pakai: {', '.join(f.label for f in catalog.enabled_features())}\n"
        "Segera hadir: Pose Transfer, Lip Sync\n\n"
        "Perintah: /start · /saldo · /topup · /cancel · /help")


# ================= INVENTORY: KARAKTER & PRODUK SAYA =================
# Ide user: simpan master (character sheet / produk) SEKALI, kasih nama sendiri,
# nanti tinggal SEBUT NAMANYA → bot otomatis pakai secara identik. Taruh di paling atas menu.
INV_ICON = {"char": "🧑\u200d🎨", "produk": "🛍️"}
INV_TITLE = {"char": "Karakter Saya", "produk": "Produk Saya"}
INV_HINT = {
    "char": "Simpan 1 foto master (wajah/karakter). Nanti kamu tinggal <b>sebut namanya</b> "
            "di fitur mana pun — bot otomatis pakai foto yang sama, jadi hasilnya konsisten.",
    "produk": "Simpan foto produkmu (label jelas, latar bersih). Nanti tinggal sebut namanya "
              "waktu bikin UGC — nggak perlu kirim ulang.",
}


def inv_kb(uid: int, kind: str) -> InlineKeyboardMarkup:
    rows = [[InlineKeyboardButton(text=f"{INV_ICON[kind]} {r['name']} · {r['uses']}×",
                                  callback_data=f"m:ch:{r['id']}")]
            for r in db.char_list(uid, kind=kind)]
    rows.append([InlineKeyboardButton(text="➕ Tambah baru", callback_data=f"m:inv:add:{kind}"),
                 InlineKeyboardButton(text="⬅️ Menu Utama", callback_data="m:home")])
    return InlineKeyboardMarkup(inline_keyboard=rows)


def inv_text(uid: int, kind: str) -> str:
    lst = db.char_list(uid, kind=kind)
    head = f"{INV_ICON[kind]} <b>{INV_TITLE[kind]}</b>\n\n{INV_HINT[kind]}\n\n"
    if not lst:
        return head + "<i>Belum ada yang disimpan.</i> Tekan ➕ Tambah baru."
    return head + "\n".join(f"· <b>{r['name']}</b> — dipakai {r['uses']}×" for r in lst) + \
        "\n\n👇 Tap salah satu buat ubah / hapus."


def inv_use_rows(uid: int, kind: str, prefix: str) -> list:
    """Baris tombol 'pakai yang tersimpan' untuk disisipkan di alur fitur."""
    return [[InlineKeyboardButton(text=f"{INV_ICON[kind]} {r['name']}",
                                  callback_data=f"{prefix}:{r['id']}")]
            for r in db.char_list(uid, kind=kind)]


def inv_parse(data: str) -> tuple[str, str]:
    """Baca callback inventory: 'm:inv:char' → ('char','buka') · 'm:inv:add:char' → ('char','add').

    (BUG 9 Okt: dulu 'm:inv:add:char' dibaca parts[2]='add' → user dapat popup
     "Jenis tidak dikenal" waktu tekan ➕ Tambah baru.)
    """
    parts = (data or "").split(":")
    aksi = parts[2] if len(parts) > 2 else ""
    if aksi == "add":
        return (parts[3] if len(parts) > 3 else ""), "add"
    return aksi, "buka"


@router.callback_query(F.data.startswith("m:inv:"))
async def cb_inv(cb: CallbackQuery, state: FSMContext):
    kind, aksi = inv_parse(cb.data)
    uid = cb.from_user.id
    if kind not in INV_ICON:
        await cb.answer("Jenis tidak dikenal", show_alert=True)
        return
    if aksi == "buka":                        # buka daftar
        await cb.message.edit_text(inv_text(uid, kind), reply_markup=inv_kb(uid, kind))
        await cb.answer()
        return
    await state.clear()                        # m:inv:add:<kind>
    await state.update_data(inv_kind=kind)
    await state.set_state(Flow.inv_photo)
    await cb.message.edit_text(
        f"{INV_ICON[kind]} <b>Tambah {INV_TITLE[kind]}</b>\n\n📸 Kirim fotonya sekarang.\n\n"
        f"<i>{INV_HINT[kind]}</i>",
        reply_markup=back_kb([[InlineKeyboardButton(text="❌ Batal",
                                                    callback_data=f"m:inv:{kind}")]]))
    await cb.answer()


@router.message(Flow.inv_photo, F.photo | F.document)
async def inv_photo(msg: Message, state: FSMContext):
    data = await state.get_data()
    kind = data.get("inv_kind", "char")
    doc = msg.document
    if doc and not str(doc.mime_type or "").startswith("image/"):
        await msg.answer("Itu bukan gambar 📄 — kirim sebagai <b>FOTO</b> ya (atau tekan ❌ Batal).")
        return
    fid = msg.photo[-1].file_id if msg.photo else doc.file_id   # type: ignore[union-attr]
    await state.update_data(inv_file_id=fid)
    await state.set_state(Flow.inv_name)
    contoh = "si rina" if kind == "char" else "kopi arabika"
    await msg.answer(
        f"✅ Foto diterima.\n\n✏️ <b>Kasih nama</b> sekarang (bebas).\n"
        f"<i>Contoh: {contoh}</i>\n\n"
        "Nanti tinggal sebut nama ini di fitur mana pun.")


@router.message(Flow.inv_name, F.text)
async def inv_name(msg: Message, state: FSMContext):
    data = await state.get_data()
    uid = msg.from_user.id
    nm = " ".join((msg.text or "").split())[:40]
    rid = data.get("inv_rename_id")
    if rid:
        okr = db.char_rename(uid, int(rid), nm)
        await state.clear()
        await msg.answer(f"✅ Nama diganti jadi <b>{nm}</b>." if okr
                         else "⚠️ Nama itu sudah dipakai. Coba nama lain.",
                         reply_markup=main_menu_kb(uid))
        return
    kind = data.get("inv_kind", "char")
    cid = db.char_save(uid, nm, data.get("inv_file_id") or "", kind=kind)
    if not cid:
        await state.update_data(inv_rename_id=None)
        await msg.answer("⚠️ Nama itu sudah dipakai — ketik nama lain ya.")
        return
    await state.clear()
    await msg.answer(
        f"✅ <b>{nm}</b> tersimpan di {INV_TITLE[kind]}.\n\n"
        "Sekarang tinggal <b>sebut namanya</b> waktu bikin konten — bot otomatis pakai foto ini.",
        reply_markup=main_menu_kb(uid))


@router.message(Flow.inv_photo)
async def inv_photo_bukan_foto(msg: Message):
    """Anti-bingung: user kirim video/stiker/teks padahal diminta foto."""
    await msg.answer("📸 Kirim <b>FOTO</b> ya (bukan video/teks) — atau tekan ❌ Batal di layar sebelumnya.")


@router.message(Flow.inv_name)
async def inv_name_bukan_teks(msg: Message):
    """Anti-bingung: user kirim foto padahal diminta nama."""
    await msg.answer("✏️ Ketik <b>nama</b>-nya (huruf/teks) ya, misal: <i>si rina</i>")


@router.callback_query(F.data.startswith("m:chr:"))          # ganti nama
async def cb_char_rename(cb: CallbackQuery, state: FSMContext):
    cid = int(cb.data.split(":")[2])
    r = db.char_get(cb.from_user.id, cid)
    if not r:
        await cb.answer("Tidak ketemu", show_alert=True)
        return
    await state.clear()
    await state.update_data(inv_rename_id=cid, inv_kind=r["kind"] or "char")
    await state.set_state(Flow.inv_name)
    await cb.message.answer(f"✏️ Ketik <b>nama baru</b> untuk {INV_ICON[r['kind']]} <b>{r['name']}</b>:")
    await cb.answer()


@router.callback_query(F.data.startswith("m:chd:"))          # hapus
async def cb_char_delete(cb: CallbackQuery, state: FSMContext):
    cid = int(cb.data.split(":")[2])
    r = db.char_get(cb.from_user.id, cid)
    if not r:
        await cb.answer("Tidak ketemu", show_alert=True)
        return
    kind = r["kind"] or "char"
    db.char_delete(cb.from_user.id, cid)
    try:
        await cb.message.delete()
    except Exception:                        # noqa: BLE001
        pass
    await cb.message.answer(f"🗑 <b>{r['name']}</b> dihapus dari {INV_TITLE[kind]}.",
                            reply_markup=inv_kb(cb.from_user.id, kind))
    await cb.answer("Dihapus")


@router.callback_query(F.data.startswith("m:ch:"))
async def cb_char_detail(cb: CallbackQuery, state: FSMContext):
    cid = int(cb.data.split(":")[2])
    r = db.char_get(cb.from_user.id, cid)
    if not r:
        await cb.answer("Tidak ketemu", show_alert=True)
        return
    kind = r["kind"] or "char"
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✏️ Ganti nama", callback_data=f"m:chr:{cid}"),
         InlineKeyboardButton(text="🗑 Hapus", callback_data=f"m:chd:{cid}")],
        [InlineKeyboardButton(text=f"🔙 {INV_TITLE[kind]}", callback_data=f"m:inv:{kind}")]])
    cap = (f"{INV_ICON[kind]} <b>{r['name']}</b>\n"
           f"📊 Dipakai: {r['uses']}×\n"
           f"📅 Disimpan: {time.strftime('%d %b %Y', time.localtime(r['created_at']))}")
    try:
        await cb.message.delete()
    except Exception:                        # noqa: BLE001
        pass
    await cb.message.answer_photo(r["file_id"], caption=cap, reply_markup=kb)
    await cb.answer()


# ============================ teks bebas ============================
# Didaftarkan PALING AKHIR supaya tidak menabrak handler ber-FSM di atas.

_DUR_RE = re.compile(r"^\s*(\d{1,2})\s*(?:d(?:tk|etik)?|s(?:ec|dtk|econd)?)?\s*$", re.I)


@router.message(F.text)
async def on_free_text(msg: Message, state: FSMContext):
    """Teks di luar alur — mis. user ngetik '15 detik' di layar menu (kasus nyata).

    Kalau angkanya cocok dengan pilihan durasi fitur aktif, langsung dipakai.
    """
    m = _DUR_RE.match((msg.text or "").strip())
    if m:
        want = int(m.group(1))
        data = await state.get_data()
        f = catalog.get(data.get("feature", ""))
        if f and want in f.durations:
            await state.update_data(duration=want)
            photos = collect_photos(data, f)
            if photos or data.get("prod_photos") or data.get("prompt") or data.get("brief"):
                await _confirm(msg, state, msg.from_user.id)
            else:
                await msg.answer(
                    f"✅ Oke, <b>{want} detik</b> ({catalog.cost_for(f.key, want):g} Token).\n\n"
                    f"{f.hint or 'Kirim fotonya sekarang.'}\n\n"
                    f"<i>Kirim foto → langsung ketik prompt → tekan Render.</i>")
            return
    await msg.answer("Ketik /start buat buka menu ya 🙂  (atau /help kalau bingung)")


# ============================ entrypoint ============================

def check() -> int:
    errs = settings.validate()
    print("=== KREE.AI — pemeriksaan konfigurasi ===")
    print(f"backend   : {settings.backend}")
    print(f"db        : {settings.db_path}")
    print(f"work      : {settings.work_dir}")
    print(f"admin     : {settings.admin_ids}")
    print(f"harga     : Rp{settings.harga_per_10k} = {settings.tokens_per_10k} token")
    print(f"prompt LLM: {'aktif' if (settings.promptsmith_key and settings.promptsmith_model) else 'template offline'}")
    print("\n=== Katalog fitur ===")
    for f in catalog.FEATURES.values():
        print(f"  {f.label:34s} {f.cost:>4g} token  (Rp{catalog.price_rp(f, settings.tokens_per_10k, settings.harga_per_10k)})  "
              f"foto {f.min_photos}-{f.max_photos}" + ("  [UGC bertingkat]" if f.kind == "ugc" else ""))
    print("\n=== Gaya UGC (PromptSmith) ===")
    for s in promptsmith.STYLES.values():
        print(f"  {s.label:28s} {s.duration}s  {'(tanpa bicara)' if not s.talk else ''}")
    print("\n=== Statistik DB ===")
    print(f"  {db.stats()}")
    if errs:
        print("\n⚠️  Masalah:")
        for e in errs:
            print("  -", e)
        return 1
    print("\n✅ Konfigurasi OK.")
    return 0


async def _resume_one(bot: Bot, job: dict) -> None:
    """Lanjutkan SATU job: poll task lama → unduh → kirim → tandai selesai."""
    jid = int(job["id"])
    uid = int(job["telegram_id"])
    f = catalog.get(job["feature"])
    work = Path(settings.work_dir) / f"job_{jid}"
    work.mkdir(parents=True, exist_ok=True)
    out = work / "hasil.mp4"
    t0 = time.time()
    try:
        while True:
            if time.time() - t0 > settings.job_timeout:
                raise TimeoutError("melebihi batas waktu render (resume)")
            st: GenStatus = await backend.poll(str(job["task_id"]))
            if st.state == "failed":
                raise RuntimeError(st.error or "backend gagal")
            if st.state == "done":
                rp = str(st.result_path or "")
                if rp.startswith("http"):
                    result = await fetch_url(rp, out)
                elif rp and Path(rp).exists():
                    result = Path(rp)
                else:
                    result = out
                break
            await asyncio.sleep(settings.poll_interval)
        result = await asyncio.to_thread(unwrap_media, result)  # kalau ZIP, ambil media
        result = await asyncio.to_thread(smooth_fps, result)   # 16fps → 30fps halus
        db.set_job(jid, status="done", result_path=str(result))
        await send_result(bot, uid, result,
                          f"✨ <b>{f.label if f else job['feature']}</b> selesai tanpa watermark!\n"
                          f"🆔 Job <code>{jid}</code> · {saldo_txt(uid)}")
        log.info("resume: job %s terkirim ke %s", jid, uid)
    except Exception as e:                      # noqa: BLE001
        log.exception("resume: job %s gagal", jid)
        db.set_job(jid, status="failed", error=str(e)[:400])
        if f:
            db.ledger_add(uid, f.cost, "refund", ref=str(jid))
        try:
            await bot.send_message(uid,
                f"❌ <b>Render gagal</b> (job <code>{jid}</code>) & Token dikembalikan.\n"
                f"Alasan: <code>{str(e)[:200]}</code>", parse_mode=ParseMode.HTML)
        except Exception:
            pass


async def _resume_jobs(bot: Bot) -> None:
    """Sambung job 'running' yang terputus saat service direstart.

    Tanpa ini, render yang sudah jalan di cloud (dan sudah dibayar user) tidak pernah
    terkirim — persis kasus job 5 (9 Okt).
    """
    try:
        rows = db.running_jobs()
    except Exception as e:                      # noqa: BLE001
        log.warning("resume: gagal baca job running: %s", e)
        return
    rows = [r for r in rows if not str(r["task_id"]).startswith("mock")]
    if not rows:
        return
    log.info("resume: %d job berjalan ditemukan → disambung", len(rows))
    for r in rows:
        asyncio.create_task(_resume_one(bot, dict(r)))


async def main() -> None:
    global bot
    if not settings.bot_token:
        print("❌ KREAIBOT_TOKEN kosong. Isi di .env dulu (dari @BotFather).")
        sys.exit(1)
    settings.ensure_dirs()
    bot = Bot(settings.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(router)
    me = await bot.get_me()
    log.info("KREE.AI jalan sebagai @%s (backend=%s, promptsmith=%s, bayar=%s)",
             me.username, settings.backend, "llm" if settings.promptsmith_key else "template",
             "aulaa-qris" if pay_gw else "manual")
    # Daftar perintah → Telegram menampilkan tombol "Menu" di kiri kolom ketik,
    # jadi user tidak perlu hafal/ketik /start manual.
    try:
        await bot.set_my_commands([
            BotCommand(command="start", description="🎬 Menu & bikin video"),
            BotCommand(command="saldo", description="💰 Cek saldo Token"),
            BotCommand(command="topup", description="⚡ Beli Token (QRIS)"),
            BotCommand(command="help", description="📖 Bantuan & cara pakai"),
            BotCommand(command="cancel", description="❌ Batalkan sesi"),
        ])
        log.info("perintah bot di-set → tombol Menu Telegram aktif")
    except Exception as e:                      # noqa: BLE001
        log.warning("gagal set perintah bot: %s", e)
    asyncio.create_task(poller_payments())      # cek QRIS pending tanpa perlu webhook publik
    asyncio.create_task(_resume_jobs(bot))      # sambung job yang terputus karena restart
    await dp.start_polling(bot)


if __name__ == "__main__":
    if "--check" in sys.argv:
        sys.exit(check())
    asyncio.run(main())