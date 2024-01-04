import time
from adafruit_circuitplayground import cp

while True:
    print(cp.light)
    if cp.light <= 5:
        cp.pixels.fill((255,255,255))
    if cp.light > 5:
        cp.pixels.fill((0,0,0))
    time.sleep(1)