# Baseline & Compliance: Website Desa

> **Fase 0 — HASIL RISET SELESAI** (7 Okt 2026)
> Sumber: 3 agent riset (domain/hosting, legal/pengadaan, keamanan/pasar).
> Angka bertanda *(est.)* = estimasi pasar, perlu verifikasi saat dipakai.

## 📌 Keputusan Awal
- **Domain demo:** `pamekaran.com` (Hostinger) — untuk demo/portofolio ✅ aman
- **Server:** pakai VPS pribadi yang sudah ada (biaya Rp0)
- **Catatan:** situs desa *resmi* **wajib `.desa.id`** — vendor **tidak bisa** daftar sendiri

---

## ⚡ TL;DR (yang paling penting)

1. **`.desa.id` GRATIS tahun pertama**, perpanjangan **Rp50.000/tahun + PPN 11%**. Tapi **pendaftarnya = Diskominfo kabupaten/kota** (bukan desa/vendor). Desa kasih **surat kuasa**.
2. **Ada CMS GRATIS dari pemerintah** (Komdigi): `website.desa.id` — plus **OpenSID** (open-source). ⚠️ **Ini mengubah model bisnis** — lihat bagian 8.
3. **Situs resmi wajib di server dalam negeri / PDN** (Perpres 95/2018 + Permenkomdigi 5/2025). Demo di VPS lo bebas.
4. **Harga pasar nyata:** Rp2,8–5 juta per desa (dari realisasi APBDes), maintenance **Rp100rb–2jt/bulan**. Rencana Rp3–15jt lo **agak ke atas** — perlu disesuaikan.
5. **Nilai jual kuat:** UU Keterbukaan Informasi Publik **mewajibkan** desa publikasi APBDes → jual fitur **"Transparansi APBDes"**.
6. **Wajib patuh UU PDP** kalau ada data warga (form surat online). Sanksi sampai **2% pendapatan + pidana**.

---

## 1. Domain & Hosting

### Domain `.desa.id`
| Item | Detail |
|---|---|
| Pengelola | **Ditjen Teknologi Pemerintah Digital (Komdigi)** via **domain.go.id**, kerja sama **PANDI** |
| Dasar hukum | **Permen Komdigi No. 5/2025** (Pasal 39) |
| Pendaftar | **Pemkab/Kota (Diskominfo)** atas nama bupati/walikota — **bukan** desa/vendor |
| Syarat | Surat permohonan pemkab + Perda + **surat kuasa kepala desa** + kartu ASN pejabat |
| Biaya | **Tahun-1 GRATIS**; perpanjangan **Rp50.000/thn + PPN 11%** |
| Format | `namadesa.desa.id` atau `namadesa-kabupaten.desa.id` |

### Alternatif domain (untuk demo/vendor)
| Domain | Harga (Hostinger) | Cocok |
|---|---|---|
| `.com` | Rp109.900 thn-1 / Rp209.900 perpanjang | **Demo** ✅ |
| `.my.id` | **Rp16.900** thn-1 | Termurah untuk demo |
| `.web.id` | ~Rp50rb–112rb (gratis dgn hosting) | Demo |
| `.id` | Rp210.900 thn-1 | Demo (kesan lokal) |
| `.go.id` | Rp50.000/thn | ❌ bukan untuk desa |

### Hosting
- **Aturan:** name server & IP **di wilayah hukum NKRI**; instansi wajib **PDN** (Perpres 95/2018 SPBE).
- **Shared vs VPS:** VPS lebih efisien untuk banyak klien (1 server → banyak situs desa, mis. pake CyberPanel).
- **Hostinger VPS (promo 24bln):** KVM 1 **Rp116.900/bln** (1vCPU/4GB) · KVM 2 **Rp155.900/bln** (2vCPU/8GB) · **ada DC Indonesia**.
- **VPS lokal NKRI:** Rumahweb mulai Rp50rb/bln · DomaiNesia mulai Rp43.200/bln.

> **Rekomendasi:** Fase demo → VPS lo sekarang + domain murah. Fase ada klien → arahkan ke `.desa.id` + hosting lokal/DC Indonesia.

---

## 2. Legal & Pengadaan

### Cara desa beli (via APBDes)
Diatur **Perbup/Perwali** masing-masing kabupaten (acuan **Peraturan LKPP 12/2019**). Sejak **Perpres 46/2025**, desa masuk lingkup PBJ (**Pasal 64A–64C: PBJ Desa = Pengadaan Khusus**).

| Metode (level desa) | Nilai |
|---|---|
| Pembelian Langsung | s.d. **Rp10 juta** |
| Permintaan Penawaran | s.d. **Rp200 juta** (min. 2 penawaran) |
| Lelang | **> Rp200 juta** |

> ⚠️ **Langkah pertama praktis: minta salinan Perbup PBJ Desa** kabupaten target (angka bisa beda).

### Syarat jadi vendor
- **Perorangan:** KTP + NPWP (NIK valid) + surat pernyataan + pakta integritas
- **Badan usaha:** **NIB via OSS** + NPWP badan + Akta + **KBLI** jasa TI (62010/62019/63122)
- **Rekomendasi:** minimal **NPWP**; sebaiknya bikin **CV** biar kredibel + bisa terbitkan invoice

### Dokumen & pajak
- Dokumen: KAK, HPS, penawaran, **SPK/kontrak**, kuitansi, invoice, **BAST**
- **PPh 23 jasa = 2%** (4% kalau tanpa NPWP, kecuali NIK valid)
- **PPN efektif 11%** — dipungut **bendahara desa**; ≤Rp2jt tidak dipungut
- Sepakati dulu: harga **net atau gross**

### UU PDP No. 27/2022
- Berlaku penuh **17 Okt 2024**. **Desa = Pengendali Data**, **Vendor = Prosesor Data**.
- Notifikasi kebocoran **≤3x24 jam**. Denda admin **≤2% pendapatan tahunan** + pidana **≤6 thn / Rp6 M**.
- **Risiko vendor:** hosting luar negeri = transfer data lintas negara → butuh **kontrak pemrosesan data (DPA)**.

### Regulasi terkait
- **Permen Komdigi 5/2025** (domain) & **6/2025** (aplikasi SPBE → PDN)
- **Permen Desa PDT 13/2025** (SID / platform **Satu iDesa**, integrasi dgn web desa)
- **UU 14/2008 KIP** → desa wajib publikasi APBDes (**peluang jualan!**)

---

## 3. Keamanan (standar minimum)

Dasar: **Perpres 95/2018 (SPBE)** + **Peraturan BSSN No. 4/2021**.

| Aspek | Status |
|---|---|
| **HTTPS/TLS valid** | 🔴 WAJIB |
| **Update rutin** CMS/plugin/tema | 🔴 WAJIB |
| **Backup berkala + uji restore** | 🔴 WAJIB |
| **Kontrol akses & hak pengguna** | 🔴 WAJIB |
| **Validasi input (anti SQLi/XSS/CSRF)** | 🔴 WAJIB |
| **Enkripsi data warga + batasi akses** | 🔴 WAJIB (UU PDP) |
| Log dasar (login/admin) | 🟡 Disarankan |
| WAF, SIEM, IDS, pentest, MFA | ⚪ Opsional (overkill untuk desa) |

> ⚠️ **JANGAN salah janji:** jangan klaim "aman 100%" atau "sesuai standar BSSN" kalau belum diaudit. Sebutkan spesifik yang dikerjakan.

---

## 4. Aksesibilitas
- Standar **WCAG 2.1** (POUR, target level **AA**)
- **Mobile-first wajib** — mayoritas warga akses dari HP (UU 8/2016 & PP 42/2020)
- Hemat data (kuota warga terbatas), kontras baik, alt text, navigasi keyboard

---

## 5. Pasar & Harga

### Paket (data pasar)
| Tier | Harga |
|---|---|
| **Dasar** (profil desa) | Rp600rb – Rp2,5jt/thn *(est.)* |
| **Menengah** (+SEO) | Rp2,3jt – Rp3,5jt |
| **Premium** (SID lengkap) | Rp3,5jt – Rp9jt |
| **Custom** | Rp8jt+ |

### Realisasi APBDes nyata (paling kredibel)
| Desa | Nilai |
|---|---|
| Desa Menanga (2024) | **Rp2.861.100** |
| Desa Gentanbanaran (2025) | **Rp5.000.000** |

### Maintenance bulanan
Rp100rb – Rp2jt/bulan (umum: Rp300rb–700rb). Isi: update, backup, monitoring, upload artikel, support.

### Komponen biaya
Hosting Rp100–150rb/bln · template premium Rp250rb–1,2jt · bimtek operator Rp1–2jt · jasa IT Rp1–2,5jt · **CMS pemerintah GRATIS**.

---

## 6. Fitur yang biasa diminta
- **Inti:** profil desa, berita/pengumuman, galeri, **Transparansi APBDes**, data statistik
- **Layanan publik (nilai jual utama):** pengajuan surat online + tracking, layanan mandiri warga, pengaduan, **PPID**
- **Ekonomi:** katalog UMKM/BUMDes, promosi wisata, peta desa
- **Pendukung:** CMS biar perangkat desa bisa update sendiri, training, hosting+domain+SSL

---

## 7. Contoh situs desa bagus (referensi desain)
- [Desa Salembaran Jati](https://www.salembaranjati.id/) — SID lengkap, transparansi APBDes
- [Desa Singapadu Kaler](https://singapadukaler-desa.id/informasi_publik) — menu informasi publik rapi
- [Desa Sidetapa](https://sidetapa-buleleng.desa.id/) — **Juara 2** lomba website 2024
- [Desa Pacung](https://pacung-buleleng.desa.id/) — **Juara 3**
- [Desa Sabuai](https://sabuai.digitaldesa.id/) — **Juara 1 nasional 2024**

---

## 8. 🎯 IMPLIKASI BISNIS (penting!)

1. **Pemerintah kasih CMS + domain GRATIS.** Jadi lo **bukan** jualan "website" — lo jualan:
   - **Desain & kustomisasi** yang bagus (bukan template generik)
   - **Fitur tambahan** (surat online, katalog UMKM, dashboard, PPID)
   - **Pendampingan & training** operator desa
   - **Maintenance & keamanan** (ini recurring income)
   - **Bantuan administrasi** `.desa.id` (template surat kuasa, koordinasi Diskominfo)

2. **Partner kunci = Diskominfo kabupaten**, bukan cuma kepala desa. Mereka yang pegang pendaftaran domain. Bangun relasi ke sini = pintu masuk semua desa di kabupaten.

3. **Harga realistis: Rp2,8–5 juta/desa** (bukan Rp3–15jt). Maintenance Rp300–700rb/bln = income rutin.

4. **Hook jualan terkuat:** "Pak, UU Keterbukaan Informasi mewajibkan desa publikasi APBDes. Website kami bikin itu otomatis & rapi — plus kepatuhan UU PDP." → kades takut kena masalah, lo nawarin solusi.

5. **Jangan belanja hosting mahal dulu** — pakai VPS yang ada sampai ada klien.

---

## 9. Checklist praktis
- [ ] Minta **salinan Perbup PBJ Desa** kabupaten target
- [ ] Urus **NPWP** (+ pertimbangkan bikin **CV** + NIB OSS)
- [ ] Siapkan template: **Surat Kuasa `.desa.id`**, KAK, SPK, invoice, BAST
- [ ] Siapkan klausul **UU PDP** (DPA) di kontrak
- [ ] Beli domain demo murah + pakai VPS yang ada
- [ ] Bangun **1 demo website desa** (fitur: profil, berita, APBDes, statistik)
- [ ] Bangun relasi ke **Diskominfo** kabupaten

---

## 🔗 Sumber utama
- Domain: https://domain.go.id/syarat-biaya · https://domain.go.id/faq
- CMS gratis: https://website.desa.id/cms/login · https://opendesa.id/
- Perpres 95/2018 (SPBE): https://peraturan.bpk.go.id/Details/96913
- Peraturan BSSN 4/2021: https://peraturan.bpk.go.id/Details/174275
- Peraturan LKPP 12/2019: https://pasal.id/peraturan/perban/peraturan-lkpp-no-12-tahun-2019
- Perpres 46/2025: https://peraturan.bpk.go.id/Details/318647
- UU PDP 27/2022: https://peraturan.bpk.go.id/Details/229798
- Contoh RAB: https://indodesa.id/contoh-rab-pengadaan-website-desa/

#bisnis #website-desa #riset #compliance