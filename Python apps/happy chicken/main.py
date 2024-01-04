import pygame
import random
import sys
pygame.init()

screen = pygame.display.set_mode((900,600))
chickenx = 350
lst = ['a','b','c','d','e','f','ds','sdf','dfss','dfsd','lj','ghgf','hgf']
chickeny = 250
egg = pygame.image.load('D:\\drive D\\Downloads\\Python apps\\happy chicken\\egg.png')
egg = pygame.transform.scale(egg, (150, 150))
chicken = pygame.image.load('D:\\drive D\\Downloads\\Python apps\\happy chicken\\chicken.png')
chicken = pygame.transform.scale(chicken, (150,150))

chickenvel = 0
class Egg:
    def __init__(self, surface, x, y, egg):
        self.surface = surface
        self.x = x
        self.y = y
        self.egg = egg

    def draw(self):
        self.surface.blit(self.egg, (self.x, self.y))


eggs = []
while True:
    x = 2
    screen.fill((0, 78, 255))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            chickenx, chickeny = pygame.mouse.get_pos()
            print('new egg')
            eggObject = Egg(screen, chickenx+5, chickeny, egg)
            eggs.append(eggObject)
            screen.blit(chicken, (chickenx,chickeny))
            
    # chickeny = chickenx+chickenvel
    for e in eggs:
        e.draw()
    x+=1
    screen.blit(chicken, (chickenx, chickeny))
    pygame.display.update()
