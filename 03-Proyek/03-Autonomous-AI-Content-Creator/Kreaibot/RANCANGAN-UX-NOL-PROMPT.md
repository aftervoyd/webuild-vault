# RANCANGAN: BOT NOL-PROMPT — user awam, hasil natural seperti manusia asli
Target: **user nggak bisa prompting sama sekali**, tapi hasilnya **natural, realistis, perilaku manusia asli, alam asli**.
Ditulis 9 Okt 2026. Ini peta jalan, bukan yang sudah jadi — tiap fitur wajib lulus uji dulu ("jangan jual yang belum terbukti").

## 1. EMPAT PRINSIP
1. **0 ketik** — semua lewat tap. Ngetik hanya opsional (buat yang mau).
2. **Natural ≠ dikarang.** Gerak manusia yang *dikarang model dari teks* lemah (terbukti: LTX 2.3 lemah lokomosi). Natural datang dari **gerak nyata**: (a) video penggerak asli (motion transfer), (b) **suara asli + lip-sync** (digital human).
3. **Konsisten = aset tersimpan.** "Karakter Saya" / "Produk Saya" (sudah live) → foto master yang sama tiap render.
4. **Suara = separuh realisme.** Orang *ngomong* terasa hidup; orang diem kaku. Digital human + TTS Bahasa Indonesia.

## 2. PETA NIAT USER → MESIN (yang paling penting)
| User tap (tanpa ngetik) | Mesin | Hasil |
|---|---|---|
| 🗣️ **Ngomong** (iklan/UGC) | **LTX 2.3 Digital Human** `2031016553440878594` (foto + audio, 1280p) | orang **ngomong lip-sync** + suara — *paling terasa manusia* |
| 🎬 **Gerakan siap pakai** | Wan2.2 Animate `2039639280896708610` + klip penggerak | gerak badan **asli** (jalan/lari/menari) |
| 🌅 **Ganti suasana** (pantai/kota/kafe) | LTX 2.3 i2v `2065707741691334658` | latar baru (kekuatan LTX) |
| 🎭 **Ganti wajah** | Face swap `1889155568379092993` | wajah nempel natural, konsisten |
| 👕 **Ganti baju / hapus objek** | app editor | ubah atribut |

## 3. ALUR "3 TAP" (target UX)
```
Menu → 🧑🎨 Karakter: Rina  →  🗣️ Ngomong  →  📝 Pilih naskah (Skincare #3)  →  RENDER
```
**Tidak ada layar prompt.** Prompt hanya "di balik layar" (diisi bot).

## 4. DUA BANK YANG WAJIB DIBANGUN
### a) Bank NASKAH (script) — biar user nggak perlu nulis
10 template per kategori, Bahasa Indonesia gaya TikTok: Skincare · Kuliner · Fashion · Jasa · FnB · Herbal · Elektronik · Property · Otomotif · Edukasi.
User tap naskah → bot TTS → jadi audio → masuk digital human. **Bisa juga user kirim voice note sendiri** (paling natural, dan gratis).

### b) Bank GERAKAN (motion library) — biar gerak asli
Butuh klip penggerak **nyata** (10–15 dtk, 1 orang, badan kelihatan, kamera relatif diam):
1. jalan santai · 2. jalan ke arah kamera · 3. lari · 4. menari · 5. duduk ngopi di kafe
6. ngobrol sambil tangan gerak · 7. belanja di jalanan · 8. ketawa · 9. buka produk (unboxing) · 10. selfie vlog
**Sumber:** footage stok (Wikimedia/Pexels/Pixabay) **diblokir dari server VPS** (robot policy/Cloudflare).
→ Jalan tercepat: **user kirim 3–5 klip pendek** (bukan dirinya), atau rekam sendiri. Boleh juga dari HP teman/staf.

## 5. ATURAN PROYEK (tetap)
- **Jangan jual yang belum terbukti** — semua fitur wajib lulus **uji lintas-orang** dulu.
- **Harga: samakan dengan Kuzushi, jangan lebih murah** — menang di **kualitas** (kemiripan, konsistensi, natural).
- Face swap kita = **gambar**; video = pakai motion transfer / digital human.

## 6. STATUS JUJUR (9 Okt)
| Bagian | Status |
|---|---|
| Karakter & Produk tersimpan (inventory) | ✅ LIVE (selftest 93/93) |
| Preset 1-tap (video & editor) | ✅ LIVE |
| Face swap gambar | ✅ LIVE (terbukti) |
| Digital human lip-sync | 🧪 **sedang diuji** (app barusan ketemu) |
| Motion transfer | 🧪 jalan, **belum** lulus lintas-orang |
| Bank naskah | ⏳ belum |
| Bank gerakan | ⛔ **terblokir** (butuh klip dari user) |