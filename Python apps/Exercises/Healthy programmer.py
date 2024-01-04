import pygame
import time
import datetime
with open("healthy.txt", "w") as f:
    f.write("")
print("I will remind you when to do these:\ndrink water\neye exercise\nphysical exercise")
time2 = time.asctime()
# a = datetime.datetime.now().strftime("%H:%M:%S")
pygame.mixer.init()
sec = 0
eyesec = 0
physec = 0
second = int(sec)
time1 = time.strftime("%H:%M:%S")
a = time.asctime()
water = "F:\\downloads\\water.mp3"
eye = "F:\\downloads\\eyes.mp3"
physical = "F:\\downloads\\physical.mp3"
while True:
    time.sleep(1)
    physec+=1
    sec+=1
    eyesec+=1
    if sec==1800:
        pygame.mixer.music.load(water)
        pygame.mixer.music.play(999999999)
        print("Drink water now!!!","it's very important!!!")
        i1 = input("Type drank to stop")
        if i1=="drank":
            sec = 0
            pygame.mixer.music.stop()
            with open("healthy.txt", "a") as f:
                f.write(f"Drank water on {a}\n")
    if eyesec==3600:
        pygame.mixer.music.load(eye)
        pygame.mixer.music.play(9999999)
        print("Turn off computer now!!!","Eye Exercise time!!!")
        i2 = input("Type eyedone to stop")
        if i2=="eyedone":
            eyesec = 0
            pygame.mixer.music.stop()
            with open("healthy.txt", "a") as f:
                f.write(f"Eye exercise on {a}\n")
    if physec==2700:
        pygame.mixer.music.load(physical)
        pygame.mixer.music.play(9999999)
        print("Do some exericse now!!!","it's very important!!")
        i3 = input("Type phydone to stop")
        if i3=="phydone":
            physec = 0
            pygame.mixer.music.stop()
            with open("healthy.txt", "a") as f:
                f.write(f"Physical exercise on {a}\n")