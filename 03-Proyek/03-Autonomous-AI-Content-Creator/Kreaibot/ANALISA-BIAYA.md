---
project: KREE.AI (Kreaibot)
status: analisa biaya & harga jual — data RESMI (dari UI akun)
tanggal: 2026-10-08
---

# 💰 ANALISA BIAYA & HARGA JUAL KREE.AI

## 1. BIAYA TERUKUR (render nyata, taskId `2108059227392602114`)
| Item | Nilai |
|---|---|
| Durasi | 5,167 detik |
| Resolusi | 832×480 · 24 fps |
| Audio | **aac stereo** ✅ |
| **`consumeCoins`** | **70 koin** |
| `taskCostTime` | 348 detik GPU |
| `consumeMoney` | `null` |

→ **70 koin = 1 video 5 detik** (workflow MiniMax H3 FL2VA open-source).

## 2. PILIHAN PAKET — **WAJIB Plan A** ⚠️
- **Plan A** = untuk aplikasi AI, **workflow & model open-source** (Qwen, Wan, LTX) → **INI JALUR KITA** (H3 open-source).
- **Plan B** = untuk Canvas & layanan **closed-source** (NanoBanana, Sora, Kling). Varian Kreator Plan B **"API tidak didukung"**.
- Semua paket berlaku **31 hari**; **sisa koin kedaluwarsa otomatis** → jangan beli paket besar sebelum ada permintaan nyata.

### Harga & koin (RESMI — Plan A, harga promo)
| Paket | Harga/bln (normal) | Koin Plan A | Saldo | **Rp/koin** | Biaya video 5 dtk |
|---|---|---|---|---|---|
| Lite Plus | **$8,9** ($12,9) | 13.000 | +$0,9 | ~Rp11,1 ❌ | Rp777 |
| **Paket Dasar** | **$9,9** ($14,9) | **36.000** | +$1 | **~Rp4,5** ✅ | **Rp312** |
| **Paket Profesional** | $14,9 ($24,9) | 54.000 | +$1,5 | **~Rp4,5** ✅ | Rp312 |
| Paket Dasar Plus | $16,9 ($25,9) | 54.000 | +$1,7 | ~Rp5,1 | Rp355 |
| Paket Profesional Plus | $25,9 ($42,9) | 72.000 | +$2,6 | ~Rp5,8 | Rp408 |
| Privilegio → Ultra | $104+ | (closed-source, Seedance 2.5 $0,215/s) | – | ❌ | – |

**Kesimpulan:** titik masuk terbaik = **Paket Dasar $9,9 (36.000 koin)** — rasio koin/$ sama dengan Profesional tapi modal setengah. **Hindari Lite Plus** (~2,5× lebih mahal per koin).

## 3. ESTIMASI BIAYA PER DURASI (paket Dasar; asumsi biaya koin linear)
| Durasi | Koin | Biaya | Jual disarankan | Margin |
|---|---|---|---|---|
| 5 detik | 70 | Rp312 | Rp1.000 | 69% |
| 10 detik | 140 | Rp624 | Rp1.500 | 58% |
| 15 detik (UGC) | 269 (terukur) | **Rp1.200** | Rp2.500 | 52% |
| 30 detik (**2 klip 15 dtk disambung**) | ~538 | ~Rp2.400 | Rp4.000 | 40% |

**DATA TERUKUR (bukan asumsi):** 5 dtk 4:3 = **70 koin** · 15 dtk 9:16 = **269 koin**. Biaya per detik **naik** (14,0 → 17,9 koin/s) → **tidak linear**. Workflow FL2VA **maksimal 15 detik/render**; video 30 detik = 2 klip disambung.

Kapasitas 36.000 koin → **~514 video 5 dtk** · **~133 video 15 dtk** · **~66 video "30 dtk" (2 klip)** per bulan.

## 4. PERBANDINGAN KOMPETITOR
- @KuzushiGenBot: Rp10.000 = 10 token → **1 token = Rp1.000**; video All-in-One **30 detik** = 1 token.
- Biaya kita 30 detik ≈ **Rp1.872** → **kompetitor jual DI BAWAH biaya koin normal**.
- ⇒ Dugaan kuat: mereka memakai **jam gratis** (*"13 Hours Free Daily, 9 AM–10 PM ET"* = **20:00–09:00 WIB**) atau paket khusus. **PERLU DIKONFIRMASI apakah berlaku untuk workflow open-source H3.**

## 5. STRATEGI REKOMENDASI
1. **Langganan Paket Dasar $9,9 — pilih Plan A** (kalau salah pilih Plan B, koinnya cuma 4.000 → rugi).
2. **Fokus jual UGC 10–15 detik** (Rp1.500–2.000) → margin 53–58%. Jangan ikut perang harga 30 detik Rp1.000 dulu.
3. **Produksi massal di jam 20:00–09:00 WIB** kalau jam gratis berlaku → biaya ≈ Rp0, margin melonjak.
4. Koin **kedaluwarsa 31 hari** → jualan dulu sebelum stok koin numpuk.
5. Kunci harga final **setelah** mengukur biaya 9:16 & durasi 15/30 detik secara empiris.

## 6. YANG MASIH HARUS DIUKUR / DIPASTIKAN
- [ ] Biaya koin **9:16** (480×832) vs 4:3 832×480.
- [ ] Biaya koin **15 detik** & **30 detik** (linear atau tidak).
- [ ] Apakah **jam gratis 20:00–09:00 WIB** berlaku untuk workflow open-source H3.
- [ ] Apakah API menagih **koin** (Plan A) atau saldo dompet saat langganan aktif.

## 7. CATATAN TEKNIS
- Biaya render dibaca dari API: `POST /task/openapi/outputs` → **`consumeCoins`** + `taskCostTime`.
- **Tidak ada endpoint API untuk cek saldo koin** (4 kandidat → 404); saldo hanya di UI.
- Waktu render 5 detik ≈ 348 detik (~6 menit) → ± 10 video/jam per slot.
- Kurs yang dipakai: **Rp16.200/USD**.