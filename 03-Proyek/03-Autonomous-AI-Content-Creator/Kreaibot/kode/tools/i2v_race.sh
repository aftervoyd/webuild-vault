#!/bin/bash
# Uji banding mesin i2v — SATU PER SATU (akun RunningHub cuma boleh 1 task bersamaan:
# dua task paralel ditolak dengan code 421 TASK_QUEUE_MAXED) + coba ulang otomatis kalau antre penuh.
cd /root/projects/kreaibot || exit 1
P="A masked man forcefully presses forward against the woman pinned to the wall in a single intense, continuous motion. The woman shudders with a dramatic emotional expression. The camera remains completely static, capturing the tense cinematic scene with low-key dramatic lighting, photoreal skin texture, and precise character identity consistent with the photo, free of morphing or distortion."

run() {   # $1=appId  $2=nodes  $3=keluaran
  for i in 1 2 3 4 5 6 7 8 9 10; do
    OUT=$(RH_PROBE_FEATURE=i2v ./.venv/bin/python tools/rh_edit_probe.py "$1" "$2" work/job_31/ref1.bin "$P" "$3" 2>&1 | tail -3)
    if echo "$OUT" | grep -q "SELESAI"; then echo "✅ $3 → $OUT"; return 0; fi
    echo "↻ percobaan $i gagal untuk $3: $(echo "$OUT" | tail -1)"; sleep 75
  done
  echo "❌ MENYERAH: $3"
}

run 2045286438090051585 '[{"nodeId":"27","fieldName":"image","value":"@photo1"},{"nodeId":"24","fieldName":"text","value":"@prompt"},{"nodeId":"22","fieldName":"value","value":"8"},{"nodeId":"21","fieldName":"value","value":"832"},{"nodeId":"48","fieldName":"value","value":"6"}]' work/tests/i2v_models/B_remixv2.mp4
run 2016829906864316418 '[{"nodeId":"85","fieldName":"image","value":"@photo1"},{"nodeId":"76","fieldName":"value","value":"960"},{"nodeId":"47","fieldName":"prompt","value":"@prompt"},{"nodeId":"82","fieldName":"value","value":"5"},{"nodeId":"89","fieldName":"prompt","value":"这是一个5秒的视频"}]' work/tests/i2v_models/C_wan22free.mp4
echo "=== SELESAI SEMUA UJI MESIN ==="