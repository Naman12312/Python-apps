import pyautogui
pyautogui.FAILSAFE = False
def hit(key):
    pyautogui.press(key)
while True:
    hit("numlock")
    hit("capslock")
    hit("scrolllock")