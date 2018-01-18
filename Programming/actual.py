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
screen_x = 2000
screen_y = 1500
#rotation = rotate(flightIMG, 90)

class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super(Bullet, self).__init__()

        self.image = pygame.Surface([15, 20])


        self.rect = self.image.get_rect()

    def update(self):
        """ Move the bullet. """
        self.rect.x += 25
        self.rect.y -= 30
#def draw_flight(screen, x, y):
#    pygame.draw.rect(screen, WHITE, (x + 95, 95 + y, 50, 50),0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (screen_x, screen_y)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Controllers and graphicssssssssss part 2")

#carIMG = pygame.image.load('lamborghinhi.jpg')
flightIMG = pygame.image.load('Player1.png')

flightIMG_speed = 30

flightIMG_xcoord = 0
flightIMG_ycoord = 0
flightIMG_xvel = 0
flightIMG_yvel = 0
"""
def car(x,y):
    screen.blit(carIMG,(x,y))

x = (10)
y = (15)
"""
def flight(x,y):
    screen.blit(flightIMG,(x,y))
    #flightIMG = pygame.image.load('a380actual.jpg')
x = flightIMG_xcoord
y = flightIMG_ycoord

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
#def draw_square(screen, x, y):

all_sprites_list = pygame.sprite.Group()


bullet_list = pygame.sprite.Group()
#    pygame.draw.rect(screen, WHITE, (x + 65, 65 + y, 25, 25),0)


pygame.mouse.set_visible(False)




#-------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Fire a bullet if the user clicks the mouse button
            bullet = Bullet()
            # Set the bullet so it is where the player is
            bullet.rect.x = flightIMG_xcoord + 200
            bullet.rect.y = flightIMG_ycoord - 20
                        # Add the bullet to the lists
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                pygame.transform.rotate(flightIMG, 60)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                flightIMG_xvel = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                flightIMG_xvel += flightIMG_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                flightIMG_xvel = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                flightIMG_yvel += flightIMG_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                flightIMG_yvel = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                flightIMG_yvel -= flightIMG_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                flightIMG_yvel = 0



    # --- Game logic should go here
    pos = pygame.mouse.get_pos()
    all_sprites_list.update()

    flightIMG_xcoord += flightIMG_xvel
    flightIMG_ycoord += flightIMG_yvel
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    # --- Drawing code should go here


    '''
    if bullet.rect.x < -10:
        bullet_list.remove(bullet)
        all_sprites_list.remove(bullet)
'''
    all_sprites_list.draw(screen)

    flight(flightIMG_xcoord, flightIMG_ycoord)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(120)

    # Close the window and quit.
pygame.quit()
