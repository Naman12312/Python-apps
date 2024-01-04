import time
from adafruit_circuitplayground import cp

while True:
    print(f"Temp ~ C. : {cp.temperature}")
    if cp.temperature > 32:
        cp.pixels.fill((255, 0, 0))
    if cp.temperature < 31:
        cp.pixels.fill((0, 100, 0))
    if cp.temperature > 31:
        cp.pixels.fill((100, 0, 0))
    if cp.temperature < 25:
        cp.pixels.fill((0, 0, 100))
    if cp.temperature < 23:
        cp.pixels.fill((0, 0, 255))
    time.sleep(1)
