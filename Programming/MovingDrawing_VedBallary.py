#This code moves stuff
#
#
#
#



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

pygame.display.set_caption("Controllers and graphicssssssssss part 2")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
def draw_square(screen, x, y):
    pygame.draw.rect(screen, WHITE, (x + 65, 65 + y, 25, 25),0)

pygame.mouse.set_visible(False)

SQUARE_SPEED = 3

square_xcoord = 0
square_ycoord = 0
square_xvel = 0
square_yvel = 0

#-------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                square_xvel -= SQUARE_SPEED
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                square_xvel = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                square_xvel += SQUARE_SPEED
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                square_xvel = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                square_yvel += SQUARE_SPEED
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                square_yvel = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                square_yvel -= SQUARE_SPEED
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                square_yvel = 0

    # --- Game logic should go here
    pos = pygame.mouse.get_pos()

    square_xcoord += square_xvel
    square_ycoord += square_yvel
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(RED)

    # --- Drawing code should go here
    #draw_square(screen, 0, 0)
    #draw_square(screen, 150, 0)
    draw_square(screen, square_xcoord, square_ycoord)
    draw_square(screen, square_xcoord, square_ycoord)
    #print(pos[0] + pos[1])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

    # Close the window and quit.
pygame.quit()
