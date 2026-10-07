# 🆘 Prosedur Pemulihan Akses VPS

> Kalau nggak bisa masuk ke VPS (SSH gagal). **Jangan panik — selalu ada jalan balik.**

---

## 🚨 Gejala

- SSH ke IP publik **timeout / connection refused**
- Login gagal padahal password/key bener
- (biasanya habis ngutak-atik firewall / port / SSH)

---

## 🪜 Urutan Pemulihan (dari yang paling gampang)

### 1. Coba **Tailscale SSH**
```bash
ssh root@100.115.213.21
```
Tailscale masuk lewat jalur VPN (bukan port 22 publik) → sering **tembus** walau port 22 diblok.

### 2. Coba **Tencent Cloud Console → VNC**
- Login ke panel Tencent Cloud
- Pilih instance → **VNC / Console**
- Login langsung dari browser (nggak lewat jaringan) → **pasti bisa**

### 3. Dari dalam VPS (via jalur di atas), perbaiki
```bash
sudo ufw status verbose      # cek rule
sudo ufw disable             # matikan firewall (jalan tercepat balik akses)
sudo ss -tlnp                # cek SSH masih dengerin port 22?
sudo systemctl restart ssh    # restart SSH kalau perlu
```

### 4. Cek penyebab
```bash
journalctl -u ssh --no-pager | tail -30
grep -Ei "^Port" /etc/ssh/sshd_config
```

---

## 🛡️ Biar Nggak Kejadian Lagi

1. **Tailscale SSH aktif** = jalur cadangan ✅
2. **Agent dilarang** sentuh SSH/UFW tanpa izin (aturan di skill `webuild-server`)
3. Prosedur aman: `allow 22` **dulu** → tes sesi kedua → baru enable
4. **Snapshot** VPS sebelum perubahan besar
5. **Console Tencent** = penyelamat terakhir

---

## 📝 Pelajaran dari Kejadian Lama

Di VPS sebelumnya, agent ngutak-atik **UFW/port SSH** tanpa pengamanan → port 22 ketutup → nggak bisa login.
**Penyebab umum:** `ufw enable` dengan `default deny` tanpa `allow 22`, atau ganti port SSH yang salah setting.

**Aturan baru: perangkat apa pun (termasuk app visual macam virtual office) TIDAK BOLEH menyentuh SSH/firewall.** Cukup buka port web-nya saja.

---

## 🔗 Terkait
- [[08-Infrastruktur/VPS Manifest]]
- [[README|Vault Index]]

#infrastruktur #vps #pemulihan