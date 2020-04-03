import pygame

# initialize game window, etc
pygame.font.init()  # all fonts
pygame.mixer.init()  # all sound effects
pygame.init()

# game settings
title = "project"
window_height = 600
window_width = 800
resolution = [window_width, window_height]
fps = 60

# player properties
player_acceleration = 0.2
player_friction = -0.1   # tarcie

# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# fonts
fontCN = pygame.font.Font('font/ComicNeue-Bold.ttf', 10)
