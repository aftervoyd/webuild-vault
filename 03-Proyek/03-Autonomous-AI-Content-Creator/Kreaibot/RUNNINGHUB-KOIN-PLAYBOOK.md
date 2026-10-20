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
  | **MiniMax H3 (i2v / workflow RH)** | **±16,4 koin/detik** (video 5 dtk = **82 koin**; uji 14 Okt 08:37 WIB) |
  | AI App `otz` Pose Transfer | **±26,3 koin/detik** (16,4 dtk ≈ 431 koin) |
  | nightfunnels Wan2.2 Animate | ±25,9 koin/detik |
- 📌 **Klarifikasi promo "MiniMax H3 RH Enhanced gratis 13 jam/hari"**: berlaku **di rhTV / RHSTORY**
  (produk aplikasi RunningHub) — **BUKAN** di jalur API/workflow/AI App kita. Terbukti: render 5 dtk pada
  jam 08:37 WIB (di dalam jendela yang diklaim gratis) **tetap ditagih 82 koin**.
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

## 4. 🎬 RENCANA PRODUKSI (⚠️ BUKAN gratis — hitung koin dulu tiap render)
Aset yang sudah kita punya: pipeline i2v H3, editor Qwen, faceswap, pose, lipsync, chargen (karakter konsisten), storyboard multi-scene, + bot KREE.AI sebagai mesin.

**Langkah:**
1. Pilih 1 kategori Chroma yang sepi → tulis 1 halaman logline + shot list (≤3 mnt).
2. Render klip 5 dtk per shot — **berbayar koin** (±26 koin/detik ⇒ klip 5 dtk ≈ 130 koin).
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
**Penyebab ditemukan:** `.env` kreaibot & **kreeaimotion memakai RUNNINGHUB_API_KEY yang SAMA** (hash md5 identik) → satu kolam koin. Log kreeaimotion 13 Okt: job 18–28 jalan pukul **13:55–17:00 WIB** → kena tarif koin (normal; tarif berlaku 24 jam, bukan karena jam); job gagal (FAILED) juga tercatat (playbook klaim gagal tak ditagih — perlu verifikasi lanjut). Bukan kebocoran sistem, tapi pemborosan jadwal.

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

---
## 8. SCAN 15 OKT 2026 — pengurasan makin cepat + koreksi DAIFF + 6 kontes baru
### Saldo (rh_coins.csv, terverifikasi API)
22.729 (13 Okt) → 18.847 (14 Okt, −3.882) → **14.411 (15 Okt 08:00, −4.436)**.
3 hari: **−8.318** (rata 2.773/hari). Kecepatan terakhir 4.436/hari ⇒ **saldo habis ±18 Okt** (rata 3 hari ⇒ ±20 Okt). Membership refill berikutnya baru ±8 Nov ⇒ **RISIKO HABIS sebelum refill.**
### Penyebab terukur (bukan bocor)
Log `/var/log/kreeaimotion.log` 14 Okt **13:54–18:24 WIB**: 6 panggilan RunningHub AI App **2095689306085285890** (2× GANTI POSE ~26 koin/dtk + 3× Qwen-Edit PLUS + 4K) + 1 fallback `2003539764081008641`. Ditambah 2 job INFERHUB **GAGAL timeout 179–180 dtk** (job 32 & 33) yang lalu jatuh ke RunningHub ⇒ **bayar dobel**. `.env` kreaibot & kreeaimotion tetap **API key identik** (md5 `047e7ac6bb3cab4713afae5397c6c54b`) = satu kolam.
### ⚠️ Koreksi: DAIFF GUGUR TOTAL
FilmFreeway DAIFF: **"open to AUSTRALIAN-BASED applicants"** — bukan cuma mepet (16 Okt), tapi **tidak eligible** untuk kita. Coret dari daftar.
### Kontes baru (BUKA, global, tanpa KTP China) — belum ada di bagian 3/6/7
| Kontes | Biaya | Deadline | Catatan |
|---|---|---|---|
| **TAIFF — Türkiye Int'l AI Film Fest (ed.3)** | **GRATIS** (FilmFreeway) | **1 Nov 2026** | Istanbul, Atatürk Cultural Center, screening 7–9 Des. 2.000+ submission/100+ negara. Grand Prize Best AI Film + award craft (Director, Cinematographer, Editor, Composer, VFX). **TOP PICK baru.** |
| **TLVAIFF — Tel Aviv AI Film Fest (ed.1)** | **GRATIS** (tier regular) | **3 Nov 2026** | Cinematheque 10 Nov, bagian Tel Aviv AI Week. 5 kategori (Storytelling, Cross-Cultural, Visual Achievement). Maks 2 film/entrant. |
| **AI M0V1E Film Festival** | berbayar (tier) | 1 Nov reguler / **15 Nov late** | **Cash: $1.000 Best Feature · $700 Best Series · $500 Best Short** + distribusi di app M0V1E. Wajib bayar fee + akun m0v1e.ai + upload di sana. |
| **AI New York Awards (ed.1)** | $25–29 (naik per tier) | **15–22 Nov 2026** | NYC, screening. 8 kategori termasuk **Best AI Character Consistency** (= kekuatan pipeline kita) & Best Prompt & Workflow. |
| **New York AI Indie Awards** | $10 | **5 Nov 2026** | Manhattan 15 Nov, 8 award; genre bebas, dibuat ≥1 Jan 2025, subtitle English. |
| **Asian Independent Film Fest — AI Generated Film** | $20 | **10 Nov 2026** | Worldwide, India-based; seasonal → annual awards. |
### Yang hampir tutup (skip)
AI Filmfest Athens (reguler 15 Okt = hari ini, late 19 Okt €30, total €3.000) · Neuland Cinema Berlin (tutup 15 Okt hari ini) · Chroma S2 tetap 31 Des (masih terbaik).
### aibetas.com/competition-calendar
**Tidak ada lomba baru** — tetap 6 agenda China (31 Okt 腾讯SSV, 1 Nov 可灵, 22 Nov 鲸锐, 3 Des 泉州, 6 Des 深圳, 31 Des GBA). Hampir semua butuh KTP China.
### Aksi
1. Hentikan/diet jadwal kreeaimotion: hindari AI App 2095689306085285890 kecuali perlu; matikan fallback otomatis Inferhub→RunningHub pada job timeout (bayar dobel).
2. Klaim ±100 koin login harian (hangus 24 jam).
3. Prioritaskan **TAIFF (gratis, 1 Nov)** — pendaftaran gratis & banyak kursi award craft; Chroma S2 31 Des sebagai target utama.

## 9. SCAN 16 OKT 2026 — burnout melambat (−1.132/24 jam) + kontes baru
Saldo: **13.279 RH Coins** (Δ −1.132 vs 14.411). Rantai: 18.847 → 14.411 → 13.279 (rata −2.784/hari 2 hari terakhir).

### Kontes baru (sumber: aifc.news, diperbarui 14–16 Okt 2026)
| Kontes | Hadiah | Deadline | Catatan |
|---|---|---|---|
| **Artefact AI Film Festival × mk2** (Prancis) | **$15.000 cash** | 13 Jan 2027 | fee belum dipublikasi — top pick baru |
| **AI Film Award 2027 — 1 Billion Followers Summit (UAE)** | **$1.000.000 cash** | 20 Nov 2026 | ⚠️ wajib tool **Seedance** + 5–7 mnt satu cerita |
| **Chroma Awards S2** (koreksi angka) | **$430K+ pool** (bukan $175K) | 7 Jan 2027 | gratis via Devpost, kategori banyak |
| Hollywood AI Short Film Awards (AS) | $3.000 cash | 11 Jan 2027 | ≤22 mnt, berbayar |
| IA Play IFF Madrid (Spanyol) | $1.000 cash | 1 Jan 2027 | 100% AI, berbayar |
| AI ZONE International (online) | $500 cash | 30 Nov 2026 | **gratis** |
| AI Film Festival Africa / AIFFA (Madagaskar) | top-3 prizes | 31 Okt 2026 | **gratis** |
| WAIFF London (baru) | jalur ke Cannes | 17 Nov 2026 | berbayar bertingkat |
| Gossip Goblin x Showrunner | $20K, **gratis** | 15 Des 2026 | ❌ **wajib Showrunner Studio** — bukan toolchain kita |
| AI for Good Film Festival | undangan summit | 1 Mei 2027 | gratis, 1–10 mnt |

### Koreksi/peringatan
- **TLVAIFF Tel Aviv**: deadline reguler **15 Okt** (sudah lewat); fest 10 Nov. Jangan andalkan.
- **T-AIFF Türkiye** tidak sepenuhnya gratis: kategori internasional **$1** (nasional gratis), ≤20 mnt, maks 5 karya.
- **PixLight 2026** deadline 31 Okt, $300K, tapi **wajib PixVerse Canvas**.
- Jangan pernah menjadwalkan render ke malam dengan alasan "jam gratis" — **tarif koin 24 jam penuh** (Qwen-Edit ±50/gambar; motion ±26 koin/detik; H3 i2v ±16,4 koin/detik).

---
## 8. SCAN 19 OKT 2026 (08:00 WIB) — saldo kritis + kontes baru
**Saldo:** 7.040 RH Coins (**Δ -2.784** vs 18 Okt 9.824). Rantai: 18.847 → 14.411 → 13.279 → 12.188 → 9.824 → **7.040**. Rata-rata 3 hari terakhir ≈ **-2.400/hari** ⇒ kalau berlanjut, koin habis **±22 Okt** (refill membership baru **8 Nov** = defisit 13-17 hari). Belum ada bukti render besar hari ini; tren turun konsisten.
**Aksi:** rem koin — DILARANG render kecuali submit kontes gratis. Klaim ±100 koin login (hangus 24 jam).

### Kontes BARU (belum ada di bagian 3/6/7)
| Kontes | Biaya | Deadline | Catatan |
|---|---|---|---|
| **Artefact AI Film Festival 3rd ed. " (Dis)Connection" (Paris, mk2)** | **GRATIS** | **2 Des 2026** | **TOP PICK** — Grand Prize **€10.000** + potongan 30 dtk tayang 1 minggu di semua bioskop mk2. Peserta ed.2: 223 sutradara/52 negara. Global. |
| **AKOOL AI Film Challenge** | gratis (wajib pakai tool AKOOL) | 20 Des 2026 | Grand Prize **$50.000** — TAPI AKOOL harus dipakai signifikan ⇒ kita belum punya tool-nya (butuh akun+koin AKOOL). |
| Showrunner AI Film | cek | 15 Des 2026 | $20.000 |
| **T-AIFF Türkiye 3rd ed. (Istanbul, AKM)** | simbolis via FilmFreeway | **1 Nov 2026** (14 hari) | Gratis submit, worldwide, ≤20 mnt, **11 kategori** (banyak kursi juara), film dibuat ≥1 Jan 2025, belum tayang TV/online. Est. 4.000 submission. |
| AI M0V1E Film Festival | cek | 1 Nov 2026 | $1.000 Feature / $700 Series / $500 Short — **wajib upload ke m0v1e.ai**. |
| AI Filmfest Athens ("Myths Meet Machine") | cek | **19 Okt (HARI INI, lewat)** | €1.000/kategori — skip. |

**aibetas.com:** tidak ada agenda baru (masih 6 China: 31 Okt, 1 Nov, 22 Nov, 3 Des, 6 Des, 31 Des).

---
## 10. SCAN 20 OKT 2026 (08:00 WIB) — SALDO KRITIS + kontes baru
**Saldo:** **993 RH Coins** (Δ **-6.047** vs 19 Okt 7.040). Rantai: 18.847 → 14.411 → 13.279 → 12.188 → 9.824 → 7.040 → **993**. Refill membership 8 Nov ⇒ **defisit ±19 hari** kalau koin habis hari ini.
**Penyebab terukur (bukan bocor):** `/var/log/kreeaimotion.log` 19 Okt **00:34–23:37 WIB** — **29 job gambar** (job 77→98), **20 gagal**, app 2095689306085285890 (ganti baju/pose) + 2089183013887557633 (lapis wajah) + **video out_98.mp4 selesai 23:37**. Tarif berlaku 24 jam penuh ⇒ burn 6rb dalam 1 hari = jadwal kreeaimotion.
**Aksi:** STOP/rem semua render (kreeaibot + kreeaimotion). 993 koin ≈ 1 video 16 dtk (431) atau ~20 gambar Qwen-Edit (50/gambar). Tidak ada jam gratis.
### Kontes BARU (belum di bagian 3/6/7/8/9)
| Kontes | Biaya | Deadline | Catatan |
|---|---|---|---|
| **ElevenLabs "The Search — World's Catchiest Ad"** | GRATIS | **1 Nov 2026** (12 hari) | **$100.000 total, juara 1 $50.000**, 11 pemenang; iklan **15–45 dtk** brand fiktif + jingle **wajib dibuat di ElevenCreative**; global; pengumuman 10 Nov. TOP PICK cepat. |
| **Curious Refuge × Epidemic Sound Holiday Film** | GRATIS | **6 Des 2026** | **$7.500+ cash**; 2:00–6:00, tema Natal, wajib multi-shot hasil editan (1 klip mentah gugur); global (sumber: aifilmcontests.com). |
| **Florence AI Festival (ed.1, VIA/Roma)** | berbayar | 15 Des 2026 | 8 kategori (Horror/Animation/Doc/Narrative/Comedy/MV/Ads/New World), ≤20 mnt, 18+, wajib AI Statement 100–300 kata. |
| AI Film Fest Monaco | klaim gratis/31 Des | **ragu** | Halaman resmi `aifilmfest-monaco.com/submission` masih tulis deadline **25 Apr 2026** ⇒ klaim "$10K / 31 Des" **belum terverifikasi**, jangan diandalkan. |
- Kontes lama yang tetap relevan: **Artefact (gratis, 2 Des, cap 314 dtk)** · **Chroma S2 (buka 19 Okt–7 Jan, $430K+, gratis)** · T-AIFF Türkiye (1 Nov).
