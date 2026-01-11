from settings import Settings

from Mapstuff.feld import Feld


class Room:
    def __init__(self, typ='Leer', spieler=None):
        self.typ = typ
        self.spieler = spieler
        self.spieler_x = self.spieler.PositionX
        self.spieler_y = self.spieler.PositionY

        self.s = Settings()

        # Sorgt dafür, dass die Raumegröße immer ungrade ist.
        self.x = self.s.raumx if self.s.raumx % 2 else self.s.raumx + 1
        self.y = self.s.raumy if self.s.raumy % 2 else self.s.raumy + 1
        self.visited = False
        self.clear = False

        self.grid = [[Feld(x, y, 'Wand') for x in range(self.x)] for y in range(self.y)]
        self.entry_point = {
            'top': (self.x//2, 0),
            'bottom': (self.x//2, self.y-1),
            'left': (0, self.y//2),
            'right': (self.x-1, self.y//2)
        }
        self.generate_room()

    def generate_room(self):
        for zeile in self.grid:
            for obj in zeile:
                if 0 < obj.x < self.x - 1 and 0 < obj.y < self.y - 1:
                    obj.feldtyp = 'Weg'

        for direction, (ex, ey) in self.entry_point.items():
            self.grid[ey][ex].feldtyp = 'Entry'

    def to_string(self):
        lines = []
        for zeile in self.grid:
            line = ''
            for zelle in zeile:
                match zelle.feldtyp:
                    case 'Wand':
                        line += '/'
                    case 'Entry':
                        line += '█'
                    case 'Weg':
                        line += ' '
                    case 'Spawn':
                        line += 'S'
                    case _:
                        line += '?'

            lines.append(line)
        return '\n'.join(lines)
