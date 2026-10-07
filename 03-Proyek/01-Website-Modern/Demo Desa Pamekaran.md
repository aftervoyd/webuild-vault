# 🏡 Demo Desa Digital — "Desa Pamekaran" (v1)

> **Status:** 🟢 **JADI & LIVE** (7 Okt 2026) · Bagian dari [[03-Proyek/01-Website-Modern/README|Proyek 01]]

---

## 🔗 Akses

```
http://100.115.213.21:8080/     ← via Tailscale
```
- **Pemilik:** Webuild (demo internal)
- **Tujuan:** bahan tawaran ke **calon kepala desa** — posisikan sebagai "Demo Desa Digital" (produk/visi), bukan situs kampanye
- Catatan: desa & datanya **fiktif/representatif**, gampang diganti ke data asli

## ⚙️ Teknis

| Item | Nilai |
|---|---|
| Stack | **Astro 5 + Tailwind CSS 4** (output statis) |
| Font | Plus Jakarta Sans (fontsource, offline) |
| Ukuran situs | **280 KB** total (8 halaman) |
| Build time | **±1,5 detik** |
| Server | `server.mjs` (Node murni, **tanpa dependency**) |
| Service | systemd `desa-pamekaran` (auto-start) · port **8080** |
| Bind | **Tailscale only** (`100.115.213.21`) — privat |
| Proyek | `/root/projects/desa-pamekaran` |
| Log | `/var/log/desa-pamekaran.log` |

## 📄 8 Halaman

| Halaman | Isi |
|---|---|
| `/` | Hero gradien, statistik, APBDes ringkas, layanan, potensi, UMKM, berita, CTA |
| `/profil` | Sekilas desa, batas wilayah, **visi & misi**, demografi, struktur perangkat |
| `/apbdes` | **Transparansi anggaran** — tabel pendapatan & belanja + bar proporsi |
| `/umkm` | 6 produk unggulan warga |
| `/layanan` | Alur pengajuan, 8 layanan surat, FAQ |
| `/berita` | 4 berita/kegiatan |
| `/kontak` | Kontak, **form → WhatsApp**, peta OpenStreetMap |
| `/404` | Halaman tidak ditemukan |

## 🎨 Desain

- Tema: **hijau–biru gradien** = kesan "desa digital" (segar, modern, terpercaya)
- **Anti-template:** token warna kustom, motif batik-grid halus, animasi scroll (`animation-timeline: view()`), kartu hover, no theme jadi
- Mobile-first, aksesibel (label form, aria), SEO (meta + OG)

## 🛠️ Perbaikan bug saat build
1. Gradien progress bar tidak konsisten (gradien ikut mengecil) → fix pakai overlay, gradien tetap penuh
2. Script client tidak bisa akses variabel server (`desa`) → fix pakai `data-attribute`

## 📋 Next (v2)
- [ ] Ganti data fiktif → data desa asli
- [ ] Foto asli (hero, galeri, produk UMKM)
- [ ] Galeri/berita detail per halaman
- [ ] Form pengajuan surat (butuh backend — bisa Next.js saat produksi)
- [ ] Pindah ke **pamekaran.com** (Hostinger) / domain desa resmi

## 🔗 Terkait
- [[03-Proyek/01-Website-Modern/README]] · [[03-Proyek/Roadmap Eksekusi]]
- [[06-Tim-Agent/RepoScout - Katalog Repo]] (shadcn/ui, Magic UI, Cult UI)
- [[01-Bisnis/Baseline & Compliance - Website Desa]]

#proyek #website-modern #desa #demo #selesai
---

## 🎨 Eksperimen Redesign (7 Okt 2026) — 3 arah

**Lokasi:** `/root/projects/desa-redesign/` → live `http://100.115.213.21:8085/` (systemd `desa-redesign`, Tailscale-only)

**Kenapa:** user menilai demo lama "generik di desktop & nggak modern kalau jadi aplikasi".
Diagnosis: hero gradien hijau-biru + kartu ngambang (pola SaaS template), statistik dobel,
font default, radius besar + shadow lembut, **nol identitas lokal Madura**, nol fotografi.

**Tiga arah yang dibangun (data sama, bahasa visual beda):**
| | Arah | Gaya | Nilai juri |
|---|---|---|---|
| A | **Editorial Madura** ⭐ rekomendasi | serif raksasa, grid asimetris, palet tanah/kunyit/hijau tua, motif batik halus | **8/10** |
| B | **Civic Dark Tech** | dark-mode default, aksen limau, bento dashboard, ticker | **8/10** |
| C | **Organic Magazine** | Anton raksasa, outline type, miring/rotate, kolase | **7/10** |

**Pelajaran teknis (penting, jangan diulang):**
1. **JANGAN pakai IntersectionObserver buat reveal** → di headless/harness observer tak pernah
   jalan → konten opacity 0 → halaman KOSONG. Ganti ke **CSS murni `animation-timeline: view()`**;
   kalau browser lama tak mendukung, konten tetap terlihat (gagal-aman).
2. `data-w="42"` + JS → ganti ke **CSS custom property** `--w:41,7%` + `@keyframes grow` view-timeline.
3. Screenshot: **browser harness sering timeout** → pakai **chromium lokal headless**:
   `/root/.hermes/tools/chromium-1208/chrome-linux64/chrome --headless=new --no-sandbox \
   --hide-scrollbars --window-size=1440,4400 --virtual-time-budget=13000 --screenshot=out.png URL`
4. **Foto stok acak (picsum) berbahaya** → pernah menampilkan **Manhattan** di situs desa Madura.
5. **Wikimedia Commons = sumber foto asli berlisensi bebas** (pakai User-Agent deskriptif +
   jeda 1,5–2 dtk, kalau nggak → 403). **Wajib potong tepi ~8,5%** untuk buang watermark
   ("Wonderful Indonesia" / "NUSANTARA" nempel di sudut).
6. **Selalu verifikasi angka anggaran pakai hitungan**, dan tulis **persen** di bar — bar tanpa
   skala cuma jadi tekstur, bukan data.
7. `prefers-reduced-motion` wajib: matikan marquee/animasi + netralkan rotate.

**Data APBDes (terverifikasi balance):** belanja = pendapatan = **Rp2.847.500.000**
(41,7% + 31,3% + 12,0% + 10,5% + 4,5% = 100%).

**Kredit foto:** `foto/KREDIT.md` (23 foto Wikimedia Commons, CC BY / CC BY-SA).

---

## 🔁 Putaran kedua — 4 gaya yang lebih resmi (7 Okt 2026)

**Masukan user:** 3 arah sebelumnya *"malah lebay dan terlalu modern"*.
→ Pelajaran: untuk website desa/pemerintah, **tahan diri**. Tanpa serif raksasa, tanpa outline
type, tanpa elemen miring, tanpa animasi.

**Empat gaya baru** (`/root/projects/desa-redesign/gaya-{1..4}.html`, pemilih: `pilih.html`):

| # | Nama | Karakter | Warna | Nilai juri |
|---|---|---|---|---|
| 1 | **Resmi & Rapi** | portal instansi klasik: bar kontak, kop, menu biru, APBDes = tabel resmi | biru tua + kuning | **8/10** |
| 2 | **Hangat & Kekeluargaan** | nada menyapa, foto warga, kartu lembut | krem + bata + zaitun | **8/10** (setelah fix) |
| 3 | **Adat Nusantara** | formal simetris, pita & bingkai motif **kawung**, layanan I–VI | marun + emas + hijau tua | **9/10** |
| 4 | **Buletin Desa** | koran/buletin: masthead, headline, rubrik 3 kolom, Pengumuman | kertas + tinta + merah | **9/10** |

**Pelajaran teknis baru:**
1. **JANGAN pakai emoji sebagai ikon** → di headless/beberapa sistem jadi kotak kosong ("tofu").
   Pakai **inline SVG** (`stroke="currentColor"`), ukuran 20–22px.
2. **Kecurigaan hasil vision harus diuji ulang** — vision pernah lapor "label tombol tak terlihat",
   padahal cuma **crop-nya yang salah posisi**. Selalu zoom area spesifik sebelum "memperbaiki".
3. Angka & persen APBDes di keempat gaya konsisten: Rp2.847.500.000 (41,7/31,3/12,0/10,5/4,5).

---

## ⏸️ STATUS: MENUNGGU REFERENSI DARI USER (7 Okt 2026)

Keputusan user: **"kita lanjut nanti aja, gua bakal kirim page per page referensinya"**
→ Jangan mulai redesign lagi sampai user mengirim referensi per halaman.

**Yang sudah siap dipakai saat lanjut:**
- **4 gaya desain** siap: `gaya-1` Resmi & Rapi · `gaya-2` Hangat & Kekeluargaan ·
  `gaya-3` Adat Nusantara · `gaya-4` Buletin Desa
- Pemilih: `http://100.115.213.21:8085/pilih.html`
- 3 eksperimen lama (lebay): `index.html`
- Foto asli berlisensi + kredit: `foto/web/` & `foto/KREDIT.md`
- **Data desa siap pakai (terverifikasi balance):** APBDes Rp2.847.500.000
  (41,7 / 31,3 / 12,0 / 10,5 / 4,5) · 3.847 jiwa · 1.124 KK · 4 dusun · 412,6 Ha · 48 UMKM
- Sistem service: `desa-redesign` (port 8085, Tailscale-only), `desa-pamekaran` (port 8080)

**Cara kerja saat referensi masuk:** proses **halaman per halaman**, ikuti struktur &
proporsi referensi, tetap pakai palet/gaya yang user pilih, dan pakai data desa di atas
(jangan ganti angka dengan karangan).
