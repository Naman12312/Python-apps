import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((900,600))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255,255,255))     
    ss = pygame.image.load("stone slammer.png")
    ss = pygame.transform.scale(ss, (170,200))   
    # line = pygame.draw.line(screen, (0,0,0), (0,200), (200,100))
    screen.blit(ss, (0,0))
    pygame.display.update()