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
