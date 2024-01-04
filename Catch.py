import random
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
pygame.init()
font=pygame.font.SysFont(None,55)
def text_screen(text,color,ax,ay):
        f=font.render(text,True,color)
        screen.blit(f,[ax,ay])
if __name__=="__main__":
    clock=pygame.time.Clock()
    fps=200
    screen=pygame.display.set_mode((900,600))
    pygame.mixer.init()
    a=pygame.mixer.music.load("F:\\Downloads\\back.mp3")
    pygame.mixer.music.play(9999)
    icon=pygame.image.load("F:\\downloads\\apple.png")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("CatchWithNaman")
    white=(255,255,255)
    def gameloop():
        with open("hiscore.txt",'rt') as f:
            hiscore=f.read()
        score=0
        l=3
        exit_game=False
        game_over=False
        screen.fill((255,255,255))
        applepsos=random.randrange(15,900/2)
        katorax=0
        appley=0
        applex=300
        appleyv=3
        katorav=0
        katoray=500
        katora=pygame.image.load("F:\\downloads\\katora.png")
        apple=pygame.image.load("F:\\downloads\\apple.png")
        while not exit_game:
            if game_over:
                with open("hiscore.txt",'w') as f:
                    f.write(str(hiscore))
                n=pygame.image.load("F:\\downloads\\gameover.png")
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_RETURN:
                            welcome()
                screen.blit(n,[0,0])
                pygame.display.update()
            else:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        quit()
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_RIGHT:
                            katorav=5
                        if event.key==pygame.K_LEFT:
                            katorav=-5
                    if event.type==pygame.KEYUP:
                        if event.key==pygame.K_RIGHT:
                            katorav=0
                        if event.key==pygame.K_LEFT:
                            katorav=0
                if appley<0 or appley>600:
                    applepsos=random.randrange(15,900/2)
                    appley=0 
                    l-=1
                if abs(katorax-applepsos)<60 and abs(katoray-appley)<60:
                    appley=0
                    applepsos=random.randrange(15,900/2)
                    score+=1
                    appleyv=3
                    if score>int(hiscore):
                        hiscore=score
                elif l==0:
                    game_over=True
                screen.fill(white)
                text_screen(f"Score:{score}"+"   highscore:"+str(hiscore),(0,0,0),50,50)
                text_screen(f"Life:{l}",(0,0,0),50,100)
                katorax=katorax+katorav
                appley=appley+appleyv
                screen.blit(katora,[katorax,katoray])
                screen.blit(apple,[applepsos,appley])
                # screen.fill((0,0,0))
                pygame.display.update()
                clock.tick(fps)
    def welcome():
        back=pygame.image.load("F:\\downloads\\back2.png")
        exit_game=False
        while not exit_game:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        gameloop()
            screen.blit(back,[0,0])
            text_screen("Welcome To CatchWithNaman",(0,255,0),0,0)
            text_screen("Press Enter To Start!!!!",(0,0,255),0,100)
            text_screen("Best Game Ever!!!!",(25,100,90),0,200)
            pygame.display.update()

    welcome()
    pygame.quit()
    quit()
