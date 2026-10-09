#!/usr/bin/env python3
"""Katalog app RunningHub + BINDING NODE yang benar (diambil dari invokeExample).

Kenapa penting: selama ini node id app ditebak-tebak dan sering salah (mis. face swap yang ternyata
no-op). Setiap app di `/openapi/v2/aiapp/list` membawa `invokeExample` = contoh curl lengkap yang
berisi `nodeInfoList` (nodeId + fieldName + fieldValue + description). Dari situ binding PASTI.

Pakai:
  ./.venv/bin/python tools/rh_apps.py pull [jumlah_halaman]     # ambil & simpan katalog
  ./.venv/bin/python tools/rh_apps.py find <kata_kunci> [...]   # cari app + binding-nya
  ./.venv/bin/python tools/rh_apps.py show <appId>              # binding satu app
"""
from __future__ import annotations

import json
import re
import sys
import urllib.request
from pathlib import Path

BASE = "https://www.runninghub.ai"
CACHE = Path(__file__).resolve().parent.parent / "work" / "rh_apps.json"
KEYFILE = Path("/root/.secrets/runninghub_shared.key")


def _key() -> str:
    return KEYFILE.read_text().strip()


def _post(path: str, payload: dict) -> dict:
    req = urllib.request.Request(
        BASE + path, data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {_key()}"},
        method="POST")
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def parse_bindings(invoke: str) -> list[dict]:
    """Ambil daftar {nodeId, fieldName, fieldValue, description} dari invokeExample (curl)."""
    i = invoke.find("nodeInfoList")
    if i < 0:
        return []
    raw = invoke[i:]
    # ambil objek JSON seimbang mulai dari '[' pertama
    b = raw.find("[")
    depth, end = 0, -1
    for k, ch in enumerate(raw[b:], start=b):
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
            if depth == 0:
                end = k
                break
    if end < 0:
        return []
    body = raw[b:end + 1]
    # invokeExample biasanya sudah JSON valid, tapi sering ada escape \\\" → bersihkan
    body = body.replace('\\"', '"').replace("\\n", " ")
    try:
        items = json.loads(body)
    except Exception:                                      # noqa: BLE001
        # fallback: regex per objek
        items = []
        for m in re.finditer(r"\{[^{}]*\}", body):
            try:
                items.append(json.loads(m.group(0)))
            except Exception:                              # noqa: BLE001
                pass
    out = []
    for it in items:
        if not isinstance(it, dict) or "nodeId" not in it:
            continue
        out.append({"nodeId": str(it.get("nodeId")), "fieldName": str(it.get("fieldName") or ""),
                    "fieldValue": str(it.get("fieldValue") or "")[:60],
                    "description": str(it.get("description") or "")[:60]})
    return out


def pull(pages: int = 3, size: int = 50) -> dict:
    """Tarik katalog (HOTTEST + NEWEST) dan simpan ke work/rh_apps.json."""
    apps: dict[str, dict] = {}
    for sort in ("HOTTEST", "NEWEST"):
        for page in range(1, pages + 1):
            try:
                d = _post("/openapi/v2/aiapp/list", {"current": page, "size": size, "sort": sort})
            except Exception as e:                          # noqa: BLE001
                print(f"  halaman {sort} {page}: gagal ({e})")
                break
            recs = ((d.get("data") or {}).get("records")) or []
            if not recs:
                break
            for r in recs:
                inv = str(r.get("invokeExample") or "")
                aid = ""
                m = re.search(r"run/ai-app/(\d+)", inv) or re.search(r"webappId[\"']?\s*[:=]\s*[\"']?(\d+)", inv)
                if m:
                    aid = m.group(1)
                aid = aid or str(abs(hash(str(r.get("title")))) % 10 ** 18)
                apps[aid] = {"appId": aid, "title": str(r.get("title") or "").strip(),
                             "description": str(r.get("description") or "").strip()[:160],
                             "bindings": parse_bindings(inv)}
            print(f"  {sort} hal {page}: {len(recs)} app (total {len(apps)})")
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(apps, ensure_ascii=False, indent=1))
    return apps


def load() -> dict:
    if CACHE.exists():
        return json.loads(CACHE.read_text())
    return pull()


def find(words: list[str], limit: int = 12) -> list[dict]:
    apps = load()
    hits = []
    for a in apps.values():
        blob = (a["title"] + " " + a["description"]).lower()
        if all(w.lower() in blob for w in words):
            hits.append(a)
    return hits[:limit]


def show(app_id: str) -> dict | None:
    return load().get(app_id)


def main() -> int:
    cmd = sys.argv[1] if len(sys.argv) > 1 else "help"
    if cmd == "pull":
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 3
        apps = pull(pages=n)
        print(f"✅ katalog: {len(apps)} app → {CACHE}")
        return 0
    if cmd == "find":
        for a in find(sys.argv[2:] or ["face"]):
            b = " · ".join(f"{x['nodeId']}:{x['fieldName']}={x['fieldValue']}" for x in a["bindings"])
            print(f"[{a['appId']}] {a['title']}\n     {b or '(bindings kosong)'}")
        return 0
    if cmd == "show":
        a = show(sys.argv[2])
        print(json.dumps(a, ensure_ascii=False, indent=1) if a else "tidak ada")
        return 0
    print(__doc__)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())