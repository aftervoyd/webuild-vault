#!/bin/bash
# Sinkron kode KREE.AI dari server ke vault Obsidian (folder kode/) lalu commit+push.
# Pakai: bash tools/sync_vault.sh "pesan singkat"
# AMAN: tidak pernah menyalin .env / .venv / work / *.sqlite3 (kredensial & data).
set -e
SRC=/root/projects/kreaibot
DST=/root/Documents/Webuild/03-Proyek/03-Autonomous-AI-Content-Creator/Kreaibot/kode
mkdir -p "$DST"
for f in "$SRC"/*.py "$SRC"/*.service "$SRC"/.env.example "$SRC"/README.md; do
  [ -e "$f" ] && cp -f "$f" "$DST"/
done
cp -rf "$SRC/backends" "$DST/" 2>/dev/null || true
cp -rf "$SRC/tools" "$DST/" 2>/dev/null || true
find "$DST" -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
cd /root/Documents/Webuild
git add -A
if git diff --cached --quiet; then
  echo "ℹ️ tak ada perubahan kode untuk di-commit"
else
  git commit -q -m "KREE.AI: sinkron kode — ${1:-update}"
  git push -q origin master:main
  echo "✅ sinkron + push: $(git log --oneline -1 origin/main)"
fi