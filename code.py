from abc import ABC


class Szoba(ABC):

    def __init__(self, ar, szobaszam, foglalt=False):
        self.ar = ar
        self.szobaszam = szobaszam
        self.foglalt = foglalt

    pass


class EgyAgyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(50, szobaszam)

    pass


class KetAgyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(100, szobaszam)

    pass


class Szalloda:
    def __init__(self, nev, szobak):
        self.nev = nev
        self.szobak = szobak
        self.foglalasok = []

    pass


class Foglalas:

    def __init__(self, szobaszam, datum):
        self.szobaszam = szobaszam
        self.datum = datum
        self.nap = 1

    pass
