---
project: KREE.AI (Kreaibot)
status: referensi teknis — nama field node API RunningHub
tanggal: 2026-10-08
---

# 🔧 REFERENSI NAMA FIELD NODE (RunningHub Workflow API)

## Cara mendapatkan nama field (GRATIS, tanpa tes koin)
1. Buka halaman post workflow di RunningHub (mis. `runninghub.ai/post/<ID>/aiDetail`).
2. Klik tombol **Download** → simpan JSON workflow (tidak butuh login!).
3. Di JSON, setiap node punya array `inputs`. Widget-nya tertulis sebagai:
   ```json
   {"widget": {"name": "nama_field"}, "name": "nama_field", "type": "COMBO|STRING|INT|FLOAT"}
   ```
   → **`widget.name` = `fieldName`** yang valid untuk `nodeInfoList`.
4. ⛔ Jangan buang koin buat nebak: task dengan fieldName salah gagal di validasi
   (`803 NODE_INFO_MISMATCH … field_not_found_in_node_inputs`) **tanpa** memakan koin,
   tapi kalau tebakan benar task **langsung jalan dan menagih koin**.

## Workflow MiniMax H3 FL2VA — `2084116925483151361`
| Node | Class | fieldName valid | Catatan |
|---|---|---|---|
| 4 | `LoadImage` | `image` | **frame awal** (nilai = nama file hasil upload, mis. `api/<hash>.png`) |
| 6 | `LoadImage` | `image` | **frame akhir** |
| 5 | `RHMiniMaxH3FL2VAFirstFrameCondition` | – | First vs First+Last |
| **7** | `RHMiniMaxH3FL2VATarget` | **`aspect_ratio`**, **`duration_seconds`**, **`width`**, **`height`** | default `["4:3", 5, 832, 480]` |
| **8** | `RHMiniMaxH3FL2VAEncode` | **`prompt`** ⚠️ | BUKAN `text`; prompt format per-segmen waktu |
| 10 | `RHMiniMaxH3DualSigmaSampler` | `seed`, `sigma_points`, `video_shift`, `audio_shift` | default `[42,"fixed",50,12,3,"off",true,0.12,2,4,4]` |
| 12 | `CreateVideo` | `fps`, `bit_depth` | default 24 fps |
| 13 | `SaveVideo` | `filename_prefix`, `format`, `codec` | output mp4 h264 |
| 9/11 | `RHMiniMaxH3EmptyAVLatent` + `DecodeAV` | – | **sumber audio** (output punya audio aac) |

## Binding di `.env` (sudah aktif)
```env
RUNNINGHUB_WF_ALLINONE=2084116925483151361
RUNNINGHUB_NODES_ALLINONE=[{"nodeId":"4","fieldName":"image","value":"@photo1"},
 {"nodeId":"6","fieldName":"image","value":"@photo2"},
 {"nodeId":"8","fieldName":"prompt","value":"@prompt"},
 {"nodeId":"7","fieldName":"aspect_ratio","value":"@ratio"},
 {"nodeId":"7","fieldName":"duration_seconds","value":"@duration"},
 {"nodeId":"7","fieldName":"width","value":"@width"},
 {"nodeId":"7","fieldName":"height","value":"@height"}]
```

## Placeholder yang didukung kode (`backends/runninghub.py`)
| Placeholder | Sumber |
|---|---|
| `@photo1`..`@photo6` | foto ter-upload berurutan |
| `@prompt` | prompt hasil PromptSmith |
| `@ratio` | rasio pilihan user (`9:16`, `16:9`, `1:1`, …) |
| `@duration` | `req.duration` → env `RUNNINGHUB_DURATION_<FEATURE>` → `RUNNINGHUB_DEFAULT_DURATION` (default 5) |
| `@width` / `@height` | dipetakan dari rasio (`RATIO_SIZES`): 9:16→480×832 · 16:9→832×480 · 1:1→640×640 · 4:3→832×480 |
| `@video` | input video (untuk fitur video-to-video) |

## ⚠️ BATAS NILAI (dari validasi API — gratis, gak makan koin)
Kalau mengirim nilai di luar batas, API balas `code 433 prompt_outputs_failed_validation` **beserta `input_config` lengkap**:
```
node_errors: {"7": {"errors": [{"type": "value_bigger_than_max",
  "message": "Value 30.0 bigger than max of 15.0", "details": "duration_seconds",
  "input_config": ["FLOAT", {"default": 5.0, "min": 4.0, "max": 15.0, "step": 0.1}]}]}}
```
| Field (node 7) | Tipe | default | min | max |
|---|---|---|---|---|
| `duration_seconds` | FLOAT | 5,0 | **4,0** | **15,0** |
| `aspect_ratio` | COMBO | "4:3" | – | (9:16 / 16:9 / 1:1 terverifikasi jalan) |
| `width` / `height` | INT | 832 / 480 | – | – |

⇒ **Workflow FL2VA maksimal 15 detik per render.** Video lebih panjang = **beberapa klip disambung (chaining)**, bukan satu render. Task yang gagal validasi **tidak menagih koin**.

## Verifikasi
- Dry-run (tanpa API/koin) sudah lolos: `9:16 + 15s → aspect_ratio 9:16, duration_seconds 15, width 480, height 832` ✅
- Ukur biaya nyata: `.venv/bin/python tools/rh_measure.py --ratio 9:16 --duration 15 --photo a.png --photo b.png`
  (mencetak `consumeCoins` + estimasi rupiah)