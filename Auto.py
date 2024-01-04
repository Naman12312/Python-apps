import pyautogui
from PIL import Image,ImageGrab
import time
def hit(key):
    pyautogui.keyDown(key)
def iscollide(data):
    for i in range(300,415):
        for j in range(410,400):
            if data[i,j] <100:
                hit("down")
                return True
    for i in range(230,350):
        for j in range(330,300):
            if data[i,j] <100:
                hit("up")
                return True
    return False
if __name__ == "__main__":
    print("Hey..dino game is about to start in 3 seconds..")
    time.sleep(3)
    hit("up")
    while True:
        image = ImageGrab.grab().convert("L")
        data = image.load()
        iscollide(data)
        # print(data)
        # for i in range(230,350):
        #     for j in range(330,380):
        #         data[i,j] = 0
        # for i in range(230,350):
        #     for j in range(230,270):
        #         data[i,j] = 171
        # image.show()
        # break
        


        
