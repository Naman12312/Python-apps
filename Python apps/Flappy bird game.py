import pygame
import sys
pygame.init()
screen=pygame.display.set_mode((900,600))
exit_game=False
while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True
        if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
            exit_game=True
    # print(event)
pygame.quit()
sys.exit()