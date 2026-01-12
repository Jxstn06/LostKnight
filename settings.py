import pygame


class Settings:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.dt = self.clock.tick(self.fps) / 1000
        self.monitor_width = pygame.display.Info().current_w
        self.monitor_height = pygame.display.Info().current_h

        self.background_color = pygame.Color('black')

        self.raumx = 30
        self.raumy = 10
        self.raumtile = 32
