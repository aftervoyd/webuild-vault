import sys, time
sys.path.insert(0,'/root/.hermes/cache/scratch')
from tg import *
msg = sys.argv[1]; tag = sys.argv[2]
sh(f'DISPLAY={DISP} xdotool windowactivate --sync {WIN}'); time.sleep(1)
sh(f'DISPLAY={DISP} xdotool mousemove 500 762 click 1'); time.sleep(1.5)
# bersihkan isi kotak
key("ctrl+a"); time.sleep(0.3); key("BackSpace"); time.sleep(0.5)
typ(msg); time.sleep(1); key("Return"); time.sleep(9)
p = shot(f"/tmp/rep_{tag}.png")
rows = ocr(p, (280,55,1275,730), scale=2, psm=6)
print(f"===== kirim: {msg} =====")
for t,x,y,c in rows:
    if c >= 55: print(f"({x:4},{y:4}) c{c:3} {t}")
