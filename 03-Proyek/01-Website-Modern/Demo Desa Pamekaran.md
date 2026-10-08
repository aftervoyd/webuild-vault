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

---

## 📱 Aplikasi Mobile "Desa Digital Pamekaran" (7 Okt 2026)

**Permintaan user:** *"fokus ke mobile device dan ui/ux nya persis seperti ini"* (kirim referensi
4 layar: Login · Dashboard · Drawer · Pasar UMKM Lokal).

**Hasil:** `/root/projects/desa-mobile/app.html` — aplikasi mobile yang benar-benar jalan.
Live: **http://100.115.213.21:8086/app.html** (Tailscale-only, systemd `desa-mobile`).
Presentasi 4 HP: `/root/projects/desa-mobile/presentasi.png`

**Token desain (diambil dengan sampling piksel dari referensi, bukan perkiraan):**
- Biru utama `#1E4E9C` · layar `#EEF2F7` · kartu/tile `#FFFFFF` · ikon tile `#EAF1FB`
- Teks `#1F2937` · redup `#6B7280` · garis `#E5E7EB` · merah `#DC2626`
- Font Inter · tile 112px · gap 11px · radius kartu 16px · tombol 10px
- **Terkonfirmasi: tile dashboard PUTIH di atas latar abu-biru** (bukan kebalikannya)

**4 layar:** Login (crest, 2 input, Login, Social Login G/X/FB/LinkedIn) · Dashboard
(2x3 tile: Administrasi/Kesehatan/UMKM Lokal/Berita & Info/Pariwisata/Pelayanan + carousel
berita + nav bawah 5 ikon) · Drawer (profil + 8 menu, Dashboard aktif biru, Logout merah) ·
Pasar UMKM (chips Semua/Makanan/Kerajinan/Pertanian/Wisata + 4 produk 2 kolom + Add to Cart).

**URL param:** `?w=390` (mode bingkai tetap 390x844 untuk screenshot) · `?s=login|dash|pasar`
· `?drawer=1`.

### ⚠️ 4 JEBAKAN YANG DITEMUKAN (WAJIB DIINGAT)

1. **`onerror` + `innerHTML +=` = LOOP TAK TERBATAS.** `onerror="this.parentNode.innerHTML+='...'"`
   menulis ulang `<img>` berikut atribut `onerror`-nya → 404 → onerror → 404 → **Chrome hang
   tanpa error** (70 detik, tanpa file output). FIX: avatar ilustrasi SVG / `this.remove()`.
   **Jangan pernah pakai `innerHTML +=` di dalam handler error.**
2. **Chrome headless + `<meta viewport width=device-width>` = layout viewport ≠ ukuran window.**
   `--window-size=390,844` menghasilkan gambar 390x844 TAPI layout viewport **500px** → shell
   430px (max-width) termotong 40px di kanan. FIX: `?w=390` memaksa `.stage`/`.shell` 390x844.
3. **`.shell{width:100%}` di dalam flex item pembungkus yang belum di-CSS = ambruk.** `.stage`
   tanpa aturan → shell 99px, input 7px (placeholder "Password" jadi "P"). FIX: beri `.stage`
   aturan eksplisit + `.shell{flex:0 0 auto;min-width:0}`.
4. **Emoji sebagai ikon = kotak kosong ("tofu")** di server tanpa font emoji. **Pakai inline SVG**
   (`stroke="currentColor"`), 20-24px.

5. **Verifikasi vision HARUS lewat resolusi penuh.** Saat gambar diperkecil ke 350px, vision
   melaporkan "drawer kosong", "kolom ke-3 terpotong", "label Pelayanan terpotong" — **semuanya
   SALAH**; di resolusi penuh semuanya normal. Selalu potong area spesifik lalu zoom sebelum
   "memperbaiki" sesuatu. Jangan memperbaiki bug yang tidak ada.


---

## 🧊 Putaran 3 — Glassmorphism + nav pil melayang (8 Okt 2026)

Permintaan user: (1) **glassmorphism**, (2) nav bawah **rounded berisi 5 ikon dengan "Beranda" di tengah**, (3) versi website: **berita disusun ke bawah**.

Berkas: `/root/projects/desa-mobile/app.html` — LIVE `http://100.115.213.21:8086/app.html` (systemd `desa-mobile`, Tailscale-only).

**Yang dikerjakan**
- Token kaca baru: `--kaca`, `--kaca-grad`, `--kaca-kuat`, `--kaca-garis`, `--blur`, `--blur-kuat`, `--bayang-kaca` + fallback `@supports not (backdrop-filter:…)`.
- Latar `shell` jadi gradien **+ 6 blob radial berwarna** (`::before`). Pelajaran: glassmorphism **wajib** punya latar berwarna — kalau latarnya putih, efek kaca tak terbaca (keluhan pertama: "tiles terlihat seperti kartu putih biasa").
- Nav bawah jadi **pil melayang**: `position:absolute;left/right:16px;bottom:14px;border-radius:32px`, beranda di tengah sebagai tombol **naik** (`margin-top:-24px`, lingkaran biru gradien). Layar diberi `padding-bottom:104px` supaya konten tak ketutup pil.
- **Versi website** aktif lewat kelas `body.web` (JS: `innerWidth>=700` **atau** parameter `&web=1`): 6 tile sebaris, berita `display:block` **disusun ke bawah** (bukan carousel), pil nav di tengah, produk 4 kolom.
- Berita ditambah jadi **4 kartu** supaya versi website tidak menyisakan ruang kosong besar.
- Login: panel kaca + tautan "Lupa Password?" / "Belum punya akun? Daftar".

**⚠️ PELAJARAN MAHAL — Chrome headless**
1. **Chrome MENOLAK jendela < ~500px.** `--window-size=390,844` → viewport sebenarnya **500×757**. Akibatnya elemen di bawah y=757 (nav ada di y768-830) **tidak pernah ter-paint** padahal ada di DOM → tampak "nav hilang". FIX: render di jendela besar (`--window-size=560,1040`) lalu **crop** dengan PIL ke 390×844.
2. **Media query `min-width` dinilai dari LAYOUT VIEWPORT**, bukan lebar konten → jangan andalkan media query untuk mengaktifkan layout desktop saat render. Pakai kelas yang di-set JS + parameter URL.
3. Verifikasi lewat **angka**, bukan mata AI: `getBoundingClientRect()` lewat iframe + `--dump-dom`, dan tampilkan `innerWidth/innerHeight` di layar lewat overlay debug.


### 🔧 Revisi setelah tinjauan user (8 Okt 2026)
1. **Nav bawah → 4 ikon** (hapus hamburger): `Beranda · Profil · Pesan · Pengaturan`, masing-masing pakai label teks 9.5px. Beranda = ikon di dalam lingkaran biru 32px, label biru.
2. **Foto berita disejajarkan** dengan kolom tile di atasnya: `.geser` tak lagi full-bleed (`margin:0`), `.kartu-berita{width:100%}` → tepi kiri/kanan kartu = tepi tile, tak ada kartu kedua mengintip.
3. **Drawer menutupi nav bawah**: `buka()` menyetel `navb.style.visibility='hidden'`, `tutup()` mengembalikannya.
4. **Pasar UMKM**: kotak pencarian di atas (ikon kaca + `#ic-cari` baru) yang **menyaring realtime** digabung dengan chip kategori; **nav bawah juga tampil** di layar ini (`display` nav sekarang `(name==='login')?'none':'flex'`).

**⚠️ Dua bug nyata yang ditemukan saat verifikasi (PENTING)**
- **`.screen` adalah flex-column** → begitu konten melebihi tinggi layar, flex item dengan `flex-shrink:1` **menyusut** alih-alih menggulir. Akibatnya baris chip terjepit sampai **teksnya hilang** (chip tampak pil kosong). FIX: `flex:none` pada `.cari`, `.chips`, `.produk`. **Pelajaran: setiap blok yang tidak boleh menyusut di dalam `.screen` WAJIB `flex:none`.**
- **`aspect-ratio` diabaikan** pada `.pk .foto` karena `<img height:100%>` menyelesaikan tinggi dirinya dari rasio asli gambar → kartu tetap 289px, nav menutupi baris kedua dan tombol Add to Cart hilang. FIX: `img{position:absolute;inset:0}` + `aspect-ratio:3/2` → kartu 240px, baris kedua berakhir di y720 (nav di y768) ✓. **Pelajaran: untuk aspect-ratio, gambar harus dikeluarkan dari alur (absolut).**

**Cara ukur yang benar:** `getBoundingClientRect()` lewat iframe 390×844 + `--dump-dom`, lalu grep `.produk / .pk / .navb`. Angka jauh lebih cepat daripada menebak dari gambar.

- **Koreksi isi berita (audit foto):** kartu ke-4 memakai foto **plakat bertulisan** (nyambung tidak dengan headline "Pelatihan Pemasaran Digital"). Diganti: berita-3 → foto monumen + bendera (`berita1-wide2`), headline "Monumen Gotong Royong Desa Diresmikan Warga"; berita-4 → foto kerupuk (`kerupuk-0-wide`), label **UMKM**, headline "UMKM Kerupuk Rumahan Tembus Pasar Kecamatan". Pelajaran: **judul harus mengikuti foto yang benar-benar tersedia**, bukan sebaliknya.


### 🏁 Putaran final (8 Okt 2026)
1. **Cover berita mobile → 1:1.** `.kartu-berita{aspect-ratio:1/1;height:auto}` + `.geser{align-items:flex-start}` (tanpa itu flex `stretch` mengalahkan `aspect-ratio`). Efek: ruang kosong di bawah carousel terisi foto.
2. **Versi website desktop: sidebar PERMANEN di kiri.** Kelas `body.web`: `.drawer{transform:translateX(0);width:288px;border-radius:0}` + `.scrim{display:none}` + **`.screen{left:288px}`** (bukan `padding-left` pada `.panggung` — anak `position:absolute` diposisikan relatif ke **padding box**, jadi padding tidak menggeser mereka) + `#shell[data-screen="login"]` menonaktifkan sidebar di layar login + `#buka-drawer` disembunyikan + `buka()` diberi guard `if(document.body.classList.contains('web'))return;` supaya klik hamburger tidak menyembunyikan nav.
3. **Kolom kanan: Agenda Desa.** Grid 2 kolom di `.isi` versi web (`minmax(0,1fr) 340px`), berisi **kalender Oktober 2026** (1 Okt = Kamis → 3 sel kosong; tanggal 8 = hari ini dilingkari, 12/17/24/31 = hari acara) + 4 kartu acara. Tersembunyi di mobile (`.kolom-k{display:none}`).
4. **Finalisasi**: `<title>`, meta description, `apple-mobile-web-app-*`, **`manifest.webmanifest`** + ikon 192/512/64 (digambar PIL: rumah putih di kotak biru gradien) → aplikasi bisa di-*install* ke home screen. Status bar HP (`.sbar`) disembunyikan di versi website.

**Sisa (jujur, belum dikerjakan):** versi desktop masih memakai **nav pil bawah** (pola mobile) padahal sidebar sudah permanen → agak redundant; dan halaman Pasar hanya 4 produk sehingga bawahnya kosong.


### 📐 Putaran lebar & navbar (8 Okt 2026)
5. **Navbar bawah DIHAPUS di versi website** (permintaan user). `body.web:not(.frame) .navb{display:none!important}` — **`!important` wajib**, karena `show()` menulis `navb.style.display` sebagai inline style yang mengalahkan rule CSS biasa. Padding bawah dikurangi karena tak ada lagi nav melayang: `.isi` 132→48, `.produk` 110→48, `#s-login` 132→72.
6. **Lebar menyesuaikan laptop/komputer.** `.shell{max-width:1720px;margin:0 auto}` (di monitor ultrawide aplikasi tidak melar), `.isi`/`.produk`/`.cari`/`.chips` `max-width:1320px`, gutter `--gutter:clamp(22px,3vw,56px)`, sidebar `--sidebar:clamp(232px,18vw,288px)`. **Diuji nyata di 1366×768, 1440×900, 1920×1080** → tanpa overflow horizontal, kalender tetap muat, sidebar menyesuaikan sendiri.
7. **Dua bug halus hasil audit gambar:** (a) `.produk` memakai `margin:0 auto` di dalam flex-column → **auto-margin menang atas `align-items:stretch`**, jadi item menyusut ke lebar *fit-content* (terukur 1092px = 4×240 + gap + padding) → wajib `width:100%` eksplisit. (b) `repeat(auto-fill,…)` menyisakan track kosong di kanan → pakai **`auto-fit`**.
8. **Kolom kanan diisi tuntas:** kalender + 4 acara + **Statistik Desa** (3.847 jiwa / 1.124 KK / 48 UMKM / 412,6 Ha) + **Pengumuman** (3 item) + `position:sticky;top:24px` supaya ikut terlihat saat digulir. Foto berita 3 diganti anyaman bambu (foto monumen lama pudar).
9. **Jebakan render baru (mahal):** di mode `--dump-dom` **tidak ada paint**, jadi **CSS transition tidak pernah maju** → `getComputedStyle(el).transform` melaporkan nilai AWAL (drawer terbaca `matrix(1,0,0,1,-255.71,0)` = tertutup, padahal di screenshot sudah terbuka). **Jangan ukur transform lewat `--dump-dom`; ukur dari screenshot.** Efek samping nyata: sidebar ikut beranimasi meluncur tiap load → rule web diberi `transition:none`.

### 📱 Mobile (final)
- Cover berita **1:1** (`.kartu-berita{aspect-ratio:1/1}` + `.geser{align-items:flex-start}` — tanpa `flex-start`, `align-items:stretch` mengalahkan `aspect-ratio`).
- **PWA:** `manifest.webmanifest` + ikon 192/512/64 + `apple-mobile-web-app-*` → bisa di-install ke home screen.


### 🔔 Revisi navbar + temuan render (8 Okt 2026)
10. **Judul "Dashboard" + ikon lonceng dihapus dari bar atas versi website** (`body.web:not(.frame) #s-dash .bar{display:none}`) → isi dashboard **rata ke atas** (`.isi{padding-top:34px}`). Bar halaman Pasar tetap, karena di situ ada tombol keranjang yang berfungsi.
11. **Lonceng pindah ke navbar kiri**: item "Pemberitahuan" + badge merah "3" (`.menulist a .lencana{margin-left:auto;…}` — `.menulist a` sudah `display:flex`, jadi badge terdorong ke kanan).
12. **⚠️ Temuan besar: preview drawer SELAMA INI TIDAK PERNAH BENAR-BENAR TERBUKA.** `--virtual-time-budget` **tidak menjalankan transisi CSS** → `setTimeout(buka,120)` + `transition:transform .28s` berhenti di posisi AWAL. Terukur: panel 272px hanya tampil **~25px** (96% tertutup) padahal di DOM kelasnya sudah terbuka; tidak ada yang sadar karena papannya kecil. **FIX: query `&nofx=1`** → `body.nofx *{transition:none!important;animation:none!important}` yang di-set SEBELUM `show()`. Terukur sesudah: panel terang sampai **x≈300** ✓. **Aturan baru: semua screenshot pakai `&nofx=1`.**


### 🧹 2 cacat terakhir versi desktop (8 Okt 2026)
13. **Sidebar tidak mengikuti halaman aktif.** Kelas `.on` di drawer bersifat statis (selalu "Dashboard"), jadi saat halaman Pasar terbuka sidebar tetap menyalakan Dashboard — terlihat jelas di versi website. **FIX:** di `show(name)` tambahkan `drawer.querySelectorAll('a[data-go]').forEach(a=>a.classList.toggle('on',a.dataset.go===name))`. Terukur: halaman Pasar → item "Pasar UMKM" nyala di y=251 ✓ (sebelumnya Dashboard). `show('login')` → tak ada yang nyala ✓ benar.
14. **Logout menggantung di tengah sidebar desktop** (ruang kosong besar di bawahnya). **FIX:** `.pemisah{margin-top:auto}` → pemisah + Logout terdorong ke dasar sidebar. Terukur: Logout y=844..888 dari tinggi 900 ✓.
15. Papan final desktop: `papan-desktop-1.png` (dashboard 1920×1080 + 1366×768) & `papan-desktop-2.png` (Pasar + Login 1920). Sisa jujur: halaman Pasar masih 4 produk → separuh bawah kosong.
