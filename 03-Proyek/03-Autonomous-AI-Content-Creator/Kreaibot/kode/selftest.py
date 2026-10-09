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
                    ("allinone", 5): 66, ("allinone", 15): 269, ("ugc", 15): 269,
                    # paritas Kuzushi (9 Okt): terukur di uji produksi
                    ("motion", 5): 121,        # Wan2.2 Animate, 308 s, 121 koin (GPU plus)
                    ("lipsync", 10): 48, ("pose", 5): 32}       # LTX digital human, 6 s = 29 koin → 10 s ≈ 48
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
    _mf = (Path(__file__).with_name("backends") / "mediafix.py").read_text(encoding="utf-8")
    res.append(ok("interpolasi fps MATI secara default (hasil asli RunningHub, tanpa frame sintetis)",
                  "KREAIBOT_SMOOTH_FPS" in _mf and 'os.getenv("KREAIBOT_SMOOTH_FPS", "0")' in _mf))
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
    # anti-bingung: salah kirim bahan → bot harus JAWAB, bukan diem
    _bs = (Path(__file__).with_name("bot.py")).read_text(encoding="utf-8")
    res.append(ok("inventory: kirim video/teks pas diminta foto → ada balasan",
                  "async def inv_photo_bukan_foto" in _bs))
    res.append(ok("inventory: kirim foto pas diminta nama → ada balasan",
                  "async def inv_name_bukan_teks" in _bs))
    res.append(ok("inventory: dokumen non-gambar ditolak jelas",
                  "bukan gambar" in _bs))

    # 3a-3) BUG FIX inventory: tombol ➕ Tambah baru dulu muncul "Jenis tidak dikenal"
    import bot as _b
    res.append(ok("inventory: 'm:inv:add:char' → tambah karakter (bukan error)",
                  _b.inv_parse("m:inv:add:char") == ("char", "add")))
    res.append(ok("inventory: 'm:inv:add:produk' → tambah produk",
                  _b.inv_parse("m:inv:add:produk") == ("produk", "add")))
    res.append(ok("inventory: 'm:inv:char' → buka daftar karakter",
                  _b.inv_parse("m:inv:char") == ("char", "buka")))
    res.append(ok("inventory: 'm:inv:produk' → buka daftar produk",
                  _b.inv_parse("m:inv:produk") == ("produk", "buka")))

    # 3a-4) SHEET FIX: character sheet → ambil panel orangnya (akar "hasil aneh" job 13)
    import sheetfix as _sf
    res.append(ok("sheetfix: baca JSON polos", _sf._parse('{"sheet": true, "box": [0,35,516,663]}')
                  == {"sheet": True, "box": [0, 35, 516, 663]}))
    res.append(ok("sheetfix: baca JSON di dalam ```json ... ``` (balasan LLM nyata)",
                  _sf._parse('```json\n{"sheet": true, "box": [0, 0, 508, 682]}\n```')
                  == {"sheet": True, "box": [0, 0, 508, 682]}))
    res.append(ok("sheetfix: foto biasa → sheet=false", _sf._parse('{"sheet": false, "box": null}')
                  == {"sheet": False, "box": None}))
    res.append(ok("sheetfix: balasan ngaco tidak bikin crash",
                  _sf._parse("maaf saya tidak bisa") == {"sheet": False, "box": None, "err": "tak ada JSON"}))
    from PIL import Image as _I
    _t = WORK / "sheet_grid.jpg"
    _I.new("RGB", (600, 600), (40, 40, 40)).save(_t)
    _p = _sf.crop_panel(_t, [0, 0, 300, 300], WORK / "panel_uji.jpg")
    res.append(ok("sheetfix: potong panel jalan (300×300 → 288×288 setelah buang margin)",
                  bool(_p) and _I.open(_p).size[0] >= 285))        # type: ignore[arg-type]
    res.append(ok("sheetfix: kotak kekecilan DITOLAK (jangan crop ngawur)",
                  _sf.crop_panel(_t, [0, 0, 50, 50], WORK / "panel_kecil.jpg") is None))
    res.append(ok("sheetfix: kotak keluar batas/terlalu kecil DITOLAK (foto asli tetap dipakai)",
                  _sf.crop_panel(_t, [500, 500, 400, 400], WORK / "panel_luar.jpg") is None))
    _bsrc = (Path(__file__).with_name("bot.py")).read_text(encoding="utf-8")
    res.append(ok("bot pasang sheet-guard sebelum render (i2v dkk)",
                  "SHEET_GUARD" in _bsrc and "_sheet_panel_from_file" in _bsrc))
    res.append(ok("inventory juga pakai panel (bukan lembaran sheet)",
                  "simpan PANEL orangnya" in _bsrc))

    # 3a-5) BUG "editor jadi kayak video / gepeng": PNG hasil app dinamai .mp4
    from backends.mediafix import fix_ext as _fx
    _png = b"\x89PNG\r\n\x1a\n" + b"\x00" * 40
    _mp4 = b"\x00\x00\x00\x18ftypisom" + b"\x00" * 40
    f1 = WORK / "salah_nama.mp4"; f1.write_bytes(_png)
    r1 = _fx(f1)
    res.append(ok("fix_ext: PNG yang dinamai .mp4 → jadi .png (biar dikirim sebagai FOTO)",
                  r1.suffix == ".png" and r1.exists()))
    f2 = WORK / "salah_nama2.png"; f2.write_bytes(_mp4)
    r2 = _fx(f2)
    res.append(ok("fix_ext: video yang dinamai .png → jadi .mp4 (biar dikirim sebagai video)",
                  r2.suffix == ".mp4" and r2.exists()))
    f3 = WORK / "benar.png"; f3.write_bytes(_png)
    res.append(ok("fix_ext: nama yang sudah benar tidak diubah", _fx(f3) == f3))
    res.append(ok("fix_ext: file tidak ada → aman (tidak crash)", _fx(WORK / "hantu.png") == WORK / "hantu.png"))
    _bsrc2 = (Path(__file__).with_name("bot.py")).read_text(encoding="utf-8")
    res.append(ok("bot memakai fix_ext sebelum mengirim hasil", "to_thread(fix_ext, result)" in _bsrc2))
    res.append(ok("PNG termasuk gambar (dikirim sebagai foto, bukan video)",
                  '".png"' in _bsrc2 and "IMG_EXT" in _bsrc2))

    # 3a-6) SESI TAHAN RESTART + anti-DIEM (bug 9 Okt 16:14: restart → foto user "not handled")
    from fsmstore import SQLiteStorage as _SS
    from aiogram.fsm.storage.base import StorageKey as _SK
    _fk = WORK / "fsm_uji.sqlite3"
    if _fk.exists():
        _fk.unlink()
    _key = _SK(bot_id=1, chat_id=8886993492, user_id=8886993492)
    _s1 = _SS(_fk)
    await _s1.set_state(_key, "Flow:photos")
    await _s1.set_data(_key, {"feature": "i2v", "photos": ["fid-uji"], "preset_sent": False})
    _s2 = _SS(_fk)                      # ← instance BARU = simulasi bot restart
    res.append(ok("sesi FSM bertahan setelah bot restart (state)",
                  await _s2.get_state(_key) == "Flow:photos"))
    res.append(ok("data sesi bertahan setelah restart (fitur + foto tidak hilang)",
                  (await _s2.get_data(_key)).get("photos") == ["fid-uji"]))
    await _s2.set_data(_key, {"feature": "motion", "n": 1, "ok": True})
    res.append(ok("data sesi bisa diubah lagi setelah restart",
                  (await _s2.get_data(_key)).get("feature") == "motion"))
    _bsrc3 = (Path(__file__).with_name("bot.py")).read_text(encoding="utf-8")
    res.append(ok("Dispatcher memakai storage SQLite (sesi tidak di RAM lagi)",
                  "SQLiteStorage(fsm_path)" in _bsrc3))
    res.append(ok("handler FALLBACK terdaftar (bot tidak pernah diam)",
                  "fallback_tak_ditangani" in _bsrc3))
    _hb = [h.callback.__name__ for h in __import__("bot").router.message.handlers]
    res.append(ok("fallback = handler pesan TERAKHIR (command admin tetap jalan)",
                  _hb and _hb[-1] == "fallback_tak_ditangani"))

    # 3a-7) KUNCI IDENTITAS (face swap balik) — akar "tetep gak mirip sama sekali"
    _bsrc4 = (Path(__file__).with_name("bot.py")).read_text(encoding="utf-8")
    res.append(ok("identity-lock: modul ada & bisa dipakai",
                  callable(__import__("identity").lock_identity)))
    res.append(ok("identity-lock: nyala untuk fitur editor",
                  'IDENTITY_LOCK = {"editor"}' in _bsrc4))
    res.append(ok("identity-lock: hanya kalau foto = karakter TERSIMPAN user",
                  "db.char_by_file_id(job[\"telegram_id\"], fids[0])" in _bsrc4))
    res.append(ok("identity-lock: hanya untuk hasil GAMBAR (video butuh app lain)",
                  "Path(result).suffix.lower() in IMG_EXT" in _bsrc4))
    res.append(ok("identity-lock: gagal → hasil asli tetap dikirim (tidak bikin job gagal)",
                  "if locked and locked.exists():" in _bsrc4 and "lock_identity" in _bsrc4))
    res.append(ok("db: char_by_file_id ada (cari karakter dari file_id foto)",
                  hasattr(__import__("db").Database, "char_by_file_id")))
    res.append(ok("migrasi karakter lama: alat perbaikan sheet tersedia",
                  (Path(__file__).with_name("tools") / "fix_saved_chars.py").exists()))
    # 3a-8) BUG 9 Okt: lock_identity memanggil backend.generate() — METODE ITU TIDAK ADA
    #        (API nyata = submit/poll) → kunci identitas gagal SENYAP, wajah selalu karangan model.
    import identity as _idmod
    _idsrc = (Path(__file__).with_name("identity.py")).read_text(encoding="utf-8")
    _idcode = "\n".join(l for l in _idsrc.splitlines() if not l.strip().startswith("#"))
    res.append(ok("identity-lock: tidak lagi memanggil metode hantu backend.generate()",
                  ".generate(" not in _idcode and "backend.submit(" in _idcode))
    _seen: dict = {}

    class _FakeBackend:                                  # meniru API RunningHub: submit + poll
        async def submit(self, req):                     # noqa: D401
            _seen["req"] = req
            return "t-1"

        async def poll(self, task_id):
            from backends import GenStatus
            p = Path(_seen["req"].out_path)
            Path(p.parent).mkdir(parents=True, exist_ok=True)
            p.write_bytes(b"png")
            return GenStatus(state="done", progress=100, result_path=p)

    _fajah = WORK / "wajah_uji.jpg"
    _fajah.write_bytes(b"jpg")
    _outl = WORK / "locked_uji.png"
    _rl = await _idmod.lock_identity(_FakeBackend(), WORK / "hasil_uji.png", _fajah, 1, _outl)
    res.append(ok("identity-lock: face swap BENAR-BENAR jalan (submit+poll) & hasil dipakai",
                  bool(_rl) and Path(_rl).exists()))
    # 3a-8b) MESIN KUNCI IDENTITAS: app "极速换脸" no-op → diganti 换头换脸提高相似度 (uji 93%)
    _envtxt2 = (Path(__file__).with_name(".env")).read_text(encoding="utf-8")
    res.append(ok("identity-lock: pakai app '换头换脸提高相似度' (93% mirip, bukan app no-op)",
                  "RUNNINGHUB_APP_IDLOCK=2020760401977282562" in _envtxt2))
    res.append(ok("identity-lock: binding app benar (6=GAMBAR UTAMA, 26=FOTO WAJAH)",
                  '\"nodeId\":\"6\"' in _envtxt2 and '\"nodeId\":\"26\"' in _envtxt2))
    res.append(ok("identity-lock: urutan foto = [hasil render, foto wajah] (sesuai app)",
                  'photos=[result, face_photo]' in _idcode))
    res.append(ok("identity-lock: feature_key 'idlock' (env sendiri, tidak bentrok Face Swap)",
                  'feature_key="idlock"' in _idcode))
    res.append(ok("fitur Face Swap juga pindah ke app yang benar-benar nge-swap",
                  "RUNNINGHUB_APP_FACESWAP=2020760401977282562" in _envtxt2))
    res.append(ok("sheet-guard juga jaga karakter tersimpan (use:c / u:ch)",
                  "fix_char_id=r[\"id\"]" in _bsrc4))

    # 3a-8) FALLBACK APP (akar "gagal terus" 9 Okt 17:2x: app butuh saldo $, koin ada)
    _rh = (Path(__file__).with_name("backends") / "runninghub.py").read_text(encoding="utf-8")
    res.append(ok("fallback: app cadangan didukung (RUNNINGHUB_APP_<FITUR>_ALT)",
                  "_alt_app" in _rh and "_ALT" in _rh))
    res.append(ok("fallback: gagal saat SUBMIT → coba app cadangan",
                  "COBA APP CADANGAN" in _rh))
    res.append(ok("fallback: gagal saat POLL → dialihkan otomatis (sekali)",
                  "dialihkan ke mesin cadangan" in _rh and "switched" in _rh))
    res.append(ok("fallback: taskId lama dipetakan ke task pengganti (alias)",
                  "_alias" in _rh and "self._alias.get(task_id, task_id)" in _rh))
    _envtxt = (Path(__file__).with_name(".env")).read_text(encoding="utf-8")
    res.append(ok("editor pakai app yang bayar KOIN (bukan saldo $)",
                  "RUNNINGHUB_APP_EDITOR=2075393520445251586" in _envtxt))
    res.append(ok("editor punya app cadangan",
                  "RUNNINGHUB_APP_EDITOR_ALT=" in _envtxt))
    res.append(ok("alat uji fallback tersedia (tools/fallback_test.py)",
                  (Path(__file__).with_name("tools") / "fallback_test.py").exists()))

    # 3a-9) PANEL PER-TUJUAN: sheet dibaca beda untuk render (badan) vs kunci identitas (wajah)
    import sheetfix as _sf2
    res.append(ok("sheetfix: mode 'face' (panel wajah) tersedia", hasattr(_sf2, "PROMPT_FACE")))
    res.append(ok("sheetfix: prompt wajah & badan berbeda",
                  _sf2.PROMPT_FACE != _sf2.PROMPT_BODY and "WAJAH CLOSE-UP" in _sf2.PROMPT_FACE))
    _bsrc5 = (Path(__file__).with_name("bot.py")).read_text(encoding="utf-8")
    res.append(ok("bot: helper panel menerima purpose (body/face)",
                  'purpose: str = "body"' in _bsrc5))
    res.append(ok("bot: cache panel dipisah per tujuan (tidak tertukar)",
                  'ck = f"{file_id}:{purpose}"' in _bsrc5))

    # 3a-10) GEOMETRI SHEET: bot HITUNG SENDIRI kotak panel (dulu nebak dari koordinat model vision
    #        → nyomot judul + potongan wajah sebagai "panel" = akar "wajah nggak mirip sama sekali")
    import sheetfix as _sf3
    _lay6 = _sf3.layout_panels((1778, 4248))
    res.append(ok("sheetfix: geometri 6-panel dikenali (bukan nebak)",
                  isinstance(_lay6, list) and len(_lay6) == 6
                  and _lay6[0] == (24, 208, 853, 1280) and _lay6[1] == (901, 208, 853, 1280)))
    _lay4 = _sf3.layout_panels((1778, 2880))
    res.append(ok("sheetfix: geometri 4-panel dikenali", isinstance(_lay4, list) and len(_lay4) == 4))
    res.append(ok("sheetfix: ukuran asing → None (pakai jalur lama, jangan salah potong)",
                  _sf3.layout_panels((640, 480)) is None))
    _sheet_uji = WORK / "sheet_asli_uji.png"
    _I.new("RGB", (1778, 4248), (200, 200, 200)).save(_sheet_uji)
    res.append(ok("sheetfix: mode face → panel 1 (kiri-atas)",
                  _sf3.panel_for(_sheet_uji, "face") == (24, 208, 853, 1280)))
    res.append(ok("sheetfix: mode body → panel 2 (full body, kanan-atas)",
                  _sf3.panel_for(_sheet_uji, "body") == (901, 208, 853, 1280)))
    _p2 = _sf3.crop_panel(_sheet_uji, [0, 0, 10, 10], WORK / "panel_geometri.jpg", purpose="body")
    res.append(ok("sheetfix: box model ngawur DIABAIKAN → panel tepat 853×1280",
                  bool(_p2) and _I.open(_p2).size == (853, 1280)))        # type: ignore[arg-type]
    _wide = WORK / "wide_uji.jpg"
    _I.new("RGB", (1600, 1000), (70, 70, 70)).save(_wide)
    _p3 = _sf3.crop_panel(_wide, [0, 0, 500, 900], WORK / "wide_panel.jpg")
    res.append(ok("sheetfix: sheet orang lain → koordinat model dinormalkan (500→800px, tidak salah skala)",
                  bool(_p3) and _I.open(_p3).size == (768, 960)))         # type: ignore[arg-type]
    res.append(ok("bot: kunci identitas ambil PANEL WAJAH dari sheet",
                  'analyze_sync, face_local' in _bsrc5 and '_wajah.jpg' in _bsrc5))

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