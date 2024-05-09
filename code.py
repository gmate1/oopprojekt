from abc import ABC


class Szoba(ABC):

    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam
    pass