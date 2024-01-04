import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
# from numpy import asarray
import webbrowser as wb
import time


def hit(key):
    pyautogui.press(key)
    return

def isCollide(data):
    # Draw the rectangle for birds                     
    # for i in range(460, 490):
    #     for j in range(370, 380):
    #         if data[i, j] < 100:
    #             hit("up")         
    #             return
  
    for i in range(250, 350):
        for j in range(484,530):
                print(data[i,j]) 
                
            
            # elif data[i,j]>150 and data[i,j]<200:
            #     hit("space")
            #     print('Hello')
            #     return
            # elif data[i,j] > 100:
            #     hit('up')      
            #     return  
            # time.sleep(0.02)              
    return

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    import os
    time.sleep(3)
    while True:
        image = ImageGrab.grab().convert('L') 
        data = image.load()
        isCollide(data)
        # Draw the rectangle for cactus
        # for i in range(460, 570):
        #     for j in range(300, 360):
        #         data[i, j] =


        # for i in range(250, 350):
        #     for j in range(484,530):
        #             data[i, j] = 0
                       
        # image.show()
                    
        # break

