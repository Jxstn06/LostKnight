from sqlobject import *

sqlhub.processConnection = connectionForURI('sqlite:LostKnight.sqlite')


class Klasse(SQLObject):
    Name = StringCol()
    Leben = IntCol(default=0)
    Mana = IntCol(default=0)
    Kraft = IntCol(default=0)
    Verteidigung = IntCol(default=0)
    Geschicklichkeit = IntCol(default=0)
    Intelligenz = IntCol(default=0)
    Luck = IntCol(default=0)
    Initiative = IntCol(default=0)


class Spieler(SQLObject):
    Name = StringCol()
    Klasse = StringCol()
    Level = IntCol(default=1)
    XP = IntCol(default=0)
    Leben = IntCol(default=20)
    Mana = IntCol(default=10)
    Kraft = IntCol(default=10)
    Verteidigung = IntCol(default=5)
    Geschicklichkeit = IntCol(default=5)
    Intelligenz = IntCol(default=5)
    Luck = IntCol(default=3)
    Initiative = IntCol(default=5)
    Status_json = StringCol(default='{}')
    PositionX = IntCol()
    PositionY = IntCol()
    Map = StringCol()

    # from JSON to Dict
    @property
    def status(self):
        return json.dumps(self.Status_json)

    # from Dict to JSON saved in self.status
    @status.setter
    def status(self, status):
        self.Status_json = json.dumps(status)

    def update_status(self):
        status = self.Status
        for name, info in status.items():
            if 'dauer' in info and info['dauer'] > 0:
                info['dauer'] -= 1
        self.status = status


def create_classes():
    Spieler.createTable(ifNotExists=True)
    Klasse.createTable(ifNotExists=True)
    if Klasse.tableExists():
        Klasse(
            Name='Beserker',
            Leben=5,
            Mana=0,
            Kraft=8,
            Verteidigung=5,
            Geschicklichkeit=2,
            Intelligenz=0,
            Luck=0,
            Initiative=1
        ),
        Klasse(
            Name='Ritter',
            Leben=10,
            Mana=5,
            Kraft=3,
            Verteidigung=10,
            Geschicklichkeit=0,
            Intelligenz=2,
            Luck=0,
            Initiative=-2
        ),
        Klasse(
            Name='Magier',
            Leben=5,
            Mana=15,
            Kraft=0,
            Verteidigung=2,
            Geschicklichkeit=1,
            Intelligenz=10,
            Luck=0,
            Initiative=-1
        )
        Klasse(
            Name='Schurke',
            Leben=5,
            Mana=0,
            Kraft=5,
            Verteidigung=2,
            Geschicklichkeit=8,
            Intelligenz=2,
            Luck=2,
            Initiative=3
        )
