from tkinter import font
import pygame
import sys
import random
import time
pygame.init()
screen = pygame.display.set_mode((900,600))
pygame.display.set_caption("Slammer Rage")
ssx = 200
ssy = 300
ssv = 0
lv = 10
score = 0
linex = random.randint(0, 850)
game_over = False
liney = 0 
font23 = pygame.font.SysFont(None, 55)
def gameloop():
    global font23
    global game_over
    global score
    global ssx, ssy, ssv
    global linex, liney,lv
    def text_screen(text, color, x,y):
        font1 = font23.render(text, True, color)
        screen.blit(font1, (x,y))
    while True:
        if game_over:
            screen.fill((0,255,0))
            text_screen("Game Over!", (0,0,0), 255,255)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # gameloop()
                        print('h')
                        game_over = False
                        ssx = 200
                        ssy = 300
                        ssv = 0
                        lv = 10
                        score = 0
                        linex = random.randint(0, 850)
                        game_over = False
                        liney = 0 
                        
            pygame.display.update()
        else:
            print('hoy')
            game_over = False
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        ssv = -30
                    if event.key == pygame.K_RIGHT:
                        ssv = 30
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        ssv = 0
                    if event.key == pygame.K_RIGHT:
                        ssv = 0
            ssx = ssx+ssv
            liney = liney+ lv
            
            if liney>600:
                liney = 0
                linex = random.randint(0, 500)
            if abs(linex-ssx)<150 and abs(liney-ssy)<120:
                # quit()
                game_over = True
            # print(score)

            else:
                if liney>ssy:

                    score+=0.04
                # time.sleep(0.2)
                    print(int(score))
            if ssx>700 or ssx<0:
                ssv = 0
            screen.fill((0,255,0))     
            ss = pygame.image.load("stone slammer.png")
            ss = pygame.transform.scale(ss, (170,200))   
            # line = pygame.draw.line(screen, (0,0,0), (100,200), (200,100))
            line1 = pygame.image.load("line.png")
            line1 = pygame.transform.scale(line1, (300,200))
            screen.blit(line1, (linex,liney))
            # line2 = pygame.image.load("line.png")
            # line2 = pygame.transform.scale(line2, (300,200))
            # screen.blit(line1, (linex,liney))
            # screen.blit(line2, (linex,liney))

            screen.blit(ss, (ssx,ssy))
            # print(score)
            pygame.display.update()
gameloop()