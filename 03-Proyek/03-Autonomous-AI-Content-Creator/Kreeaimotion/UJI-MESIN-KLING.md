# UJI MESIN KLING 3 PRO REPLICA vs POSE TRANSFER — 16 Okt 2026

Uji ini menjawab: **apakah ada mesin RunningHub yang lebih baru/lebih baik** untuk Motion Control,
dan **berapa biaya koinnya yang sebenarnya** (bukan tebakan).

## Cara uji (input PERSIS SAMA)

Inputnya job #54 milik user, tidak diubah sedikit pun:

- Foto: `data/photo_8886993492_1792135981.jpg` (858x1280)
- Video acuan: `data/ref_Bo7E9ZeXimibextidwwXIfr_d2f51035_norm.mp4`
- Mesin uji: **KLING MOTION CONTROL 3 PRO REPLICA** — app `2101901146469191682`
  (node 30 = image, node 33 = video), instance `default`
- Task: `2111033384353435649`
- Skrip: `tools/uji_kling.py` · pembanding wajah: `tools/banding_kling.py`

## Hasil terukur

| | Pose Transfer (mesin sekarang) | Kling 3 Pro Replica (mesin baru) |
|---|---|---|
| Task | `2110997546898853890` (job #54) | `2111033384353435649` |
| Resolusi | **720x1280** | **480x848** |
| Durasi | 9,97 dtk | 9,90 dtk |
| FPS | 30 | 30 |
| Suara | ada (aac) | ada (aac) |
| **Biaya koin** | ≈390 koin (catatan riset 15 Okt: 25,95 koin/dtk) | **86 koin** ← DIUKUR (saldo 12.457 → 12.371) |
| Sukses | 97% | 98% |
| Rata-rata render | ±676 dtk | ±676 dtk |

Harga koin Kling diukur dari **selisih saldo API** sebelum/sesudah (`coins()` di `tools/uji_kling.py`) —
cara paling tepercaya; field `consumeCoins` dari endpoint outputs tidak mengembalikan nilai untuk task ini.

## Fakta visual (dari `BANDING_KLING.jpg`, 3 panel: foto input | mesin lama | mesin baru)

- Kacamata masih ada di KEDUA video ✓ (ini identitas wajah user — tidak boleh hilang)
- Rambut: pirang, panjang, terurai, belahan tengah — sama di keduanya
- Pakaian & latar: sama di keduanya (kardigan hijau, atasan putih, obi ungu, sofa cokelat, lantai kayu)
- Perbedaan: di mesin LAMA rahang tampak lebih menyempit, dagu lebih panjang, hidung lebih mancung;
  di mesin BARU rahang/dagu/hidung lebih mendekati foto input
- Tidak ada wajah hancur / tangan aneh di keduanya

> Penilaian "mana yang lebih realistis/lebih mirip" = HAK USER. Catatan di atas hanya fakta yang
> terlihat di gambar, bukan skor.

## Kesimpulan dagang

- Kling **≈4,5x lebih murah** per render (86 vs ≈390 koin) tetapi **resolusi lebih rendah** (480x848
  vs 720x1280 — 2,3x lebih sedikit piksel).
- Klaim deskripsi app ("Output Full HD **1080p**") **TIDAK terbukti** — keluaran nyata 480x848.
- Kling hanya punya **2 field masukan** (foto + video). Tidak ada setelan resolusi/rasio/mutu →
  resolusinya terkunci di dalam app dan **tidak bisa dinaikkan** dari sisi kita.
- Mesin lama tetap unggul untuk kebutuhan resolusi tinggi (TikTok/Reels); Kling unggul untuk
  render massal/hemat koin.

## Pilihan lain yang sudah dipetakan (belum diuji)

`/api/webapp/list` + `/api/webapp/detail` (param `search`, `sort=publishTime`, `order=desc`) —
alatnya `tools/rh_app_inspect.py`:

- KLING MOTION ULTRA HD 1080 `2101672840901709826` — sukses 90%, 712 dtk (menjanjikan 1080p)
- Minimax-H3 Multi-Image → Video (∞ durasi + auto prompt) `2103012816681041921` — sampai 6 gambar ref
- Hailuo H3 (MiniMax H3) I2V Accelerated `2087081647066263554` — dipakai 8.686x, sukses 100%,
  322 dtk → **dipakai sebagai mesin fitur 🎬 Generate Video**
- MINIMAX H3 Reference Image `2084542123856445441` · LTX2.3 High Character Consistency
  `2076725981717979138` (5 gambar ref + audio) · LTX2.3 Digital Human lip-sync `2031016553440878594`
  (79.021x dipakai — foto + audio → bicara/nyanyi) · Seedance 2.0 `2104435502584987649`

Cara memasang mesin baru di bot: cukup set `MOTIONBOT_<KUNCI>_APP/_WF/_NODES/_SET/_INSTANCE` di `.env`
(jalur video di `bot.py` sudah generik — digerakkan kunci model job, tanpa ubah kode).