"""
CollectSprites.py

Step-by-step at: http://programarcadegames.com/index.php?chapter=lab_sprite_collecting&lang=en
Adapted from http://programarcadegames.com
"""
import pygame
import random

#Constants
BLACK = (  0,   255,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400
PLAYER_VELOCITY = 3
GREEN = (0, 0, 0)


class  Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super(Block, self).__init__()

        # Visual representation of Block
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Rectangle to represent position
        self.rect = self.image.get_rect()


class  Bad_Block(Block):
    def __init__(self, color, width, height):
        super(Block, self).__init__()

        # Visual representation of Block
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)

        # Rectangle to represent position
        self.rect = self.image.get_rect()


class  Good_Block(Block):
    def __init__(self, color, width, height):
        super(Block, self).__init__()

        # Visual representation of Block
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)

        # Rectangle to represent position
        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player, self).__init__()

        self.image = pygame.Surface((20, 15))
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.xvel = 0
        self.yvel = 0

    def changevelocity(self, x, y):
        """ Changes velocity of the player """
        self.xvel += x
        self.yvel += y

    def update(self):
        """ Updates the position of the Player according to velocity """
        self.rect.x += self.xvel
        self.rect.y += self.yvel


    def message_display(text):
        largeText = pygame.font.Font('freesansbold.ttf',30)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = (650,20)
        gameDisplay.blit(score)

pygame.init()

SCORE = 0
score_font = pygame.font.SysFont("syncopate", 15)

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# TODO: Create bad_block_list
bad_block_list = Bad_Block
# TODO: Create good_block_list
good_block_list = Good_Block
block_list = pygame.sprite.Group()
block_list2 = pygame.sprite.Group()

# All sprites in app
all_sprites_list = pygame.sprite.Group()

for i in range(50):
    Bad_Block = Block(RED, 20, 15)
    Good_Block = Block(BLACK, 20, 15)
    # Random location for block
    Bad_Block.rect.x = random.randrange(SCREEN_WIDTH)
    Bad_Block.rect.y = random.randrange(SCREEN_HEIGHT)
    Good_Block.rect.x = random.randrange(SCREEN_WIDTH)
    Good_Block.rect.y = random.randrange(SCREEN_HEIGHT)

    # Add the block to the list of objects
    block_list.add(Bad_Block)
    all_sprites_list.add(Bad_Block)
    block_list2.add(Good_Block)
    all_sprites_list.add(Good_Block)
# TODO: Create instance of player class
player = Block(BLACK, 20, 15)
all_sprites_list.add(player)

done = False
clock = pygame.time.Clock()

score = 0

# -------- Main Program Loop -----------
while not done:
    # TODO: Control character with keyboard
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Clear the screen
    screen.fill(WHITE)

    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    pos = pygame.mouse.get_pos()

    # Fetch the x and y out of the list,
       # just like we'd fetch letters out of a string.
    # Set the player object to the mouse location
    player.rect.x = pos[0]
    player.rect.y = pos[1]

    # TODO: Check for good and bad collisions
    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
    blocks_hit_list2 = pygame.sprite.spritecollide(player, block_list2, True)

    # TODO: Update score - good collisions = score + 1
    #if Player == Good_Block:
    #    score += score
    # TODO: Update score - bad collisions = score - 1
    #if Player == Bad_Block:
    #    score -= score
    # Check the list of collisions.
    for Bad_Block in blocks_hit_list:
        pygame.quit()

    for Good_Block in blocks_hit_list2:
        score += 1

    score_text = score_font.render(str(score), 10, GREEN, 5)
    screen.blit(score_text, (596, 10))
    # Draw all the spites
    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
