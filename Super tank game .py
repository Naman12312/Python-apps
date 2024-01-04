import pygame
import sys
g=pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("F:\\downloads\\back.mp3")
pygame.mixer.music.play()
clock=pygame.time.Clock()
pygame.display.set_caption("Super Tank with Naman")
x=pygame.display.set_mode((650,400))
green=(0,255,0)
font=pygame.font.SysFont(None,55)
def scorev(text,color,t,u):
    fg=font.render(text,True,color)
    x.blit(fg,[t,u])
k=False
def welcome():
    pygame.image.load("F:\\downloads\\h.png")
    scorev("Welcome to tank with naman",green,100,100)
    pygame.display.update()
    while not k:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    gameloop()
def gameloop():
    red=(255,0,0)
    blue=(0,255,0)
    gameover=False
    atx=500
    aty=300
    btx=0
    bty=300
    l1=3
    l2=3
    aa=0
    a3=0
    a2x=550
    a2y=350
    p=pygame.image.load("F:\\downloads\\h.png")
    a=pygame.image.load("F:\\downloads\\a.png")
    b=pygame.image.load("F:\\downloads\\b.png")
    a1x=50
    a1y=350 
    pygame.display.update()
    while not k:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        atx=atx+5
                        a2x=a2x+5
                    if event.key==pygame.K_DOWN:
                        a3=-2
                    if event.key==pygame.K_LEFT:
                        atx=atx+-5
                        a2x=a2x+-5
                    if event.key==pygame.K_a:
                        btx=btx+-5
                        a1x=a1x+-5
                    if event.key==pygame.K_d:
                        btx=btx+5
                        a1x=a1x+5
                    if event.key==pygame.K_s:
                        aa=2
                    if gameover:
                        scorev("game over press enter to continue or esc to quit",red,100,100)
                        if event.key==pygame.K_RETURN:
                            gameloop()

        a1x=a1x+aa
        a2x=a2x+a3
        x.blit(p,(0,0))
        x.blit(a,(atx,aty))
        x.blit(b,(btx,bty))
        a1=pygame.draw.circle(x,red,[a1x,a1y],5)
        a2=pygame.draw.circle(x,red,[a2x,a2y],5)
        if abs(a2x - btx)<60 and abs(a2y - bty)<60:
                    scorev("Game over press enter to continue",red,100,100)
                    gameover=True
        if abs(a1x - atx)<60 and abs(a1y - aty)<60:
                    scorev("Game over press enter to continue",red,100,100)
                    gameover=True
        pygame.display.update()
welcome()
clock.tick(30)
pygame.quit()
quit()
