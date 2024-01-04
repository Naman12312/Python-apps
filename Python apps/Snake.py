import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import random
clock=pygame.time.Clock()
pygame.init()
pygame.mixer.init()
# c=pygame.image.load("snakeba.png")
screen=pygame.display.set_mode((1000,600))
bgimg = pygame.image.load("D:\\drive D\\Downloads\\Python apps\\happy chicken\\maxresdefault.jpg")
bgimg = pygame.transform.scale(bgimg,(1000,600))
pygame.display.set_caption("Snake")
# icon=pygame.image.load("D:\\drive D\\downloads\\Python apps\\snake-icon.png")
# pygame.display.set_icon(icon)
font=pygame.font.SysFont(None,55)
def op(text,color,ax,ay):
        f=font.render(text,True,color)
        screen.blit(f,[ax,ay])
black=(0,0,0)
red=(255,0,0)
white=(255,255,255)
green=(0,0,45)
blue=(0,255,0)
def gameloop():
    newhi = False
    if not os.path.exists('D:\\drive D\\Downloads\\Python apps\\hiscoree.txt'):
        with open("D:\\drive D\\Downloads\\Python apps\\hiscoree.txt","w") as f:
            f.write("0")
    with open("D:\\drive D\\Downloads\\Python apps\\hiscoree.txt",'r') as f:
        p=f.read()
    score=0
    screen.fill(green)
    exit_game=False
    game_over=False
    snkvx=0
    snkvy=0
    snkx=470
    snky=270
    snk_len=1
    snk_list=[]
    ricex=random.randint(15,900/2)
    ricey=random.randint(15,600/2)
    FPS=28
    def plot_snk(screen,color,x,y,size):
        for x,y in snk_list:
            snk=pygame.draw.rect(screen,green,[x,y,size,size])
    while not exit_game:
            if game_over and not newhi:
                screen.blit(bgimg,(0,0))
                op("Game over! Press enter to continue.",red,170,290)
                op(f"Score: {str(score)}",red,370,390)
                with open('D:\\drive D\\Downloads\\Python apps\\hiscoree.txt','w') as f:
                    f.write(str(p))
                for event in pygame.event.get():
                     if event.type==pygame.QUIT:
                        pygame.quit()
                        exit()
                     if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_RETURN:
                            welcome()
                        if event.key==pygame.K_ESCAPE:
                            pygame.quit()
                            exit()
            elif game_over and newhi:
                screen.blit(bgimg,(0,0))
                op("Game over! Press enter to continue.",red,170,290)
                op(f"Score: {str(score)}",red,370,390)
                op("New Highscore!",red,330,460)
                with open('D:\\drive D\\Downloads\\Python apps\\hiscoree.txt','w') as f:
                    f.write(str(p))
                for event in pygame.event.get():
                     if event.type==pygame.QUIT:
                        pygame.quit()
                        exit()
                     if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_RETURN:
                            welcome()
                        if event.key==pygame.K_ESCAPE:
                            pygame.quit()
                            exit()
            
                # print("000000000002022022011111100101001010011010")
                # print(event)
            else:
                screen.blit(bgimg,(0,0))
                for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                            quit()
                        if event.type==pygame.KEYDOWN:
                            if event.key==pygame.K_RIGHT:
                                snkvx=10
                                snkvy=0

                            if event.key==pygame.K_LEFT:
                                snkvx=-10
                                snkvy=0
                            if event.key==pygame.K_UP:
                                snkvy=-10
                                snkvx=0
                            if event.key==pygame.K_DOWN:
                                snkvy=10
                                snkvx=0
                # print("000000000002022022011111100101001010011010")
                snkx=snkx+snkvx
                snky=snky+snkvy
                if abs(snkx-ricex)<25 and abs(snky-ricey)<25:
                            ricex=random.randint(20,900/2)
                            ricey=random.randint(20,600/2)
                            if abs(snkx-ricex)<30 and abs(snky-ricey)<30:
                                ricex=random.randint(20,900/2)
                                ricey=random.randint(20,600/2)
                            snk_len+=2
                            score+=1
                            if score>int(p):
                                p=score
                                newhi = True
                            else:
                                newhi=False
                if snkx<0 or snkx>1000 or snky<0 or snky>600:

                            game_over=True
                screen.blit(bgimg,(0,0))
                op("Score:"+str(score)+"   Highscore:"+str(p),red,0,0)
                head=[]
                head.append(snkx)
                head.append(snky)
                snk_list.append(head)
                rice=pygame.draw.rect(screen,red,[ricex,ricey,20,20])
                if len(snk_list)>snk_len:
                    del snk_list[0]
                if head in snk_list[:-1]:
                    game_over=True
                plot_snk(screen,black,snk_list,20,20)
            pygame.display.update()
            clock.tick(FPS)
def welcome():
    keep_going=False
    while not keep_going:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    gameloop()
        screen.blit(bgimg,[0,0])
        op("Welcome to Snakes by GoldarmGang!",blue,140,200)
        op("Press enter to start!",blue,300,300)
        pygame.display.update()
screen.fill(black)
pygame.display.update()
welcome()
pygame.quit()
quit()
