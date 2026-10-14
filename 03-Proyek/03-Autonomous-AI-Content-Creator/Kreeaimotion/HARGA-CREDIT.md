# HARGA CREDIT KREEAMOTION — hitungan berbasis biaya nyata (14 Okt 2026)

> Semua angka di bawah **terukur**, bukan perkiraan. Sumber: `consumeCoins` dari API RunningHub
> (lihat `tools/ukur_biaya.py`) + harga koin dari paket tahunan RunningHub.

## 1. Biaya mesin (yang benar-benar kita bayar)

| Yang diukur | Hasil nyata | Sumber |
|---|---|---|
| Video motion (mesin otz) | **25,95 koin / detik video** | 387 koin ÷ 15,1 dtk (job #42) & 431 ÷ 16,4 (sesi 13 Okt) |
| Ganti Baju — AI App (cadangan) | **41–44 koin / gambar** | job #38 (41) & #39 (44) |
| Ganti Pose — AI App | **47–48 koin / gambar** | job #35 (48) & #36 (47) |
| Ganti Baju — jalur Inferhub | **±Rp 40–90 / gambar (0 koin)** | uji Inferhub |
| Generate Gambar — Inferhub | **±Rp 40–90 / gambar (0 koin)** | uji Inferhub |
| Waktu render | motion ±1,62 dtk/frame (30 fps) → 15 dtk video ≈ 16 menit | job #42: 967 dtk |

## 2. Harga koin RunningHub (kurs Rp 17.926/USD, 14 Okt 2026)

| Paket tahunan | Harga | Koin/bulan | Rp/koin | Biaya video per detik |
|---|---|---|---|---|
| **Personal $89,9** | Rp 1,61 jt/thn | 36.000 | **Rp 3,73** | Rp 96,8 |
| Pro $139 | Rp 2,49 jt/thn | 54.000 | Rp 3,85 | Rp 99,8 |
| Pro Plus $236,9 | Rp 4,25 jt/thn | 72.000 | Rp 4,92 | Rp 127,6 |
| Lite Plus $71,9 | Rp 1,29 jt/thn | 13.000 | Rp 8,26 | Rp 214,4 |

👉 **Beli paket Personal** (Rp 3,73/koin) — termurah per koin. Hindari Lite Plus untuk produksi
(margin turun ~15 poin).

## 3. ⚠️ Harga yang dipasang SEKARANG = RUGI

| Fitur | Jual sekarang | Dapat (Rp) | Biaya nyata | Hasil |
|---|---|---|---|---|
| Motion 10 dtk | 1 credit | Rp 455–833 | **Rp 968** | ❌ RUGI |
| Motion 15 dtk | 1,5 credit | Rp 682–1.250 | **Rp 1.452** | ❌ RUGI |
| Motion 20 dtk | 2 credit | Rp 909–1.667 | **Rp 1.936** | ❌ RUGI |
| Motion 60 dtk | 4 credit | Rp 1.818–3.333 | **Rp 5.809** | ❌ RUGI |

Paket lama: 6 cr/Rp 5.000 (Rp 833/cr) · 16/Rp 10.000 (Rp 625) · 50/Rp 25.000 (Rp 500) ·
110/Rp 50.000 (Rp 455).

## 4. ✅ USULAN HARGA (1 credit = Rp 1.000)

### Paket top up
| Paket | Credit | Harga | Rp/credit | Bonus |
|---|---|---|---|---|
| Coba | 5 | Rp 5.000 | Rp 1.000 | — |
| Kreator | 11 | Rp 10.000 | Rp 909 | 9% |
| Pro | 28 | Rp 25.000 | Rp 893 | 11% |
| Studio | 57 | Rp 50.000 | Rp 877 | 12% |

### Harga per fitur (yang dipotong dari saldo user)
| Fitur | Credit | Harga (Rp) | Biaya nyata | Margin |
|---|---|---|---|---|
| Motion 10 detik | 3 | 3.000 | Rp 1.276 | **52–57%** |
| Motion 15 detik | 5 | 5.000 | Rp 1.914 | **56–62%** |
| Motion 20 detik | 6 | 6.000 | Rp 2.551 | **52–57%** |
| Motion sesuai video (maks 60 dtk) | 18 | 18.000 | Rp 7.654 | **52–57%** |
| Ganti Baju | 1 | 1.000 | Rp 90–206 | **76–91%** |
| Ganti Pose | 1 | 1.000 | Rp 231 | **74–77%** |
| Generate Gambar | 1 | 1.000 | Rp 90 | **90–91%** |
| Mode realistis | +2 (tambahan) | 2.000 | perlu diukur | — |

Margin dihitung pada paket koin Pro Plus (Rp 4,92/koin) — konservatif. Kalau pakai paket Personal
(Rp 3,73), margin naik ±10–13 poin.

## 5. Yang masih perlu diputuskan user
- Angka final paket & harga per fitur (di atas = usulan).
- Harga langganan **Unlimited** (tombolnya sudah ada di bot, harganya belum ditentukan).
- Bonus referral sekarang 2,5 credit/orang. Dengan harga baru itu = biaya akuisisi ±Rp 2.100 per
  pasangan undangan — masih wajar, tapi turunkan kalau mau lebih hemat.

## 6. Cara menerapkan (tanpa ubah kode)
Isi di `.env` bot kreeaimotion, lalu `systemctl restart kreeaimotion`:
```
MOTIONBOT_COST_10=3
MOTIONBOT_COST_15=5
MOTIONBOT_COST_20=6
MOTIONBOT_COST_FULL=18
MOTIONBOT_IMG_COST=1
MOTIONBOT_GEN_COST=1
MOTIONBOT_PACK_6=5000      # jadi: 5 credit = Rp 5.000
MOTIONBOT_PACK_16=10000    #       11 credit = Rp 10.000
MOTIONBOT_PACK_50=25000    #       28 credit = Rp 25.000
MOTIONBOT_PACK_110=50000   #       57 credit = Rp 50.000
```
(Untuk paket, angka pertama `PACKAGES` di `config.py` juga harus ikut diubah — lihat catatan
implementasi di bawah.)

## 7. Catatan implementasi paket
`config.py` baris `PACKAGES = [(6, pack_6), (16, pack_16), (50, pack_50), (110, pack_110)]` —
angka credit-nya masih ditulis di kode. Kalau mau paket baru (5/11/28/57) tinggal ubah daftar itu.