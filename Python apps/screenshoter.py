m = input("Tell the name of the file (with extention): ")
from PIL import Image, ImageGrab
from pygame import mixer
mixer.init()
import time
for i in range(3, 0, -1):
    print(f"Taking screenshot in {i}")
    # speak(f"{i}")
    time.sleep(1)
print(f"Taking screenshot in 0")
time.sleep(1)

a = ImageGrab.grab()
mixer.music.load("m.mp3")
mixer.music.play()
time.sleep(1)
a.save(f"{m}")
img = ImageGrab.Image.open(f"{m}")
img.show()