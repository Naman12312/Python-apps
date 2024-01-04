from adafruit_circuitplayground import cp
import time
import random
l = [0,1,2,3,4,5,6,7,8,9]
red = 25
x = len(l)
print(x)
while True:
        if cp.button_a:            
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
        if cp.button_b:
            for i in l:
                cp.pixels[i] = (25,0,0)
                cp.pixels[i-1] = (0,0,0)
                time.sleep(0.1)
            for i in range(9,0,-1):
                cp.pixels[i-1] = (0,25,0)
                cp.pixels[i] = (0,0,0)
                time.sleep(0.1)
            for i in l:
                cp.pixels[i] = (0,0,25)
                cp.pixels[i-1] = (0,0,0)
                time.sleep(0.1)
            for i in range(9,0,-1):
                cp.pixels[i-1] = (25,25,0)
                cp.pixels[i] = (0,0,0)
                time.sleep(0.1)
            for i in l:
                cp.pixels[i] = (0,0,0)
                cp.pixels[i-1] = (0,0,0)
                time.sleep(0.1)
            #cp.pixels.fill((0,0,0))
#range(9, -1, -1)
    