"""
 Pygame Boilerplate

 Adapted from:
 http://programarcadegames.com
"""

import pygame
import random

# Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
WIDTH = 800
HEIGHT = 600

score = 0

# Classes
class Block(pygame.sprite.Sprite):
    def __int__(self, colour, height, width):
        super(Block, self).__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(colour)

        self.rect = self.image.get_rect()

    def reset_pos(self):
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(WIDTH)

    def update(self):
        """Called each frame. Moves the block down one pixel"""
        self.rect.y +=1

        if self.rect.y > HEIGHT:
            self.reset_pos()

class Player(pygame.sprite.Sprite):
    def __init__(self, height, width):
        super(Player, self).__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(RED)

        self.rect = self.image.get_rect()
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x = mouse_pos[0]
        player.rect.y = mous_pos[1]


def main():
    pygame.init()

    # Screen properties
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("")

    done = False

    clock = pygame.time.Clock()

    block_list = pygame.sprite.Group()
    all_sprites_list = pygame.sprite.Group()


    for i in range(50):
        block = Block(BLACK, 20, 15)
        block.rect.x =random.randrange(WIDTH)
        block.rect.y = random.randrange(HEIGHT)

        block_list.add(block)
        all_sprites_list.add(block)


    player = Block(20, 15)
    all_sprite_list.add(player)

    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(WHITE)

        all_sprite_list.update()

        blocks_hit_list = pygame.spritecollide(player, block_list, True)

        for block in blocks_hit_list:
            score += 1
            print(score)


        all_sprites_list.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
