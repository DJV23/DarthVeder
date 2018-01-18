"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (1100, 900)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Test by Ved!!!!!!!!")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

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
    screen.fill(WHITE)

    # --- Drawing code should go here
    # [x_coord, y_coord, width, height]
    rcolour = random.randrange(0, 5)
    if rcolour == "1":
        rcolour = BLACK
    elif rcolour == "2":
        rcolour = WHITE
    elif rcolour == "3":
        rcolour = GREEN
    elif rcolour == "4":
        rcolour = RED



#for
    drawing = pygame.draw.line(screen, BLACK, [random.randrange(1, 999), random.randrange(1,999)], [random.randrange(1, 999), random.randrange(1,999)], 1)
    if drawing == "150":
        done = True
    else:
        done = False
    #if event.type == pygame.QUIT:
        #done = True
    #

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
