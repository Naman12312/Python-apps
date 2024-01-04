import pygame
pygame.init()
screen=pygame.display.set_mode((900,600))
exit_game=False
pad1x=6
pad1y=400
pad2x=870
pad2y=500
pad1v=0
pad2v=0
ballxv=1/2
ballyv=1/2
ballx=45
bally=67
while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                pad2v=1/2
            if event.key==pygame.K_UP:
                pad2v=-1/2
            if event.key==pygame.K_s:
                pad1v=1/2
            if event.key==pygame.K_w:
                pad1v=-1/2
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_DOWN:
                pad2v=0
            if event.key==pygame.K_UP:
                pad2v=0
            if event.key==pygame.K_s:
                pad1v=0
            if event.key==pygame.K_w:
                pad1v=0
    if ballx>600:
        ballxv=1/2
        ballyv=-1/2
    if abs(pad2x-ballx)<60 and abs(pad2y-bally)<60:
        ballxv=-1/2
        ballyv=-1/2 
    if ballx<0:
        ballxv=-1/2
        ballyv=1/2
    # if ballx>600 or ballx<0:
    #     print("Goal")
    #     ballx=45
    #     bally=67       
    pad1y=pad1y+pad1v
    pad2y=pad2y+pad2v    
    ballx=ballx+ballxv
    bally=bally+ballyv        
    screen.fill((255,255,255))
    pad1=pygame.draw.rect(screen,(0,0,0),[pad1x,pad1y,20,50])
    pad2=pygame.draw.rect(screen,(0,0,0),[pad2x,pad2y,20,50])
    ball=pygame.draw.circle(screen,(255,0,0),[ballx,bally],10)
    pygame.display.update()
pygame.quit()
quit()