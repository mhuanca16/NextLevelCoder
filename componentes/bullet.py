import pygame
from utils.constants import (RED, BLACK, SCREEN_HEIGHT, SCREEN_WIDTH, IMG_DIR)
from os import path
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((5, 5))
        #self.image.fill(RED)
        self.image = pygame.image.load(path.join(IMG_DIR, "bullet.png")).convert()
        self.image = pygame.transform.scale(self.image, (10, 10))
        # color de fondo de la imagen
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y = self.rect.y + self.speedy
        if self.rect.bottom < 0:
            self.kill()