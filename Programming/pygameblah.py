"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame

# Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Ball():

  def __init__(self):
    self.x = 0
    self.y = 0

    self.xvel = 0
    self.yvel = 0

    self.size = 10

    self.colour = GREEN

  #--Class Methods--
  def move(self):
    self.x += self.xvel
    self.y += self.yvel
  def draw(self, screen):
    pygame.draw.circle(screen, self.colour, [self.x, self.y], self.size)


pygame.init()

# Set the width and height of the screen [width, height]
screen = pygame.display.set_mode(600,500)

pygame.display.set_caption("Window")

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
    ball.draw(screen)

    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
