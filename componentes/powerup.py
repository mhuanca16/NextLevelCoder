import pygame
import random
from utils.constants import (YELLOW, SCREEN_HEIGHT, SCREEN_WIDTH)
allowed_speed = list(range(3, 7))
class Powerup(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_HEIGHT - self.rect.height)
        self.rect.y = random.randrange(-100, 100)
        self.speedx = random.choice(allowed_speed)
        self.speedy = random.choice(allowed_speed)


    def update(self):
        # se mueve la bolita de poder
        self.rect.y = self.rect.y + self.speedy