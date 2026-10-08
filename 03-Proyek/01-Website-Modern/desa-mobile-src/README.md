# 📱 Desa Digital Pamekaran — sumber aplikasi (mobile + website)

**Status: UI/UX FINAL — dibekukan 8 Okt 2026.** Perubahan berikutnya hanya kalau ada fitur baru.

## Isi
- `app.html` — SATU file berisi seluruh aplikasi (CSS + JS inline): 4 layar (login, dashboard, pasar UMKM, drawer), glassmorphism, nav pil melayang 4 ikon.
- `manifest.webmanifest` + `img/ikon-{64,192,512}.png` — agar bisa di-*install* ke home screen (PWA).
- `img/` — foto produk & berita.
- `susun-*.py` — skrip penyusun papan presentasi (PIL).

## Cara pakai (sudah jalan di VPS)
- Mobile: `http://100.115.213.21:8086/app.html?w=390` (Tailscale-only, service `desa-mobile`)
- Desktop: `.../app.html?web=1` — otomatis juga kalau jendela ≥700px
- **Screenshot: WAJIB pakai `&nofx=1`** (tanpa itu transisi CSS tidak jalan di headless → drawer tampil ~25px saja)
- Parameter lain: `?s=login|dash|pasar`, `&drawer=1`, `?w=390` (bingkai HP), `?web=1&h=…` (lebar paksa)

## Kalau mau jalankan di komputer lain
`app.html` + folder `img/` + `manifest.webmanifest` — taruh di satu folder, buka `app.html`. Tidak butuh build, tidak butuh npm.
