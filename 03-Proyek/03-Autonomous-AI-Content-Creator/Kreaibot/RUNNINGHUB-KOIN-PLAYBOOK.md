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
## 16. SCAN 28 OKT 2026 (08:00 WIB) — SALDO 5.831, burn tinggi 2 hari berturut = uji render, bukan bocor
**SALDO: 5.831 RH Coins** (delta **-2.617** vs 27 Okt 8.448). Wallet $0,0100. Tugas jalan: 0.
Rantai: 11.771 (24) -> 11.515 (25) -> 11.345 (26) -> 8.448 (27) -> **5.831 (28)**.
Rata-rata burn 3 hari = **+/-1.895/hari** => kalau diteruskan, saldo habis **+/-31 Okt (3 hari lagi)**. KRITIS.

### Penyebab terukur (log kreeaimotion + sqlite + data/)
- **7 job gambar** bot kreeaimotion (133,134,135 gagal,136,138,139,dll) @ +/-50 koin = **+/-350**.
- **3 job motion 15 dtk** (137, 140, 141). Job **141 retry otomatis**: percobaan 1 **GPU OOM (WanVideoSampler)**, percobaan 2 sukses => **bayar 2x**. 15 dtk x +/-26 koin = +/-390/job => **+/-1.560**.
- **Uji workflow favorit lagi**: MT_WanAnimate_0.mp4 (04:02), MT_VACE_0.mp4 (04:04), LAMA_resep_asli.mp4 (17:19) => **+/-700-900**.
=> Total +/-2.610, cocok dengan delta. TIDAK ADA kebocoran.
AKSI WAJIB: matikan retry otomatis job motion untuk kasus GPU OOM (retry OOM = koin hangus 2x).

### Kontes — scan 28 Okt (aifilmcontests.com/contests/new + aifc.news)
| Kontes | Biaya | Deadline | Hadiah | Status |
|---|---|---|---|---|
| **SVAIFF Korea 2026** | GRATIS | **25 Nov 2026** | pool **KRW 30 jt (+/-$21.600)**, kategori narrative/animation/documentary | BARU — tool AI bebas, internasional |
| **NEXMUSE AI Music Video 2027** | GRATIS | 28 Des 2026 | KRW 21 jt (+/-$15.100), **32 pemenang** | BARU — cocok dengan mesin motion kita |
| Greenlight Cascade x BytePlus Seedance | gratis (wajib Cascade) | 15 Des | $65K + 1,5 jt kredit | terkunci tool |
| Wandura Drama Challenge Ep.1 | gratis (wajib Wandura) | 31 Okt | $10K | terkunci tool, 3 hari |
| AIFFA Madagascar | gratis | 31 Okt | top 3 | 3 hari, non-cash |
| WAIFF London | berbayar tier | 17 Nov | jalur ke Cannes | cek |
| 1 Billion AI Film Award 2027 | gratis-ish | 20 Nov | **$1 juta** | prioritas #1 (wajib >=70% Seedance) |
| PixLight 2026 | gratis (wajib PixVerse) | 31 Okt | $300K | terkunci tool |
| AI Toronto Genre Awards 2027 | - | 22 Mei 2027 | laurel/prize | baru, cash belum jelas |
| Milan AI Festival 1st | - | 15 Feb 2027 | trofi, non-cash | baru |

### Aksi 28 Okt (prioritas)
1. **STOP uji render** — saldo cuma cukup +/-3 hari kalau burn tetap. Matikan retry OOM job motion.
2. **Klaim +/-100 koin login harian** (hangus 24 jam) — cukup 2 gambar Qwen-Edit.
3. **Daftar SVAIFF Korea 2026 (gratis, 25 Nov)** + **NEXMUSE Music Video (gratis, 28 Des)** — cash nyata, tool bebas, NEXMUSE pas pipeline motion.
4. **Publish workflow creator qwen-consistency-edit** (id 2108638842228461570) — masih $0,00; satu-satunya jalur koin masuk.
WARNING: tidak ada jam gratis. Tarif: gambar Qwen-Edit +/-50 koin, motion +/-26 koin/detik (16 dtk = 431 koin).

## 17. SCAN 30 OKT 2026 (08:00 WIB) — SALDO 1.999 (SISA ±1 HARI) + Artefact Paris €10K
**SALDO: 1.999 RH Coins** (delta **-3.832** vs 28 Okt 5.831; laporan 29 Okt gagal — HTTP 404 model, jadi ini delta 48 jam). Wallet $0,0100. Tugas jalan: 0.
Rantai: 11.345 (26) -> 8.448 (27) -> 5.831 (28) -> **1.999 (30)**. Rata-rata ±1.916/hari => **habis ±31 Okt–1 Nov**.
Kapasitas sisa: ±40 gambar Qwen-Edit ATAU **±4 video 16 dtk** (motion ±26 koin/dtk, 20 dtk ±520).

### Penyebab terukur (bukan bocor)
- **Uji workflow favorit lagi** (`data/uji_wf_favorit/`): **93 PNG baru + 2 MP4** (LAMA_native_新V6, V10_uji_0) sejak 28 Okt 08:00 => porsi terbesar.
- Bot kreeaimotion: job **143** (t15, 15 dtk), **145** (t20, 20 dtk), **147** (t20, 20 dtk) + gambar 144/146.
- Job **141** (27 Okt) gagal `ServerDisconnectedError` setelah 2.010 dtk -> kemungkinan retry = bayar 2x.
=> Uji eksperimen, bukan kebocoran. Rem total sampai ada koin masuk.

### Kontes — scan 30 Okt (aifilmcontests.com)
| Kontes | Biaya | Deadline | Hadiah | Status |
|---|---|---|---|---|
| **Artefact AI Film Festival 2026 (Paris, ed.3 "(Dis)Connection", x mk2)** | gratis* | **2 Des 2026** (+33 hari) | **€10.000 Grand Prix** + potongan 30 dtk tayang seminggu di semua bioskop mk2 | ✅ **BARU** — global, short **maks 314 dtk (±5m14s)**, WAJIB pakai generative AI di tiap tahap (pra/produksi/pasca). Juri Nakache & Toledano. *cek fee di artefact-ai-film-festival.com |
| **TAIFF Istanbul (ed.3)** | gratis | 1 Nov 2026 | Grand Prize Best AI Film + craft awards | ⚠️ 2 hari, skip |
| **AI ZONE (30 Nov) / Cine Prague (28 Nov) / Cue Xmas (20 Nov)** | gratis | lihat §13 | $500 / $1.000 / cash TBA | sudah tercatat |
| **AKOOL $50K (20 Des)** | wajib AKOOL | 20 Des | $500K pool | terkunci tool |
| **Berlin AI Film Festival** | cek | 31 Des 2026 | cek | baru, belum terverifikasi |
| **WAICF India** | cek | cek | kategori Feature/Short/Micro | baru, data belum lengkap |
- Astana AAIFF **tutup 7 Sep 2026** (8.067 film, 125 negara) -> lewat, jangan diangkut.
- Jeju Global AI Film Contest 2026 -> **sudah selesai** (pemenang diumumkan) -> lewat.
- Prioritas tetap: **1 Billion AI Film Award ($1 jt, 20 Nov, wajib ≥70% Seedance)** & **Chroma S2 ($450K, 7 Jan 2027)**.

### Aksi 30 Okt (prioritas)
1. **STOP semua uji render/uji workflow** — sisa ±1 hari. Tidak ada jam gratis.
2. **Klaim ±100 koin login harian** (hangus 24 jam).
3. **Publish workflow creator `qwen-consistency-edit`** (id 2108638842228461570) — masih $0,00; satu-satunya jalur koin masuk.
4. Siapkan **Artefact Paris (2 Des, €10K, ≤314 dtk)** sebagai target produksi berikutnya — tapi **jangan render sebelum koin diisi**.
WARNING: tarif nyata 24 jam — gambar Qwen-Edit ±50 koin, motion ±26 koin/detik (16 dtk ≈ 431, 20 dtk ≈ 520).

## 18. SCAN 1 NOV 2026 (08:01 WIB) — 🔴 SALDO 0 KOIN (HABIS TOTAL)
**SALDO: 0 RH Coins** (delta **-604** vs 31 Okt 604). Wallet $0,0100. Tugas jalan: 0.
Rantai: 11.345 (26) -> 8.448 (27) -> 5.831 (28) -> 1.999 (30) -> 604 (31) -> **0 (1 Nov)**.
=> Kapasitas produksi = **NOL**. Tidak bisa render apa pun sampai koin masuk. Burn 24 jam terakhir -604 (uji kecil / sisa terpakai).

### Kontes — scan 1 Nov (aifilmcontests.com/contests/new + topics closing Dec)
Tidak ada kontes BARU yang layak (hadiah cash nyata + tool bebas + deadline jauh):
| Kontes | Biaya | Deadline | Hadiah | Status |
|---|---|---|---|---|
| **NEXTALE Award** | gratis | 14 Des 2026 | $3.000 pool + 100% revenue 6 bln | BARU tapi wajib **serial 20+ episode** di NEXTALE Studio -> di luar kapasitas |
| **Turquoise Ankara (Turkuaz)** | gratis | 10 Des 2026 | **NON-CASH** (laurel+trofi) | BARU, skip (tidak ada uang) |
| **Twin Rivers AI FF 2027** | berbayar | 8 Mar 2027 | 20% net entry fee saja | BARU, skip |
| WAICF Jaipur / JIFF | $55-$100 | 5 Des 2026 | "s/d INR 25 lakh tergantung sponsor" | berbayar, tidak pasti |
| Florence AI Festival | tier FilmFreeway | 15 Des 2026 | cek | timeline kontradiktif di rules -> hati-hati |
| KACF Korea | gratis | 31 Okt (tutup) | layar bioskop | lewat |
Prioritas tetap (tidak butuh koin RH): **1 Billion AI Film Award ($1 jt, 20 Nov, wajib >=70% Seedance)** & **Chroma S2 ($450K, 7 Jan 2027)** & **Artefact Paris (EUR10K, 2 Des)**.

### Aksi 1 Nov (urutan wajib)
1. **Isi koin**: klaim login harian (+/-100, hangus 24 jam) -> cukup +/-2 gambar Qwen-Edit saja. Kalau mau produksi: **top-up / invite `baaxhjzz` / publish workflow creator** — bukan render.
2. **Publish workflow creator `qwen-consistency-edit`** (id 2108638842228461570) — masih $0,00; satu-satunya jalur koin masuk tanpa bayar.
3. **Naskah/storyboard dulu** (nol koin) untuk Artefact + AKOOL; render hanya setelah koin terisi.
WARNING: TIDAK ADA jam gratis. Tarif nyata 24 jam: gambar Qwen-Edit +/-50 koin, motion +/-26 koin/dtk (16 dtk +/-431, 20 dtk +/-520).

## 19. SCAN 3 NOV 2026 (08:01 WIB) - saldo 0, delta -77 (koin login 2 Nov HANGUS)
**SALDO: 0 RH Coins** (delta **-77** vs cek terakhir 77). Wallet $0,0100. Tugas jalan: 0.
Rantai: 604 (31 Okt) -> 0 (1 Nov) -> 77 (2 Nov, klaim login) -> **0 (3 Nov)**.
=> Bukti keras aturan 24 jam: 77 koin tidak dipakai sehari = hangus. 77 pun < 2 gambar Qwen-Edit (+/-50/gambar).

### Kontes - scan 3 Nov (aifc.news, aifilmcontests.com, adarena, aibetas)
**Tidak ada kontes BARU yang layak.** Item "baru" (added 21-27 Okt) semuanya sudah dievaluasi:
- MetaMorph AI Film Award 2027 (UK, 15 Mei 2027) = hadiah kredit TapNow, BERBAYAR -> skip
- Sin Camara 2027 (Spanyol, 5 Mei 2027) = wajib bahasa Spanyol -> skip
- PROMPT Festival Toronto (16 Apr 2027, berbayar, non-cash) / AI Slop FF (16 Des, non-cash, berbayar) / GAIMVA (1 Jan, berbayar, non-cash) -> skip
- LundinStudio (21 Jan 2027, $300, berbayar) -> skip
NOTE: status **Curious Refuge x Epidemic Sound Holiday ($7.500+, 6 Des)** KONTRADIKTIF antar halaman aifilmcontests (halaman kontes: buka, submit 15 Okt; halaman topik: "belum diumumkan") -> verifikasi ke curiousrefuge.com sebelum dijadikan andalan.
Koreksi kecil: aifc.news mencantumkan **Artefact x mk2 (Prancis) 13 Jan 2027, $15K, "call opens"** - beda dari catatan lama (2 Des, EUR10K). Cek ulang saat call resmi buka.

### Aksi 3 Nov (prioritas)
1. **Publish workflow creator `qwen-consistency-edit`** (id 2108638842228461570) - masih $0,00, satu-satunya jalur koin masuk tanpa bayar. Ini yang belum pernah dieksekusi.
2. Klaim login harian (+/-100) HANYA kalau hari itu langsung dipakai render 1 gambar; kalau tidak, hangus (terbukti hari ini).
3. Naskah/storyboard (nol koin) untuk AKOOL (20 Des) / 1 Billion (20 Nov) / Cue Xmas (20 Nov).
WARNING: TIDAK ADA jam gratis. Tarif 24 jam: Qwen-Edit +/-50 koin/gambar, motion +/-26 koin/dtk (16 dtk +/-431).

## 20. SCAN 4 NOV 2026 (08:01 WIB) — saldo 0, delta 0 (stabil) + 2 kontradiksi LAMA terpecahkan
**SALDO: 0 RH Coins** (delta **+0** vs 3 Nov 0). Wallet $0,0100. Tugas jalan: 0.
Rantai: 604 -> 0 -> 77 -> 0 -> **0**. Tidak ada koin masuk; tidak ada render.

### Resolusi kontradiksi (diverifikasi aifilmcontests.com, listing "checked daily")
- **Curious Refuge x Epidemic Sound Holiday**: **BUKA**, deadline **6 Des 2026**, **$7.500+ cash**, gratis, short film/contest -> ✅ LAYAK (bukan "belum diumumkan").
- **Artefact AI Film Festival ed.3 "(Dis)Connection" (Paris, x mk2)**: deadline **2 Des 2026** (BUKAN 13 Jan 2027), hadiah **€10.000 Grand Prix** + tayang 30 dtk di semua bioskop mk2. Maks **314 dtk**, wajib GenAI di pra/produksi/pasca. -> catatan "13 Jan / $15K" = SALAH.

### Catatan kontes
- **1 Billion AI Film Award ($1 jt, 20 Nov)** tetap target terbesar; diverifikasi ulang: 5-7 mnt, 16:9 1080p MOV/MP4, subtitle EN, **>=70% Seedance**. RunningHub punya Seedance 2.0/2.5 (token-based) => syarat teknis terpenuhi, tapi **wallet $0,01 -> mustahil render 5-7 mnt**.
- **Jingrui AI Creation Contest (GASP)** di direktori = $1 jt, 5-7 mnt, Seedance, 20 Nov -> kemungkinan **arm internasional dari 鲸锐 (Jingrui)** yang dulu ditandai "wajib KTP China". Perlu dicek: kalau benar global, ini duplikat jalur $1 jt (bukan peluang kedua).
- Tidak ada kontes BARU lain: SVAIFF Korea (25 Nov, 30 jt KRW), Cine Prague ($1K, 28 Nov), AI ZONE ($500, 30 Nov), Florence FAIF (15 Des), NEXTALE (14 Des) sudah tercatat.

### Aksi 4 Nov (prioritas)
1. **Publish workflow `qwen-consistency-edit`** (id 2108638842228461570) — masih $0,00; hari ke-3 belum dieksekusi; satu-satunya jalur koin tanpa bayar.
2. Klaim +/-100 koin login HANYA kalau dipakai hari itu (hangus 24 jam, terbukti 2 Nov).
3. Kalau mau serius ke kontes: **Artefact (2 Des, <=314 dtk)** lebih murah diproduksi daripada 1 Billion (5-7 mnt) — tapi tetap nol render sampai koin/wallet diisi.
WARNING: TIDAK ADA jam gratis. Qwen-Edit +/-50 koin/gambar, motion +/-26 koin/dtk (16 dtk +/-431).

## 21. SCAN 5 NOV 2026 (08:00 WIB) — koin login masuk (+100), kontes baru: TIDAK ADA
**SALDO: 100 RH Coins** (delta **+100** vs 4 Nov 0). Wallet $0,0100. Tugas jalan: 0.
Rantai: 604 → 0 → 77 → 0 → **100** (bonus login harian berhasil diklaim; hangus 24 jam = 6 Nov 08:00).
Kapasitas hari ini: **tepat 2 gambar Qwen-Edit (±50/gambar)**. Motion mustahil (±26 koin/dtk → 16 dtk = ±431).

### Kontes — scan aifilmcontests.com (home, /contests/new, /contests/free, /prize/cash-prizes), aibetas, gasptv
**Tidak ada kontes BARU yang layak.** Yang terlihat "baru" di direktori:
| Item | Verdict |
|---|---|
| SVAIFF Korea 2026 (Seoul, 17 Des) | sudah tercatat. Verifikasi ulang: **GRATIS, tanpa batas kewarganegaraan**, deadline **25 Nov 14:59 UTC**, ≤20 mnt, **KRW 30 jt** (~$21K), 19 juara / 12 kategori + 31 Encouragement. Jalur ke final Silicon Valley Jan 2027. Kandidat terkuat setelah Artefact. |
| CSFCCA AI Film Festival Winter | berbayar $22–28, **cash tidak dijamin** → skip |
| AI for the Future COP31 | NON-CASH (screening UN) → skip |
| Veritas AIFF (Kanada, 30 Nov) | showcase 16 film, non-cash → skip |
| Future Vision XPRIZE ($3,5 jt) | **TUTUP 15 Agu 2026** → lewat |
| LifeArt AI Global | deadline Agu/Sep 2026 → lewat |
Prioritas cash tanpa syarat tool tetap: **Artefact Paris €10K (2 Des, ≤314 dtk)** > **1 Billion $1 jt (20 Nov, ≥70% Seedance, wallet $0,01 = mustahil)** > **Chroma S2 (7 Jan 2027)** > **Curious Refuge Holiday $7.500+ (6 Des, gratis)** > **Cue Film Fest Xmas (20 Nov, gratis)** > **AI ZONE $500 (30 Nov, gratis)**.

### Aksi 5 Nov
1. **PAKAI 100 koin hari ini** — hangus 6 Nov 08:00. Pakai untuk **2 keyframe Qwen-Edit** naskah Artefact (maks 314 dtk → cukup 1 setting + 1 karakter). Jangan simpan.
2. **Publish workflow `qwen-consistency-edit`** (id 2108638842228461570) — hari ke-4 belum dieksekusi, masih $0,00. Satu-satunya jalur koin tanpa bayar (creator reward).
3. Naskah Artefact "(Dis)Connection" (nol koin) — 2 Des makin dekat.
WARNING: TIDAK ADA jam gratis. Qwen-Edit ±50 koin/gambar, motion ±26 koin/dtk (16 dtk ±431).


### §3b. TEMUAN 6 NOV 2026 — dua kontes GRATIS baru (deadline 20 Nov, tinggal 14 hari)
| Kontes | Hadiah | Deadline | Syarat kunci |
|---|---|---|---|
| **1 Billion AI Film Award 2027** (Dubai, TikTok+BytePlus) | **USD 1.000.000** (1 pemenang) | **20 Nov 2026** | GRATIS, 18+, global. Film 5-7 mnt, 16:9 1080p, subtitle Inggris, 5 tema tetap. **>=70% WAJIB Dreamina Seedance** -> pipeline Qwen/MiniMax kita TIDAK memenuhi. Top10 vote 15 Des, Top5 25 Des, final Dubai 8-10 Jan 2027. |
| **Cue Xmas 26** (AFRO TV) | 4 hadiah cash (Best Film/Image/Sound/Music Video) + tayang TV kabel nasional | **20 Nov 2026** | **GRATIS**, 18+, tema Natal, 2-6 mnt, short film ATAU AI music video. Finalis 10, festival live 12 Des. |
- Cine Prague: Grand Prix USD 1.000 tapi **fee USD 50 + wajib hadir di Praha** untuk hadiah -> lewati.
- Catatan: 1B Award = tool-locked (Seedance). Cue Xmas = bebas tool -> satu-satunya yang cocok pipeline kita.

## 22. SCAN 7 NOV 2026 (08:00) — saldo 0 (delta 0), koin login BELUM masuk + kontes GRATIS baru: M.AI Cagliari
**SALDO: 0 RH Coins** (delta **0** vs 6 Nov). Wallet $0,0100. Tugas jalan: 0. Rantai: 604 → 0 → 77 → 0 → 100 → 0 → **0**.
Berbeda dari 5 Nov: bonus login hari ini **belum dikreditkan** (butuh login manual di web) — bukan kebocoran. Kalau diklaim: 100 koin = tepat 2 gambar Qwen-Edit.

### Kontes BARU (belum ada di §3/§3b) — sumber aifilmcontests.com (verified 5 Nov)
| Kontes | Hadiah | Deadline | Syarat |
|---|---|---|---|
| **M.AI International AI Short Film Festival** (Cagliari, Sardinia, 18–20 Des 2026) | **€5.750 cash**, 6 award (Grand Prix, Best Experimental & Visual Innovation, dll) | **20 Nov 2026** (14 hari) | **GRATIS**, global, AI-driven cinema/animation/eksperimental/hybrid. Runtime belum terverifikasi (cek FilmFreeway) |
- Duplikat yang BUKAN kontes baru: "Jingrui AI Creation Contest" (= 1 Billion AI Film Award 2027, Seedance ≥70%) · "The AI in Anime 2026" (10 Nov, non-cash, screening Las Vegas).
- Lewati: AI New York Awards (non-cash), WAIFF London (UK-only, £75), IASFF India ($30 fee), Veritas ($9, non-cash).
Prioritas cash bebas-tool: **Artefact Paris €10K (2 Des)** > **M.AI €5.750 (20 Nov)** > **SVAIFF Korea (25 Nov)** > **Cue Xmas (20 Nov, gratis)** > **AI ZONE $500 (30 Nov, gratis)**.

### Aksi 7 Nov
1. Login web → klaim ±100 koin → **langsung** habiskan 2 gambar Qwen-Edit (keyframe Artefact). Jangan disimpan, hangus 24 jam.
2. Publish workflow `qwen-consistency-edit` (id 2108638842228461570) — masih $0,00.
3. Daftar M.AI (gratis) sebelum 20 Nov; cek runtime di FilmFreeway.
WARNING: TIDAK ADA jam gratis. Qwen-Edit ±50 koin/gambar, motion ±26 koin/dtk (16 dtk ±431).

## 23. SCAN 8 NOV 2026 (08:00) — saldo 0 (Δ 0), wallet HABIS ($0,0000) + kontes baru: HASFA $2.750
**SALDO: 0 RH Coins** (Δ **0** vs 7 Nov). Wallet **$0,0100 → $0,0000** (habis). Tugas jalan: 0.
Rantai: 604 → 0 → 77 → 0 → 100 → 0 → 0 → **0**. Bonus login hari ini **belum masuk** (butuh login web manual), bukan kebocoran.

### ⚠️ Cek penting: masa aktif membership
§0 (historis 10 Okt) mencatat Personal membership **aktif s/d 8 Nov 2026** = **HARI INI**.
Kalau benar, jatah 36.000 koin/bulan **berhenti** dan saldo akan tetap 0 tanpa top-up/renew.
Belum diverifikasi ulang via API → **cek dashboard sebelum menghitung rencana render**.

### Kontes BARU (belum ada di §3/§3b/§22) — sumber aifilmcontests.com (verified 5–6 Nov)
| Kontes | Hadiah | Deadline | Biaya | Catatan |
|---|---|---|---|---|
| **Hollywood AI Short Film Awards (HASFA)** | **$2.750 cash** (Best Picture $750, tiap genre award $250) | **15 Des 2026** (37 hari) | **$25–55** (bertingkat) | AI tools bebas, durasi **s/d 22 mnt**, film jadi setelah 1 Jan 2024, screening LA 13 Feb 2027 |
| **NEXTALE Award** | **$3.000** ($2.000 grand + $100×10 early) | 14 Des 2026 | Gratis | ⚠️ wajib **serial AI 20+ episode** di NEXTALE Studio — berat |
| Gossip Goblin Competition | $20.000 | 15 Des 2026 | Gratis | ✗ **wajib Showrunner Studio + watermark** (tool-locked) |
| AI Toronto Genre Awards | laurels | 22 Mei 2027 | — | non-cash |
| Twin Rivers AI Film Festival 2027 | 20% net entry fee | 8 Mar 2027 | — | non-cash efektif |
| Montreal AI Indie Festival / AI Independent Montreal | laurels (cash tak disebut) | 4 Jan / 2 Jul 2027 | — | non-cash |
| Kursaal San Sebastián 2027 | trofi | 31 Jan 2027 | €10 | non-cash |
| HKAIIFF 2027 | 7 Unicorn Award | 1 Mar 2027 | $99 | non-cash |

### Verifikasi ulang (bukan baru)
- **M.AI Cagliari**: GRATIS, **€5.750** (Grand Prix €1.500 + Best Experimental €750 + lain), deadline **20 Nov (13 hari)**, film jadi setelah 1 Jan 2024, AI tools bebas. **Runtime resmi masih belum dipublikasi** di listing → cek FilmFreeway.
- **Cue Xmas '26**: GRATIS, 20 Nov, 2:00–6:00 mnt bertema Natal, **4 award cash**, tayang AFRO TV 12 Des. Single clip tanpa editing = gugur.

### Aksi 8 Nov (prioritas)
1. **Login web → klaim ±100 koin → langsung** bakar ke 2 gambar Qwen-Edit (keyframe Artefact). Jangan disimpan, hangus 24 jam.
2. **Cek status membership** (habis hari ini?) — tentukan perlu renew/top-up atau fokus jalur gratis (kontes tak butuh koin).
3. Publish workflow `qwen-consistency-edit` (id 2108638842228461570) — masih $0,00.
4. Daftar **M.AI (gratis)** sebelum 20 Nov; HASFA hanya kalau siap bayar $25–55.
WARNING: TIDAK ADA jam gratis. Qwen-Edit ±50 koin/gambar, motion ±26 koin/dtk (16 dtk ±431 koin).

## 24. SCAN 9 NOV 2026 (08:00) — saldo 0 (Δ 0), membership LEWAT 8 Nov + kontes baru: SVAIFF KOREA (gratis, 25 Nov)
**SALDO: 0 RH Coins** (Δ **0** vs 8 Nov). Wallet **$0,0000**. Tugas jalan: 0. `remainPoint`: 7.0 · `apiType`: NORMAL.
Rantai: 77 → 0 → 100 → 0 → 0 → **0**. Koin login harian **lagi-lagi belum masuk** (butuh login web manual).
⚠️ **Membership Personal tercatat aktif s/d 8 Nov 2026 = sudah LEWAT.** API `accountStatus` **tidak** mengembalikan field membership → tidak bisa diverifikasi lewat API. Konsekuensi: jatah 36.000 koin/bulan berhenti; saldo akan tetap 0 sampai renew/top-up. **Cek dashboard sebelum rencana render apa pun.**

### Kontes BARU (belum ada di §3/§6/§7/§8/§23)
| Kontes | Hadiah | Deadline | Biaya | Catatan |
|---|---|---|---|---|
| **SVAIFF KOREA 2026** (Silicon Valley AI Film Festival Korea) | **KRW 30 jt** total (±$21K) — Grand Prize **KRW 10 jt**, 19 pemenang di 12 kategori + 31 Encouragement | **25 Nov 2026** (16 hari) | **GRATIS** | ✅ **BUKA untuk SEMUA kewarganegaraan**, individu/tim. Kategori: Narrative ≤20 mnt, Animation ≤20, Documentary ≤20, **Advertising ≤3 mnt**, **Music Video ≤7 mnt**, Arirang K-Culture ≤20. AI ≥50% visual/unsur cerita, hybrid live-action boleh, wajib Creative Statement + Evidence Scenes. 50 pemenang Korea lanjut grand final Silicon Valley Jan 2027. ⚠️ Form data pemenang menyebut 주민등록번호·rekening Korea → **wajib tanya panitia soal pembayaran non-Korea**. |
| **Melbourne AI Film Festival (MAIFF) 2026** | non-cash (laurel) + kategori internasional Narrative/Documentary/Animation | regular 8 Nov (lewat), **late 29 Nov** | via FilmFreeway (fee) | prioritas rendah |
| **Cine Prague: AI Short Film** | non-cash | **18 Nov** | **$50** (late) | prioritas rendah, ≤5 mnt |

### Verifikasi ulang (bukan baru)
- **1 Billion Followers Summit AI Film Award 2027** — tetap GRATIS, **20 Nov**, $1 jt, 5–7 mnt, ≥70% Seedance → jalur hadiah terbesar, tapi butuh koin/biaya token belum terukur.
- **Cue Xmas '26** — GRATIS, 20 Nov, 2–6 mnt, wajib multi-shot + final edit manusia.
- **M.AI Cagliari** — GRATIS, €5.750, 20 Nov.
- **HIIFF Hainan** — 15 Nov, tapi **hanya via LibTV (platform China)** → skip.
- **WAIFF London** — hanya kreator UK → skip.

### Aksi 9 Nov
1. **Login web RunningHub** → cek status membership (habis?) + klaim ±100 koin harian → kalau dapat, langsung bakar ke 2 gambar Qwen-Edit, jangan disimpan (hangus 24 jam).
2. **Putuskan renew/top-up** — tanpa membership, saldo mentok 0 dan semua pipeline render terhenti; kontes gratislah yang masih bisa jalan.
3. **Daftar SVAIFF KOREA** (gratis, 19 kursi juara, 25 Nov) — kursi terbanyak per dolar di daftar saat ini.
4. Publish workflow `qwen-consistency-edit` (id 2108638842228461570) — masih $0,00.
WARNING: TIDAK ADA jam gratis. Qwen-Edit ±50 koin/gambar, motion ±26 koin/dtk (16 dtk ±431 koin).

## 25. SCAN 10 NOV 2026 (08:00) — saldo 0 (Δ 0, hari ke-6), poin ikut habis (7 → 0) + TIDAK ada kontes cash baru
**SALDO: 0 RH Coins** (Δ **0** vs 9 Nov). Wallet **$0,0000**. Tugas jalan: 0. `remainPoint`: **0,0** (turun dari 7,0 — pertama kali poin juga 0) · `apiType`: NORMAL.
Rantai 8 hari: 1999 → 604 → 0 → 77 → 0 → 0 → **100** → 0 → 0 → 0 → **0**. Koin login harian belum masuk lagi (butuh login web manual).
⚠️ **Membership Personal lewat 8 Nov (hari ke-2 tanpa jatah 36.000 koin/bulan).** `accountStatus` tetap tidak mengembalikan field membership → tidak bisa diverifikasi via API. Saldo akan mentok 0 sampai renew/top-up. Cek dashboard sebelum rencana render apa pun.

### Kontes — hasil scan aifilmcontests.com (66 terbuka, 71 aktif, $3,0 jt+ hadiah)
**TIDAK ADA kontes CASH baru** dibanding §24. Penambahan terbaru semuanya **non-cash** (FilmFreeway):
| Kontes | Deadline | Hadiah | Catatan |
|---|---|---|---|
| Reel Sessions: The Black AI Film Festival | 31 Des 2026 | belum ada cash terverifikasi | fee FilmFreeway |
| NeoCinema AI Film Festival | 31 Des 2026 | non-cash (laurel) | fee |
| AI Cinema Festival Québec City 2027 | 24 Jan 2027 | non-cash | fee |
| SIAFF Seoul 2027 (ke-6) | 30 Apr 2027 | **trofi/sertifikat, tanpa cash** | fee, Seoul |
| KCAIF 2027 (K-Culture, ke-2) | 10 Apr 2027 | Grand Prize/Gold/Silver + 16 kategori, **cash tidak terverifikasi** | fee, Gangnam 1 Mei 2027 |

### Verifikasi ulang (bukan baru — tetap prioritas)
- **SVAIFF Korea 2026** — GRATIS, **25 Nov** (15 hari), KRW 30 jt, 19 kursi juara. ✅ jalur terbaik sekarang.
- **1 Billion Followers Summit AI Film Award 2027** — GRATIS, **20 Nov** (10 hari), Grand Prize $1 jt, 5–7 mnt, ≥70% Seedance (butuh biaya token belum terukur).
- **M.AI Cagliari** €5.750 & **Cue Xmas '26** — GRATIS, 20 Nov. **Chroma S2** — 31 Des (tanggal di tracker: 7 Jan), $175K+.
- Sudah tutup/lewat: The AI in Anime, IASFF (10 Nov). AI New York Awards 15 Nov, WAIFF London 17 Nov (khusus UK).

### Aksi 10 Nov
1. **Login web RunningHub** → cek status membership (lewat 8 Nov?) + renew/top-up + klaim ±100 koin harian. Kalau dapat koin: bakar 1–2 gambar Qwen-Edit (±50 koin/gambar), jangan disimpan (hangus 24 jam).
2. Kalau **tidak** renew: semua pipeline render berhenti → alihkan energi ke **SVAIFF Korea (gratis, 19 kursi)** pakai tool/kredit non-RH.
3. Jangan kejar SIAFF/KCAIF/Québec/NeoCinema dulu — non-cash dan pakai fee.

WARNING: TIDAK ADA jam gratis. Qwen-Edit ±49–52 koin/gambar, motion ±16,4–26 koin/dtk (16 dtk ≈ 431 koin). Hitung koin dulu sebelum render.

## 26. SCAN 11 NOV 2026 (08:00) — saldo 0 (Δ 0, hari ke-7 kosong) + 6 kontes GRATIS-cash BARU (Artefact Paris, AKOOL, Curious Refuge, NEXTALE, NEXMUSE, AI for Good) & KOREKSI deadline Chroma S2 → 7 Jan 2027
**SALDO: 0 RH Coins** (Δ **0** vs 10 Nov). Wallet **$0,0000**. Tugas jalan: 0. `apiType`: NORMAL.
Rantai 9 hari: 1999 → 604 → 0 → 77 → 0 → 0 → **100** → 0 → 0 → 0 → 0 → **0** (hari ke-7 kosong berturut-turut).
⚠️ **Membership Personal lewat 8 Nov = hari ke-3 tanpa jatah 36.000 koin/bulan.** API `accountStatus` tak punya field membership → verifikasi hanya via dashboard web.

### Kontes BARU (belum tercatat di §24/§25) — semua GRATIS masuk & hadiah cash nyata
| Kontes | Deadline | Hadiah | Syarat kunci |
|---|---|---|---|
| **Artefact AI Film Festival (Paris, ed.3)** | **2 Des 2026** | **€10.000** grand prix + 3×€1.000 (Juri/Audiens/Inovasi) | ≤**314 dtk**, 1 film/orang, tema *(Dis)Connection*, **wajib GenAI di pra-produksi, produksi, DAN pasca** (cuma Runway/Kling di shot = gugur) |
| **Curious Refuge × Epidemic Sound — AI Holiday** | **6 Des 2026** | **$7.500+** cash | short libur/Natal full-AI |
| **AKOOL AI Film Challenge** | **20 Des 2026** | **$50.000** grand (juara 2 $25rb, 3 $15rb, 10 finalis ×$2.500); listing klaim "$500.000 Creator Rewards" | 3 kategori: trailer 30–90 dtk film fiktif / AI short / "Impossible". **WAJIB pakai AKOOL** secara bermakna, publish tag @AKOOL #AKOOLFilmChallenge |
| **NEXTALE Award** | **14 Des 2026** | $3.000 pool + 100% revenue 6 bln | wajib **series 20+ episode** di NEXTALE Studio |
| **NEXMUSE AI Music Video 2027** | **28 Des 2026** | **₩21.000.000** (~$15rb) / **32 pemenang** (umum + pelajar) | wajib lagu+video dari 1 dari 24 karakter idol mereka |
| **AI for Good Film Festival (ITU)** | **1 Mei 2027** | hadiah + screening Jenewa | 1–10 mnt, **difilmkan 1 Sep 2026–1 Mei 2027**, gratis |

### KOREKSI PENTING
- **Chroma Awards S2** — deadline sebenarnya **7 Jan 2027, 23:45 PT** (bukan 31 Des), dibuka 19 Okt, **$450.000+** cash, 5 divisi + Student, karya ≥1 Feb 2026, menang diumumkan 11 Feb 2027. → masih ada **57 hari**, bukan 50.
- **LAAIMPA (LA AI Motion Pictures Awards)** — GRATIS, siklus **bulanan** (submit tgl 20 → nominee 28 → juara akhir bulan), gala Beverly Hills akhir 2026. Bisa dipakai latihan berulang tanpa biaya.
- **Showrunner Gossip Goblin** 15 Des ($20rb) — **tool-locked** (harus di Showrunner Studio) → skip.
- **Berlin AI Film Festival** 31 Des ($40, screening) & **Florence AI Festival** 15 Des (fee) → non-cash prioritas rendah.

### Peta peluang per (kekurangan) modal
Karena saldo 0, urutan realistis: (1) **Artefact Paris** — €10rb, gratis, 314 dtk pendek = paling murah diproduksi; (2) **AKOOL** — $50rb tapi wajib langganan AKOOL (cek free tier); (3) **Curious Refuge** $7.500 6 Des; (4) **Chroma S2** 7 Jan (paling besar tapi butuh produksi panjang); (5) **SVAIFF Korea** 25 Nov (19 kursi, gratis).

### Aksi 11 Nov
1. **Login web RunningHub** → cek/renew membership + klaim ±100 koin harian; kalau dapat, langsung bakar 1–2 gambar Qwen-Edit (±50/gambar), jangan disimpan.
2. **Daftar Artefact Paris sekarang** (gratis, 2 Des) — 314 dtk masih bisa dikerjakan tanpa render mahal (storyboard + Qwen still + Ken Burns/animasi ringan).
3. Jangan render motion panjang sebelum koin ada: ±26 koin/dtk (16 dtk ≈ 431 koin).

WARNING: TIDAK ADA jam gratis. Qwen-Edit ±49–52 koin/gambar · motion ±16,4–26 koin/dtk. Hitung koin dulu sebelum render.

## 27. 🆕 KONTES BARU (ditemukan 12 Nov 2026) — AI Film Award 2027 (1 Billion Followers Summit, Dubai)
- Hadiah **$1.000.000 cash**, 1 pemenang, **gratis**, global (≥18 th), sumber: 1billionsummit.com/ai-film-award + T&C.
- Syarat: film **5–7 mnt**, 16:9, 1080p, MOV/MP4, subtitle EN, tema dari 5 pilihan, **≥70% wajib Digenerate via Seedance (Dreamina)**.
- Deadline **20 Nov 2026** (Top10+public voting 15 Des, Top5 25 Des, premiere 8–10 Jan 2027 Dubai). Skor: AI 30% / Story 30% / Kreativitas 20% / Teknis 20%.
- ✅ Jalur kita memenuhi syarat tools: RH punya `bytedance/seedance-2.5-token/text-to-video` & `/image-to-video`.
- ⚠️ Realita: 8 hari sisa + saldo 0 koin → tidak realistis untuk karya 5–7 mnt baru. Simpan Seedance untuk **Chroma S2 (7 Jan 2027)**.

## 28. SCAN 13 NOV 2026 (08:01) — saldo 0 (Δ 0, hari ke-10 kosong) + TIDAK ada kontes cash baru
**SALDO: 0 RH Coins** (Δ **0** vs 12 Nov). Wallet **$0,0000**. Tugas jalan: 0. `apiType`: NORMAL.
Rantai 10 hari: 1999 → 604 → 0 → 77 → 0 → 0 → **100** → 0 → 0 → 0 → 0 → 0 → **0** (terakhir ada koin: 100 pada 5 Nov).
⚠️ **Membership Personal lewat 8 Nov = hari ke-5 tanpa jatah 36.000 koin/bulan.** Verifikasi hanya via dashboard web (API tak punya field membership).

### Kontes — hasil scan 13 Nov (aifilmcontests.com /contests/free + /prize/free-entry + topics closing Nov & Dec; kajimelo index; aicompetition.dev)
**TIDAK ADA kontes CASH baru** dibanding §26/§27. Semua yang muncul sudah tercatat: AI ZONE ($500, 30 Nov), Cine Prague ($1.000, 28 Nov), Artefact Paris (€10.000, 2 Des), Curious Refuge x Epidemic ($7.500, 6 Des), NEXTALE ($3.000, 14 Des), AKOOL (pool $50rb / $500rb creator rewards, 20 Des — terkunci tool AKOOL), Chroma S2 ($175K+, 7 Jan 2027), JIFF Jaipur (5 Des), SVAIFF Korea (25 Nov).
Catatan baru non-prioritas: **World AI Cinema Festival "Remember the Future"** (Cannes, ronde bulanan, cutoff tahunan 30 Jul 2027) — **berbayar** (earlybird/late tier) ⇒ bukan jalur cash gratis; ronde Nov sudah tutup 8 Nov.

### Aksi 13 Nov (prioritas)
1. **Login web RunningHub** → cek/renew membership + klaim ±100 koin harian (hangus 24 jam). Tanpa login manual, saldo tetap 0.
2. Kalau koin masuk: bakar cepat (1–2 gambar Qwen-Edit ±50 koin/gambar), jangan disimpan.
3. Kalau tidak renew: fokus kontes GRATIS tanpa RH — Artefact Paris (2 Des, ≤314 dtk = paling murah diproduksi) dan Chroma S2 (7 Jan).
WARNING: TIDAK ADA jam gratis. Qwen-Edit ±49–52 koin/gambar, motion ±16,4–26 koin/dtk (16 dtk ≈ 431 koin). Hitung koin dulu sebelum render.
