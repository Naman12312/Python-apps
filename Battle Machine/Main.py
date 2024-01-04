import pygame
import sys
import os
import time
# import asyncio
import threading
# os.chdir("../")
pygame.init()
screen = pygame.display.set_mode((1000, 650))
pygame.display.set_caption("Battle Machine")
clock = pygame.time.Clock()
cross = True
sleepcount = 1
font = pygame.font.SysFont(None, 55)
def text_screen(text, color, ax, ay):
    fg = font.render(text, True, color)
    screen.blit(fg, (ax,ay))
def waitandtrue():
    global cross
    global sleepcount
    time.sleep(sleepcount)
    cross = True
    sleepcount-=0.05
def GameLoop():
    global cross
    pygame.mixer.music.load("Koven - Never Have I Felt This [NCS Release].mp3")
    pygame.mixer.music.play(999999)
    game_over = False
    jump = False
    wizardx = 100
    wizardy = 360
    pekkax = 800
    pekkay = 350
    pekkav = -20
    score = 0
    v = 5
    m = 1
    while True:
        if game_over:
            text_screen("Game Over! Press Enter to play again.", (255,0, 0), 200, 200)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
            pygame.display.update()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if jump == False:
                        if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                            jump = True
                    if event.key == pygame.K_RIGHT:
                        wizardx += 100
                    if event.key == pygame.K_LEFT:
                        wizardx += -100
            if jump:
                f = (7/1)*m*(v**2)
                wizardy -= f
                v = v-1
                if v<0:
                    m = -1
                if v == -6:
                    jump = False
                    v = 5
                    m = 1 
            screen.fill((255,255,255))
            bg = pygame.image.load("bg.png")
            bg = pygame.transform.scale(bg,(1000,650)).convert_alpha()
            wizard = pygame.image.load("battle machine.png")
            wizard = pygame.transform.scale(wizard, (250,250)).convert_alpha()
            pekka = pygame.image.load("pekka.png")
            pekka = pygame.transform.scale(pekka, (200,200)).convert_alpha()
            # pekka = pygame.transform.flip(pekka, True, False)
            if abs(pekkax - wizardx) < 100 and abs(pekkay - wizardy)<100:
                game_over = True
            elif abs(pekkax-wizardx)<200 and cross:
                cross=False
                
                score+=1
                t = threading.Thread(target=waitandtrue)
                t.start()
                # t.join()
                pekkav-=1
            # print(score)
                # asyncio.run(waitandtrue())
                # value+=


            
            screen.blit(bg, (0,0))
            screen.blit(wizard, (wizardx , wizardy))
            screen.blit(pekka, (pekkax, pekkay))
            if pekkax < -419:
                pekkax = 1000
            pekkax = pekkax + pekkav
            clock.tick(400)
            text_screen(f"Score: {int(score)}", (0,0,0), 70, 0)
            pygame.time.delay(10)
            
            pygame.display.update()
def welcome():
    pygame.mixer.music.load("Koven - Never Have I Felt This [NCS Release].mp3")
    pygame.mixer.music.play()
    bg = pygame.image.load("bg.png")
    bg = pygame.transform.scale(bg,(1000,650)).convert_alpha()
    screen.blit(bg, (0,0))
    text_screen("Welcome to Battle Machine!", (0,0,0), 100, 100)
    text_screen("Made my Naman Sharma!", (0,0,0), 100, 200)
    text_screen("Press enter to start!", (0,0,0), 100, 300)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    GameLoop()
        pygame.display.update()
            
# GameLoop()
welcome()

