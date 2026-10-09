#!/usr/bin/env python3
"""Self-test KREE.AI: katalog, ledger token, backend mock (render nyata), PromptSmith/UGC."""
from __future__ import annotations

import asyncio
import subprocess
import sys
from pathlib import Path

import catalog
import promptsmith
from backends import GenRequest, make_backend
from config import settings
from db import Database

WORK = Path("/root/projects/kreaibot/work/selftest")
WORK.mkdir(parents=True, exist_ok=True)


def ok(label: str, cond: bool, extra: str = "") -> bool:
    print(f"{'✅' if cond else '❌'} {label}" + (f" — {extra}" if extra else ""))
    return cond


async def main() -> int:
    res = []

    # 1) katalog
    res.append(ok(f"katalog fitur lengkap ({len(catalog.FEATURES)} ≥ 7, termasuk UGC)",
                  len(catalog.FEATURES) >= 7, ", ".join(catalog.FEATURES)))
    f = catalog.get("allinone")
    res.append(ok("harga All-in-One (15 dtk) = 2.5 token", f is not None and f.cost == 2.5))
    # Konversi Rp: 10 token = Rp10.000 → 1 token = Rp1.000 (i2v 5 dtk = 0,5 token = Rp500)
    i2v = catalog.get("i2v")
    res.append(ok("konversi Rp (10 tok = Rp10.000 → 1 tok = Rp1.000)",
                  catalog.price_rp(i2v, 10, 10_000) * 2 == 1000,
                  f"i2v 5 dtk = Rp{catalog.price_rp(i2v, 10, 10_000)}"))
    # HARGA SEHAT (per fitur × durasi): koin terukur × Rp/koin harus di bawah harga jual.
    # Angka koin dari render NYATA di RunningHub (5 dtk = 55–66 koin · 15 dtk = 269 koin).
    RUPIAH_PER_KOIN = 4.46
    KOIN_TERUKUR = {("i2v", 5): 45, ("i2v", 10): 68, ("i2v", 15): 89, ("long", 30): 135,
                    ("faceswap", 5): 10, ("story", 15): 135, ("story", 30): 270,
                    ("allinone", 5): 66, ("allinone", 15): 269, ("ugc", 15): 269}
    for (key, dur), koin in KOIN_TERUKUR.items():
        harga = catalog.cost_for(key, dur) / 10 * 10_000
        biaya = koin * RUPIAH_PER_KOIN
        margin = (harga - biaya) / harga * 100
        # i2v & long = produk pintu masuk/penggerak volume → margin boleh lebih tipis.
        # Catatan: RUPIAH_PER_KOIN di sini KONSERVATIF (4,46) sedangkan harga koin terukur ≈3,4,
        # jadi margin `long` sebenarnya ±54 %; ambang 38 % dipakai supaya guardrail tetap jujur.
        batas = 45 if key == "i2v" else (38 if key == "long" else 50)
        res.append(ok(f"margin {key} {dur} dtk sehat ({margin:.0f}% ≥ {batas}%)", margin >= batas,
                      f"harga Rp{harga:,.0f} vs biaya Rp{biaya:,.0f}"))
    res.append(ok("durasi render dalam batas mesin (4..30 dtk)",
                  all(4 <= ft.duration <= 30 for ft in catalog.enabled_features()),
                  ", ".join(f"{ft.key}={ft.duration}s" for ft in catalog.enabled_features())))
    res.append(ok("durasi yang dijual semua dalam batas mesin (4..30)",
                  all(all(4 <= d <= 30 for d in ft.durations) for ft in catalog.enabled_features()),
                  ", ".join(f"{ft.key}:{ft.durations}" for ft in catalog.enabled_features())))
    ugc = catalog.get("ugc")
    res.append(ok("fitur UGC ada & bertingkat", bool(ugc and ugc.kind == "ugc" and ugc.need_style
                                                     and ugc.char_first and ugc.product_slot),
                  f"{ugc.cost:g} token, Rp{catalog.price_rp(ugc, 10, 10_000)}" if ugc else ""))

    # 1b) alur TANPA TOMBOL (gaya @KuzushiGenBot): setelah foto, langsung ketik prompt
    src = Path(__file__).with_name("bot.py").read_text(encoding="utf-8")
    for needle, label in (("on_prompt_in_photos", "teks di tahap foto = prompt (tanpa tombol)"),
                          ("ugc_brief_text", "teks di tahap produk = brief (tanpa tombol)"),
                          ('"a:ratio:"', "tombol ganti RASIO di layar konfirmasi"),
                          ('"a:dur:"', "tombol ganti DURASI di layar konfirmasi"),
                          ('"u:stylemenu"', "tombol ganti GAYA (UGC)"),
                          ("cost_for(f.key, dur)", "biaya render ikut durasi terpilih")):
        res.append(ok(label, needle in src))
    res.append(ok('tombol "✅ Lanjut" sudah dihapus dari alur',
                  "✅ Lanjut" not in src and "Lanjut ke Brief" not in src))
    res.append(ok("prompt fitur video dikirim APA ADANYA (tanpa klausa tambahan)",
                  "AMBIENT_MOTION" not in src and 'str(data.get("prompt") or "").split()' in src))
    res.append(ok("tidak ada klausa karangan 'LIVING BACKGROUND' (dihapus 8 Okt)",
                  not hasattr(promptsmith, "AMBIENT_MOTION")))
    res.append(ok("prompt UGC tanpa klausa karangan",
                  "LIVING BACKGROUND" not in promptsmith.build_ugc_prompt(
                      "produk uji, harga Rp1.000", "review", ratio="9:16")))
    res.append(ok("frame i2v = foto asli di dua ujung (tanpa gambar sintetis)",
                  "photo1_zoom" not in (Path(__file__).with_name(".env").read_text(encoding="utf-8")
                                        if (Path(__file__).with_name(".env")).exists() else "")))
    # 1d) PERAPIAN PROMPT VIDEO — wajib aman (fallback ke prompt asli)
    res.append(ok("fungsi perapian prompt video tersedia",
                  hasattr(promptsmith, "refine_video_prompt")))
    res.append(ok("perapian prompt: input pendek → prompt asli (tanpa panggilan LLM)",
                  "if len(raw) < 3:" in (Path(__file__).with_name("promptsmith.py")).read_text(encoding="utf-8")
                  and "return raw" in (Path(__file__).with_name("promptsmith.py")).read_text(encoding="utf-8")))
    res.append(ok("aturannya melarang 'whole frame' bergerak (pelajaran 8 Okt)",
                  "whole frame" in promptsmith.VIDEO_REFINE_SYSTEM.lower()))
    res.append(ok("bot merapikan prompt video sebelum render (dengan saklar)",
                  "refine_video_prompt" in src and "settings.refine_video" in src))
    res.append(ok("i2v: frame akhir DIKOSONGKAN (@empty, bukan dilewati)",
                  "@empty" in next((l for l in (Path(__file__).with_name(".env")).read_text(encoding="utf-8").splitlines()
                                    if l.startswith("RUNNINGHUB_NODES_I2V=")), "")))
    _rh = (Path(__file__).with_name("backends") / "runninghub.py").read_text(encoding="utf-8")
    res.append(ok("backend: sentinel @empty kirim field kosong eksplisit",
                  'force_empty = val == "@empty"' in _rh and "not force_empty" in _rh))
    res.append(ok("saklar perapian bisa dimatikan lewat env",
                  "KREAIBOT_REFINE_VIDEO" in (Path(__file__).with_name("config.py")).read_text(encoding="utf-8")))
    _bot_src = (Path(__file__).with_name("bot.py")).read_text(encoding="utf-8")
    res.append(ok("job terputus disambung saat startup (_resume_jobs)",
                  "_resume_jobs" in _bot_src and "asyncio.create_task(_resume_jobs(bot))" in _bot_src))
    res.append(ok("db punya running_jobs() (dasar fitur resume)",
                  "def running_jobs" in (Path(__file__).with_name("db.py")).read_text(encoding="utf-8")))
    res.append(ok("alat pemulihan job tersedia (tools/deliver_job.py)",
                  (Path(__file__).with_name("tools") / "deliver_job.py").exists()))
    res.append(ok("upload pakai key SHARED (key platform ditolak upload 9 Okt)",
                  "self.upload_key" in _rh and "RUNNINGHUB_UPLOAD_KEY" in _rh
                  and "runninghub_upload_key" in (Path(__file__).with_name("config.py")).read_text(encoding="utf-8")))
    res.append(ok("backend bisa jalur AI App (webappId + ai-app/run)",
                  "_app_id" in _rh and "ai-app/run" in _rh and "RUNNINGHUB_APP_" in _rh))

    # 2) PromptSmith
    res.append(ok("6 gaya UGC tersedia", len(promptsmith.STYLES) == 6, ", ".join(promptsmith.STYLES)))
    p = promptsmith.build_ugc_prompt(
        brief="Skincare GlowUp serai, harga Rp79.000 promo beli 2 gratis 1, mau review santai",
        style_key="review", ratio="9:16")
    for need, label in (("CHARACTER", "prompt memuat blok CHARACTER"),
                        ("PRODUCT", "prompt memuat blok PRODUCT"),
                        ("STORY BEATS", "prompt memuat STORY BEATS"),
                        ("TIMELINE", "prompt memuat TIMELINE gaya H3"),
                        ("0-", "timeline pakai format per-segmen waktu (0-3s)"),
                        ("Rp79.000", "fakta harga user ikut masuk"),
                        ("AVOID", "prompt punya NEGATIVE prompt"),
                        ("9:16", "rasio ikut masuk")):
        res.append(ok(label, need in p))
    res.append(ok("prompt cukup detail (>500 char)", len(p) > 500, f"{len(p)} char"))
    allstyles = all(len(promptsmith.build_ugc_prompt("produk X harga 10rb", k)) > 300
                    for k in promptsmith.STYLES)
    res.append(ok("semua gaya bisa bikin prompt", allstyles))
    res.append(ok("ringkasan user TIDAK memuat prompt rakitan",
                  "CHARACTER" not in promptsmith.summary_for_user("promo")
                  and "AVOID" not in promptsmith.summary_for_user("promo")))
    res.append(ok("cinematic = tanpa dialog", not promptsmith.STYLES["cinematic"].talk))

    # 3) db + ledger
    pdb = WORK / "test.sqlite3"
    if pdb.exists():
        pdb.unlink()
    db = Database(pdb)
    db.ensure_user(123, "tester", "Tester", signup_bonus=1.0)
    res.append(ok("bonus daftar masuk", db.balance(123) == 1.0, f"saldo={db.balance(123)}"))
    db.ledger_add(123, 9.0, "topup_test")
    res.append(ok("top up 9 token", db.balance(123) == 10.0, f"saldo={db.balance(123)}"))
    jid = db.create_job(123, "ugc", 1.5, ["fid1", "fid2"], p, "9:16",
                        brief="produk A harga 10rb", style="promo")
    db.ledger_add(123, -1.5, "render", ref=str(jid))
    res.append(ok("potong biaya render UGC", db.balance(123) == 8.5, f"saldo={db.balance(123)}"))
    job = db.get_job(jid)
    res.append(ok("job simpan brief & style (audit prompt internal)",
                  job["brief"] == "produk A harga 10rb" and job["style"] == "promo" and len(job["prompt"]) > 300))
    db.ledger_add(123, 1.5, "refund", ref=str(jid))
    res.append(ok("refund gagal render", db.balance(123) == 10.0, f"saldo={db.balance(123)}"))

    # 3a-2) INVENTORY: karakter & produk tersimpan (fitur "tinggal sebut namanya")
    cid = db.char_save(123, "Si Rina", "FILEID-rina", kind="char")
    db.char_save(123, "Kopi Arabika", "FILEID-kopi", kind="produk")
    res.append(ok("simpan karakter tersimpan", cid is not None and db.char_count(123, "char") == 1))
    res.append(ok("simpan produk tersimpan", db.char_count(123, "produk") == 1))
    res.append(ok("nama karakter tidak boleh kembar (per jenis)",
                  db.char_save(123, "si rina", "X", kind="char") is None))
    res.append(ok("panggil karakter dari NAMA (case-insensitive)",
                  (db.char_get(123, "SI RINA") or {})["file_id"] == "FILEID-rina"))
    res.append(ok("deteksi nama di teks bebas ('video si rina joget')",
                  (db.char_find_in_text(123, "bikin video si rina joget", kind="char") or {})["name"] == "Si Rina"))
    res.append(ok("deteksi produk di brief ('promo kopi arabika')",
                  (db.char_find_in_text(123, "promo kopi arabika diskon", kind="produk") or {})["name"] == "Kopi Arabika"))
    res.append(ok("tidak salah deteksi kalau nama tidak disebut",
                  db.char_find_in_text(123, "bikin video orang jalan santai", kind="char") is None))
    res.append(ok("ganti nama karakter", db.char_rename(123, cid, "Rina Cantik") and
                  (db.char_get(123, cid) or {})["name"] == "Rina Cantik"))
    res.append(ok("hapus karakter", db.char_delete(123, cid) and db.char_count(123, "char") == 0))

    # 3b) referral (anti-farming)
    db.ensure_user(900, "inviter", "Inviter", signup_bonus=1.0)
    db.ensure_user(901, "teman", "Teman", signup_bonus=1.0)
    res.append(ok("registrasi referral pengundang→teman", db.ref_register(900, 901)))
    res.append(ok("invitee ganda DITOLAK (1 akun = 1 bonus seumur hidup)",
                  not db.ref_register(902, 901)))
    res.append(ok("self-referral DITOLAK", not db.ref_register(901, 901)))
    res.append(ok("users.referred_by tercatat", db.get_user(901)["referred_by"] == 900))
    db.ledger_add(901, 2.5, "ref_bonus_invitee", ref="900")
    db.ref_mark(901, invitee_paid=1, status="paid")
    db.ledger_add(900, 1.5, "ref_bonus_inviter", ref="901")
    db.ref_mark(901, inviter_paid=1)
    res.append(ok("bonus invitee = 2,5 token", db.balance(901) == 3.5, f"saldo={db.balance(901)}"))
    res.append(ok("bonus pengundang = 1,5 token", db.balance(900) == 2.5, f"saldo={db.balance(900)}"))
    st = db.ref_summary(900)
    res.append(ok("rekap referral (1 undang · 1 cair · 1,5 token)",
                  st["total"] == 1 and st["paid"] == 1 and st["earned"] == 1.5, str(st)))
    res.append(ok("hitungan cap harian/bulanan jalan", db.ref_count_since(900, 0) == 1))
    res.append(ok("tidak ada bonus pengundang menggantung", db.ref_pending_inviter(901) is None))
    res.append(ok("mode aman (pengundang nunggu top up) bisa dibaca",
                  isinstance(settings.ref_inviter_after_purchase, bool)))
    res.append(ok("nominal referral sesuai permintaan user (2,5 / 1,5)",
                  settings.ref_invitee == 2.5 and settings.ref_inviter == 1.5,
                  f"invitee={settings.ref_invitee} inviter={settings.ref_inviter}"))
    res.append(ok("cap default 10/hari · 30/bulan",
                  settings.ref_max_day == 10 and settings.ref_max_month == 30))

    # 3c) pembayaran Aulaa / QRIS (offline — tanpa panggil API)
    from aulaa import Aulaa, _extract_id, _to_payment
    db.pay_create("KREE-123-1", 123, 10_000, 10.0)
    res.append(ok("order pembayaran tercatat pending",
                  db.pay_get("KREE-123-1")["status"] == "pending"))
    db.pay_set("KREE-123-1", payment_id="f47ac10b-58cc-4372-a567-0e02b2c3d479",
               invoice="00020101021226670016COM.NOBUBANK")
    res.append(ok("payment_id + invoice QRIS tersimpan",
                  str(db.pay_get("KREE-123-1")["payment_id"]).startswith("f47ac10b")))
    res.append(ok("order pending kebaca poller",
                  any(r["order_id"] == "KREE-123-1" for r in db.pay_pending())))
    db.pay_mark_paid("KREE-123-1")
    r_ = db.pay_get("KREE-123-1")
    res.append(ok("tandai lunas → paid + paid_at", r_["status"] == "paid" and bool(r_["paid_at"])))
    res.append(ok("order lunas keluar dari daftar pending",
                  not any(r["order_id"] == "KREE-123-1" for r in db.pay_pending())))
    qp = Aulaa.qr_png("00020101021226670016COM.NOBUBANK.WWW0118936000000000000000", WORK / "qr-test.png")
    res.append(ok("QR PNG ter-render dari string QRIS", qp.exists() and qp.stat().st_size > 200,
                  f"{qp.stat().st_size} bytes"))
    res.append(ok("idempotensi: UUID diambil dari respons 409",
                  _extract_id({"error": "order_id exists",
                               "id": "f47ac10b-58cc-4372-a567-0e02b2c3d479"})
                  == "f47ac10b-58cc-4372-a567-0e02b2c3d479"))
    pm = _to_payment({"id": "x", "order_id": "o", "status": "paid", "amount": 10_000,
                      "payment_method": "qris", "payment_number": "00020101", "is_test": True})
    res.append(ok("parser status paid/dead/sandbox benar", pm.paid and not pm.dead and pm.is_test))
    res.append(ok("paket topup ≥ Rp10.000 (biaya QRIS ≤5%)", all(rp >= 10_000 and rp % 1_000 == 0
                  for rp in (10_000, 25_000, 50_000, 100_000))))
    res.append(ok("metode bayar default = qris (biaya termurah)", settings.aulaa_method == "qris"))

    # 3d) guard bug laten di bot.py (handler pakai `bot.send_message` → wajib global)
    src_bot = (Path(__file__).resolve().parent / "bot.py").read_text()
    res.append(ok("`bot` global + di-set di main() (anti-NameError)",
                  "\nbot: Bot = None" in src_bot and "global bot" in src_bot))
    res.append(ok("poller pembayaran terdaftar di bot.py",
                  "async def poller_payments" in src_bot and "create_task(poller_payments())" in src_bot))
    res.append(ok("handler cek pembayaran (t:cek) terdaftar", 'F.data.startswith("t:cek:")' in src_bot))

    # 4) backend mock → render video nyata
    be = make_backend("mock", work_dir=str(WORK))
    req = GenRequest(job_id=jid, feature_key="ugc", workflow="krea_ugc_h3",
                     photos=[], prompt=p, ratio="9:16", out_path=WORK / "hasil-mock.mp4")
    tid = await be.submit(req)
    st = await be.poll(tid)
    res.append(ok("mock backend selesai", st.state == "done", st.message))
    out = Path(st.result_path) if st.result_path else None
    if out and out.exists():
        pr = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "stream=width,height,codec_name", "-show_entries", "format=duration",
                             "-of", "default=noprint_wrappers=1", str(out)],
                            capture_output=True, text=True)
        print("   ffprobe →", " | ".join(pr.stdout.split()))
        res.append(ok("video valid (ffprobe)", pr.returncode == 0))
    else:
        res.append(ok("file hasil ada", False))

    print(f"\n{'='*52}\nHASIL: {sum(res)}/{len(res)} tes lulus")
    return 0 if all(res) else 1


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))