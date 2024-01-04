import random
import sys
import pygame
from pygame.locals import *
FPS=60
SCREENWIDTH=289
SCREENHEIGHT=511
SCREEN=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GROUNDY=SCREENHEIGHT*0.8
GAME_SPRITES={}
GAME_SOUNDS={}
PLAYER='F:\\downloads\\flappy bird.png'
BACKGROUND='F:\\downloads\\bg.png'
PIPE='F:\\downloads\\pipe.png'
exit_game=False
while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True
        
pygame.quit()
quit()