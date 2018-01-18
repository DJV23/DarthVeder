"""
ClassesandGraphics.py
Ved Ballary
Last edit: 17 November 2017
Version 1
This program randomly moves randomly generated ellipses and rectangles.

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

class Rectangle(object):
   def __init__(self):

       self.xmove = random.randrange(1, 700)
       self.ymove = random.randrange(1,500)
       self.x = random.randrange(1,700)
       self.y = random.randrange(1, 500)
       self.height = random.randrange(20,70)
       self.width = random.randrange(20,70)
       self.xvel = random.randrange(-3, 3)
       self.yvel = random.randrange(-3, 3)
       self.colour = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
   def draw(self,screen):
       pygame.draw.rect(screen, self.colour, [self.x, self.y, self.height, self.width], 0)
   def move(self):
       self.x += self.xvel
       self.y += self.yvel

class Ellipse(Rectangle):


   def draw(self, screen):

       pygame.draw.ellipse(screen, self.colour,[self.x, self.y, self.height, self.width], 0 )

   def move(self):
       self.x += self.xvel
       self.y += self.yvel

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

my_object = Rectangle() or Ellipse()
my_list = []
i = 0
for i in range(1000):
    my_list.append(Rectangle())
    my_list.append(Ellipse())

# -------- Main Program Loop -----------
while not done:
   # --- Main event loop
   screen.fill(BLACK)
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           done = True
   for my_object in my_list:

       # --- Game logic should go here

       # --- Screen-clearing code goes here

       # Here, we clear the screen to white. Don't put other drawing commands
       # above this, or they will be erased with this command.

       # If you want a background image, replace this clear with blit'ing the
       # background image.


       # --- Drawing code should go here

        my_object.draw(screen)
        my_object.move()

       # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

       # --- Limit to 60 frames per second
        clock.tick(120)

# Close the window and quit.
pygame.quit()
