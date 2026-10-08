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
from db import Database

WORK = Path("/root/projects/kreaibot/work/selftest")
WORK.mkdir(parents=True, exist_ok=True)


def ok(label: str, cond: bool, extra: str = "") -> bool:
    print(f"{'✅' if cond else '❌'} {label}" + (f" — {extra}" if extra else ""))
    return cond


async def main() -> int:
    res = []

    # 1) katalog
    res.append(ok("katalog 7 fitur (termasuk UGC)", len(catalog.FEATURES) == 7, ", ".join(catalog.FEATURES)))
    f = catalog.get("allinone")
    res.append(ok("harga All-in-One (15 dtk) = 2.5 token", f is not None and f.cost == 2.5))
    i2v = catalog.get("i2v")
    res.append(ok("konversi Rp (10 tok = Rp10.000 → 1 tok = Rp1.000)",
                  catalog.price_rp(i2v, 10, 10_000) == 1000,
                  f"Rp{catalog.price_rp(i2v, 10, 10_000)}"))
    # HARGA SEHAT: biaya koin terukur × Rp/koin harus di bawah harga jual (margin ≥ 40%).
    # Angka koin dari render NYATA di RunningHub (5 dtk 4:3 = 70 · 15 dtk 9:16 = 269).
    RUPIAH_PER_KOIN, KOIN_TERUKUR = 4.46, {"i2v": 70, "allinone": 269, "ugc": 269}
    for key, koin in KOIN_TERUKUR.items():
        ft = catalog.get(key)
        harga = catalog.price_rp(ft, 10, 10_000)
        biaya = koin * RUPIAH_PER_KOIN
        margin = (harga - biaya) / harga * 100
        res.append(ok(f"margin {key} sehat ({margin:.0f}%)", margin >= 40,
                      f"harga Rp{harga:,} vs biaya Rp{biaya:,.0f}"))
    res.append(ok("durasi render dalam batas workflow (4..15 dtk)",
                  all(4 <= ft.duration <= 15 for ft in catalog.enabled_features()),
                  ", ".join(f"{ft.key}={ft.duration}s" for ft in catalog.enabled_features())))
    ugc = catalog.get("ugc")
    res.append(ok("fitur UGC ada & bertingkat", bool(ugc and ugc.kind == "ugc" and ugc.need_style
                                                     and ugc.char_first and ugc.product_slot),
                  f"{ugc.cost:g} token, Rp{catalog.price_rp(ugc, 10, 10_000)}" if ugc else ""))

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