# Kreaibot

Bot Telegram **studio konten AI** — bikin karakter konsisten dari foto, ganti outfit/scene,
image→video, pose transfer, lip-sync. Backend model pluggable (RunningHub / fal / mock).

## Struktur
```
bot.py               # entrypoint: menu, alur 3 langkah, worker render, admin
config.py            # semua konfigurasi dari .env
catalog.py           # katalog fitur + harga token
db.py                # SQLite: user, ledger token, job, voucher
backends/
  __init__.py        # kontrak Backend + factory
  mock.py            # render video uji lokal (ffmpeg) — buat dev tanpa biaya
  runninghub.py      # adapter ComfyUI-cloud (sama pola dengan kompetitor)
  fal.py             # adapter fal.ai (opsional)
selftest.py          # tes: katalog, ledger, backend (11 tes)
kreaibot.service     # unit systemd
.env.example         # template konfigurasi
```

## Jalankan
```bash
pip3 install -r requirements.txt
cp .env.example .env && nano .env      # isi KREAIBOT_TOKEN dari @BotFather
python3 bot.py --check                 # validasi konfigurasi
python3 selftest.py                    # tes lokal (tanpa Telegram)
python3 bot.py                         # jalankan bot
```

Produksi (VPS):
```bash
cp kreaibot.service /etc/systemd/system/
systemctl daemon-reload && systemctl enable --now kreaibot
journalctl -u kreaibot -f
```

## Alur fitur (3 langkah)
`pilih fitur → kirim 1–6 foto referensi → prompt → rasio → render → hasil dikirim (tanpa watermark)`

## Fitur & harga (token)
| Fitur | Token | Foto |
|---|---|---|
| 🌌 Video All-in-One (30s) | 1.0 | 1–6 |
| 🎬 Image to Video | 0.5 | 1 |
| 🎭 Face Swap & Motion | 2.0 | 2 |
| 🕺 Pose Transfer & Style | 0.5 | 2 |
| 🎤 Video Lip Sync | 0.5 | 1 |
| 🖌️ AI Image Editor | 0.3 | 1 |

Konversi: `Rp10.000 = 10 Token` (1 Token = Rp1.000) → atur di `.env`.

## Admin
`/admin` statistik · `/give <id> <token>` · `/voucher <KODE> <token> [max]` · `/cek`

## Ganti backend
`.env` → `KREAIBOT_BACKEND=runninghub`, isi `RUNNINGHUB_API_KEY`,
`RUNNINGHUB_WF_<FITUR>` (workflowId), dan `RUNNINGHUB_NODES_<FITUR>` (binding node →
`@photo1..@photo6`, `@prompt`, `@ratio`, `@video`). Tanpa ubah kode.

## Keamanan
- `.env` **jangan** di-commit (`chmod 600`).
- Token bot = kredensial penuh bot → simpan hanya di server.
- Refund otomatis kalau render gagal.