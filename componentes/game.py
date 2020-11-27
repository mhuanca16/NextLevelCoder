import pygame

from componentes.player import Player
from utils.constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TITLE, BLACK
)

class Game:
        def __init__(self):
            pygame.init()
            pygame.display.set_caption(TITLE)
            self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            self.clock = pygame.time.Clock()
        def run(self):
            self.create_components()
            #game loop:
            self.playing = True
            while self.playing:
                self.clock.tick(60)
                self.events()
                self.update()
                self.draw()
            pygame.quit() #metodo para cerrar la pantalla


        def create_components(self):
            self.all_sprites = pygame.sprite.Group()
            player = Player()
            self.all_sprites.add(player)

        def update(self):
            self.all_sprites.update()

        def events(self):
            for event in pygame.event.get():
                #tipo de evento
                if event.type == pygame.QUIT: #QUIT es constante
                    self.playing = False


        def draw(self):
            self.screen.fill(BLACK)
            self.all_sprites.draw(self.screen)
            pygame.display.flip()


