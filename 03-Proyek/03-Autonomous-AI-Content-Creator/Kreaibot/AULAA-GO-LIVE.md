# Aulaa — GO LIVE (terverifikasi 8 Okt 2026, 20:57 WIB)

## Status: 🟢 LIVE & TERUJI DENGAN UANG NYATA

| Item | Nilai |
|---|---|
| Project ID | `b7a4e839-63c4-488c-a0a0-2b20d9b30f93` |
| Mode | **Live** (switch di dashboard Aulaa — sudah di-flip user) |
| Metode aktif | 14 (QRIS min Rp1.000 · maks Rp10jt) |
| Webhook | **TIDAK dipakai** — bot pakai **polling** `GET /v1/payments/{id}` tiap **6s** |
| Biaya QRIS | 0,9% + Rp500 → dari Rp10.000 netto ≈ **Rp9.410** |
| Settlement | H+1 jam 13:00 ke rekening terdaftar |

## Bukti transaksi LIVE pertama (uang nyata)
- order `LIVE-8886993492-1791464237`, payment_id `f53bbb83-858a-4fca-93a6-b3560550d8d0`
- `is_test=0`, status **paid**, nominal Rp10.000 → **+10 token** (saldo 34,5 → 44,5)
- QRIS asli: `ID.CO.DANAMON.WWW` · merchant **"Aulaa Pay"** · kota KEDIRI
- Auto-kredit **via poller** (tanpa tombol), pesan QR otomatis berubah "✅ LUNAS"
- Log: `topup lunas (via poller): order=LIVE-... token=+10.0`

## Cara tes ulang
```bash
cd /root/projects/kreaibot
.venv/bin/python tools/aulaa_live_test.py 10000   # kirim QR LIVE ke chat owner, pantau auto-kredit
.venv/bin/python tools/aulaa_live_test.py status   # lihat order LIVE terakhir
```

## Pengaman uang nyata (sudah aktif)
- Nominal dari gateway **WAJIB sama** dengan order lokal; kalau beda → token **TIDAK** dikredit + admin dialert.
- Kredit idempoten (ledger dulu, baru tandai paid) → tidak mungkin dobel.
- Fallback manual (info pembayaran + approve admin 1 klik) kalau Aulaa error.
- ⛔ **JANGAN ganti Webhook/Callback URL** di project yang sudah approved → review ulang + Live mati sementara.
