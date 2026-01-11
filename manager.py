class Manager:
    def __init__(self):
        self.c_szene = None

    def switch_szene(self, new_szene):
        self.c_szene = new_szene

    def handle_events(self, event):
        self.c_szene.handle_events(event)

    def update(self, dt):
        if self.c_szene:
            self.c_szene.update(dt)

    def draw(self, screen):
        if self.c_szene:
            self.c_szene.draw(screen)
