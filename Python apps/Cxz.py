import pygame as Pygame
screen = Pygame.display.set_mode([800,600])
keep_going=True
GREEN = (0,225,0)
radius = 100

while keep_going:
    for event  in Pygame.event.get():
        if event.type == Pygame.QUIT:
            keep_going = False
            print(type(quit))
            print(type(exit))

            Pygame.quit()
            exit()
Pygame.draw.circle(screen,GREEN,(100,100),radius)
Pygame.display.update()     
