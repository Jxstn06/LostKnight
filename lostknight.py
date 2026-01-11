import pygame
import sys


class Lostknight:
    def __init__(self):
        pygame.init()
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

        pygame.quit()
        sys.exit()
