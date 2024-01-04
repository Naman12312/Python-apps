import time
import board
from rainbowio import colorwheel
import neopixel
import random
pin = board.A1
no_of_pixels = 20
pixels = neopixel.NeoPixel(pin, no_of_pixels, brightness=0.3, auto_write=False)
while True:    
    
    for i in range(0, 20):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        pixels[i] = ((r,g,b))
      
        pixels.show()