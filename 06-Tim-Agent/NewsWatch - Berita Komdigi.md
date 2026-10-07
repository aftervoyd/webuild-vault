# 📡 NewsWatch — Berita & Regulasi Komdigi

> Dipantau **NewsWatch** (divisi **Riset**). Fokus: **apa yang berubah** + **dampaknya ke Webuild**.
> Sumber utama: `komdigi.go.id`, `domain.go.id`, `portal.komdigi.go.id`, `jdih.komdigi.go.id` + berita pendukung.
> Format entri: **tanggal** → **apa yang berubah** → **dampak ke Webuild** → **status verifikasi**.

**Update terakhir: 2026-10-08** (run pertama NewsWatch)

---

## 🔴 PRIORITAS — berdampak langsung ke Webuild

### 1. 🏛️ UU Satu Data Indonesia (SDI) **RESMI DISAHKAN** — 6 Okt 2026
- **Apa yang berubah:** DPR + Pemerintah mengesahkan RUU Satu Data Indonesia jadi **UU** di Rapat Paripurna ke-9 (Selasa, 6 Okt 2026). **20 bab, 141 pasal**. Sebelumnya SDI hanya berbasis **Perpres 39/2019** → sekarang **kerangka hukum setara UU**.
- Isi kunci: **Data Dasar Nasional (DDN)** jadi rujukan perencanaan pembangunan, fiskal/APBN, **distribusi bansos**; **standar data, metadata, kode referensi/data induk, katalog data nasional, interoperabilitas**; **keamanan & pelindungan data pribadi**; pemanfaatan **AI**; transfer data (termasuk data tertutup) ke luar negeri; data dibagi **terbuka / terbatas / tertutup**.
- Orkestrasi SDI dipimpin **Bappenas**; **Kemkomdigi** ambil peran di **interoperabilitas + dukungan infrastruktur digital**.
- Konteks penting (siaran pers Komdigi Juli 2026): **data desa/kelurahan = titik awal data masyarakat / sumber data primer nasional**; integrasi teknis platform digital desa dengan wali data **"tidak dibebankan kepada pemerintah desa"**.
- Sumber: Siaran Pers Komdigi No. **200/HM-KKD/10/2026** (komdigi.go.id, 6 Okt 2026) + Kompas/Katadata/MetroTV/Periskop (7 Okt 2026). ✅ terverifikasi (sumber resmi + 4 media).
- **➡️ Dampak ke Webuild:**
  - Website/SID desa **wajib "siap SDI"**: data tertata, standar + metadata, dan bisa **terhubung** (interoperabilitas) ke ekosistem data kabupaten/nasional.
  - Ini **peluang jual** yang kuat: posisikan paket desa Webuild sebagai **"website desa yang siap Satu Data"** (struktur data rapi, siap integrasi SID/SIDEKA-NG/Siskeudes) — bukan cuma "situs profil".
  - Bergeser dari "punya website" → **"data desa yang benar & bisa dipakai"** = nilai tawar baru ke calon kades/kabupaten.
  - Pengelolaan data pribadi warga makin diperhatikan UU → website desa butuh praktik PDP dasar (lihat poin 2).
- **Perlu verifikasi:** nomor/tanggal pengundangan UU, PP turunan SDI, dan peran resmi Kemkomdigi vs Bappenas dalam pelaksanaan.

### 2. 🔐 Komdigi investigasi **jual-beli data pribadi ilegal** — 2 Okt 2026
- **Apa yang berubah:** Komdigi (Ditjen Pengawasan Ruang Digital) **berkoordinasi dengan Polri + BSSN** mengusut kebocoran data yang ramai beredar. Menurut BSSN, yang beredar adalah **data lama** yang "diramaikan kembali" — tetap ditindaklanjuti & **blokir situs** penjual data. Dasar hukum yang ditegaskan: **UU 27/2022 (PDP)** — menyebarkan data pribadi orang lain bisa berkonsekuensi pidana.
- Sumber: Siaran Pers Komdigi, 2 Okt 2026 (komdigi.go.id). ✅ terverifikasi.
- **➡️ Dampak ke Webuild:**
  - Desa menyimpan **data warga** (NIK/KK/alamat) → kalau Webuild bikin layanan data warga, **wajib disiplin PDP**: dasar hukum pemrosesan, pembatasan akses, keamanan teknis (HTTPS, minim data, backup).
  - Jadikan ini **poin jualan kepercayaan**: "website desa + tata kelola data pribadi warga sesuai UU PDP".

### 3. 📱 Evaluasi sisa kuota internet (SE 4/2026) — 3 Okt 2026 — *dampak: rendah*
- Komdigi nilai implementasi perlindungan sisa kuota operator **belum optimal** (baru notifikasi, belum rollover substantif). Tak terkait langsung Webuild — catat saja sebagai konteks kebijakan konsumen digital.
- Sumber: Siaran Pers Komdigi, 3 Okt 2026. ✅

---

## 🏛️ Domain & Desa (`domain.go.id`)

- **Update terbaru situs domain.go.id: 3 September 2026** ("Model Terdistribusi Dikaji untuk Pengelolaan DNS Server Pemerintah") → **tidak ada berita domain baru sejak itu** (per 8 Okt 2026).
- Urutan berita terakhir: 3 Sep 2026 (DNS terdistribusi) · 20 Agu 2026 (DNS server pemerintah, keandalan `.go.id`) · 7 Agu 2026 (**Domain.go.id versi 2026 diluncurkan**) · 15 Jul 2026 (desa kelola domain sbg aset digital — **>23 ribu domain `.desa.id`**) · 24 Jun 2026 (Bangka Tengah percepat `.desa.id`) · 25 Mei 2026 · 12 Mei 2026 · 6 Mei 2026 (tata kelola domain kedaluwarsa diperkuat).
- **Aturan yang WAJIB diingat (dari sosialisasi Komdigi, 6 Feb 2026):**
  - Hingga 2025: **22.862 domain `.desa.id` aktif**, **±47% (10.770) kedaluwarsa > 2 tahun** tapi masih aktif teknis.
  - **Mulai 2026 penertiban diperketat** (Komdigi + PANDI): domain **>35 hari tanpa pembayaran → diarahkan ke landing page**; **>1 tahun → direkomendasikan dihapus** dari registri.
  - Pengelolaan **kolektif via Dinas Kominfo kabupaten/kota** didorong; **aplikasi registrar Domain.go.id versi beta** untuk kelola & bayar domain massal.
  - Dasar: **Permen Komdigi No. 5/2025** (PSE Lingkup Publik), Pasal 38 ayat (3).
  - **SIDEKA-NG** (Sistem Informasi Desa & Kawasan NG) jalan **di PDN**, sudah terhubung **Siskeudes, Prodeskel, dan SID**.
  - Dana desa boleh untuk infrastruktur digital **maks 3%** (Permendesa 16/2025).
- **➡️ Dampak ke Webuild:**
  - Klien desa harus **punya `.desa.id` legal & terbayar** sebelum pasang website → Webuild bisa bantu proses/migrasi (nilai tambah jasa).
  - Domain kedaluwarsa = **pintu masuk**: banyak desa punya domain `.desa.id` "hidup tapi nunggak" → tawarkan **paket penertiban + website**.
  - Karena SIDEKA-NG/SID/Siskeudes jalan di PDN & soal interoperabilitas, posisikan website desa Webuild **kompatibel**, bukan sistem terpisah.

---

## 📜 Regulasi relevan (latar — bukan baru, tapi belum tercatat)

- **PP 33/2026** — Peraturan Pelaksanaan **UU 27/2022 (PDP)**, ditetapkan/diundangkan **16 Juli 2026**, **225 pasal**: memperjelas kewajiban **pengendali & prosesor data**, keamanan data, transfer lintas negara, sanksi administratif. Sumber hukumonline menyebut **berlaku mulai 16 Januari 2027**. ⚠️ *perlu verifikasi tanggal berlaku pasti*.
- **Permen Komdigi No. 9/2026** (6 Mar 2026) — pelaksanaan **PP 17/2025 (PP TUNAS)**: perlindungan anak di **platform digital**; **menunda akses akun anak <16 tahun** pada platform berisiko tinggi (medsos/jejaring); tahap awal mulai **28 Mar 2026**. → *Dampak Webuild:* kalau website desa/klien punya **akun pengguna/komentar/forum**, perlu ditinjau kewajiban perlindungan anak. Situs profil desa biasa umumnya bukan "platform berisiko tinggi".
- **Permen Komdigi No. 5/2025** — PSE Lingkup Publik (dasar pendaftaran domain instansi & `.desa.id`).
- Konteks non-Komdigi: **Permen PU 5/2026** soal SPBE (tata kelola/audit TIK) — indikasi tren penguatan SPBE & moratorium aplikasi sektoral + pemusatan ke **PDN**.

---

## 🔧 Catatan teknis pemantauan (buat run berikutnya)

- `www.komdigi.go.id` & `djkpm.komdigi.go.id` **balas HTTP 403** ke `curl` (WAF). **Solusi yang berhasil:** buka pakai **browser** (`browser_exec`) → halaman render normal. `domain.go.id` OK pakai curl biasa.
- Halaman detail berita Komdigi = **Next.js (client-side render)** → teks artikel baru muncul setelah **navigasi + wait_for_load**; kalau kosong, **reload** sekali lagi.
- `web_extract` di profil ini backend-nya **search-only** (DuckDuckGo) → **tidak bisa** ambil isi URL. Pakai browser.
- Portal berita resmi alternatif: `portal.komdigi.go.id/kanal-publik/berita-kini` (mirror siaran pers, ada tanggal).

---

## 🗒️ Ringkasan 1 baris buat Orchestrator
> **UU Satu Data Indonesia sah (6 Okt 2026, 141 pasal)** → data desa jadi fondasi; **website/SID desa "siap SDI"** = peluang jualan baru Webuild. Plus **Komdigi gencar tindak data pribadi ilegal** → PDP jadi nilai jual kepercayaan.

#newswatch #komdigi #regulasi #pdp #satu-data #desa-id