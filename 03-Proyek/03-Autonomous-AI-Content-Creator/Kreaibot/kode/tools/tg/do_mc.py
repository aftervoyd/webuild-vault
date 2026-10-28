import sys, time
sys.path.insert(0,'/root/.hermes/cache/scratch')
from tg import *
sh(f'DISPLAY={DISP} xdotool windowmove {WIN} 0 0'); sh(f'DISPLAY={DISP} xdotool windowsize {WIN} 1270 780')
time.sleep(2); sh(f'DISPLAY={DISP} xdotool windowactivate --sync {WIN}'); time.sleep(1)
# 1) tombol reply-keyboard: Generate Motion Control
click(590, 597); time.sleep(9)
p = shot("/tmp/mc_a.png")
rows = ocr(p, (285, 240, 1010, 560), scale=3, psm=6)
print("--- setelah pilih menu Motion (baris + koordinat) ---")
for t,x,y,c in rows:
    if c >= 45: print(f"  ({x:4},{y:4}) c{c:3} {t}")
