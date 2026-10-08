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

- `bot.py` — menu + alur umum 3 langkah (foto → prompt → rasio) **+ alur UGC 5 langkah** + worker render + admin + refund otomatis
- `catalog.py` — **7 fitur** + harga token (acuan teardown kompetitor + UGC)
- `promptsmith.py` — **perakit prompt UGC**: 6 gaya (review/unboxing/problem-solution/testimoni/promo/sinematik) → prompt profesional, **plus penghalusan via LLM** (opsional)
- `db.py` — SQLite: user, ledger token, job (+`brief`/`style`), voucher (audit trail lengkap)
- `backends/` — kontrak pluggable: `mock` (render uji ffmpeg) · `runninghub` (ComfyUI cloud) · `fal`
- `selftest.py` — **22/22 lulus** (katalog, PromptSmith, ledger, render video h264 nyata)
- `kreaibot.service` — unit systemd (auto-restart)

## 🛍️ FITUR UGC — ALUR 5 LANGKAH (terbukti e2e 8 Okt 2026)
Alur: **character sheet → foto produk (1–3) → brief bebas → pilih gaya → rasio → render.**

1. **Character sheet** = foto kreator (identitas dijaga konsisten antar frame)
2. **Foto produk** = produk asli ikut masuk video (bentuk/label harus setia)
3. **Brief bebas** (santai, bahasa lo sendiri): nama produk, harga, keunggulan, maunya video seperti apa
4. **Pilih gaya** → PromptSmith rakit prompt profesional (hook → body → CTA + kamera + tone + durasi)
5. **Rasio → Render.**

🔒 **Prompt hasil rakitan TIDAK PERNAH ditampilkan ke user** — user cuma lihat brief & pilihannya. Prompt disimpan di DB untuk audit; admin bisa lihat dengan `/prompt <job_id>`.

**Bukti e2e live (job #2):** `status=done`, `style=promo`, `ratio=9:16`, prompt internal **1450 → 1343 char setelah dihaluskan LLM**, hasil video h264 720×1280 24fps, saldo 6.0 → 4.5 (biaya 1.5 token), ledger konsisten.

**3 bug nyata ketemu dari e2e ini (semua sudah di-fix):**
- Rasio kepotong jadi `9` — `callback_data "f:ratio:9:16"` di-`split(":")[2]`. → pakai `cb.data[len("f:ratio:"):]`
- Mock gagal di systemd: ffmpeg VPS ada di `/root/.hermes/tools/...`, bukan `/usr/bin` (PATH systemd minimal) → symlink `/usr/local/bin/ffmpeg` + resolver `FFMPEG_BIN` di `backends/mock.py`
- UX buntu: kalau saldo kurang, user cuma dapat tombol Top Up tanpa jalan balik → ditambah tombol **"🔁 Sudah Top Up — Lanjut Render"** (`f:recheck`)

Tes yang lulus: katalog · PromptSmith (6 gaya & prompt >500 char) · prompt tak bocor ke ringkasan user · bonus daftar · top-up · potong biaya · refund · job (`brief`/`style` tersimpan) · render video valid.

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
**Fase 1 — Bot hidup (setelah token #1).** ✅ **SELESAI** — token tercolok, `/start` jalan, **alur UGC sudah diuji end-to-end** pakai backend `mock` (gratis). Lanjut: naikkan ke `runninghub`.
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