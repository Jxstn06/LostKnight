from Mapstuff.raum import Room


class Dungeon:
    def __init__(self, spieler):
        self.spieler = spieler
        self.spieler_x = spieler.PositionX
        self.spieler_y = spieler.PositionY

        self.rooms = {}
        start_id = self.get_room_id(self.spieler_x, self.spieler_y)
        self.rooms[start_id] = Room()
        self.current_room_id = start_id
        self.current_room = self.rooms[start_id]

        self.save_dungeon()

    def save_dungeon(self):
        data = {
            'current_room': self.current_room_id,
            'rooms': {rid: {} for rid in self.rooms.keys()}
        }
        self.spieler.dungeon = data

    # Hatte Fehler mit der nicht static Version
    @staticmethod
    def get_room_id(x, y):
        return f'{x}_{y}'

    def get_room(self, x, y):
        room_id = self.get_room_id(x, y)
        if room_id not in self.rooms:
            self.rooms[room_id] = Room()
        return self.rooms[room_id]
