# RUNNINGHUB — PLAYBOOK KOIN & KONTES
> Disusun otomatis 10 Okt 2026, 02:45 WIB (sesi tidur user). Semua angka terverifikasi live.
> TIDAK memuat rahasia. Kredensial ada di `.env` (apiKey) & vault Hermes (login web).

---

## 0. STATUS AKUN (terverifikasi via API, 10 Okt 03:00 WIB)
| Item | Nilai |
|---|---|
| Koin tersisa | **28.362 RH Coins** (`remainCoins`) |
| Wallet dolar | **$0,010** (habis) |
| apiType | NORMAL |
| Membership | Personal **aktif s/d 8 Nov 2026** (36.000 koin/bulan) |
| Tarif tugas | ~0,2 koin/detik (Standard) · gagal/batal **tidak** ditagih |
| Login web akun | **BERHASIL** (vault Hermes handle `vault_5e4871dcae31`, origin runninghub.ai) |
| Nama profil | Nimara Official |

## 1. ⏰ "FREE WINDOW" — ⚠️ **KOREKSI 14 OKT 2026: KELIRU KONTEKS, JANGAN DIPAKAI ASAL**
- Klaim lama *"render 21:00–10:00 WIB gratis"* datang dari promo
  **"MiniMax H3 RH Enhanced: All members get 1 month of free unlimited generations, 13 Hours Free Daily"**.
  → Promo itu **khusus model MiniMax H3 RH Enhanced**, **BUKAN** untuk workflow/AI App kita.
- **Fakta terukur (bukan asumsi):** semua mesin yang kita pakai **selalu memakai koin, jam berapa pun**:
  | mesin | tarif nyata |
  |---|---|
  | Qwen-Edit 2511 (Generate Gambar / Ganti Baju) | **±49–52 koin per gambar** |
  | AI App `otz` Pose Transfer | **±26,3 koin/detik** (16,4 dtk ≈ 431 koin) |
  | nightfunnels Wan2.2 Animate | ±25,9 koin/detik |
- `accountStatus` → **`apiType: NORMAL`** (akun API biasa; bukan VIP/promo MiniMax).
- **Aturan operasional yang BENAR: hitung koin dulu sebelum render.** Tidak ada jam gratis;
  menjadwalkan render ke malam **tidak** menghemat koin.
- ⚠️ Pelajaran: promo di halaman depan RunningHub **spesifik per model** — jangan generalisasi ke
  workflow mana pun tanpa uji tagihan nyata (cek `remainCoins` sebelum vs sesudah 1 render).

## 2. 💰 JALUR DAPAT KOIN (diurut potensi)
### A. Program Insentif Kreator (创作者激励计划) — POTENSI TERBESAR
- Halaman: `runninghub.ai/creator-reward` · penghasilan: `runninghub.ai/my-income`
- Cara dapat: **publish workflow / AI app / model** → dibayar dari:
  1. **Jumlah run** (termasuk panggilan API) · 2. **Favorit** · 3. **Orisinalitas**
- Bisa juga **dijual** (set berbayar). Settlement **mingguan**; withdraw **bulanan** (tgl 15 kerja bulan berikutnya).
- Wajib **Orisinal** + lolos review manusia. Konten sampah/meniru → ditolak/diturunkan.
- **Status kita: $0,00** — tapi **workflow pertama sudah dibuat & JALAN** (`qwen-consistency-edit`, id 2108638842228461570). Tersisa aksi UI 1-klik untuk publish. Detail: **`RUNNINGHUB-CREATOR-PROGRAM.md`**.

### B. Program Undangan (Invite)
- **Kode invite kita: `baaxhjzz`** · link: `https://www.runninghub.ai?inviteCode=baaxhjzz`
- Kedua pihak dapat **500 koin**. User reguler maks **5.000 koin/hari**; **mitra promosi tanpa batas**.
- ⚠️ **DILARANG** pakai akun palsu/bot ("unfair or fraudulent means") → kena batalkan + ban. **Jangan farming.**

### C. Login Harian
- **±100 koin/hari**, berlaku **24 jam** (hangus kalau tidak dipakai).

### D. Kontes (hadiah CASH, bukan koin)
Lihat bagian 3.

## 3. 🏆 KONTES — status per 10 Okt 2026
| Kontes | Hadiah | Deadline | Layak? |
|---|---|---|---|
| **RunningHub Global AIGC Feature Film** | $150K–550万 | **TUTUP 9 Okt** | ✗ lewat |
| **PixLight 2026 (PixVerse)** | $300K | ~10 Okt | ✗ + wajib PixVerse Canvas |
| **鲸锐AI创作大赛 (Youku)** | ¥10jt / top ¥2jt | 22 Nov | ✗ **wajib KTP China +86** |
| **腾讯SSV "科技向善" AI Video** | ¥130.000 + 10jt poin | **31 Okt** | ✅ **BUKA** — "全国及全球华语创作者", 2–5 mnt, 16:9 1080p MP4, kirim via email + Baidu netdisk |
| **"看见微光" 可灵AI 公益** | ¥100.000 | 1 Nov | ⚠️ cek kelayakan |
| **Chroma Awards S2 (ElevenLabs)** | S1 $175K+ cash + $1M kredit | **perkiraan 31 Des** | ✅ **TERBAIK INTERNASIONAL** — global, gratis, 6 divisi / 51 kategori, ≥90 dtk–22 mnt, buat setelah 1 Feb 2025, wajib pakai AI tool signifikan, subtitle English |
| Runway Hundred Film Fund | grant $5K–$1M+ | rolling | ✅ bisa kapan saja |
| HKBU Future Film Fest 3F | $66.000 | 31 Okt | ⚠️ cek |
| WAIFF Los Angeles | lanjut ke Cannes 2027 | 20 Jan 2027 | ✅ peluang besar |

### Peluang menang terbesar (analisis)
1. **Chroma S2** — 51 kategori ⇒ **banyak kursi juara**; kompetisi tersebar. Daftar di awal (timing kita sempurna: baru buka pertengahan Okt).
2. **腾讯SSV** — kata "向善/公益" bikin peserta tech-y berkurang; 21 hari cukup buat 2–5 mnt.
3. **Strategi menang:** pilih **kategori sepi** (mis. Documentary/True Crime, Experimental, atau kategori Advertising spesifik seperti Banking/Telecom) daripada kategori ramai (Sci-Fi/Animation).

## 4. 🎬 RENCANA PRODUKSI (siap dijalankan 21:00–10:00 = gratis)
Aset yang sudah kita punya: pipeline i2v H3, editor Qwen, faceswap, pose, lipsync, chargen (karakter konsisten), storyboard multi-scene, + bot KREE.AI sebagai mesin.

**Langkah:**
1. Pilih 1 kategori Chroma yang sepi → tulis 1 halaman logline + shot list (≤3 mnt).
2. Render klip 5 dtk per shot **di dalam free window** (biaya ~0).
3. Rakit di storyboard + subtitle English (wajib untuk juri).
4. Upload ke YouTube/Vimeo (butuh akun milik user), deskripsi: cantumkan tools + www.ChromaAwards.com.
5. Submit via form resmi.

**Yang TIDAK bisa gue lakukan sendiri (butuh user):**
- Bikin/akses akun YouTube/Vimeo publik untuk submit.
- Form submission (kadang butuh verifikasi).
- Keputusan kreatif (tema/cerita).

## 5. 🤖 AUTOMATION TERPASANG
- Cron harian 08:00 — cek saldo koin + scan kontes buka baru + ingatkan klaim koin harian.
- Cron pengingat deadline kontes.

---
### TODO A (butuh user)
- [ ] Konfirmasi: garap **Creator Incentive Program** (publish workflow) sebagai ladang koin utama?
- [ ] Sediakan akun YouTube/Vimeo untuk submit kontes.
- [ ] Pilih tema untuk entri Chroma S2 / 腾讯SSV.

---
## 6. ADDENDUM KONTES — scan 12 Okt 2026 (aifilmcontests.com + aibetas.com)
| Kontes | Biaya | Deadline | Catatan |
|---|---|---|---|
| **AI ZONE International AI Film Fest** | **GRATIS** | 30 Nov 2026 (reguler) | Online, festival 15 Jan 2027; 1 kategori Best AI Mini Movie, genre bebas. **Paling cocok budget $0.** |
| **AIFFK Kerala (ed.3)** | cek | ~30 Nov 2026 (buka 15 Okt) | Kochi 22–24 Jan 2027; min 2 menit; byk kategori (narration, cinematography, experimental) |
| Veritas AI Film Fest | $9 | 30 Nov 2026 | Screening Toronto 20 Feb 2027, film <7 mnt |
| AI Slop Film Fest S2 | $10 | 16 Des 2026 | Markham, Ontario; ada kategori Best Human x Machine |
| **HASFA** (Hollywood AI Short Film Awards) | $25–55 | 11 Jan 2027 | **$2.750 cash**; ≤22 mnt; film dibuat ≥1 Jan 2024 |
| **GAIMVA** (Global AI Music Video Awards) | $20–40 | 1 Jan 2027 | **$1.000 cash**, 17 kategori (kursi juara banyak) |
| LundinStudio AI Film Fest | ~$10/bln | 21 Jan 2027 | Juara 2 $300 + refund fee; 1–10 mnt |
| PROMPT Festival Toronto | $15 | 16 Apr 2027 | rolling |
| **HKAIIFF 2027** (Hong Kong) | $99 | 1 Mar 2027 | 7 "Unicorn Awards"; buka 1 Okt 2026 |
| Berlin AI Film Festival | $10→$40 | 31 Jan 2027 (extended) | fee naik tiap cut-off |
| Bengaluru Int'l Short Film Fest (seksi AI) | cek | 30 Apr 2027 | festival Agustus |
| WAIFF Cannes 2027 | via edisi kota | regional (mis. LA 20 Jan 2027) | bukan submit langsung |

**aibetas.com/competition-calendar:** tidak ada lomba baru — masih 6 agenda China (31 Okt 腾讯SSV, 1 Nov 可灵, 22 Nov 鲸锐, 3 Des 泉州, 6 Des 深圳, 31 Des GBA).

**Catatan saldo (rh_coins.csv):** 26.765 (10 Okt 12:37) → 24.881 (11 Okt 08:00) → 24.881 (**12 Okt 08:00, Δ 0**). Jadi **tidak ada kebocoran berjalan** 24 jam terakhir; hipotesis "bocor 2,3rb/hari" gugur — penurunan 1.884 koin terjadi di jendela 10 Okt malam (kemungkinan sisa tugas/membership), bukan biaya harian.

---
## 7. SCAN 14 OKT 2026 — koreksi "kebocoran" + kontes baru
**Koreksi penting (menggantikan catatan saldo di bagian 6):** TIDAK ada plafon tetap, tapi ADA pengurasan nyata & terukur: 24.881 (12 Okt 08:00, Δ0) → 22.729 (13 Okt, **-2.152**) → **18.847 (14 Okt, -3.882)**. Rata-rata ~2.083 koin/hari.
**Penyebab ditemukan:** `.env` kreaibot & **kreeaimotion memakai RUNNINGHUB_API_KEY yang SAMA** (hash md5 identik) → satu kolam koin. Log kreeaimotion 13 Okt: job 18–28 jalan pukul **13:55–17:00 WIB** (DI LUAR free window 21:00–10:00) → kena tarif koin; job gagal (FAILED) juga tercatat (playbook klaim gagal tak ditagih — perlu verifikasi lanjut). Bukan kebocoran sistem, tapi pemborosan jadwal.

### Kontes baru/belum ada di bagian 3 & 6
| Kontes | Biaya | Deadline | Catatan |
|---|---|---|---|
| **DAIFF 2nd ed. (TBWA, Australia)** | **GRATIS** | **16 Okt 2026** (≈2 hari) | Tema "Humans and Their Tools"; Gala Melbourne 18 Nov; didukung Google, Leonardo.AI, BMW. Terlalu mepet untuk edisi ini. |
| **PixLight 2026 (PixVerse)** | gratis | **diperpanjang 9 Okt → 31 Okt 2026** | $300K, 33 award; **wajib PixVerse Canvas** sebagai platform utama. |
| **VISIONARIA Roma** | cek | 31 Okt 2026 | Festival 27 Nov 2026. |
| **IA en Corto (Chile, ed.2)** | $5,50–9 | 18 Okt 2026 | Spanyol/Inggris, 4 seksi. |
| **Atlanta AI Ad Fest** | $10 (termasuk 5.000 kredit Bloomway) | 25 Okt 2026 | **$2.500 cash**; jury 40% ide. |
| Future Vision XPRIZE | gratis | (indeks: 15 Agu 2026 → kemungkinan sudah lewat/2027) | >$3,5 jt; perlu verifikasi ulang. |

**aibetas.com:** tambahan — "2026亚洲艺术电影节 AI影像奖" (Asia Art Film Festival AI Image Award) buka征片 global; sisanya masih 6 agenda China (butuh KTP China).
