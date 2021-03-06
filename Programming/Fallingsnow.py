"""
 FallingSnow.py
 Tim Ubial
 19 October 2017
 Version 0.2
 Animation of snow softly falling in sky

 Changelog:
 0.2 - Created Fall Speed
     - Renamed variables from Star to Snow

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Constants
BLACK =  (0, 0, 0)
WHITE =  (255, 255, 255)
GREEN =  (0, 255, 0)
RED =    (255, 0, 0)

WIDTH =  800
HEIGHT = 600

NUMBER_OF_SNOWFLAKES = 100

FALL_SPEED = 1

pygame.init()

# Set the width and height of the screen [width, height]
screen = pygame.display.set_mode([WIDTH, HEIGHT])

pygame.display.set_caption("Snow Softly Falling")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

snow_coords = []
for i in range(NUMBER_OF_SNOWFLAKES):
    x = random.randrange(0, WIDTH)
    y = random.randrange(0, HEIGHT)
    snow_coords.append([x, y])

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here

    for item in snow_coords:
        item[1] += FALL_SPEED
        pygame.draw.circle(screen, WHITE, item, 2)

        if item[1] > HEIGHT:
            item[0] = random.randrange(WIDTH)
            item[1] = random.randrange(-10, -2)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
