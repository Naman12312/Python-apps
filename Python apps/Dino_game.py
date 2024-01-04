import pygame
from pygame.locals import *
import sys
pygame.init()
screen=pygame.display.set_mode((900,300))
cactusx = 800
cactusy = 110
cactusxvel = -1
dinox=100
dinoy=140
jumping = False
playerjumpvel = -8
dinominvel = -4
dinomaxvel = -11
playerfall = 100
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE or event.key==pygame.K_UP:
                if dinoy > 0:
                    dinoy = playerjumpvel
                    jumping = True
        if not jumping:
            dinoy+=playerfall
        if jumping:
                jumping=False
    cactusx = cactusx + cactusxvel
    screen.fill((255,255,255))
    base = pygame.image.load("F:\\downloads\\base (1).png")
    cactus = pygame.image.load("F:\\downloads\\cactus2 (1).png")
    dino = pygame.image.load("F:\\downloads\\Dino.png")
    screen.blit(base,(0,200))
    screen.blit(dino,(dinox,dinoy))
    screen.blit(cactus,(cactusx,cactusy))
    if cactusx<0 or cactusx<-800:
        cactusx=800
    if abs(dinox-cactusx)<60 and abs(dinoy-cactusy)<60:
        cactusxvel = 0
        print("Game over!")
    pygame.display.update()
