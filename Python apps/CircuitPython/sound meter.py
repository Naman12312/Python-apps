# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""This example uses the sound sensor, located next to the picture of the ear on your board, to
light up the NeoPixels as a sound meter. Try talking to your Circuit Playground or clapping, etc,
to see the NeoPixels light up!"""
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
no_of_pixels = 20
pixels = neopixel.NeoPixel(pin, no_of_pixels, brightness=0.3, auto_write=False)

def constrain(value, floor, ceiling):
    return max(floor, min(value, ceiling))


def log_scale(input_value, input_min, input_max, output_min, output_max):
    normalized_input_value = (input_value - input_min) / (input_max - input_min)
    return output_min + math.pow(normalized_input_value, 0.630957) * (
        output_max - output_min
    )


def normalized_rms(values):
    minbuf = int(sum(values) / len(values))
    return math.sqrt(
        sum(float(sample - minbuf) * (sample - minbuf) for sample in values)
        / len(values)
    )


mic = audiobusio.PDMIn(
    board.MICROPHONE_CLOCK, board.MICROPHONE_DATA, sample_rate=16000, bit_depth=16
)

samples = array.array("H", [0] * 160)
mic.record(samples, len(samples))
input_floor = normalized_rms(samples) + 10

# Lower number means more sensitive - more LEDs will light up with less sound.
sensitivity = 500
input_ceiling = input_floor + sensitivity

peak = 0
while True:
    mic.record(samples, len(samples))
    magnitude = normalized_rms(samples)
    magnitude = int(magnitude)

    if magnitude>20:
        no_of_pixels = magnitude//15
    elif magnitude<20:
        no_of_pixels = magnitude
    if no_of_pixels>20:
        no_of_pixels = 20



    for i in range(no_of_pixels):
        pixels[i] = (0,255,0)
        pixels.show()
        time.sleep(0.01)
    for j in range(0, 20):
        pixels[-j] = (0,0,0)
        pixels.show()
        time.sleep(0.01)




