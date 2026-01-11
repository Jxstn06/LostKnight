class Manager:
    def __init__(self, szene):
        self.szene = szene

        self.spieler = None
        self.map = None

    def get_szene(self):
        return self.szene

    def set_szene(self, szene):
        self.szene = szene
