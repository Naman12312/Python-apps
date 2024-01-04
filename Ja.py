import pygame
pygame.init()
tankx=300
tanky=450
tank2x=700
tank2y=0
tank2xv=-1/2
life=3
cirx=370
ciry=500
ciryv=0
cirxv=0
tankxv=0
tankyv=0
screen=pygame.display.set_mode((900,600))
exit_game=False
tank=pygame.image.load("tank.png")
tank2=pygame.image.load("tank2.png")
while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                ciryv=-1
            if event.key==pygame.K_RIGHT:
                tankxv=1
                cirxv=1
            if event.key==pygame.K_LEFT:
                tankxv=-1
                cirxv=-1
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                tankxv=0
                cirxv=0
            if event.key==pygame.K_RIGHT:
                tankxv=0
                cirxv=0
            
    tankx=tankx+tankxv
    tanky=tanky+tankyv
    ciry=ciry+ciryv
    cirx=cirx+cirxv
    tank2x=tank2x+tank2xv
    if ciry<0 or ciry>500 or cirx<0 or cirx>900:
        ciryv=0
        ciry=500
        life-=1
    if tank2x<0 or tank2x>900 or tank2y<0 or tank2y>900:
        tank2x=700
    elif abs(ciry-tank2y)<20:
        quit()
    screen.fill((255,255,255))
    screen.blit(tank,[tankx,tanky])
    screen.blit(tank2,[tank2x,tank2y])
    g1=pygame.draw.circle(screen,(255,0,0),[cirx,ciry],5)
    pygame.display.update()
    # print(event)
pygame.quit()
quit()