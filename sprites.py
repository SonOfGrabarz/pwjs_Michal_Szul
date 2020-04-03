import pygame

import settings

# vector with 2 dimensions
# for 2d variables - velocity, acceleration, position
vector = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    # ta klasa dziedziczy po pygame'owej klasie Sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 60))
        self.image.fill(settings.red)
        self.rect = self.image.get_rect()

        # center player sprite in the window
        self.rect.center = vector(settings.window_width / 2, settings.window_height / 2)
        self.position = vector(settings.window_width / 2, settings.window_height / 2)
        self.velocity = vector(0, 0)
        self.acceleration = vector(0, settings.player_gravity)

    def jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.velocity.y = -20

    def update(self):
        self.acceleration = vector(0, 0.5)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.acceleration.x = -settings.player_acceleration
            print('left')

        if keys[pygame.K_d]:
            self.acceleration.x = settings.player_acceleration
            print('right')

        # wzory fizyczne opisujace ruch ( tarcie, przyspieszenie, predkosc)
        self.acceleration.x += self.velocity.x * settings.player_friction
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration

        # "wychodzenie" poza ekran
        if self.position.x > settings.window_width:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = settings.window_width

        self.rect.midbottom = self.position


class Platform(pygame.sprite.Sprite):

    def __init__(self, x, y, platform_width, platform_height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((platform_width, platform_height))
        self.image.fill(settings.green)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Timer():
    # możliwe, że się przyda
    def __init__(self):
        self.time_start = 0

    def start(self):
        self.time_start = pygame.time.get_ticks()

    def current(self):
        return (pygame.time.get_ticks() - self.time_start)/1000


class Map(Platform, Timer):
    pass


class Lvl1(Map):
    pass
