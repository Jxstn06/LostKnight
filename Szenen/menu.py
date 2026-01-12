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
            Button(
                self.s.monitor_width//2 - self.s.buttonsizes['big'][0]/2,
                self.s.monitor_height//15*5,
                self.s.buttonsizes['big'][0],
                self.s.buttonsizes['big'][1],
                'Load', True, True),
            Button(
                self.s.monitor_width // 2 - self.s.buttonsizes['big'][0] / 2,
                self.s.monitor_height // 15 * 7.5,
                self.s.buttonsizes['big'][0],
                self.s.buttonsizes['big'][1],
                'Settings'),
            Button(
                self.s.monitor_width // 2 - self.s.buttonsizes['big'][0]/2,
                self.s.monitor_height // 15 * 10,
                self.s.buttonsizes['big'][0],
                self.s.buttonsizes['big'][1],
                'Quit')
        ]

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        for button in self.buttons:
            if button.handle_event(event):
                if button.text == 'Load':
                    pass
                elif button.text == 'Quit':
                    pygame.quit()
                    sys.exit()

    def update(self, dt):
        for button in self.buttons:
            button.update()

    def draw(self, screen):
        self.display.fill(self.s.background_color)

        for button in self.buttons:
            button.draw(self.display)
