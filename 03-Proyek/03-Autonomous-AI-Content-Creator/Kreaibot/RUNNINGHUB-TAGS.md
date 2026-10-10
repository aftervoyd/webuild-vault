# RunningHub — TAKSONOMI TAG (referensi publish)
> Diambil dari picker Tag di halaman `/publish/<workflowId>` (UI Indonesia), 10 Okt 2026.
> **Minimal 1 tag WAJIB** — submit tanpa tag → modal "Pilih setidaknya satu tag", metadata tidak tersimpan.
> Tidak ada API publik untuk daftar ini (`/api/portal/template/tags` → 404); hanya bisa dibaca dari UI.

## Grup & sub-tag
- **Manusia Digital**
- **Pembuatan Gambar** → Teks ke Gambar · Gambar ke Gambar · Prompt Inferens
- **Pembuatan video** → Teks ke Video · Gambar ke Video · Video ke Video
- **Efek Video** → Efek khusus figur · Efek Spesial Berbasis Adegan · Efek Pertempuran ·
  Filter Efek · Efek Transisi · Pergerakan kamera video
- **Anime** → Realistis · Gadis cantik · IP Populer · Karakter anime · Karakter game · Tema Kampus ·
  Tema Jepang Tradisional · Gaya Fantasi · Cyberpunk · Karakter Mecha · Chibi / Gaya Lucu ·
  Hewan Peliharaan/Hewan · Berdasarkan Skenario
- **Pembuatan Audio**
- **Poster** → Pembuatan Poster · Font
- **Pemrosesan Gambar** → **Hapus Latar Belakang** · **Hapus Tanda Air** · **Outpaint** ·
  **Upscale HD** · **Filter** · **Inpaint** · **Retus** · **Hapus** · **Stilisasi** ·
  **Pencahayaan** · **Ekstrak Line Art** · **Pewarnaan Line Art** · **Restorasi foto lama** ·
  **Ganti Latar Belakang Gambar** · Pemrosesan gambar lainnya
- **Fotografi** → **Foto Potret** · **Foto ID** · **Fotografi Produk** · **Tukar Wajah** ·
  Fotografi Hewan Peliharaan · **Riasan** · **Ganti Pakaian** · Fotografi Lainnya
- **Film & Game** → **Desain Karakter** · **Konsistensi Karakter** · **Pembuatan Gambar Storyboard** ·
  Roleplay · Properti Adegan · Video · Film dan Game Lainnya
- **Model 3D** → Karakter · Lingkungan Adegan · Properti Objek · Struktur Bangunan · Kendaraan ·
  Senjata dan Peralatan · Hewan Biologis
- **Fitur Kreatif** → Gaya Transfer · Karakter Kreatif · Ide Kreatif · Figur Rintangan Misteri ·
  Kreatif lainnya
- **Desain Grafis** → logo · Festival · Pakaian · Desain Grafis Lainnya
- **Produk e-commerce** → **Ubah Latar Belakang Produk** · **Ganti Kemasan Produk** ·
  Tampilan Produk Model · Transfer Pola · Menata Ulang Pencahayaan · Tampilan Pakaian ·
  Penggantian Produk · Produk e-commerce lainnya
- **Desain Interior & Eksterior** → Tambahkan karakter ke dalam adegan ·
  Renovasi Rumah Kosong Satu-Klik · Ubah gaya dekorasi · Tambahkan latar belakang untuk
  furnitur/arsitektur · Sketsa ke Render · Arsitektur Lainnya dan Desain Ruang
- **Lukisan Bergaya** → Gaya Lukisan Klasik · Gaya Kerajinan Tangan · CG Fantasi ·
  Ilustrasi Kreatif Modern · Seni piksel · Tiongkok Tradisional · Gaya Barat · IP Populer ·
  Anime · Kartun 3D · Lukisan gaya lainnya
- **Pemrosesan Video** → Transfer Gerakan · Konversi Gaya Video · Super-resolusi video ·
  Hapus elemen video · Hapus Tanda Air · Penukaran Wajah Video · Ganti Latar Belakang Video ·
  Pemrosesan video lainnya
- **Plugin** → Hulu*** · Plugin lainnya
- **Lainnya**

## Yang dipakai workflow `qwen-consistency-edit`
`Konsistensi Karakter` + `Ganti Latar Belakang Gambar` + `Gambar ke Gambar`
(terdaftar di API sebagai: Consistent Characters · Background Swap · Image-to-Image)

## Panduan memilih
- **2–3 tag** paling relevan; jangan lebih.
- Jangan pakai tag yang tidak nyambung (mis. Anime/Video/3D untuk tool edit foto) — muncul di
  pencarian yang salah → run sedikit + rasio favorit jelek.
- Prioritaskan tag yang **dicari banyak orang**: Hapus Latar Belakang, Ganti Latar Belakang Gambar,
  Upscale HD, Foto ID, Restorasi foto lama, Konsistensi Karakter, Ubah Latar Belakang Produk.