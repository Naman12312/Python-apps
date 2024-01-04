from adafruit_circuitplayground import cp
import time
x = 1
while True:
    if cp.touch_A1 and x==1:
            cp.pixels[-4] = (25,0,0)
            x=0
            time.sleep(0.1)
    if cp.touch_A1 and x==0:
            cp.pixels[-4] = (0,0,0)
            x=1
            time.sleep(0.1)
    