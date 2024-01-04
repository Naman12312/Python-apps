import pygame
import sys
pygame.init()
screen = pygame.display.set_mode([900,700])
keep_going =True
g=str(input("enter the path\t"))
pic = pygame.image.load(g)
while keep_going:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(pic,(100,100))
    pygame.display.update()
