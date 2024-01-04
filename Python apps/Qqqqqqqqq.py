import pygame
import random
clock=pygame.time.Clock()
#from win32com.client import *
q=pygame.init()
p=pygame.display.set_mode((900,600))
pygame.display.set_caption("Snake")
pygame.display.update()
keep_going=False
s_x=5
s_y=55
size=10
ricex=random.randint(15,900/2)
ricey=random.randint(15,600/2)
white=(255,255,255)
black=( 0, 0, 0)
red=(255,0,0)
xo=0
yo=0
fps=30
while not keep_going:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                keep_going=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    xo=7
                    yo=0
                if event.key==pygame.K_LEFT:
                    xo=-7
                    yo=0
                if event.key==pygame.K_UP:
                    yo=-7
                    xo=0
                if event.key==pygame.K_DOWN:
                    yo=7
                    xo=0
        s_x=xo+s_x
        s_y=yo+s_y
        score=0

        p.fill(white)
        pygame.draw.rect(p, black, [s_x, s_y, size, size])
        pygame.draw.rect(p, red, [ricex, ricey, size, size])
        if abs(s_x - ricex)<6 and abs(s_y - ricey)<6:
            score +=1
            print("Score:",score)
            ricex=random.randint(15,900/2)
            ricey=random.randint(15,600/2)

        pygame.display.update()
        clock.tick(fps)
        pygame.display.update()

pygame.quit()
quit()
