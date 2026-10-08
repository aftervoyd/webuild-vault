---
project: KREE.AI (Kreaibot)
status: analisa biaya & harga jual — data terukur
tanggal: 2026-10-08
---

# 💰 ANALISA BIAYA & HARGA JUAL KREE.AI

## 1. BIAYA TERUKUR (bukan asumsi)
Dari render nyata pertama (taskId `2108059227392602114`, workflow MiniMax H3 FL2VA):

| Item | Nilai |
|---|---|
| Durasi video | 5,167 detik |
| Resolusi | 832×480 (4:3) · 24 fps |
| Audio | aac stereo ✅ |
| **`consumeCoins`** | **70 koin** |
| `taskCostTime` | 348 detik GPU |
| `consumeMoney` | `null` (tidak ditagih uang) |

→ **70 koin = 1 video 5 detik**. Koin gratis 100 → sisa 30 (habis 70).

## 2. HARGA PAKET RunningHub (dari screenshot halaman vip-rights, ⚠️ perlu konfirmasi)
Model paket: tiap paket punya **Plan A** (koin banyak + dompet kecil) dan **Plan B** (koin sedikit + dompet = harga paket).

| Paket | Harga/bln | Plan A | Plan B |
|---|---|---|---|
| Lite Plus | $8,9 | 13.000 RH Coins + $0,9 dompet | 2.000 RH Coins + $8,9 dompet |
| Paket Dasar | $9,9 | 36.000 RH Coins + $1 dompet | 4.000 RH Coins + $9,9 dompet |
| Paket Dasar Plus | $16,9 | 54.000 RH Coins | 8.000 RH Coins |
| Paket Profesional | $14,9 | 54.000 RH Coins | 6.000 RH Coins |
| Paket Profesional Plus | $25,9 | 72.000 RH Coins | 8.000 RH Coins |
| Privilege → Ultra | $104–$270 | +400 s/d +1.000 RH Coins (angka besar, tidak terbaca jelas) | – |

## 3. KONVERSI (kurs ± Rp16.200/USD, pakai Plan A)
| Paket | Rp/koin | 1 video 5 dtk | Estimasi 15 dtk | Estimasi 30 dtk |
|---|---|---|---|---|
| Lite Plus $8,9 / 13.000 | ~Rp11,1 | **~Rp777** | ~Rp2.330 | ~Rp4.660 |
| **Paket Dasar $9,9 / 36.000** | **~Rp4,4** | **~Rp311** | **~Rp933** | **~Rp1.865** |
| Dasar Plus $16,9 / 54.000 | ~Rp5,1 | ~Rp355 | ~Rp1.065 | ~Rp2.130 |
| Profesional Plus $25,9 / 72.000 | ~Rp5,8 | ~Rp408 | ~Rp1.224 | ~Rp2.448 |

⚠️ Angka koin dari OCR screenshot → **wajib dikonfirmasi di UI akun**. Asumsi: biaya koin naik **linear** dengan durasi — belum diuji.

## 4. PERBANDINGAN KOMPETITOR
- @KuzushiGenBot: **Rp10.000 = 10 token → 1 token = Rp1.000**, video All-in-One **30 detik** = 1 token.
- Biaya kita untuk 30 detik ≈ **Rp1.865** (paket termurah-per-koin) → **di ATAS harga jual mereka**.
- ⇒ Kompetitor **tidak mungkin untung** kalau bayar koin normal. Dugaan kuat: mereka memanfaatkan **jam gratis**
  (*"13 Hours Free Daily, 9 AM–10 PM ET"* = **20:00–09:00 WIB**) atau paket kredit khusus/tier murah.
  → **PRIORITAS: cek apakah promo gratis harian itu berlaku untuk workflow ComfyUI open-source (H3)**, bukan cuma model resmi.

## 5. STRATEGI YANG DISARANKAN
1. **Masuk pakai Paket Dasar $9,9 (36.000 koin)** — rasio koin/$ terbaik; setara ~514 video 5 detik.
2. **Fokus jual UGC iklan 10–15 detik**, bukan 30 detik: biaya ~Rp330–930 → jual **Rp1.500–2.000** → margin 40–60%.
3. **Manfaatkan jam gratis 20:00–09:00 WIB** untuk produksi massal (kalau berlaku) → margin naik drastis.
4. Video 30 detik dijual **Rp2.500–3.000** (jangan ikut Rp1.000 mereka dulu) atau dipecah jadi 2 klip.
5. Ukur biaya **9:16** + durasi 15/30 detik secara empiris (2–3 render) sebelum menetapkan harga final.

## 6. YANG MASIH HARUS DIUKUR
- [ ] Biaya koin untuk rasio **9:16** (480×832) vs 4:3.
- [ ] Biaya koin untuk **15 detik** dan **30 detik** (cek linear/tidak).
- [ ] Apakah jam gratis harian berlaku untuk workflow open-source H3.
- [ ] Apakah Plan A (koin) dipakai otomatis atau perlu pemilihan saat langganan.

## 7. CATATAN TEKNIS
- Biaya render bisa dibaca langsung dari API: `POST /task/openapi/outputs` → field **`consumeCoins`** (+ `taskCostTime`).
- **Tidak ada endpoint API untuk cek saldo koin** (4 kandidat diuji → 404). Saldo hanya di UI.
- Waktu render 5 detik ≈ **348 detik** (~6 menit) → kapasitas ± 10 video/jam per slot task.