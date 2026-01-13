import pygame
import sys

from settings import Settings
from Base.szene import Szene
from Base.button import Button


class Load(Szene):
    def __init__(self, display, manager):
        super().__init__()
        self.display = display
        self.manager = manager
        self.s = Settings()

        self.buttons = []

    def handle_events(self, event): pass
    def update(self, dt): pass
    def draw(self, screen): pass
