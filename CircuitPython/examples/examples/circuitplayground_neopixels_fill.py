import array
import math
import board
import audiobusio
from adafruit_circuitplayground import cp
import time
import board
from rainbowio import colorwheel
import neopixel
import random
pin = board.A1
no_of_pixels = 50
pixels = neopixel.NeoPixel(pin, no_of_pixels, brightness=0.3, auto_write=False)
while 1:
    for i in range(50):
        pixels[i] = (255, 0, 0)
        pixels.show()
        time.sleep(0.01)
    for i in range(50):
        pixels[i] = (204, 48, 20)
        pixels.show()
        time.sleep(0.01)
    for i in range(50):
        pixels[i] = (204, 130, 27)
        pixels.show()
        time.sleep(0.01)
    for i in range(50):
        pixels[i] = (227, 205, 9)
        pixels.show()
        time.sleep(0.01)
    for i in range(50):
        pixels[i] = (152, 189, 8)
        pixels.show()
        time.sleep(0.01)
    
        time.sleep(0.01)
    for i in range(50):
        pixels[i] = (0, 255, 0)
        pixels.show()
        time.sleep(0.01)
    for i in range(50):
        pixels[i] = (0, 255, 110)
        pixels.show()
        time.sleep(0.01)
    for i in range(50):
        pixels[i] = (23, 235, 157)
        pixels.show()
        time.sleep(0.01)
    for i in range(50):
        pixels[i] = (9, 232, 232)
        pixels.show()
        time.sleep(0.01)
    for i in range(50):
        pixels[i] = (20, 227, 227)
        pixels.show()
        time.sleep(0.01)
    for i in range(50):
        pixels[i] = (8, 127, 191)
        pixels.show()
        time.sleep(0.01)
    for i in range(50):
        pixels[i] = (10, 101, 247)
        pixels.show()
        time.sleep(0.01)
    for i in range(50):
        pixels[i] = (10, 101, 247)
        pixels.show()
        time.sleep(0.01)
    for i in range(50):
        pixels[i] = (37, 3, 255)
        pixels.show()
        time.sleep(0.01)
    for i in range(50):
        pixels[i] = (83, 4, 209)
        pixels.show()
        time.sleep(0.01)
    for i in range(50):
        pixels[i] = (167, 20, 224)
        pixels.show()
        time.sleep(0.01)
    for i in range(50):
        pixels[i] = (217, 38, 237)
        pixels.show()
        time.sleep(0.01)
    for i in range(50):
        pixels[i] = (171, 15, 114)
        pixels.show()
        time.sleep(0.01)
    
    for i in range(50):
        pixels[i] = (255, 15, 127)
        pixels.show()
        time.sleep(0.01)
    for i in range(50):
        pixels[i] = (191, 38, 71)
        pixels.show()
        time.sleep(0.01)
    