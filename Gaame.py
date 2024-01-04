import pygame
import random
x=pygame.init()
screen=pygame.display.set_mode((900,600))
font=pygame.font.SysFont(None,55)
def op(text,color,ax,ay):
        f=font.render(text,True,color)
        screen.blit(f,[ax,ay])
def gameloop():
    life=3
    exit_game=False
    car1=pygame.image.load("C:\\Users\\Naman Sharma\\Downloads\\Flappy bird\\CAR1.png")
    car2=pygame.image.load("C:\\Users\\Naman Sharma\\Downloads\\Flappy bird\\CAR2.png")
    car1x=300
    car1y=400
# car2x=300
    car1v=0
    car2y=50
    car2v=1
    car2x=random.randrange(20,900)
    while not exit_game:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    car1v=2
                if event.key==pygame.K_LEFT:
                    car1v=-2
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT:
                        car1v=0
                if event.key==pygame.K_LEFT:
                        car1v=0
        screen.fill((255,255,255))
        screen.blit(car1,[car1x,car1y])
        screen.blit(car2,[car2x,car2y])
        car2y=car2y+car2v
        car1x=car1x+car1v
        if car2y>600 or car2y<0:
            car2y=50
            car2x=random.randrange(20,900/2)
        if abs(car1x-car2x)<100 and abs(car1y-car2y)<100:
            car2v=0
            game_over()  
        pygame.display.update()
def game_over():
    exit_game=False
    while not exit_game:
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    gameloop()
        op("Game over!!!",(255,0,0),100,100)
        pygame.display.update()
    pygame.quit()
gameloop()