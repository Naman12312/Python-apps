from adafruit_circuitplayground import cp
from adafruit_circuitplayground.express import cpx
import time
x = 0
l = [0,1,2,3,4,5,6,7,8,9]
#cp.pixels.fill((0,25,0))
while True:
    time.sleep(0.1)
    if cp.light > 5 and x == 0:
        for i in l:
            cp.pixels[i] = (5,0,0)
            time.sleep(0.03)
        #cp.pixels.fill((0,0,0))
        for j in range(9, -1, -1):
            cp.pixels[j] = (0,5,0)
            time.sleep(0.03)
        for j in l:
            cp.pixels[j] = (0,0,5)
            time.sleep(0.03)
        for j in range(9,-1,-1):
            cp.pixels[j] = (5,5,0)
            time.sleep(0.03)
        for i in l:
            cp.pixels[i] = (0,0,0)
            time.sleep(0.03)
        cp.play_file("m.wav")
        cp.play_file("m.wav")
        cp.play_file("m.wav")
        cp.play_file("m.wav")

    if cp.light < 5:
       pass
#cpx.play_tone(220, 0.5)
    if cp.button_b:
        time.sleep(0.01)
        if cp.button_b:
            while True:
                cpx.play_tone(22220, 0)
                x = 1
                print("B")
                for i in l:
                    cp.pixels[i] = (25,0,0)
                    cp.pixels[i-1] = (0,0,0)
                    time.sleep(0.1)
                for i in range(9,0,-1):
                    cp.pixels[i-1] = (25,0,0)
                    cp.pixels[i] = (0,0,0)
                    time.sleep(0.1)
                for i in l:
                    cp.pixels[i] = (25,0,0)
                    cp.pixels[i-1] = (0,0,0)
                    time.sleep(0.1)
                for i in range(9,0,-1):
                    cp.pixels[i-1] = (25,0,0)
                    cp.pixels[i] = (0,0,0)
                    time.sleep(0.1)
                for i in l:
                    cp.pixels[i] = (25,0,0)
                    cp.pixels[i-1] = (0,0,0)
                    time.sleep(0.1)
                for i in range(9,0,-1):
                    cp.pixels[i-1] = (25,0,0)
                    cp.pixels[i] = (0,0,0)
                    time.sleep(0.1)

            #break
                    x = 1
                if cp.button_a:
                        time.sleep(0.01)
                        if cp.button_a:
                            x = 0
                            for i in l:
                                cp.pixels[i] = (25,0,0)
                                cp.pixels[i-1] = (0,0,0)
                                time.sleep(0.03)
                            for i in range(9,0,-1):
                                cp.pixels[i-1] = (0,25,0)
                                cp.pixels[i] = (0,0,0)
                                time.sleep(0.03)
                            for i in l:
                                cp.pixels[i] = (0,0,25)
                                cp.pixels[i-1] = (0,0,0)
                                time.sleep(0.03)
                            for i in range(9,0,-1):
                                cp.pixels[i-1] = (25,25,0)
                                cp.pixels[i] = (0,0,0)
                                time.sleep(0.03)
                            for i in l:
                                cp.pixels[i] = (0,0,0)
                                cp.pixels[i-1] = (0,0,0)
                                time.sleep(0.03)
                            break

