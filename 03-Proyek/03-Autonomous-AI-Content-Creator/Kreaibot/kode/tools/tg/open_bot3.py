import sys, time
sys.path.insert(0, "/root/.hermes/cache/scratch")
from tg import *
sh(f'DISPLAY={DISP} xdotool windowfocus --sync {WIN}'); time.sleep(1.5)
key("ctrl+f"); time.sleep(2)
typ("motioncontrolpro"); time.sleep(3.5)
sh(f'DISPLAY={DISP} scrot -o /root/.hermes/cache/scratch/tg_s2.png')
key("Return"); time.sleep(6)
print("title:", sh(f'DISPLAY={DISP} xdotool getwindowname {WIN}').strip())
sh(f'DISPLAY={DISP} scrot -o /root/.hermes/cache/scratch/tg_s2b.png')
