"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
 image via google images
"""

import pygame

pygame.mixer.init(44100, -16, 2, 2048)

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#background image

background_image = pygame.image.load("galaxy.jpg")

spaceship_image = pygame.image.load("player.png")

laser_sound = pygame.mixer.Sound("laser5.ogg")

pygame.init()

# Set the width and height of the screen [width, height]
size = (800, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Space gamez")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

spaceship_image_speed = 3
spaceship_image_xcoord = 0
spaceship_image_ycoord = 0
spaceship_image_xvel = 0
spaceship_image_yvel = 0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                spaceship_image_xvel -= spaceship_image_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                spaceship_image_xvel = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                spaceship_image_xvel += spaceship_image_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                spaceship_image_xvel = 0
            if event.key == pygame.K_SPACE:
                laser_sound.play()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                spaceship_image_yvel += spaceship_image_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                spaceship_image_yvel = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                spaceship_image_yvel -= spaceship_image_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                spaceship_image_yvel = 0



    # --- Game logic should go here

    spaceship_image_xcoord += spaceship_image_xvel
    spaceship_image_ycoord += spaceship_image_yvel

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    # --- Drawing code should go here
    screen.blit(background_image, [0,0])
    screen.blit(spaceship_image, [spaceship_image_xcoord, spaceship_image_ycoord])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(300)

# Close the window and quit.
pygame.quit()
