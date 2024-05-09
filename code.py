from abc import ABC


class Szoba(ABC):

    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

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

    def foglalas(self, szobaszam, datum, nev):
        talalt_szoba = next((szoba for szoba in self.szobak if szoba.szobaszam == szobaszam), None)
        if talalt_szoba is None:
            return "Nincs ilyen szobaszámú szoba a szállodában"
        else:
            foglalas = Foglalas(talalt_szoba, datum, nev)
            self.foglalasok.append(foglalas)
            return foglalas.ar

    pass


class Foglalas:

    def __init__(self, szoba, datum, nev):
        self.szoba = szoba
        self.datum = datum
        self.nap = 1
        self.nev = nev
        self.ar = self.nap * szoba.ar

    pass
