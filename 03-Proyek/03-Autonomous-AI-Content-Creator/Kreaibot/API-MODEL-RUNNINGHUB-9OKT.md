# API MODEL RUNNINGHUB — hasil bongkar 9 Okt 2026 (login pakai kredensial vault)

Sumber: https://www.runninghub.ai/id/call-api dan https://www.runninghub.ai/runninghub-api-doc-en
(browser dalam keadaan login pakai kredensial Hermes Vault — akun `marketing.nimara@gmail.com`).

## 1. Bentuk API (dari dokumentasi resmi)

| Jenis | Pola panggil | Catatan |
|---|---|---|
| **Model API** | submit → `taskId` → poll → hasil | **HANYA untuk Enterprise-Shared API Key** (kita punya) |
| **AI App API** | idem | app kemasan, input ramah |
| **Workflow API** | idem | ComfyUI hosting |
| **LLM API** | langsung / streaming | OpenAI-Anthropic-Gemini compatible |

- Submit Model API: `POST https://www.runninghub.ai/openapi/v2/{endpoint}` header `Authorization: Bearer <key>`
- Run AI App: `POST https://www.runninghub.ai/openapi/v2/run/ai-app/{webappId}`
- Versi `.cn` (dipakai produksi kita sekarang): `/task/openapi/ai-app/run` + `apiKey` → **bayar koin**, bukan dolar.

## 2. Cara membaca katalog internal (trik, tanpa klik-klik)

- Cari model: `POST https://www.runninghub.ai/api/sku/list` body `{"pageNum":1,"pageSize":40,"search":"ltx"}`
- Detail satu model: `POST https://www.runninghub.ai/api/sku/detail?id=<skuId>`
  → mengembalikan **`rhEndpoint`** (nama endpoint asli) + **`inputConfigJson`** (skema parameter + default).
- Ini kuncinya: katalog web menulis `ltx-2.3/image-to-video`, tapi endpoint aslinya
  **`rhart-video/ltx-2.3/image-to-video`** — makanya panggilan kita dulu "invalid".

## 3. Daftar harga yang relevan (per 9 Okt 2026)

| Model | Harga | Keterangan |
|---|---|---|
| **ltx-2.3/image-to-video** | **$0,01/detik** | ada **audio ambient**, native 9:16, 5–20 s, queue 1000 / concurrency 500 |
| ltx-2.3/text-to-video | $0,01/detik | idem |
| seedance-v1.5-pro-image-to-video | $0,01/detik | (versi `-fast` $0,03/s) |
| **wan-2.6-image-to-video-flash** | **$0,02/detik** | 30 fps + audio; lebih murah dari slug `alibaba/...` ($0,04/s) |
| wan-2.6-reference-to-video-flash | $0,02/detik | |
| alibaba/wan-2.6/image-to-video | $0,38/call | |
| kling-v2.5-turbo-std | $0,18/call | |
| kling-v2.5-turbo-pro | $0,30/call | |
| kling-v3.0-pro | $0,114 → $0,10/detik | |

## 4. Spesifikasi LTX-2.3 image-to-video (hasil `/api/sku/detail`)

- `rhEndpoint`: `/rhart-video/ltx-2.3/image-to-video`
- skuId: `2034461796984971265` · instanceType: `plus`
- Parameter: `imageUrl` (IMAGE, wajib) · `prompt` (STRING, wajib) ·
  `resolution` (480p/720p/1080p, default 480p) · `aspectRatio` (9:16/16:9, default 16:9) ·
  `duration` (INT, default 5, hingga 20)
- Deskripsi resmi: "…**generates matching ambient sound effects** and visual motion in a single pass,
  achieving perfect audio-visual alignment within 5-20 second durations."

## 5. Hasil uji langsung (bukan teori)

| Uji | Hasil |
|---|---|
| `alibaba/wan-2.6/image-to-video-flash` 5 s 720p + `enableAudio` | **BERHASIL** — 42 detik, $0,20, hasil **30 fps + audio AAC stereo 44,1 kHz** |
| `rhart-video/ltx-2.3/image-to-video` 5 s | **DIBLOKIR** `errorCode 605 — Your balance is insufficient` |
| `rhart-video/ltx-2.3/text-to-video` 5 s | sama, 605 |

Saldo akun saat uji: **$0,28** (setelah uji Wan 2.6 Flash dari $0,48). Biaya LTX 5 s cuma $0,05 —
jadi blokir 605 **bukan** soal 5 detik itu, tapi ambang saldo minimum per model (instanceType `plus`).
→ **Perlu top up dulu** (saran minimal $5–10) sebelum LTX bisa diuji nyata.

## 6. Hitungan biaya LTX vs harga jual kita

$0,01/detik ≈ Rp162/detik (kurs ±16.200).

| Durasi | Biaya LTX | Harga jual kita sekarang | Putus? |
|---|---|---|---|
| 5 s | ±Rp810 | Rp500 (0,5 Token) | ❌ rugi |
| 10 s | ±Rp1.620 | Rp1.000 (1 Token) | ❌ rugi |
| 15 s | ±Rp2.430 | belum dijual | — |

Kesimpulan: jalur API (dolar) memberi **suara + 30 fps + jauh lebih cepat**, tapi **wajib naikkan harga**
(atau dijual sebagai tier "HD Bersuara") kalau mau untung.

## 7. Jalur koin (lebih murah) — petunjuk

- AI App ber-basis LTX 2.3 sudah ada di katalog app: **`2031016553440878594`**
  ("LTX2.3 数字人说话唱歌对口型" = talking-head / lip-sync LTX 2.3) → ini kandidat **Lip Sync** jalur koin.
- Kandidat app lain yang sudah tercatat: face swap `1889155568379092993`, animate/pose `1975951975441412098`.
- Cara menyisir katalog app: `POST https://www.runninghub.cn/openapi/v2/aiapp/list` body
  `{"current":1,"size":50,"sort":"HOTTEST","days":30,"keyword":"..."}` (field record: `title`, `description`,
  `cover`, `invokeExample` — `invokeExample` sudah memuat contoh curl lengkap beserta id app).