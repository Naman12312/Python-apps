from unittest.mock import AsyncMockMixin
import pygame
import random
pygame.init()
a = pygame.display.set_mode((1000, 600))
exit_game = False
headx = 155
ammoxvel = 0
ammoxmove = 0
ammoymove = 0
ammoyvel = 0
heady = 155
headvelx = 0
headvely = 0
rectx = random.randint(0, 500)
recty = random.randint(0, 500)
rectvel = 1
gameover = False
ammox = 180
ammoy = 180
score = 0
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                headvelx = 1
                headvely = 0
                ammoxmove = 1
                ammoymove = 0
            if event.key == pygame.K_a:
                headvelx = -1
                headvely = 0
                ammoymove = 0
                ammoxmove = -1
            if event.key == pygame.K_w:
                headvely = -1
                headvelx = 0
                ammoymove = -1
                ammoxmove = 0
            if event.key == pygame.K_s:
                headvely = 1
                headvelx = 0
                ammoxmove = 0
                ammoymove = 1
            if event.key == pygame.K_RIGHT:
                ammoxvel = 5
                ammoyvel = 0
                ammoxmove = 0
                ammoymove = 0
            if event.key == pygame.K_LEFT:
                ammoxvel = -5
                ammoyvel = 0
                ammoxmove = 0
                ammoymove = 0
            if event.key == pygame.K_UP:
                ammoyvel = -5
                ammoxvel = 0
                ammoxmove = 0
                ammoymove = 0
            if event.key == pygame.K_DOWN:
                ammoyvel = 5
                ammoxvel = 0
                ammoxmove = 0
                ammoymove = 0
    headx += headvelx
    heady += headvely
    rectx += rectvel
    ammox += ammoxvel
    ammoy += ammoyvel
    ammox += ammoxmove
    ammoy += ammoymove
    # ammoy+=ammoyvelz
    if ammox < 0:
        ammox = headx
        ammoy = heady
        ammoxvel = 0
        ammoyvel = 0
        # ammoymove = 1
        # ammoxmove = 1
    if ammox > 1000:
        ammox = headx
        ammoy = heady
        ammoxvel = 0
        ammoyvel = 0
        # ammoymove = 1
        # ammoxmove = 1
    if ammoy < 0:
        ammox = headx
        ammoy = heady
        ammoxvel = 0
        ammoyvel = 0
        # ammoymove = 1
        # ammoxmove = 1
    if ammoy > 600:
        ammox = headx
        ammoy = heady
        ammoxvel = 0
        ammoyvel = 0
        # ammoymove = 1
        # ammoxmove = 1
    if rectx > 1000:
        rectx = 0
        recty = random.randint(0, 600)
    if headx > 910:
        print('Game Over!')
        exit()
    if headx < 10:
        print('Game Over!')
        exit()
    if heady > 570:
        print('Game Over!')
        exit()
    if heady < 10:
        print('Game Over!')
        exit()
    # print(rects
    if abs(headx-rectx) < 55 and abs(heady-recty) < 55:
        # print(abs(headx-ress
        # print('h')
        print("Game Over!")
        exit()
    if abs(rectx-ammox) < 55 and abs(recty-ammoy) < 55:
        # print('o')
        score += 1
        recty = random.randint(0, 600)
        rectx = 0
        # exit()
    print(score)
    # a.blit(boy, (0,0))
    head = pygame.image.load('pixlr-bg-result.png')

    head = pygame.transform.scale(head, (100, 100)).convert_alpha()
    a.fill((0, 250, 0))
    ammo = pygame.draw.rect(a, (0, 0, 0), [ammox, ammoy, 5, 5])

    a.blit(head, (headx, heady))
    boy = pygame.draw.rect(a, (0, 0, 0), [rectx, recty, 50, 50])
    pygame.display.update()
