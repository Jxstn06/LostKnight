from Mapstuff.raum import Room
from lostknightdb import Spieler

Spieler.createTable(ifNotExists=True)


class Dungeon:
    def __init__(self, spieler=None):
        self.spieler_x = spieler.PositionX
        self.spieler_y = spieler.PositionY
        self.spieler = spieler

        self.rooms = {}
        spawnraum = self.get_room_id(self.spieler_x, self.spieler_y)
        self.rooms[spawnraum] = Room(self.spieler)
        self.c_room_id = self.rooms[spawnraum]

        # Räume herstellen aus JSON
        dungeon_rooms = self.spieler.dungeon

    # Hatte Fehler mit der nicht static Version
    @staticmethod
    def get_room_id(x, y):
        return f'{x}_{y}'

    def get_room(self, x, y):
        room_id = self.get_room_id(x, y)
        if room_id not in self.rooms:
            self.rooms[room_id] = Room()
        return self.rooms[room_id]


# Test
# spielerwa = Spieler(Name='Justin', Klasse='Schurke')
# Dung = Dungeon(spieler=spielerwa)
# print(Dung.rooms)
# print(Dung.get_room(0, 0))
# spielerwa.deleteBy(Name='Justin')
