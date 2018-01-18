import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
size = (1100, 900)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Test by Ved!!!!!!!!")
done = False
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop


    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    question = raw_input("Ans: ")
    if question == "RED":
        screen.fill(RED)
        done = True
    elif question == "GREEN":
        screen.fill(GREEN)
        done = True
    elif question == "WHITE":
        screen.fill(WHITE)
        done = True
    elif question == "BLACK":
        screen.fill(BLACK)
        done = True
