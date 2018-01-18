 #This code moves stuff
#
#
#
#


import datetime
import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
screen_x = 1980
screen_y = 1020
bullet_x = 200
bullet_y = 20
bullet_movex = 5
bullet_movey = 10
t = datetime.time(0)
bullet_count = 0
BACKGROUND = pygame.image.load("Grid.jpg")



class Bullet(pygame.sprite.Sprite):

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super(Bullet, self).__init__()

        self.image = pygame.Surface([15, 20])


        self.rect = self.image.get_rect()

    def update(self):
        """Moves the bullet"""
        self.rect.x += bullet_movex
        self.rect.y -= bullet_movey

#Add this later
#def score()
#class enemytr(pygame.sprite.Sprite):

#    def __init__(self):
        # Call the parent class (Sprite) constructor
#        super(Bullet, self).__init__()

#        self.enemytr(screen, GREEN, [50,60], [20,30], 0)


#    def update(self):

#        self.rect.cx += computer_movex
#        self.rect.cy -= computer_movey


#def draw_flight(screen, x, y):
#    pygame.draw.rect(screen, WHITE, (x + 95, 95 + y, 50, 50),0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (screen_x, screen_y)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Controllers and graphicssssssssss part 2")

#carIMG = pygame.image.load('lamborghinhi.jpg')
flightIMG = pygame.image.load('Player1 3.png')

################################################################################

flightIMG_speed = 30

flightIMG_xcoord = 800
flightIMG_ycoord = 450
flightIMG_xvel = 0
flightIMG_yvel = 0

################################################################################

enemytr = pygame.image.load("Enemy.png")

################################################################################

enemytr_speed = 40

enemytr_xcoord = 30
enemytr_ycoord = 50
enemytr_xvel = 10
enemytr_yvel = 10


def flight(x,y):
    screen.blit(flightIMG,(x,y))
    #flightIMG = pygame.image.load('a380actual.jpg')
x = flightIMG_xcoord
y = flightIMG_ycoord



def enemy():
    screen.blit(enemytr,(enemytr_xcoord,enemytr_ycoord))






# Loop until the user clicks the close button
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
#def draw_square(screen, x, y):

all_sprites_list = pygame.sprite.Group()


bullet_list = pygame.sprite.Group()

computer_sprite_list = pygame.sprite.Group()
#    pygame.draw.rect(screen, WHITE, (x + 65, 65 + y, 25, 25),0)


pygame.mouse.set_visible(True)





#-------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if bullet_count >= 0:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Fire a bullet if the user clicks the mouse button
                bullet = Bullet()
                # Set the bullet so it is where the player is
                bullet.rect.x = flightIMG_xcoord + bullet_x
                bullet.rect.y = flightIMG_ycoord - bullet_y
                # Add the bullet to the lists
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
                bullet_count = bullet_count + 1


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                flightIMG = pygame.image.load("Player1 3.png")
                bullet_x = -10
                bullet_y = -10
                bullet_movex = -7
                bullet_movey = 22
###############################################################################
        if event.type == pygame.KEYUP:
            pass
###############################################################################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                flightIMG = pygame.image.load("Player1 4.png")
                bullet_x = 170
                bullet_y = 20
                bullet_movex = 7
                bullet_movey = 22
###############################################################################
        if event.type == pygame.KEYUP:
            pass
###############################################################################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                flightIMG = pygame.image.load("Player1 5.png")
                bullet_x = 300
                bullet_y = -200
                bullet_movex = 22
                bullet_movey = -7
###############################################################################
        if event.type == pygame.KEYUP:
            pass
###############################################################################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                flightIMG = pygame.image.load("Player1 6.png")
                bullet_x = 20
                bullet_y = -180
                bullet_movex = -7
                bullet_movey = -22

################################################################################

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                enemytr_xvel -= enemytr_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                enemytr_xvel = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                enemytr_xvel += enemytr_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                enemytr_xvel = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                enemytr_yvel += enemytr_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                enemytr_yvel = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                enemytr_yvel -= enemytr_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                enemytr_yvel = 0

################################################################################

    # --- Game logic should go here
    """
    if bullet_count == 10:
        print(bullet_count)
    """


    screen.blit(BACKGROUND, [30,0])

    pos = pygame.mouse.get_pos()
    all_sprites_list.update()

    flightIMG_xcoord += flightIMG_xvel
    flightIMG_ycoord += flightIMG_yvel

    enemytr_xcoord += enemytr_xvel
    enemytr_ycoord += enemytr_yvel
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    if bullet_x and bullet_y == enemytr_xcoord and enemytr_ycoord:
        done = True

    if bullet_count == 5:
        bullet_count == -200
    # --- Drawing code should go here

    all_sprites_list.draw(screen)

    flight(flightIMG_xcoord, flightIMG_ycoord)

    enemy()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(120)

    # Close the window and quit.
pygame.quit()
