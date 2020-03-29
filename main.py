import pygame
import random

import settings
import sprites


class Game:
    def __init__(self):
        # initialize game window, etc
        pygame.init()
        pygame.mixer.init()  # all sound effects
        pygame.display.set_caption(settings.title)
        self.window = pygame.display.set_mode(settings.resolution)
        self.clock = pygame.time.Clock()
        self.running = True

    def new(self):
        # start new game, reset game
        self.all_sprites = pygame.sprite.Group()
        self.player = sprites.Player()
        self.all_sprites.add(self.player)
        game.run()

    def run(self):
        # game loop
        self.playing = True
        while self.playing:
            self.clock.tick(settings.fps)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # game loop - update
        self.all_sprites.update()

    def events(self):
        # game loop - events
        # process input (events)
        for event in pygame.event.get():
            # quit event
            if event.type == pygame.QUIT: # or event.type == pygame.K_ESCAPE:
                # breaking main loop
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # game loop - draw
        self.window.fill(settings.black)
        self.all_sprites.draw(self.window)

        # *after* drawing everything, flip the display
        pygame.display.flip()

    def start_screen(self):
        pass

    def end_screen(self):
        pass


game = Game()

game.start_screen()
while game.running:
    game.new()
    game.end_screen()

pygame.quit()

