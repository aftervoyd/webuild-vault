# REALISME GAMBAR + BIAYA NYATA — 16 Okt 2026

Pertanyaan user: *"hasil generate gambarnya udah konsisten tapi kurang realistis"*.
Jawaban terukur: **penyebabnya UKURAN keluaran**, bukan prompt. Sudah diperbaiki.

## 1. Bukti: mesin sama, foto sama, prompt sama — beda ukuran

Kasus nyata = job #56 milik user (foto `imgsrc_8886993492_1792143994.jpg` 717x1276, prompt ganti baju).

| diminta | hasil nyata | berkas | waktu | biaya USD | ≈Rp |
|---|---|---|---|---|---|
| 1024x1536 (**setelan bot sebelum**) | 848x1264 | 1,4 MB | 26 dtk | 0,001955 | 31 |
| 1536x2304 | 1696x2528 | 5,2 MB | 228 dtk | 0,002214 | 35 |
| 2160x3840 (**setelan baru**) | **3072x5504** | 17,7 MB | 58 dtk | 0,003800 | 60 |

Mesin: `gemini-3.0-pro-image`. Baca dari kolom `usage` respons (`output_tokens` 1348 → 2252).

**Fakta visual** (dari `BUKTI-REALISME/BANDING_DETAIL.jpg`, potongan kepala resolusi asli):
panel 4K memperlihatkan tekstur kulit, helai rambut satu-satu, dan pantulan lensa kacamata yang
TIDAK terlihat di panel 1,5 MP; panel 1,5 MP tampak lebih halus/lembut. Orang, kacamata, dan rambut
identik di ketiganya. Penilaian akhir tetap hak user.

**Margin harga:** 4K = Rp 60 vs harga 1 credit = Rp 1.000 → **16,7x**. Cosplay (2 kandidat) = Rp 120
untuk 2 credit. Sehat.

## 2. Setelan bot yang diubah

`MOTIONBOT_IMAGE_SIZE: 1024x1536 → 2160x3840` (commit `ae27773`). Dipilih 2160x3840 karena itu
**ukuran yang sudah terbukti di Ganti Baju** (`MOTIONBOT_OUTFIT_SIZE`) — bukan eksperimen baru.
Mesin tidak diubah (tetap gpt-image-2 utama, gemini cadangan).

Batasan Telegram sudah aman dari awal: `bot.py:2564` — berkas >9 MB dibuatkan pratinjau 1600px untuk
`send_photo`, dan berkas penuh dikirim sebagai dokumen (17,7 MB aman).

## 3. Tiga mode gagal konten (PENTING — jangan salah baca)

Diagnosa 4 sel (`tools/diagnosa_edit.py`, mesin gemini, foto sama):

| sel | prompt | ukuran | hasil |
|---|---|---|---|
| A | netral | 1024x1024 | **200** dalam 24 dtk |
| C | netral | 1536x2304 | **200** dalam 32 dtk |
| B | bikini (milik user) | 1024x1024 | **HANG** 150 dtk |
| D | bikini (milik user) | 1536x2304 | **HANG** 240 dtk |

⇒ Endpoint sehat, ukuran besar sehat, **kontennya yang digantung** — dan mode gagalnya **bukan**
`400` cepat, melainkan menggantung sampai batas waktu. Menaikkan batas waktu tidak akan menolong.

| mode | ciri | arti | tindakan |
|---|---|---|---|
| tolak konten | `400` dalam 1–4 dtk | permanen | ganti mesin |
| **gantung konten** | timeout menit, padahal prompt netral 200 | soft-block | ganti mesin |
| gangguan | `502/503/504/524` setelah menit | upstream padat | ulangi nanti |
| batas model | `429` "Credits exhausted" | sementara per-model | **coba lagi 30 dtk → 200** |

## 4. `429` = transient, dan satu celah yang sudah ditutup

Terukur: `gpt-image-2` balas `429 {"code":14018,"msg":"Credits exhausted"}` — **30 detik kemudian
balas 200 lagi** dengan kunci yang sama. Jadi 429 BUKAN saldo habis.

Celah yang ditemukan: jalur **Cosplay** hanya jatuh ke cadangan pada `(502,503,504,524)` → kena 429
langsung menyerah tanpa mencoba mesin lain. **Diperbaiki** (commit `3b7d791`): `(429,500,502,503,504,524)`.
Jalur Generate Gambar/Ganti Baju sudah aman (loop semua kandidat model × bentuk field).

## 5. Qwen-Edit RunningHub — klaim "4K" PALSU

App `2095689306085285890` ("4K Direct-Output E-Commerce Model Outfit Transfer"). Diuji 2x:

| input | keluaran | koin |
|---|---|---|
| 717x1276 | 760x1352 | 51 |
| **2143x3840** (char sheet besar) | **760x1360** | 55 |

⇒ Resolusinya **terkunci ±1 MP**, tidak ikut ukuran input. Nama appnya menyesatkan.
Yang benar: wajah/kacamata/latar terjaga ✓, baju dari acuan benar-benar terpasang ✓, tanpa sensor,
~51-55 koin/render, 259-290 dtk. Berguna sebagai jalur **tanpa sensor**, bukan sebagai jalur 4K.

## 6. Alat yang ditinggalkan (bisa dipakai lagi)

- `tools/diagnosa_edit.py` — 4 sel pemisah konten vs ukuran vs gangguan (WAJIB dipakai sebelum menyimpulkan)
- `tools/cek_penyedia_gambar.py` — probe prompt netral: penyedia sehat atau tumbang
- `tools/ukur_biaya_gambar.py` — biaya nyata per ukuran dari field `usage`
- `tools/uji_realisme.py` — banding antar mesin/ukuran (cadangan=None supaya hasil asli tiap mesin)
- `tools/banding_detail.py` — potongan resolusi ASLI (kalau diperkecil, bedanya hilang)
- `tools/uji_kling.py` · `tools/banding_kling.py` · `tools/uji_qwen4k.py` (lihat `UJI-MESIN-KLING.md`)

## 7. Yang belum beres

- `gpt-image-2` = **0/3 berhasil** pada uji hari ini (429 2x, 524 1x). Sebagian karena tes berbarengan
  yang menghantam model itu → bukti belum bersih. Mesin ini satu-satunya yang **bisa merender konten
  bikini** (job #56 ✓), sedangkan gemini menggantung untuk konten itu. Jadi urutannya belum dibalik.
- Bila mau jalur 4K untuk konten yang digantung gemini: pilihannya `gpt-image-2` di ukuran besar
  (masih rawan 524) atau mesin tanpa sensor di RunningHub (terkunci ±1 MP). Belum ada yang ideal.