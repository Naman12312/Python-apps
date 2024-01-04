from adafruit_circuitplayground import cp
from adafruit_circuitplayground.express import cpx
import time
x = 0
cp.pixels.fill((0,25,0))
while True:
    time.sleep(0.5)
    if cp.light > 4 and x == 0:
        
    #cpx.play_tone(220, 0.5)
        cpx.play_tone(7000, 2)
    if cp.button_b:
        time.sleep(0.01)
        if cp.button_b:
            cpx.play_tone(0, 0)
            x = 1
            print("B")
            cp.pixels.fill((25,0,0))
            #break
    if cp.button_a:
            time.sleep(0.01)
            if cp.button_a:
                x = 0
                print("A")
                for i in l:
                    cp.pixels[i] = (25,0,0)
                    time.sleep(0.1)
                #cp.pixels.fill((0,0,0))
                for j in range(9, -1, -1):
                    cp.pixels[j] = (0,25,0)
                    time.sleep(0.1)
                for j in l:
                    cp.pixels[j] = (0,0,25)
                    time.sleep(0.1)
                for j in range(9,-1,-1):
                    cp.pixels[j] = (25,25,0)
                    time.sleep(0.1)
                for i in l:
                    cp.pixels[i] = (0,0,0)
                    time.sleep(0.1)
            
