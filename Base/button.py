import pygame


class Button:
    def __init__(self, x, y, b, h, text='', selectable=False, is_input=False):
        self.rect = pygame.Rect(x, y, b, h)
        self.text = text
        self.font = pygame.font.Font(None, 32)
        self.base_color = (200, 200, 200)
        self.current_color = self.base_color
        self.h_color = (160, 160, 0)
        self.hover = False

        self.selectable = selectable
        self.selected = False
        self.s_color = (210, 210, 0)

        self.is_input = is_input

    def get_value(self):
        return self.text

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Mouseclick
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                # selected if selectable
                if self.selectable:
                    self.selected = not self.selected
                else:
                    return True
            # Unselect if Mouseclick happens afo - away from object
            else:
                if self.selectable:
                    self.selected = False
        if event.type == pygame.KEYDOWN and self.selected and self.is_input:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif len(self.text) < 12:
                self.text += event.unicode
        return False

    def update(self):
        maus_pos = pygame.mouse.get_pos()
        self.hover = self.rect.collidepoint(maus_pos)

        if self.selectable and self.selected:
            self.current_color = self.s_color
        elif self.hover:
            self.current_color = self.h_color
        else:
            self.current_color = self.base_color

    def draw(self, screen):
        pygame.draw.rect(screen, self.current_color, self.rect)

        text = self.font.render(self.text, True, (0, 0, 0))
        text_surf = text.get_rect(center=self.rect.center)
        screen.blit(text, text_surf)
