import pyautogui
import time
def hit(key,p):
    pyautogui.hotkey(key, p)
time.sleep(3)
while True:
    hit("ctrl", "r")