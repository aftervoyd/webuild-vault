---
project: KREE.AI (kode: Kreaibot)
status: 🟢 BOT LIVE di VPS — @kreeaibot, tinggal kredensial backend render
tanggal: 2026-10-08
---

# 🚀 KREE.AI — Rencana Build sampai BISA JUALAN

## 🟢 STATUS LIVE (8 Okt 2026)
- **Bot:** `@kreeaibot` · nama **KREE.AI** · token di `/root/projects/kreaibot/.env` (chmod 600)
- **Service:** `systemd kreaibot` (enabled + auto-restart) · log `/var/log/kreaibot.log`
- **Terbukti jalan:** `/start` → user terdaftar otomatis + **bonus 1 token** (cek DB: `users`), menu 6 fitur + Top Up/Saldo/Panduan/Referral tampil
- **Backend:** `mock` (render video uji via ffmpeg) — belum nyala biaya API
- **Auto-download Telegram Desktop dimatikan** (folder `/root/Downloads/Telegram Desktop` dikunci `chattr +i`)

## ✅ Yang SUDAH jadi (8 Okt 2026)
Fondasi produksi **jalan & teruji** di VPS → `/root/projects/kreaibot` (copy di folder ini):

- `bot.py` — menu + alur 3 langkah (foto → prompt → rasio) + worker render + admin + refund otomatis
- `catalog.py` — 6 fitur + harga token (acuan hasil teardown kompetitor)
- `db.py` — SQLite: user, ledger token, job, voucher (audit trail lengkap)
- `backends/` — kontrak pluggable: `mock` (render uji ffmpeg) · `runninghub` (ComfyUI cloud) · `fal`
- `selftest.py` — **11/11 lulus**, termasuk render video h264 720×1280 nyata
- `kreaibot.service` — unit systemd (auto-restart)

Tes yang lulus: katalog · konversi Rp · bonus daftar · top-up · potong biaya · refund · job · render video valid.

## 🔑 YANG GUE BUTUH DARI LO (checklist)
| # | Yang dikirim | Dari mana | Buat apa |
|---|---|---|---|
| 1 | ~~**Token bot**~~ ✅ **SUDAH** | @BotFather | `@kreeaibot` hidup & teruji |
| 2 | **Akun + API key RunningHub** | runninghub.ai (isi saldo) | mesin render (ComfyUI cloud) |
| 3 | **Workflow ComfyUI** (All-in-One dkk) | dibuat di RunningHub (gue bisa bantu susun) | pipeline model |
| 4 | *(opsional, sebagai cadangan)* **fal.ai key** | fal.ai | model MiniMax Hailuo 3 / LTX |
| 5 | **Akun Midtrans/Xendit** *(nanti, buat QRIS otomatis)* | daftar merchant | top-up otomatis |
| 6 | Domain/subdomain (opsional) | pamekaran.com | landing + webhook pembayaran |

**Cara kirim yang AMAN:** kirim token **sekali** di chat → gue langsung simpan ke `.env` (chmod 600) → **hapus pesan lo** dari chat. Jangan pernah kirim di grup.

## 🗺️ Roadmap
**Fase 1 — Bot hidup (setelah token #1).** Colok token → `/start` jalan → tes alur pakai backend `mock` (gratis) → naikkan ke `runninghub`.
**Fase 2 — Mesin render asli (#2, #3).** Upload workflow → binding node di `.env` → tes 1 render nyata per fitur → kalibrasi harga.
**Fase 3 — Monetisasi (#5).** QRIS otomatis (webhook), paket token, voucher, referral berbayar.
**Fase 4 — Jualan.** Landing page, 10 pilot user gratis (cari feedback + konten testimoni), lalu buka umum. Target: harga setara/lebih murah dari kompetitor dengan kualitas setara.

## 🛡️ Soal "cara yang aman" — rekomendasi gue
1. **Bot terpisah, bukan akun pribadi.** Bot Telegram = identitas sendiri; akun pribadi lo jangan dipakai buat bot produksi.
2. **Sesi Telegram Desktop di VPS = titik risiko.** Setelah probe selesai, sebaiknya **logout / hapus `tdata`** (login ulang kapan saja). Sekarang masih nyala sesuai permintaan lo.
3. **Kredensial → `.env` chmod 600**, tidak di kode, tidak di chat, tidak di git.
4. **Probe sisa (file mentah / C2PA):** cukup pakai **rekam layar lokal** (ffmpeg x11grab) — tidak perlu dekripsi cache `tdata` (ribet & nggak aman). Nilainya kecil; intel sudah 95% lengkap.
5. **Pembayaran pakai gateway resmi** (Midtrans/Xendit) → otomatis, tanpa nyimpen data kartu, aman dari chargeback.
6. **Data user minimal** (UU PDP): simpan ID Telegram + saldo + riwayat job saja. Jangan simpan foto user lebih lama dari perlu.

## 💰 Acuan harga (dari teardown @KuzushiGenBot)
- Kompetitor: **Rp10.000 = 10 Token**, video All-in-One 30 dtk = 1 Token (Rp1.000)
- Biaya modal kita: ~Rp1.000–2.000 per render (tergantung harga RunningHub per detik GPU)
- Strategi: harga setara, kualitas & UX lebih baik; margin dari paket besar + referral

## ⚙️ Tech stack
Telegram (aiogram 3) · Python 3.14 · SQLite (bisa naik ke Postgres) · ComfyUI cloud (RunningHub) · ffmpeg · systemd

## 📌 Catatan operasional
- Runtime: `/root/projects/kreaibot` · DB: `kreaibot.sqlite3` · hasil: `work/job_<id>/`
- Ganti model/backend = **tanpa ubah kode** (cukup `.env`)
- Semua job punya audit trail + refund otomatis kalau gagal