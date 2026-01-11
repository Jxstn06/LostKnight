import pygame
import sys

from settings import Settings
from Base.szene import Szene
from Base.button import Button


class Menu(Szene):
    def __init__(self, display, manager):
        super().__init__()
        self.display = display
        self.manager = manager
        self.s = Settings()

        self.buttons = [
            Button(self.s.monitor_width//2-200, self.s.monitor_height//10*3, 400, 50, 'Load', True),
            Button(self.s.monitor_width // 2 - 200, self.s.monitor_height // 10 * 6, 400, 50, 'Quit')
        ]

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        for button in self.buttons:
            button.update()
            if button.handle_events(event):
                if button.text == 'Load':
                    continue
                if button.text == 'Quit':
                    pygame.quit()
                    sys.exit()

    def update(self, dt):
        pass

    def draw(self, screen):
        self.display.fill(self.s.background_color)

        for button in self.buttons:
            button.draw(self.display)
