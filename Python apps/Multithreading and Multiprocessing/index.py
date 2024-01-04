import pygame
import time
import random
 
pygame.init()

# Set up the game window
window_width = 500
window_height = 500
game_display = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set up the clock
clock = pygame.time.Clock()

# Set up the font
font_style = pygame.font.SysFont(None, 30)

def message(msg, color):
    text = font_style.render(msg, True, color)
    game_display.blit(text, [window_width/6, window_height/3])

def game_loop():
    # Set up the initial position of the snake and the food
    snake_size = 10
    snake_speed = 15
    x1 = window_width / 2
    y1 = window_height / 2
    x1_change = 0
    y1_change = 0
    food_x = round(random.randrange(0, window_width - snake_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, window_height - snake_size) / 10.0) * 10.0
    score = 0

    # Set up the game loop
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_size
                    x1_change = 0

        # Move the snake
        x1 += x1_change
        y1 += y1_change

        # Check if the snake has collided with the wall
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_over = True

        # Draw the snake and the food
        game_display.fill(black)
        pygame.draw.rect(game_display, green, [food_x, food_y, snake_size, snake_size])
        pygame.draw.rect(game_display, white, [x1, y1, snake_size, snake_size])
        pygame.display.update()

        # Check if the snake has eaten the food
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, window_width - snake_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, window_height - snake_size) / 10.0) * 10.0
            score += 10

        # Display the score
        score_font = font_style.render("Score: " + str(score), True, blue)
        game_display.blit(score_font, [0, 0])

        # Update the clock
        clock.tick(snake_speed)

    # Quit Pygame
    pygame.quit()
    quit()

game_loop()
