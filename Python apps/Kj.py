# from turtle import *
# t=Pen()
# t.reset()
# g=str(input("give a color"))
# t.fillcolor(g)



# t.begin_fill()
# for x in range(1, 38):
#     t.forward(100)
#     t.left(175)




# t.end_fill()
import pygame as pg
from gtts import gTTS
a = gTTS("Hello, I am google assistant!")
a.save('a.mp3')
pg.mixer.init()
b = pg.mixer.music.load("a.mp3")
pg.mixer.music.play()
while True:
    pass