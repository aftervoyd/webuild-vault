# Kreea.ai — Landing Page

Halaman publik (statis) untuk **Kreea.ai**, studio konten AI di Telegram.

- Bot: [@kreeaibot](https://t.me/kreeaibot)
- Fitur: UGC Video Iklan (foto kreator + foto produk), Video All-in-One, Image to Video
- Rasio: 9:16 · 16:9 · 1:1 — durasi hingga 15 detik, dengan audio
- Pembayaran: QRIS (paket token mulai Rp10.000)

## Endpoint webhook

`/webhook.html` — alamat yang didaftarkan sebagai Callback/Webhook URL di payment gateway
(menerima HTTP POST JSON). Verifikasi status pembayaran dilakukan server-side lewat API gateway.

## Struktur

```
index.html    landing page (self-contained, tanpa build step)
webhook.html  halaman endpoint webhook
logo.png      logo resmi (512×512, untuk dashboard & media kit)
```