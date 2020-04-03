import pygame

import settings
import sprites


class Game:
    def __init__(self):
        pygame.display.set_caption(settings.title)
        self.window = pygame.display.set_mode(settings.resolution)
        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = True

    def new(self):
        # start new game, reset game
        self.player = sprites.Player()
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        platform1 = sprites.Platform(0, settings.window_height - 50, settings.window_width, 40)
        self.platforms.add(platform1)
        self.all_sprites.add(platform1)

        platform2 = sprites.Platform(settings.window_width / 2 - 50, settings.window_height * 3 / 4, 100, 20)
        self.all_sprites.add(platform2)
        self.platforms.add(platform2)

        game.run()

    def run(self):
        # testowanie działania liczenia czasu
        t = sprites.Timer()
        pygame.time.wait(300)
        print(t.current())

        # game loop
        # self.playing = True
        while self.playing:
            self.clock.tick(settings.fps)
            self.events()
            self.update()
            self.draw()
            self.dev_tools()

    def update(self):
        # game loop - update
        self.all_sprites.update()

        collision = pygame.sprite.spritecollide(self.player, self.platforms, False)

        if collision:
            self.player.position.y = collision[0].rect.top
            self.player.velocity.y = 0

    def events(self):
        # game loop - events
        # process input (events)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            # quit event
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                # breaking main loop
                print("Wcisnieto ESC lub zamknięto okno!")
                if self.playing:
                    self.playing = False
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()

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

    # "drawing" variables on screen for tests
    def dev_tools(self):
        self.text1 = settings.fontCN.render('Acceleration: {0}'.format(self.player.acceleration * 100), True,
                                            settings.white)
        self.text2 = settings.fontCN.render('Velocity: {0}'.format(self.player.velocity * 100), True, settings.white)
        self.text3 = settings.fontCN.render('Position: {0}'.format(self.player.position), True, settings.white)

        self.window.blit(self.text1, (10, 10))
        self.window.blit(self.text2, (20, 50))
        self.window.blit(self.text3, (10, 80))

        pygame.display.flip()


# "creating game"
game = Game()

# start screen with menu (probably)
game.start_screen()

# main loop
while game.running:
    game.new()
    game.end_screen()

pygame.quit()
