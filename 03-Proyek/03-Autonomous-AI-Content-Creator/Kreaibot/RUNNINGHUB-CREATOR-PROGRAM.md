# RUNNINGHUB — CREATOR INCENTIVE PROGRAM: jalur publish workflow
> 10 Okt 2026. Semua langkah di bawah **sudah terbukti jalan** (workflow `qwen-consistency-edit`
> sudah ter-import, tersimpan, dan **sukses dijalankan** via API). Rahasia tidak ditulis di sini.

---

## 0. STATUS
| Item | Nilai |
|---|---|
| Workflow | **`qwen-consistency-edit`** (11 node, orisinal) |
| workflowId di RH | **2108638842228461570** |
| Struktur | valid — validasi server: `node_errors: {}` |
| Sudah di-**Save** | ✅ (editor → tombol Save → "Workflow has been saved.") |
| Sudah di-**jalankan** | ✅ task `2108639276355883009` selesai **73,7 dtk**, output PNG 848×1280 |
| Publikasi | ⬜ **belum** — tersisa aksi UI 1-klik (lihat §5) |
| Penghasilan | `runninghub.ai/my-income` masih $0,00 |

## 1. APA ITU PROGRAM INI (aturan resmi)
- Bayaran dari: **① jumlah run** (termasuk panggilan API) · **② favorit** · **③ orisinalitas**.
- **Semua karya lewat review MANUAL**; karya non-orisinal **tidak dibayar**; pelanggaran → turun/ban.
- Konten bermutu rendah → visibilitas dibatasi. → **Kualitas > kuantitas.**
- Settlement mingguan; pencairan bulanan. Cara cair: `POST /api/cash/apply` + bind PayPal/bank
  (`/api/cash/paypal/bind`, `/api/bank/bind`).

## 2. RESEP MEMBUAT WORKFLOW (yang sudah terbukti)
1. **Ambil contoh workflow publik** (format ComfyUI UI) — endpoint ini **tanpa login**:
   ```
   curl -s -X POST https://www.runninghub.ai/api/workflow/export \
     -H 'Content-Type: application/json' -H 'client: web' \
     -d '{"workflowId":"<id workflow publik>"}'
   ```
2. **Rakit JSON baru** (jangan copy — wajib orisinal). Skema node harus ikut yang terbukti jalan.
   Builder: `work/rh_workflows/build_qwen_wf.py` (referensi node diambil dari workflow publik .ai).
3. **Import ke RH** — buka `/workspace` → klik `Import` → set `<input type=file accept=application/JSON>`
   via CDP `DOM.setFileInputFiles` (file dibaca dari disk server) → muncul "Upload Workflow Success".
4. **Save** — buka `/workflow/<id>?source=workspace`, tunggu ±25 dtk (editor berat), klik tombol **Save**
   → *"Workflow has been saved."* **Wajib**, tanpa ini task API ditolak `810 WORKFLOW_NOT_SAVED_OR_NOT_RUNNING`.
5. **Uji jalan** (gratis di free window): `tools/rh_test_mywf.py --photo <img> --wf <id> --node <LoadImage id>`.

### Jebakan yang sudah kena (jangan diulang)
- **`widgets_values` wajib ada di node** — kalau hilang: `required_input_missing: unet_name`.
- **JANGAN tulis `"link": null`** pada input widget — bikin input dianggap kosong. Kalau tidak ada link,
  **hilangkan key `link`** sepenuhnya.
- Setiap link harus tercatat di **kedua sisi** (`outputs[i].links` **dan** `inputs[j].link`).
- `nodeId` di `nodeInfoList` dikirim sebagai **string**.

## 3. ENDPOINT PENTING (web, butuh `Authorization: <Rh-Accesstoken>`)
| Endpoint | Fungsi |
|---|---|
| `POST /api/workflow/export` {workflowId} | ambil JSON workflow (**tanpa auth**) |
| `POST /api/workflow/check` | audit teks sebelum publish (moderasi) |
| `POST /api/workflow/publish` | publikasikan (payload: workflowId, publishType, workflow{...}) |
| `POST /api/workflow/webapp-price-estimate` | estimasi harga AI App |
| `POST /api/cash/apply`, `/api/cash/paypal/bind`, `/api/bank/bind` | pencairan |
| `POST /uc/getUserInfo` | profil + saldo |

Publish form (`publishType:"1"` = workflow, `"2"` = AI app) butuh:
`workflowName`, `description`, `tags[]`, `coverFiles[]` (**butuh gambar cover**),
`englishCoverFiles[]`, `instanceType:"standard"`, `accessType`, `publishScope`.

## 4. FREE WINDOW — ⚠️ TERNYATA SPESIFIK MODEL
Promo "13 jam gratis/hari 21:00–10:00 WIB" berlaku untuk **model tertentu** (mis. MiniMax H3),
**bukan semua**. Bukti: uji-jalan `qwen-consistency-edit` (73,7 dtk) **memakan ±632 koin**
(27.912 → 27.280). → Jangan asumsikan render gratis; **cek delta koin** lewat `tools/rh_coin_check.py`.

## 5. RUNBOOK PUBLISH (tersisa — aksi UI, ~1 menit)
1. Login `runninghub.ai` di browser **normal** (sesi web di VPS cepat expired).
2. Buka **Workspace → `qwen-consistency-edit`** → editor terbuka.
3. Cari tombol **Publish** di editor (kemungkinan: header kanan editor, atau menu pada judul workflow).
4. Isi form: **nama** (mis. *Qwen Consistency Edit*), **deskripsi**, **tag** (qwen, image-edit,
   consistency), **cover** (pakai hasil render `work/qwen-consistency-edit.png`), kategori.
5. Submit → tunggu review manual → terbit di `/page-workflow`.

> Catatan teknis: route `/PublishView` **tidak render** kalau diakses langsung (butuh state SPA dari editor),
> jadi publish harus dipicu dari dalam editor, bukan via URL.

## 6. PELUANG LANJUTAN
- Tambah **workflow kedua** yang lebih "viral-friendly" (mis. restyle foto produk e-commerce).
- Sebar hasil render ke sosial (butuh akun user) → menambah run/favorit.
- Publish **AI App** (`publishType:"2"`) dari workflow yang sama untuk pengguna non-ComfyUI.