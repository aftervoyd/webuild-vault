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