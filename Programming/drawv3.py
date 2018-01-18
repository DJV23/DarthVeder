"""



"""
import random
import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
Navy = (0,0,128)
Orange = (255,165,0)
Blue = (0,191,255)
#x = 0
#for i in range(100):


pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False
#r*i = 0:
#    if i == "3":
#        done = True
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
    screen.fill(Navy)

    # --- Drawing code should go here
    #pygame.draw.circle(screen, RED, [(random.randrange(700,800)), (random.randrange(500,600))], 4, 0)
    pygame.draw.rect(screen,BLACK,[(175,375),(390,375)],0)
    pygame.draw.rect(screen,WHITE,[(155,300),(290,300)],0)
    #pygame.draw.polygon(screen,Orange,[(175,200),(175,200),(175,200),(175,200)],0)
    pygame.draw.circle(screen, WHITE, [525,450 ], 20, 0)
    pygame.draw.circle(screen, Orange,[100,100],90,0)
    pygame.draw.circle(screen, BLACK,(525,450),8,0)
    pygame.draw.circle(screen,Blue, (500,100),80,0)
    #pygame.draw.polygon(screen,RED,[(500,100),(450,50),(400,75)])

    #pygame.draw.circle(screen, WHITE,(100,390),25,10)
    #pygame.draw.cirlce(screen, WHITE,[])
    #    i = 1
    #else:
    #    pass
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
