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
        self.manager = Manager()
        self.manager.switch_szene(Menu(self.screen, self.manager))

    def run(self):
        while self.running:
            # delta time
            dt = self.clock.tick(self.s.fps) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                    self.running = False
                self.manager.handle_events(event)

            self.manager.update(dt)
            self.manager.draw(self.screen)
            pygame.display.flip()

        pygame.quit()
        sys.exit()
