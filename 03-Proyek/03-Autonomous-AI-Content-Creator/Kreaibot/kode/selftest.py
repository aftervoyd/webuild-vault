#!/usr/bin/env python3
"""Self-test Kreaibot: cek katalog, ledger token, dan backend mock (render nyata via ffmpeg)."""
from __future__ import annotations

import asyncio
import subprocess
import sys
from pathlib import Path

import catalog
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
    res.append(ok("katalog 6 fitur", len(catalog.FEATURES) == 6, ", ".join(catalog.FEATURES)))
    f = catalog.get("allinone")
    res.append(ok("harga All-in-One = 1 token", f is not None and f.cost == 1.0))
    res.append(ok("konversi Rp (10 tok = Rp10.000 → 1 tok = Rp1.000)",
                  catalog.price_rp(f, 10, 10_000) == 1000, f"Rp{catalog.price_rp(f, 10, 10_000)}"))

    # 2) db + ledger
    db = Database(WORK / "test.sqlite3")
    db.ensure_user(123, "tester", "Tester", signup_bonus=1.0)
    res.append(ok("bonus daftar masuk", db.balance(123) == 1.0, f"saldo={db.balance(123)}"))
    db.ledger_add(123, 9.0, "topup_test")
    res.append(ok("top up 9 token", db.balance(123) == 10.0, f"saldo={db.balance(123)}"))
    jid = db.create_job(123, "allinone", 1.0, ["fid1", "fid2"], "prompt uji", "9:16")
    db.ledger_add(123, -1.0, "render", ref=str(jid))
    res.append(ok("potong biaya render", db.balance(123) == 9.0, f"saldo={db.balance(123)}"))
    res.append(ok("job tercatat", db.get_job(jid)["status"] == "queued"))
    db.ledger_add(123, 1.0, "refund", ref=str(jid))
    res.append(ok("refund gagal render", db.balance(123) == 10.0, f"saldo={db.balance(123)}"))

    # 3) backend mock → render video nyata
    be = make_backend("mock", work_dir=str(WORK))
    req = GenRequest(job_id=jid, feature_key="allinone", workflow="krea_allinone_h3",
                     photos=[], prompt="tes", ratio="9:16", out_path=WORK / "hasil-mock.mp4")
    tid = await be.submit(req)
    st = await be.poll(tid)
    res.append(ok("mock backend selesai", st.state == "done", st.message))
    out = Path(st.result_path) if st.result_path else None
    res.append(ok("file hasil ada", bool(out and out.exists()),
                  f"{out.stat().st_size if out and out.exists() else 0} byte" if out else "kosong"))
    if out and out.exists():
        pr = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "stream=width,height,codec_name", "-show_entries", "format=duration",
                             "-of", "default=noprint_wrappers=1", str(out)],
                            capture_output=True, text=True)
        print("   ffprobe →", " | ".join(pr.stdout.split()))
        res.append(ok("video valid (ffprobe)", pr.returncode == 0))

    print(f"\n{'='*46}\nHASIL: {sum(res)}/{len(res)} tes lulus")
    return 0 if all(res) else 1


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))