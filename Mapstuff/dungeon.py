from Mapstuff.raum import Room


class Dungeon:
    def __init__(self, spieler=None):
        self.rooms = {}
        self.spieler_x = 0
        self.spieler_y = 0
        self.c_room_id = self.get_room_id(0, 0)
        self.spieler = spieler

        # spawnraum = self.get_room_id(self.spieler_x, self.spieler_y)
        # spawnraum.spieler_pos =

    # Hatte Fehler mit der nicht static Version
    @staticmethod
    def get_room_id(x, y):
        return f'{x}_{y}'

    def get_room(self, x, y):
        room_id = self.get_room_id(x, y)
        if room_id not in self.rooms:
            self.rooms[room_id] = Room()
        return self.rooms[room_id]
