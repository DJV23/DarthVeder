"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Controllers and graphicssssssssss")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def draw_snowman(screen, x, y):
    #Draw a circle for the head
    pygame.draw.ellipse(screen, WHITE, [35 + x, y, 25, 25])
    #Draw the middle snowman cirlce
    pygame.draw.ellipse(screen, WHITE, [23 + x, 20 + y, 50, 50])
    #Draw the bottom of the snowman
    pygame.draw.ellipse(screen, WHITE, [x, 65 + y, 100, 100])

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    pos = pygame.mouse.get_pos()

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here
    #draw_snowman(screen, 0, 0)
    #draw_snowman(screen, 150, 0)
    draw_snowman(screen, pos[0], pos[1])
    #print(pos[0] + pos[1])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
