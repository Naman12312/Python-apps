import pygame, random
pygame.init()
play = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode((700, 750))
pygame.display.set_caption("Car Game")

# Define a bunch of colours
GREEN = (20, 255, 100)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
BLUE = (0, 0, 255)

all_sprites = pygame.sprite.Group()  # Creates a list of all sprites in the game

playerCar = Car(RED, 20, 30)  # Defines the car, its colour, and its 
size
playerCar.rect.x = 200
playerCar.rect.y = 300

AutoCar1 = AutoCar(BLUE, 20, 30)
AutoCar1.rect.x = 200
AutoCar1.rect.y = 20

all_sprites.add(playerCar)  # Adds the playerCar to the list of sprites
all_sprites.add(AutoCar1)  # Adds an automated 'enemy' car which you must avoid



while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If the detected event is clicking the exit button, stop the program.
            play = False
        if event.type == pygame.KEYDOWN:  # If a key is pressed and the key is 'x', quit the game.
            if event.key == pygame.K_x:
                play = False

keys = pygame.key.get_pressed()  # Defines a variable keys that consists of whatever event is happening in the game
if keys[pygame.K_LEFT]:
    playerCar.move_left(5)
if keys[pygame.K_RIGHT]:
    playerCar.move_right(5)
if keys[pygame.K_DOWN]:
    playerCar.move_backward(5)
if keys[pygame.K_UP]:
    playerCar.move_forward(5)

all_sprites.update()  # Draws in all sprites
AutoCar1.auto_move_forward(3)  # Makes the 'enemy' move forward automatically.



# Create the background
screen.fill(GREEN)
# Create the road
pygame.draw.rect(screen, GREY, [100, 0, 500, 750])
# Draw the lines on the road
pygame.draw.line(screen, WHITE, [340, 0], [340, 750], 5)
