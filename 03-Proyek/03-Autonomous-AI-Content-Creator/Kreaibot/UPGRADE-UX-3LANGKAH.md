# KREE.AI — Upgrade UX "3 Langkah" + Parity Fitur @KuzushiGenBot
*Dibuat: 8 Okt 2026 · status: LIVE di bot (@kreeaibot)*

## 1. Kenapa dirombak
Hasil coba user: di @KuzushiGenBot, **setelah kirim foto tidak ada pertanyaan dan tidak perlu klik
"Lanjut"** — bot langsung minta prompt. Alur kita sebelumnya 5 langkah dengan tombol "✅ Lanjut"
berulang. Sekarang: **foto → langsung ketik prompt → layar konfirmasi → Render.**

## 2. Alur baru (tanpa tombol Lanjut)

**Fitur biasa (Image→Video / All-in-One)**
1. Pilih fitur → bot minta foto
2. Kirim foto (bisa beberapa) — bot hitung otomatis
3. **Langsung ketik prompt** (tanpa tombol apa pun) → layar konfirmasi
4. Layar konfirmasi: tombol 🚀 Render + pilih **rasio** + pilih **durasi** + Batal (satu layar)

**UGC Video Iklan**
1. Pilih UGC → kirim **foto karakter**
2. Langsung kirim **foto produk** (1–3)
3. **Langsung ketik brief** → layar konfirmasi
4. Bisa ganti **gaya** (🎨) sebelum render

Kunci teknis: teks yang masuk saat masih di tahap foto = **prompt** (`on_prompt_in_photos`),
saat masih di tahap produk = **brief** (`ugc_brief_text`). Tombol lama (`f:next`,
`u:prod:next`) tetap didukung biar sesi lama tidak rusak.

## 3. Harga bertingkat per durasi (acuan pasar Kuzushi)

| Fitur | Durasi | Token | Rupiah | Biaya koin (ukur) | Margin |
|---|---|---|---|---|---|
| Image→Video | 5 dtk | 0,5 | Rp500 | 66 koin ≈ Rp294 | 41% |
| Image→Video | 10 dtk | 1,5 | Rp1.500 | ~150 koin ≈ Rp669 | 55% |
| Image→Video | 15 dtk | 2,5 | Rp2.500 | 210 koin ≈ Rp937 | 63% |
| All-in-One | 5 dtk | 1,0 | Rp1.000 | 66 koin ≈ Rp294 | 71% |
| All-in-One | 15 dtk | 2,5 | Rp2.500 | 269 koin ≈ Rp1.200 | 52% |
| UGC Iklan | 15 dtk | 2,5 | Rp2.500 | 269 koin ≈ Rp1.200 | 52% |

Harga diatur di **satu tempat**: `catalog.py` → `DURATION_COST` + `cost_for(key, duration)`.
Ubah angka di situ, seluruh bot (menu, tombol, ledger) ikut otomatis.
1 Token = Rp1.000 (`KREAIBOT_TOKENS_PER_10K=10`).

## 4. Fix bug video: frame pertama bocor ke sampel RunningHub

**Gejala:** video i2v diawali adegan lain (orang balon udara) selama ~1–2,5 dtk, baru hard-cut ke foto user.

**Akar masalah:** workflow-nya **FL2VA** (First + Last frame) — node **6 = frame PERTAMA**
(link 17), node **4 = frame TERAKHIR** (link 18). Binding bot cuma mengisi **node 4**, jadi
frame pertama tetap memakai sampel default workflow.

**Bukti dari 3 render nyata (masing-masing ~300 dtk, 55–66 koin):**
- `bug_none` (hanya node 6 diisi) → video **diakhiri** adegan balon → membuktikan node 4 = frame terakhir.
- `fix_dup` (node 6 + node 4 = foto identik) → bersih, tapi gerakannya cuma morph ekspresi (nyaris statis).
- `fix_zoom` (node 6 = foto asli, node 4 = foto di-zoom 1,12x) → **paling bagus**: push-in kamera natural.

**Perbaikan final (dipakai produksi):**
- `RUNNINGHUB_NODES_I2V`: node 6 ← `@photo1`, node 4 ← `@photo1_zoom`
- `RUNNINGHUB_NODES_UGC/ALLINONE`: node 6 ← `@photo1` (**frame awal**), node 4 ← `@photo2` (**frame akhir**)
- Backend (`backends/runninghub.py`) mengenal placeholder baru `@photoN_zoom`: foto ke-N
  di-cover-crop ke rasio output lalu di-zoom 1,12x dari tengah, di-upload otomatis.
- Kalau Pillow tidak ada / upload gagal → otomatis jatuh ke foto asli (tidak mematikan render).

**Uji tanpa bakar koin:** `tools/rh_zoom_test.py` (verifikasi zoom-variant + upload + resolusi
binding) → 4/4 ✅.

## 5. Menu yang dilihat user sekarang
`catalog.SIAP_JUAL = ("ugc", "allinone", "i2v")` — hanya fitur yang tersambung mesin render nyata
yang tampil. `/help` menyebut sisanya sebagai "segera hadir".

## 6. Roadmap fitur Kuzushi yang belum tersambung
Ada di katalog tapi **belum tampil** karena butuh workflow RunningHub sendiri (node map beda):

| Fitur | Kuzushi | Butuh apa |
|---|---|---|
| 🎭 Face Swap & Motion | 2,0 T | workflow faceswap (foto + video gerakan → video) |
| 🕺 Pose Transfer & Style | 0,5 T | workflow pose transfer |
| 🎤 Video Lip Sync | 0,5 T | workflow lip-sync + dukungan input audio |
| 🖌️ AI Image Editor | 0,3 T | workflow image-edit (output gambar, bukan video) |
| 🌌 All-in-One "Star Trail" | 1,0 T | ✅ sudah jalan (H3) |

## 7. Bukti uji
- `selftest.py`: **64/64 lulus** (termasuk 11 tes baru: alur tanpa tombol, harga × durasi, margin sehat)
- `tools/rh_zoom_test.py`: 4/4 ✅ (0 koin)
- Render nyata terakhir: `fix_dup` 276 dtk/55 koin · `bug_none` 332 dtk/66 koin · `fix_zoom` 332 dtk/66 koin