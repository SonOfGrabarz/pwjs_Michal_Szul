import pygame

import settings

# vector with 2 dimensions
vector = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 60))
        self.image.fill(settings.red)
        self.rect = self.image.get_rect()

        # center player sprite in the window
        self.rect.center = (settings.window_width / 2, settings.window_height / 2)

        self.position = vector(settings.window_width / 2, settings.window_height / 2)
        self.velocity = vector(0, 0)
        self.acceleration = vector(0, 0)

    def update(self):
        self.acceleration = vector(0, 0)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.acceleration.x = -settings.player_acceleration
        if keys[pygame.K_d]:
            self.acceleration.x = settings.player_acceleration

        # wzory fizyczne opisujace ruch ( tarcie, przyspieszenie, predkosc)
        self.acceleration += self.velocity * settings.player_friction
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration

        # "wychodzenie" poza ekran
        if self.position.x > settings.window_width:
             self.position.x = 0
        if self.position.x < 0:
             self.position.x = settings.window_width

        self.rect.center = self.position
