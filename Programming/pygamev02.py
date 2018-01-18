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
    pygame.draw.ellipse(screen, WHITE, [x, y, 25, 25])
    #Draw the middle snowman cirlce
    pygame.draw.ellipse(screen, WHITE, [x, y, 50, 50])
    #Draw the bottom of the snowman
    pygame.draw.ellipse(screen, WHITE, [x, y, 100, 100])

pygame.mouse.set_visible(False)

def draw_sheep(screen, x, y):
    pygame.draw.rect(screen,WHITE,[(175 + x),(390 + y), 10, 20],0)
    pygame.draw.rect(screen,WHITE,[(155 + x),(290 + y), 20, 40],0)




SNOWMAN_SPEED = 3

snowman_xcoord = 0
snowman_ycoord = 0
snowman_xvel = 0
snowman_yvel = 0


SHEEP_SPEED = 5

sheep_xcoord = 0
sheep_ycoord = 0
sheep_xvel = 0
sheep_yvel = 0



# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snowman_xvel -= SNOWMAN_SPEED
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                snowman_xvel = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snowman_xvel += SNOWMAN_SPEED
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                snowman_xvel = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                snowman_yvel += SNOWMAN_SPEED
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                snowman_yvel = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snowman_yvel -= SNOWMAN_SPEED
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                snowman_yvel = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                sheep_xvel -= SHEEP_SPEED
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                sheep_xvel = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                sheep_yvel += SHEEP_SPEED
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                sheep_yvel = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                sheep_xvel = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                sheep_xvel += SHEEP_SPEED
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                sheep_yvel = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                sheep_yvel -= SHEEP_SPEED
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                snowman_yvel = 0

    if snowman_xcoord <= 0:
        snoman_xcoord = 0
    if snowman_xcoord >= 500:
        snowman_xcoord = 500

    if sheep_xcoord <= 0:
        sheep_xcoord = 0
    if sheep_xcoord >= 500:
        sheep_xcoord = 500

    if snowman_ycoord <= 0:
        snowman_ycoord = 0
    if snowman_ycoord >= 700:
        snowman_ycoord = 700

    if sheep_ycoord <= 0:
        sheep_ycoord = 0
    if sheep_ycoord >= 700:
        sheep_ycoord = 700



    # --- Game logic should go here
    pos = pygame.mouse.get_pos()

    snowman_xcoord += snowman_xvel
    snowman_ycoord += snowman_yvel
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(RED)

    # --- Drawing code should go here
    #draw_snowman(screen, 0, 0)
    #draw_snowman(screen, 150, 0)
    draw_snowman(screen, snowman_xcoord, snowman_ycoord)
    draw_sheep(screen, sheep_xcoord, snowman_ycoord)
    #print(pos[0] + pos[1])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
