import pygame
pygame.init()
screen = pygame.display.set_mode((900,600))
jin1_jump=False
jin2_jump=False
jin1x = 0
jin1y = 270
jin2x = 700
jin2y=270
jin2xv = 0
jin1xv = 0
m = 1
v = 5
g1x=180
g1y=300
g2x=750
g2y=300
g1v = 0
g2v = 0
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                jin2_jump=True
            if event.key==pygame.K_w:
                jin1_jump=True  
            if event.key==pygame.K_a:
                jin1xv=-9
                g1v = -9
            if event.key==pygame.K_d:
                jin1xv=9
                g1v = 9
            if event.key==pygame.K_RIGHT:
                jin2xv=9
                g2v = 9
            if event.key==pygame.K_LEFT:
                jin2xv=-9
                g2v = -9
            if event.key==pygame.K_x:
                g1v = 9
            if event.key==pygame.K_RCTRL:
                g2v = -9
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_a:
                jin1xv=0
                g2v = 0
                g1v = 0
            if event.key==pygame.K_d:
                jin1xv=0
                g2v = 0
                g1v = 0
            if event.key==pygame.K_RIGHT:
                jin2xv=0
                g1v = 0
                g2v = 0
            if event.key==pygame.K_LEFT:
                jin2xv=0
                g1v = 0
                g2v = 0
    g1x+=g1v
    g2x+=g2v        
    jin1x+=jin1xv
    jin2x+=jin2xv
    screen.fill((255,255,255))
    jin1 = pygame.image.load("jin.png")
    jin1 = pygame.transform.scale(jin1,(230,230)).convert_alpha()
    jin2 = pygame.transform.flip(jin1,True,False)
    jin2 = pygame.transform.scale(jin2,(230,230)).convert_alpha()
    screen.blit(jin1,(jin1x,jin1y))
    screen.blit(jin2,(jin2x,jin2y))
    jin1g = pygame.draw.circle(screen,(0,0,0),(g1x,g1y),10,10)
    jin2g = pygame.draw.circle(screen,(0,0,0),(g2x,g2y),10,10)
    if jin1_jump:
        f = (5/1)*m*(v**2)
        jin1y-=f
        v=v-1
        if v<0:
            m=-1
        if v==-6:
            jin1_jump=False
            v=5
            m=1
    if jin2_jump:
        f = (10/1)*m*(v**2)
        jin2y-=f
        v=v-1
        if v<0:
            m=-1
        if v==-6:
            jin2_jump=False
            v=5
            m=1
    pygame.time.delay(40)
    if abs(g1x-jin2x)<60 and abs(g1y-jin2y)<100:
        quit()
    if abs(g2x-jin1x)<60 and abs(g2y-jin1y)<100:
        quit()
    pygame.display.update()