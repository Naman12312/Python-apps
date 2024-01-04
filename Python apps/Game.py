import pygame
import random
import time
time1 = time.strftime("%H:%M:%S")
str1 = '9:00:00'
if time1>str1:
    print("Hello")
else:
    print("oh")
x = random.randrange(-5,5)
y = random.randrange(-5,5)
pygame.init()
screen=pygame.display.set_mode((400,666))
font=pygame.font.SysFont(None,55)
def text_screen(text,x,y,color):
    f = font.render(text,True,color)
    screen.blit(f,(x,y))
def gameloop():
    clock=pygame.time.Clock()
    fps=60
    black=(0,0,0)
    white=(255,255,255)
    sizex=100
    sizey=30
    px=200
    py=400
    cx=250
    cy=400
    cvx=5
    cvy=5
    lx=0
    ly=560
    pygame.display.set_caption("Bounce!")
    screen.fill(white)
    pygame.display.update()
    game_over=False
    c=False
    while not c:
        pygame.init()
        if game_over:
            screen.fill((255,255,255))
            text_screen("Game over!",100,200,(0,0,0))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        gameloop()
            pygame.display.update()

        else:            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    c=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        px+=50
                    if event.key==pygame.K_LEFT:
                        px+=-50
            cx=cx+-cvx
            cy=cy+-cvy
            screen.fill(white)
            line = pygame.image.load("F:\\downloads\\line.png")
            t=pygame.draw.rect(screen,black,[px,py,sizex,sizey])
            cir=pygame.draw.circle(screen,black,[cx,cy],10)   
            screen.blit(line,(lx,ly))
            if cx>400:
                cvx=5
                cvy=-5
            if cy>666:
                cvy=5
                cvx=-5
            if cy<0:
                cvy = -5
                cvx = -5
            if cx<0:
                cvy=5
                cvx=-5
            
            if abs(px-cx)<50 and abs(py-cy)<50:
                cvy=5
                cvx=5
            if abs(cx-lx)<100 and abs(cy-ly)<100:
                game_over=True
            clock.tick(fps)
            pygame.display.update()
    pygame.quit()
gameloop()
