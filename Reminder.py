from tkinter import *
root = Tk()
root.title("GUI")
root.geometry("644x678")
root.mainloop()
exit()
from plyer import notification
import datetime
import time
import pygame
pygame.init()
play = False
pygame.mixer.init()
time1 = int(datetime.datetime.now().hour)
ti = 0
def notifyme(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = None,
        timeout = 15
    )
    pygame.mixer.music.load("F:\\Downloads\\closer.mp3")
    pygame.mixer.music.play()
    time.sleep(15)
    pygame.mixer.music.stop()
while True:
    break
    notifyme("Study Now!", "Study Right Now! with this music...")  
    time.sleep(10800)
