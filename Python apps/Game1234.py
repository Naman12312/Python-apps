import pygame
import random
pygame.init()
screen=pygame.display.set_mode((300,600))
exit_game=False
youx=100
youy=100
yous=20
youvx=0
youvy=0
mass1x=random.randint(20,600/2)
mass1y=random.randint(20,600/2)
mass2x=random.randint(20,600/2)
mass2y=random.randint(20,600/2)
mass3x=random.randint(20,600/2)
mass3y=random.randint(20,600/2)
mass4x=random.randint(20,600/2)
mass4y=random.randint(20,600/2)
mass5x=random.randint(20,600/2)
mass5y=random.randint(20,600/2)
mass6x=random.randint(20,600/2)
mass6y=random.randint(20,600/2)
mass7x=random.randint(20,600/2)
mass7y=random.randint(20,600/2)
mass8x=random.randint(20,600/2)
mass8y=random.randint(20,600/2)
mass9x=random.randint(20,600/2)
mass9y=random.randint(20,600/2)
mass10x=random.randint(20,600/2)
mass10y=random.randint(20,600/2)
mass11x=random.randint(20,600/2)
mass11y=random.randint(20,600/2)
mass12x=random.randint(20,600/2)
mass12y=random.randint(20,600/2)
mass13x=random.randint(20,600/2)
mass13y=random.randint(20,600/2)
mass14x=random.randint(20,600/2)
mass14y=random.randint(20,600/2)
mass15x=random.randint(20,600/2)
mass15y=random.randint(20,600/2)
mass16x=random.randint(20,600/2)
mass16y=random.randint(20,600/2)
mass17x=random.randint(20,600/2)
mass17y=random.randint(20,600/2)
mass18x=random.randint(20,600/2)
mass18y=random.randint(20,600/2)
mass19x=random.randint(20,600/2)
mass19y=random.randint(20,600/2)
mass20x=random.randint(20,600/2)
mass20y=random.randint(20,600/2)
mass21x=random.randint(20,600/2)
mass21y=random.randint(20,600/2)
mass23x=random.randint(20,600/2)
mass23y=random.randint(20,600/2)
mass24x=random.randint(20,600/2)
mass24y=random.randint(20,600/2)
mass25x=random.randint(20,600/2)
mass25y=random.randint(20,600/2)
mass26x=random.randint(20,600/2)
mass26y=random.randint(20,600/2)
mass27y=random.randint(20,600/2)
mass27x=random.randint(20,600/2)
mass28y=random.randint(20,600/2)
mass28x=random.randint(20,600/2)
mass29y=random.randint(20,600/2)
mass29x=random.randint(20,600/2)
mass30y=random.randint(20,600/2)
mass30x=random.randint(20,600/2)
mass31y=random.randint(20,600/2)
mass31x=random.randint(20,600/2)
mass32y=random.randint(20,600/2)
mass32x=random.randint(20,600/2)
mass33y=random.randint(20,600/2)
mass33x=random.randint(20,600/2)
mass34y=random.randint(20,600/2)
mass34x=random.randint(20,600/2)
mass35y=random.randint(20,600/2)
mass36x=random.randint(20,600/2)
mass36y=random.randint(20,600/2)
mass37x=random.randint(20,600/2)
mass37y=random.randint(20,600/2)
while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                youvx=0.5
                youvy=0
            if event.key==pygame.K_LEFT:
                youvx=-0.5
                youvy=0
            if event.key==pygame.K_UP:
                youvy=-0.5
                youvx=0
            if event.key==pygame.K_DOWN:
                youvy=0.5
                youvx=0
    youx=youx+youvx
    youy=youy+youvy
    screen.fill((255,255,255))
    you=pygame.draw.circle(screen,(0,0,255),[youx,youy],yous)
    mass1=pygame.draw.circle(screen,(4,54,3),[mass1x,mass1y],5)
    mass2=pygame.draw.circle(screen,(4,54,3),[mass2x,mass2y],5)
    mass3=pygame.draw.circle(screen,(4,54,3),[mass3x,mass3y],5)
    mass4=pygame.draw.circle(screen,(4,54,3),[mass4x,mass4y],5)
    mass5=pygame.draw.circle(screen,(4,54,3),[mass5x,mass5y],5)
    mass6=pygame.draw.circle(screen,(4,54,3),[mass6x,mass6y],5)
    mass7=pygame.draw.circle(screen,(4,54,3),[mass7x,mass7y],5)
    mass8=pygame.draw.circle(screen,(4,54,3),[mass8x,mass8y],5)
    mass9=pygame.draw.circle(screen,(4,54,3),[mass9x,mass9y],5)
    mass10=pygame.draw.circle(screen,(4,54,3),[mass10x,mass10y],5)
    mass11=pygame.draw.circle(screen,(4,54,3),[mass11x,mass11y],5)
    mass12=pygame.draw.circle(screen,(4,54,3),[mass12x,mass12y],5)
    mass13=pygame.draw.circle(screen,(4,54,3),[mass13x,mass13y],5)
    mass14=pygame.draw.circle(screen,(4,54,3),[mass14x,mass14y],5)
    mass15=pygame.draw.circle(screen,(4,54,3),[mass15x,mass15y],5)
    mass16=pygame.draw.circle(screen,(4,54,3),[mass16x,mass16y],5)
    mass17=pygame.draw.circle(screen,(4,54,3),[mass17x,mass17y],5)
    mass18=pygame.draw.circle(screen,(4,54,3),[mass18x,mass18y],5)
    mass19=pygame.draw.circle(screen,(4,54,3),[mass19x,mass19y],5)
    mass20=pygame.draw.circle(screen,(4,54,3),[mass20x,mass20y],5)
    mass21=pygame.draw.circle(screen,(4,54,3),[mass21x,mass21y],5)
    mass22=pygame.draw.circle(screen,(4,54,3),[mass23x,mass23y],5)
    mass23=pygame.draw.circle(screen,(4,54,3),[mass23x,mass23y],5)
    mass24=pygame.draw.circle(screen,(4,54,3),[mass24x,mass24y],5)
    mass25=pygame.draw.circle(screen,(4,54,3),[mass25x,mass25y],5)
    mass26=pygame.draw.circle(screen,(4,54,3),[mass26x,mass26y],5)
    mass27=pygame.draw.circle(screen,(4,54,3),[mass27x,mass27y],5)
    mass28=pygame.draw.circle(screen,(4,54,3),[mass28x,mass28y],5)
    mass32=pygame.draw.circle(screen,(4,54,3),[mass29x,mass29y],5)
    mass33=pygame.draw.circle(screen,(4,54,3),[mass30x,mass30y],5)
    mass34=pygame.draw.circle(screen,(4,54,3),[mass31x,mass31y],5)
    mass35=pygame.draw.circle(screen,(4,54,3),[mass32x,mass32y],5)
    mass36=pygame.draw.circle(screen,(4,54,3),[mass33x,mass33y],5)
    pygame.display.update()
pygame.quit()
quit()