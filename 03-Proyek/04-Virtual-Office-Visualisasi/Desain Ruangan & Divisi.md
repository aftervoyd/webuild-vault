# 🏢 Desain Ruangan & Zonasi Divisi — Webuild Office

> Rancangan bagaimana kantor **tumbuh sesuai kebutuhan**, bukan diborong di awal.
> Bagian dari [[03-Proyek/04-Virtual-Office-Visualisasi/README|Proyek 04]]
> **Status: Fase 1 🟢 JADI** · dirancang 7 Okt 2026

---

## 1️⃣ Prinsip

> **Ruangan dibuat HANYA kalau ada alasan fungsional — bukan karena estetika.**

Alasan fungsional yang sah:
- **Kapasitas** — meja tidak cukup
- **Privasi** — pekerjaan butuh ruangan tertutup (server, rekaman)
- **Kebutuhan alat** — butuh peralatan khusus (studio, dapur, kamar mandi)
- **Tamu** — terima klien butuh ruang presentasi

Alasan yang **TIDAK** sah: "biar keliatan rame", "biar keren".

---

## 2️⃣ Kondisi Sekarang (Fase 1 — AKTIF)

Semua divisi kerja di **satu kantor utama**, tapi dipisah jadi **5 ZONA meja** yang berdekatan.

Kenapa begitu? Karena:
- Kapasitas kantor = **10 meja** (spot-1…spot-10)
- Agen = **13** (2 sudah menempati spot khusus: Boss + Orchestrator)
- **Satu ruangan masih cukup** — yang kurang cuma *keteraturan*, bukan *ruang*

### Peta Zona

| Divisi | Emoji | Zona meja | Posisi |
|---|---|---|---|
| **Riset & Intel** | 🔍 | `spot-6`, `spot-4`, `spot-5` | Klaster tengah-atas |
| **Produksi Web** | 🏗️ | `spot-3`, `spot-7` | Kiri & kanan-bawah |
| **Kreatif & Studio** | 🎨 | `spot-9`, `spot-10` | Klaster kanan |
| **Distribusi & Sosmed** | 📱 | `spot-8` | Kanan-bawah |
| **Bisnis & Koordinasi** | 📊 | `spot-2`, `spot-8` | Dekat pintu (terima klien) |
| *(pemilik)* Boss Webuild | 👑 | `spot-1` | Meja bos |
| *(AI)* Orchestrator | 🧠 | `spot-2` | Meja kedua |

**Isi divisi:**

- 🔍 **Riset** — RepoScout, NewsWatch, TrendScout
- 🏗️ **Produksi** — WebBuilder, OpsAgent
- 🎨 **Kreatif** — DesignerBot, MotionAgent, VoiceAgent, ContentWriter
- 📱 **Distribusi** — SocialAgent, WebPublisher
- 📊 **Bisnis** — SalesAgent, Orchestrator

### Cara kerjanya (teknis)

1. Server Hermes kirim event webhook → `profil` + `tool`
2. `PROFILE_TO_AGENT` (server) petakan profil → role kantor
3. `ROLE_TO_DIVISION` (`src/divisions.ts`) petakan role → divisi
4. `assignSpot(agents, spots, zonaDivisi)` — agen **cari meja di zona divisinya dulu**, baru fallback ke meja bebas
5. Label zona di lantai nampilin emoji + nama + **jumlah agent** yang sedang di zona itu

**Hasil:** satu divisi duduk berdekatan → kelihatan "siapa kerja di mana".

---

## 3️⃣ Aturan Kapan Nambah Ruangan (TRIGGER)

Ruangan baru **WAJIB** dibuat kalau salah satu kena:

| # | Trigger | Ambang | Efek |
|---|---|---|---|
| 1 | **Kapasitas** | agen kerja serentak **> 10** (semua meja penuh) | Tambah meja / ruangan |
| 2 | **Zona kekecilan** | satu divisi **> 3 agen** di zona | Perluas zona |
| 3 | **Ruang sendiri** | satu divisi **≥ 4 agen aktif** | Divisi itu dapat ruangan sendiri |
| 4 | **Butuh privasi** | Divisi mulai kerja yang butuh ruang tertutup | Ruangan khusus (server/studio) |
| 5 | **Terima tamu** | Ada meeting/demo klien nyata | Meeting room aktif |

> Aturan #1 & #2 = **otomatis** (algoritma bisa deteksi).
> Aturan #3–5 = **manual** (Orchestrator mutusin, karena butuh konteks bisnis).

---

## 4️⃣ Rencana Pertumbuhan Ruangan (ROOM_GROWTH_PLAN)

| Ruangan | Divisi | Alasan fungsional | Trigger |
|---|---|---|---|
| 🏢 **Kantor Utama** | semua | Markas + 5 zona | ✅ **AKTIF** |
| 🖥️ **Server Room** | Produksi | OpsAgent kerja di ruangan dingin & bising — kalau di kantor terbuka ganggu divisi lain | ⏭️ Begitu OpsAgent pegang deployment produksi |
| 🎨 **Design Studio** | Kreatif | Butuh ruangan gelap + monitor warna terkalibrasi. **Ini ruangan yang bisa ditunjukin ke klien** | 📅 DesignerBot + MotionAgent aktif pegang proyek klien |
| 🎙️ **Studio Rekaman** | Kreatif | VoiceAgent butuh **kedap suara** buat TTS Indonesia/Sunda/Jawa | 📅 VoiceAgent mulai produksi narasi |
| 🤝 **Meeting Room** | Bisnis | SalesAgent + Orchestrator terima klien (calon kades, UMKM) | 📅 Ada demo/meeting klien nyata |
| ☕ **Ruang Istirahat** | semua | Tempat agent sosialisasi antar-divisi (bukan kerja) | 📅 Agen > 15 orang |

**Estimasi:** ruangan baru dibutuhkan mulai **agen ke-14** atau saat **OpsAgent/Kreatif mulai kerja produksi**.

---

## 5️⃣ Cara Bikin Ruangan Baru (Teknis)

### Yang dibutuhkan
1. **Background pixel-art** 800×600 (versi siang + malam)
2. **Entry di `src/rooms.ts`** — id, nama, furniture[], agentSpots[], waypoints[], connections[]
3. **Pintu penghubung** (`toRoom`) dari main-office → ruangan baru
4. **Alokasi divisi** di `src/divisions.ts`

### 🚨 TEMUAN PENTING
CSS multi-ruangan **SUDAH ADA** di repo (`src/styles/rooms.css`):
- `.room-navigator`, `.room-sidebar` — sidebar navigasi ruangan
- `.fp-*` (floor plan) — **tampilan denah** semua ruangan + badge hunian
- `.room-door-hotspot`, `.door-label` — pintu antar-ruangan
- `.room-transition-*` — animasi pindah ruangan

**TAPI komponen React-nya belum dibuat.** Repo asli punya fondasinya, tapi App kita cuma render `main-office`.

→ **Artinya:** bikin multi-ruangan = **bikin komponennya**, CSS-nya tinggal pakai. Bukan mulai dari nol. 🎯

### Background art
- Bisa **di-generate sendiri** pakai Python PIL (lihat `scripts/gen-office-bg.py`) — gratis
- Atau ambil dari aset repo asli (`public/rooms/*.png` — belum ada, cuma office utama)

---

## 6️⃣ Roadmap

- [x] **Fase 1** — Zonasi 5 divisi + label lantai + nama agent asli ✅
- [ ] **Fase 2** — Komponen multi-ruangan (pakai CSS yang sudah ada) + Floor Plan view
- [ ] **Fase 3** — Ruangan pertama: **Server Room** (saat OpsAgent aktif)
- [ ] **Fase 4** — **Design Studio** + **Studio Rekaman** (saat Kreatif aktif)
- [ ] **Fase 5** — **Meeting Room** (saat jualan ke desa jalan)

---

## 🔗 Terkait
- [[03-Proyek/04-Virtual-Office-Visualisasi/README]] — arsitektur teknis Webuild Office
- [[06-Tim-Agent/Team Registry]] — 5 divisi & 13 agent
- [[03-Proyek/Roadmap Eksekusi]]

#proyek #virtual-office #desain #divisi #arsitektur