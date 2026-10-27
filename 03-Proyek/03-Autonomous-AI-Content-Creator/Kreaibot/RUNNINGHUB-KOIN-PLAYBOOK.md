# RUNNINGHUB — PLAYBOOK KOIN & KONTES
> Disusun otomatis 10 Okt 2026, 02:45 WIB (sesi tidur user). Semua angka terverifikasi live.
> TIDAK memuat rahasia. Kredensial ada di `.env` (apiKey) & vault Hermes (login web).

---

## 0. STATUS AKUN (historis 10 Okt 03:00 WIB — ⚠️ angka di bawah BASI; status terkini lihat §8)
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

---
## 11. SCAN 21 OKT 2026 (08:00 WIB) — 🔴 SALDO HABIS TOTAL (0 KOIN)
**Saldo:** **0 RH Coins** (Δ **-993** vs 20 Okt). Wallet $0,01. Tugas jalan: 0.
Rantai penuh: 26.765 (10 Okt) → 18.847 → 14.411 → 13.279 → 12.188 → 9.824 → 7.040 → 993 → **0**.
**Bukti kegagalan nyata (bukan estimasi):** `/var/log/kreeaimotion.log` & DB `jobs` → error RunningHub
`{"code": 605, "msg": "NOT_ENOUGH_BALANCE"}`:
- job **104** (video, 20 Okt) → **605 NOT_ENOUGH_BALANCE**
- job **107** (21 Okt 00:01 WIB, gambar) → **605 NOT_ENOUGH_BALANCE**
- job 106 (gambar) masih `done`; job 103 & 105 motion selesai 20 Okt 13:55 & 15:05.
⇒ 20 Okt kira-kira: 8 job gambar (99–107an) + 2 video motion (103, 105) = menghabiskan 993 sisa koin.
**Konsekuensi:** semua render (kreaibot + kreeaimotion) **mustahil jalan** sampai koin diisi; refill membership baru **±8 Nov** ⇒ defisit **±18 hari**.
**Aset yang masih hidup:** kreeaimotion service `active` (siap terima order tapi render PASTI gagal 605) · kreaibot `active` · 0 proses render nyangkut.

### Kontes — hasil scan hari ini (aibetas, aifilmcontests, melies, screenweaver, huskistudio)
**TIDAK ADA kontes baru** yang layak & belum tercatat. Yang muncul di indeks sudah kita punya:
- AKOOL AI Film Challenge ($50K, 20 Des, wajib tool AKOOL) · Showrunner ($20K, 15 Des, wajib Showrunner Studio)
- Artefact Paris (gratis, €10K, 2 Des) · Berlin AIFF (31 Jan 2027) · AI ZONE (gratis, $500, 30 Nov) · Chroma S2 (7 Jan)
- Kandidat "baru" yang saya cek & **gugur**: **Reply AI Film Festival** (€8K + Venice) → *"no 2027 window published"*, edisi 2026 tutup 2 Jun ⇒ **belum bisa dilamar**. **Astana AIFF** ($450K grand) → deadline tidak terkonfirmasi, jangan diandalkan.
- `aibetas.com/competition-calendar` — masih 6 agenda China (butuh KTP China / +86) ⇒ tidak layak.

### Aksi 21 Okt (urutan wajib)
1. **Hentikan jualan/order di kreeaimotion** (tombol/maintenance) — user masih bisa bayar via Aulaa QRIS tapi render pasti gagal `605` ⇒ risiko komplain & refund. Bukan masalah harga, tapi kehabisan kolam koin.
2. **Klaim ±100 koin login harian** (hangus 24 jam) → cukup untuk ~2 gambar Qwen-Edit (±50/gambar). Video 16 dtk (431 koin) **di luar jangkauan**.
3. Jalur isi ulang tanpa bayar: **Program Insentif Kreator** (publish workflow `qwen-consistency-edit`, id 2108638842228461570 — tersisa aksi UI 1-klik, lihat `RUNNINGHUB-CREATOR-PROGRAM.md`) + **invite `baaxhjzz`** (500 koin/pasangan, dilarang farming).
4. Kontes: prioritas **ElevenLabs "The Search"** (gratis, 1 Nov, $100K) dan **Artefact Paris** (gratis, 2 Des, €10K) — keduanya nol koin RunningHub.
⚠️ **Tidak ada jam gratis.** Tarif koin berlaku 24 jam penuh. Hitung koin dulu sebelum render.

---
## 7. ADDENDUM KONTES — scan 22 Okt 2026 (aifilmcontests.com + aifc.news)
**Konteks saldo: RH Coins = 0** (job render gagal 605). Prioritas HANYA kontes GRATIS sampai koin terisi.
| Kontes | Biaya | Deadline | Hadiah | Catatan layak |
|---|---|---|---|---|
| **Gossip Goblin Competition** | **GRATIS** | 15 Des 2026 | **$20K** | 2–20 mnt, AI film, online — **BARU, potensi terbesar gratis** |
| **Cue Xmas '26 (Cue Film Fest / AFRO TV)** | **GRATIS** | 20 Nov 2026 | 4 kategori cash + tayang TV kabel nasional | Tema Natal, 2–6 mnt, 18+, wajib multi-shot (bukan 1 klip mentah) |
| **Cine Prague AI Film Festival 2026** | berbayar | 28 Nov 2026 | **$1.000 Grand Prix** | Global, ≤5 mnt, terima film AI & tradisional — BARU |
| **Chroma Awards** | GRATIS | ~7 Jan 2027 | **$430K+ pool** | Global, any AI tool — tetap terbaik |
| IA Play Int'l FF Madrid | berbayar | 1 Jan 2027 | $1K cash | 100% AI |
| AI Film Award 2027 (1 Billion Followers Summit, UAE) | fee TBA | 20 Nov 2026 | **$1M** | ⚠️ wajib tool Seedance → cek feasibility |
| AIFFA (Madagascar) | GRATIS | 31 Okt 2026 | Top 3 | Short/video, any AI tool |
| WAIFF London | £55–75 | 17 Nov 2026 | Jalur ke Cannes | ✗ **UK-only** — tidak eligible |
| PAIFF Prague | cek | 31 Okt 2026 | — | BARU, cek fee |

---

## 8. ADDENDUM KONTES + SALDO — scan 23 Okt 2026 (08:00 WIB)
**💰 SALDO PULIH: 13.881 RH Coins** (Δ **+13.881** vs 22 Okt yang **0**). Wallet $0,010. Tugas jalan: 0.
Rantai: 28.362 (10 Okt) → … → 0 (21–22 Okt) → **13.881 (23 Okt)**.
⚠️ Penyebab kenaikan **belum dikonfirmasi** (kemungkinan top-up / settlement insentif / pembelian) — bukan bukti renewal membership (jadwal renewal ±8 Nov). Verifikasi manual di `runninghub.ai/my-income`.
⇒ **Render kembali MUNGKIN**, tapi batasnya: gambar Qwen-Edit ±50 koin/gambar · motion ±26 koin/detik (16 dtk ≈ 431) ⇒ 13.881 koin ≈ 276 gambar ATAU ±32 video 16 dtk. **Tetap hitung koin sebelum render.**

### Kontes BARU yang layak (belum tercatat di §7)
| Kontes | Biaya | Deadline | Hadiah | Catatan layak |
|---|---|---|---|---|
| **Curious Refuge x Epidemic Sound — AI Holiday Film 2026** | **GRATIS** | **6 Des 2026** | **$7.500+ cash** | **Global, any AI tool**, short liburan AI penuh — hadiah cash gratis TERBESAR yang baru · terverifikasi 13 Sep |
| **Artefact AI Film Festival 3rd (Paris)** | **GRATIS** | 2 Des 2026 | **€10.000** Grand Prix + 3×€1.000 | Global, ≤314 dtk, **tanpa wajib tool**; wajib AI di pra+produksi+pasca · tayang 1 minggu di semua bioskop mk2 |
| **MetaMorph x TapNow — Winter** | **GRATIS** | 30 Des 2026 | £500 + 20.000 kredit | ⚠️ wajib ≥50% digenerate di TapNow canvas publik |
| **NEXMUSE AI Music Video Contest 2027** | cek | 28 Des 2026 | **₩21.000.000** (±$15K), 32 pemenang | Baru — musik video/idol; cek fee & hak cipta lagu |
| **Florence AI Festival (FAIF) — 1st** | berbayar | 15 Des 2026 | Best of Festival + 8 kategori | 8 kategori (Horror/Docu/Comedy/New World), cap 20 mnt, wajib AI Statement 100–300 kata |

### Kontes yang ditolak / sudah tutup (jangan diangkut lagi)
- ✗ **Future Vision XPRIZE** ($3,5jt; grand $2,5jt + $100K) — **TUTUP 15 Agu 2026**, pemenang sudah diumumkan 25 Sep 2026 (trailer AI "The Gifted"). Situsnya masih menyebut "largest film competition 2026" tapi **sudah lewat** — jangan alokasikan waktu.
- ✗ **WAIFF Africa (Abidjan)** 31 Des — hanya 10 negara Afrika Barat ⇒ tidak eligible.
- ✗ **TAIFF Türkiye** 1 Nov — gratis tapi **tanpa hadiah cash**; prioritas rendah.
- ✗ **AI Slop FF S2 / Berlin AIFF / LAAIMPA / WAICF Jaipur** — berbayar atau hadiah non-cash.

### Aksi 23 Okt (prioritas)
1. **Klaim ±100 koin login harian** (hangus 24 jam) — pakai ke 2 gambar Qwen-Edit.
2. **Publish workflow creator `qwen-consistency-edit`** (id 2108638842228461570) — aksi UI 1-klik, masih `$0,00`; jalur pendapatan koin jangka panjang.
3. Kontes: satu film pendek gratis bisa masuk **Artefact (2 Des) + Chroma S2 (31 Des) + Curious Refuge (6 Des)** sekaligus — nol koin RunningHub.
⚠️ **Tidak ada jam gratis.** Tarif 24 jam penuh; hitung koin dulu sebelum render.


---

## 12. SCAN 24 OKT 2026 (08:00 WIB) — pembakaran normal (-2.110) + kontes $1 JT baru
**SALDO: 11.771 RH Coins** (delta **-2.110** vs 23 Okt 13.881). Wallet $0,0100. Tugas jalan: 0.
Rantai: 0 (21-22 Okt) -> 13.881 (23) -> **11.771 (24)**. Laju bakar +/-2.110/24 jam -> **~5,5 hari** sisa (habis +/-29 Okt) tanpa pemasukan.
=> Kapasitas: 11.771 koin = +/-235 gambar Qwen-Edit ATAU +/-27 video 16 dtk (motion +/-26 koin/dtk).

### Kontes BARU (belum tercatat di bagian 3/6/7/8/11)
| Kontes | Biaya | Deadline | Hadiah | Catatan layak |
|---|---|---|---|---|
| **1 Billion Followers Summit - AI Film Award 2027 (Dubai)** | **GRATIS** | **20 Nov 2026** | **$1.000.000** grand prize (1 pemenang) | Global, 18+, 5-7 mnt, 16:9 1080p, subtitle Inggris. WAJIB >=70% digenerate dengan ByteDance Seedance. Shortlist 10 film 15 Des, finalis 5 film 25 Des, pemenang diumumkan di summit Dubai 8-10 Jan 2027. Backed BytePlus + TikTok |
| **FilmsAI Halloween Contest 2026** | GRATIS | **28 Okt 2026** (+/-4 hari) | $1.000 total (6 pemenang) | Tema Halloween, min 90 dtk, wajib akun FilmsAI + TANPA watermark generator. Livestream X 30 Okt-1 Nov. Cocok kalau ada short jadi |
| **Wandura Drama Challenge** | GRATIS | 31 Okt 2026 | **$10.000** (5K/3K/2K + $2K favorit) | WAJIB 100% dibuat di Wandura Drama/Cinema Studio + storyboard direview <=48 jam |
| **Tencent Cloud "AI CAN DO IT"** (Singapura) | GRATIS | 30 Okt 2026 | SGD 2.000 + kredit | Tool lock GenTube + Miora; BELUM jelas entrant luar Singapura boleh menang |
| **AIAF Atlanta AI Ad Fest** | $10 | 15 Nov 2026 (koreksi, bukan 25 Okt) | **$2.500 cash** + kredit | Spec ad Home Depot / Chick-fil-A; registran dapat 1.500 kredit Bloomway |

### Catatan penting
- **AI Film Fest Monaco** (klaim $10K / 31 Des) - masih BELUM terverifikasi (halaman resmi tulis deadline lama) => jangan diandalkan.
- **Qolaba** (tutup 18 Okt), **Higgsfield Global Film Festival** (tutup 16 Sep), **Reply AIFF** (tutup 2 Jun) => SUDAH LEWAT, jangan diangkut.
- Backend `web_extract` error (ddgs search-only) - verifikasi halaman resmi manual kalau mau submit.

### Aksi 24 Okt (prioritas)
1. **Klaim +/-100 koin login harian** (hangus 24 jam).
2. **Hitung koin dulu** sebelum render (TIDAK ADA jam gratis - tarif 24 jam penuh).
3. Kalau ada short jadi: **upload FilmsAI Halloween sebelum 28 Okt** (nol koin).
4. **Publish workflow creator `qwen-consistency-edit`** (id 2108638842228461570) - masih $0,00.

## 13. SCAN 25 OKT 2026 (08:01 WIB) — pembakaran melambat tajam (-256) + 3 kontes baru
**SALDO: 11.515 RH Coins** (delta **-256** vs 24 Okt 11.771). Wallet $0,0100. Tugas jalan: 0.
Rantai: 13.881 (23) -> 11.771 (24) -> **11.515 (25)**. Laju bakar turun drastis (+/-256/24 jam, vs +/-2.110 sehari sebelumnya).
=> Tanpa pemasukan & tanpa render baru: sisa +/-45 hari (habis +/-9 Des), BUKAN lagi 29 Okt.
=> Kapasitas: 11.515 koin = +/-230 gambar Qwen-Edit ATAU +/-26 video 16 dtk (motion +/-26 koin/dtk).
Catatan: laju bakar fluktuatif karena top-up (22 Okt 0 koin) & render manual; pakai angka harian, bukan rata-rata lama.

### Kontes BARU (belum tercatat di bagian 3/6/7/8/11/12)
| Kontes | Biaya | Deadline | Hadiah | Catatan layak |
|---|---|---|---|---|
| **Cue Xmas '26 (Cue Film Fest / AFRO TV)** | **GRATIS** | **20 Nov 2026** 23:59 ET | 4 hadiah CASH (Best Film/Image/Sound/AI Music Video) — **nominal BELUM diumumkan** (tergantung sponsor) | Open worldwide, 18+, film 2:00-6:00, natal, WAJIB multi-shot + edit manusia (1 klip mentah = gugur), 16:9 >=1080p, subtitle Inggris kalau bukan Inggris. Tayang live 12 Des di AFRO TV (Xfinity ch.1623) + NOW TV. Film harus dibuat >=1 Jan 2026. |
| **AI ZONE International AI Film Festival 2026 (edisi 2)** | GRATIS | **30 Nov 2026** | **$500** Grand Prize cash | Online penuh, **semua negara**, TANPA batasan tool AI. Syarat hadiah: film pemenang setuju dipublikasikan non-eksklusif di platform AI ZONE. Festival 15 Jan 2027. |
| **Cine Prague AI Film Festival (PAIFF)** | GRATIS/cek | **28 Nov 2026** | **$1.000** Grand Prix cash | Praha, short <=5 mnt, menerima AI-generated, AI-assisted, dan film tradisional. Finalis tayang di Kino Edison, pemenang 1 Des. |
| **AI M0V1E** | cek | 1 Nov 2026 | sampai **$1.000** | ✅ terkonfirmasi ada di daftar Nov; detail aturan belum diverifikasi |
| ~~WAIFF London~~ | - | 17 Nov | - | ✗ **HANYA kreator UK** (13+) -> tidak layak untuk kita |

### Koreksi/peringatan
- **Cue Xmas '26**: nominal hadiah = "to be announced", jangan dipakai sebagai target pendapatan; nilai sebenarnya = tayangan TV + seleksi 11 film (peluang masuk lebih besar).
- Backend `web_extract` masih error (ddgs search-only) -> verifikasi halaman resmi manual sebelum submit.

### Aksi 25 Okt (prioritas)
1. **Klaim +/-100 koin login harian** (hangus 24 jam).
2. **Hitung koin dulu** sebelum render. TIDAK ADA jam gratis - tarif 24 jam penuh (Qwen-Edit +/-50 koin/gambar, motion +/-26 koin/dtk).
3. **Publish workflow creator `qwen-consistency-edit`** (id 2108638842228461570) - masih $0,00 -> ini satu-satunya jalur pendapatan koin nyata.
4. Kontes gratis prioritas: **FiLM AI Halloween (28 Okt, +/-3 hari)** lalu **Cue Xmas '26 (20 Nov)**.

## 14. SCAN 26 OKT 2026 (08:00 WIB) — pembakaran tetap pelan (-170) + KONTES $1 JUTA bisa diakses
**SALDO: 11.345 RH Coins** (delta **-170** vs 25 Okt 11.515). Wallet $0,0100. Tugas jalan: 0.
Rantai: 13.881 (23) -> 11.771 (24) -> 11.515 (25) -> **11.345 (26)**. Laju bakar +/-170/24 jam (normal, bukan krisis).
=> Tanpa render baru: sisa +/-66 hari. Kapasitas: +/-226 gambar Qwen-Edit ATAU +/-26 video 16 dtk.

### Kontes BARU (belum tercatat di bagian 3/6/7/8/11/12/13)
| Kontes | Biaya | Deadline | Hadiah | Layak? |
|---|---|---|---|---|
| **AI Film Award 2027 — 1 Billion Followers Summit (Dubai, TikTok/BytePlus)** | **GRATIS** | **20 Nov 2026** | **$1.000.000 cash** (1 pemenang) | ✅ **PALING BESAR & GLOBAL** — 18+, film 5-7 mnt, 16:9 1080p MOV/MP4, bahasa apa pun + subtitle Inggris, tema (Society/Truth/Humans & AI/Climate/Human Relationships), **WAJIB >=70% dihasilkan Seedance**. Top10 + voting publik 15 Des, Top5 25 Des, finalis tayang Dubai 8-10 Jan 2027, bayar via transfer bank <=60 hari. |
| **Gossip Goblin x Showrunner (Fable)** | GRATIS | 15 Des 2026 | **$20K** pool | ✗ **terkunci Showrunner Studio** (film wajib dibuat di sana, mulai dari kursi Ripper Doc) -> tidak pakai pipeline kita |
| **Greenlight — Cascade x BytePlus x Seedance** | GRATIS (slot terbatas) | 15 Des 2026 | **$100K pool** (4 pemenang; ±$65K cash + 1,5 jt kredit Cascade) | ✗ wajib pakai **Cascade Studio** |
| **AI Film Festival Africa (AIFFA)** | GRATIS | 31 Okt 2026 | Top-3 (non-cash) | ⚠️ terlalu mepet |
| **Gossip Goblin / GAIMVA / Hollywood AI Short Film Awards / IA Play Madrid / Artefact x mk2 / LundinStudio / Jaipur IFF** | berbayar | Des 2026-Jan 2027 | $300-$15K | ⚠️ berbayar, prioritas rendah |

### KOREKSI PENTING
- **Chroma Awards S2**: deadline terkonfirmasi **7 Jan 2027** (sebelumnya "perkiraan 31 Des"), hadiah **$450K cash**, gratis, via Devpost -> jalur terbaik setelah $1M Seedance.
- **RunningHub PUNYA Seedance 2.0 global** (`seedance-2.0-global/multimodal-video`, token-based, ±$6,3-7 per 1 juta token; ada juga varian fast `*/multimodal-video-rc`). Artinya syarat ">=70% Seedance" pada kontes $1 juta **secara teknis BISA dipenuhi lewat akun kita**. ⚠️ Biaya token untuk 5-7 mnt 1080p **belum terverifikasi** -> WAJIB ukur dulu 1 klip pendek (cek remainCoins sebelum vs sesudah) sebelum komit produksi.
- **AI M0V1E**: $1.000 Best AI Feature (wajib 40-90 mnt), $700 Best AI Series, $500 Best AI Short; deadline 1 Nov; **wajib juga upload ke m0v1e.ai** kalau lewat FilmFreeway.
- WAIFF London tetap **hanya kreator UK** -> skip.
- Backend `web_extract` masih mati (ddgs search-only) -> pakai `curl` + strip HTML untuk baca halaman resmi.

### Aksi 26 Okt (prioritas)
1. **Klaim +/-100 koin login harian** (hangus 24 jam).
2. **Hitung koin dulu** sebelum render. TIDAK ADA jam gratis - tarif 24 jam penuh (Qwen-Edit +/-50 koin/gambar, motion +/-26 koin/dtk, video 16 dtk +/-431 koin).
3. **Publish workflow creator `qwen-consistency-edit`** (id 2108638842228461570) - masih $0,00 -> satu-satunya jalur pendapatan koin nyata.
4. **Uji biaya Seedance 1 klip (5 dtk)** kalau mau serius ke AI Film Award 2027 ($1 juta, 20 Nov) - tanpa angka biaya, jangan mulai produksi 6 menit.

## 15. SCAN 27 OKT 2026 (08:00 WIB) — pembakaran TINGGI (-2.897) = uji workflow, bukan kebocoran
**SALDO: 8.448 RH Coins** (delta **-2.897** vs 26 Okt 11.345). Wallet $0,0100. Tugas jalan: 0.
Rantai: 13.881 (23) -> 11.771 (24) -> 11.515 (25) -> 11.345 (26) -> **8.448 (27)**.
=> Laju 24 jam ini naik tajam (2.897 vs 170 sehari sebelumnya). Tanpa render baru: sisa +/-29 hari.

### Penyebab terukur (bukan bocor)
Semua task RunningHub terpantau 26 Okt (dari `work/poll_*.py` + `data/uji_wf_favorit/`):
- Uji **workflow favorit** (`uji_wf_favorit.py`): WF1_nightfunnels (id **2042526099766251522**) & WF2_hifidelity10s (id **2106585458498420737**) -> `WF1_nightfunnels_default.mp4` (16:55), `WF2_hififi_user.mp4` (17:33).
- Seri **LAMA pose-transfer** (task 2114634612022272002, 2114642576758108162, 2114650563212038146, 2114655582170734594, 2114656960087683073, 2114657298677063681, 2114703142839218178, 2114711121051340801, 2114711799559712770) -> `C_photoreal*.mp4` (18:04-05), `LAMA_pose_transfer_revived.mp4` (21:11), `LAMA_userbaru_1DMY_10s.mp4` (21:42), `LAMA_userbaru_1DMY_full.mp4` (21:50).
- Job bot kreeaimotion **132** (Kling Motion 720x1280 15 dtk): percobaan 1 **GAGAL GPU OOM (WanVideoSampler)**, percobaan 2 sukses -> `out_132.mp4` (18:10). Retry = bayar 2x GPU.
=> Kesimpulan: -2.897 = **belasan run workflow/pose-transfer + 1 retry OOM**. Tarif berlaku 24 jam penuh; TIDAK ADA jam gratis.

### Kontes (scan 27 Okt; aifilmcontests.com — aibetas.com masih 6 agenda China/wajib KTP)
| Kontes | Biaya | Deadline | Hadiah | Status |
|---|---|---|---|---|
| **AKOOL AI Film Challenge** (detail terverifikasi 25 Okt) | gratis (wajib tool AKOOL) | 20 Des 2026 | pool **$500.000** Creator Rewards: grand $50K, 2 $25K, 3 $15K, 10 finalis $2,5K, +$100/entry premium | ✅ terverifikasi - tapi terkunci tool AKOOL |
| **Cannes Film Awards 2027 — kategori AI perdana** | tier FilmFreeway | **21 Jan 2027** | $1K+ cash + $25K+ partner/promosi, laurel Cannes 25-27 Jun 2027 | ✅ **BARU** — internasional, semua tool AI boleh |
| **Runway Hundred Film Fund** | **GRATIS** | rolling (66 hari ke 31 Des) | **$5K-$1M+ per proyek** + sampai $2M kredit | ✅ **AKSI NYATA SEKARANG** (keputusan +/-14 hari, wajib pakai Runway) |
| Gossip Goblin x Showrunner | gratis | 15 Des | $20K | ✗ wajib Showrunner Studio |
| KIAFF Kerala 2027 | cek | 15 Feb 2027 (buka 15 Jan) | non-cash | belum bisa dilamar |
| AI for Good FF 2027 (ITU/UN Geneva) | cek | 1 Mei 2027 (buka 15 Jan) | non-cash, panggung PBB | belum bisa dilamar |
| Bengaluru BISFF "Machine Made Movies" | FilmFreeway | 30 Apr 2027 | non-cash, kualifikasi Oscar | belum bisa dilamar |
Prioritas tetap: **1 Billion AI Film Award ($1 juta, gratis, 20 Nov, wajib >=70% Seedance)** & **Chroma S2 ($450K, 7 Jan, gratis)**.

### Aksi 27 Okt (prioritas)
1. **Klaim +/-100 koin login harian** (hangus 24 jam) -> cukup +/-2 gambar Qwen-Edit.
2. **Rem uji-coba workflow**: batasi `uji_wf_favorit.py`/pose-transfer berulang; matikan retry otomatis job OOM (bayar 2x).
3. **Publish workflow creator `qwen-consistency-edit`** (id 2108638842228461570) - masih $0,00, satu-satunya jalur pendapatan koin.
4. Kontes gratis tanpa koin RH: **Runway Hundred Film Fund (rolling)** + **Chroma S2 (7 Jan)** + **Cue Xmas (20 Nov)**.
WARNING: hitung koin dulu sebelum render. Tarif nyata: gambar Qwen-Edit +/-50 koin/gambar, motion +/-26 koin/detik (16 dtk = 431 koin).
