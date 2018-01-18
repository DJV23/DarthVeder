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
BLUE = (0, 191, 255)
screen_x = 1024
screen_y = 2900

pygame.init()

# Set the width and height of the screen [width, height]
size = (screen_x, screen_y)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Controllers and graphicssssssssss part 2")

carIMG = pygame.image.load('lamborghinhi.jpg')
flightIMG = pygame.image.load('a380actual.jpg')

flightIMG_speed = 10

flightIMG_xcoord = 0
flightIMG_ycoord = 0
flightIMG_xvel = 0
flightIMG_yvel = 0


car_speed = 3

car_xcoord = 0
car_ycoord = 0
car_xvel = 0
car_yvel = 0

def car(x,y):
    screen.blit(carIMG,(x,y))

x = car_xcoord
y = car_ycoord

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
#    pygame.draw.rect(screen, WHITE, (x + 65, 65 + y, 25, 25),0)

#def draw_flight(screen, x, y):
#    pygame.draw.rect(screen, WHITE, (x + 95, 95 + y, 50, 50),0)

pygame.mouse.set_visible(False)




#-------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == ord('a'):
                car_xvel -= car_speed
        if event.type == pygame.KEYUP:
            if event.key == ord('a'):
                car_xvel = 0
        if event.type == pygame.KEYDOWN:
            if event.key == ord('d'):
                car_xvel += car_speed
        if event.type == pygame.KEYUP:
            if event.key == ord('d'):
                car_xvel = 0
        if event.type == pygame.KEYDOWN:
            if event.key == ord('s'):
                car_yvel += car_speed
        if event.type == pygame.KEYUP:
            if event.key == ord('s'):
                car_yvel = 0
        if event.type == pygame.KEYDOWN:
            if event.key == ord('w'):
                car_yvel -= car_speed
        if event.type == pygame.KEYUP:
            if event.key == ord('w'):
                car_yvel = 0

            '''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                flightIMG_xvel -= flightIMG_speed
        if event.type == pygame.KEYUP:
            if event.key == K_LEFT:
                flightIMG_xvel = 0
        if event.type == pygame.KEYDOWN:
            if event.key == K_RIGHT:
                flightIMG_xvel += flightIMG_speed
        if event.type == pygame.KEYUP:
            if event.key == K_RIGHT:
                flightIMG_xvel = 0
        if event.type == pygame.KEYDOWN:
            if event.key == K_DOWN:
                flightIMG_yvel += flightIMG_speed
        if event.type == pygame.KEYUP:
            if event.key == K_DOWN:
                flightIMG_yvel = 0
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                flightIMG_yvel -= flightIMG_speed
        if event.type == pygame.KEYUP:
            if event.key == K_UP:
                flightIMG_yvel = 0
            '''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                flightIMG_xvel -= flightIMG_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                flightIMG_xvel = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                flightIMG_xvel += flightIMG_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                flightIMG_xvel = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                flightIMG_yvel += flightIMG_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                flightIMG_yvel = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                flightIMG_yvel -= flightIMG_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                flightIMG_yvel = 0

    if flightIMG_xcoord <= 0:
        flightIMG_xcoord = 0
    if flightIMG_xcoord >= 320:
        flightIMG_xcoord = 320



    if flightIMG_ycoord <= 0:
        flightIMG_ycoord = 0
    if flightIMG_ycoord >= 500:
        flightIMG_ycoord = 500

    if car_xcoord <= 0:
        car_xcoord = 0
    if car_xcoord >= 670:
        car_xcoord = 670



    if car_ycoord <= 0:
        car_ycoord = 0
    if car_ycoord >= 570:
        car_ycoord = 570



    # --- Game logic should go here
    pos = pygame.mouse.get_pos()

    car_xcoord += car_xvel
    car_ycoord += car_yvel
    flightIMG_xcoord += flightIMG_xvel
    flightIMG_ycoord += flightIMG_yvel
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    # --- Drawing code should go here
    #draw_square(screen, 0, 0)
    #draw_square(screen, 150, 0)
    #draw_square(screen, car_xcoord, square_ycoord)
    #draw_square(screen, car_xcoord, square_ycoord)
    #draw_flight(screen, car_xcoord, square_ycoord)
    #draw_flight(screen, flightIMG_xcoord, flightIMG_ycoord)
    #print(pos[0] + pos[1])
    #print('carIMG')
    #print('flightIMG')
    #car(x,y)
    flight(flightIMG_xcoord, flightIMG_ycoord)
    car(car_xcoord, car_ycoord)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(1000)

    # Close the window and quit.
pygame.quit()
