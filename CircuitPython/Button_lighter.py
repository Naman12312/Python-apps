import board
import time
import simpleio
import busio

from digitalio import DigitalInOut, Direction

led = simpleio.DigitalOut(board.D13)
button1 = DigitalInOut(board.D4)
button1.direction = Direction.INPUT
button2 = DigitalInOut(board.D5)
button2.direction = Direction.INPUT
led.value = False
while True:
    if button1.value is True:
        time.sleep(1)
        if button1.value is True:
            led.value = True
            time.sleep(0.5)
    elif button2.value is True:
        time.sleep(1)
        if button2.value is True:
            led.value = False
            time.sleep(0.5)