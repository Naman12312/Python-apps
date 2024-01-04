import pygame
import random
pygame.init()
green=(0,255,0)
screen=pygame.display.set_mode((900,600))
f=pygame.font.SysFont(None,55)
def text_screen(text,color,x,y):
    fg=f.render(text,True,color)
    screen.blit(fg,[x,y])
def main_game(): 
    chx=random.randint(0,600)
    chy=random.randint(0,900)
    FPS=1000
    LIFE=3
    clock=pygame.time.Clock()
    score=0
    exit_game=False
    ch=pygame.image.load("F:\\downloads\\untitled.png")
    while not exit_game:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
        wait2=pygame.time.wait(100)
        chx=random.randint(0,600/2)
        wait=pygame.time.wait(1000)  
        chy=random.randint(0,900/2)
        clock.tick(FPS)  
        pos=list(pygame.mouse.get_pos())
        pygame.display.update() 
        if abs(chx-pos[0])<200 and abs(chy-pos[1])<200:
            score=score+1
        else:
            LIFE=LIFE-1
        print("life:",LIFE) 
        if LIFE==0:
            exit_game=True 
        text_screen("score:"+str(score),green,5,5)
        text_screen("lfie:"+str(LIFE),green,0,0)
        screen.blit(ch,(chx,chy))
    pygame.display.update()         
    pygame.quit()

# def welcome():
main_game()
