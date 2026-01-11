import pygame
import sys

from settings import Settings
from manager import Manager

# Szene
from Szenen.menu import Menu


class Lostknight:
    def __init__(self):
        pygame.init()
        self.running = True
        self.s = Settings()
        self.screen = pygame.display.set_mode((self.s.monitor_width, self.s.monitor_height))
        self.clock = pygame.time.Clock()

        # Manager mit Menu Szene
        self.manager = Manager(None)
        self.manager.set_szene(Menu(self.screen, self.manager))

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                    self.running = False
                self.manager.get_szene().handle_events(event)

            self.manager.get_szene().update()
            self.manager.get_szene().draw()
            pygame.display.update()
            self.clock.tick(self.s.fps)

        pygame.quit()
        sys.exit()
