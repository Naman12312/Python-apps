import pygame
import random
import sys
pygame.init()
mariox=100
marioy=500
down=False
mariovy=0
black=(0,0,0)
white=(255,255,255)
clock=pygame.time.Clock()
fps=60
screen=pygame.display.set_mode((300,600))
mario = pygame.image.load("mario.png")
pipe = pygame.image.load("pipe.png")
back = pygame.image.load("back.png")
pygame.draw.rect(screen,black,[90,90,90,90])
clock.tick(fps)
screen.fill(white)
exit_game=False
while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x:
                mariovy=-0.1
            if event.key==pygame.K_c:
                mariovy=0
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_x:
                mariovy=0.1
    marioy=marioy+mariovy
    screen.blit(mario,[mariox,marioy]) 
    pygame.display.update()
