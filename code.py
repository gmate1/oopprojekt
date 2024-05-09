from abc import ABC
from datetime import datetime


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
        talalt_foglalas = next((foglalas for foglalas in self.foglalasok if
                                foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum), None)
        if talalt_foglalas is not None:
            return "Ez a szoba már foglalt arra a dátumra"
        if talalt_szoba is None:
            return "Nincs ilyen szobaszámú szoba a szállodában"
        else:
            foglalas = Foglalas(talalt_szoba, datum, nev)
            self.foglalasok.append(foglalas)
            return "A foglalás megtörtént, az összeg pedig: " + str(foglalas.ar) + "Ft"

    def lemondas(self, nev):
        talalt_foglalas = next((foglalas for foglalas in self.foglalasok if foglalas.nev == nev), None)
        if talalt_foglalas is None:
            return "Nincs ilyen foglalás"
        else:
            self.foglalasok.remove(talalt_foglalas)
            return "Sikeres lemondás"

    def foglalasok_list(self):
        output = 'Foglalások:\n'
        for foglalas in self.foglalasok:
            output += "Szobaszám: " + str(foglalas.szoba.szobaszam) + '\n'
            output += "Név: " + foglalas.nev + '\n'
            output += "Dátum: " + foglalas.datum.strftime("%Y-%m-%d") + '\n\n'

        return output

    pass


class Foglalas:

    def __init__(self, szoba, datum, nev):
        self.szoba = szoba
        self.datum = datum
        self.nap = 1
        self.nev = nev
        self.ar = self.nap * szoba.ar

    pass


szobak_tomb = []
szoba1 = EgyAgyasSzoba(1)
szoba2 = EgyAgyasSzoba(2)
szoba3 = KetAgyasSzoba(3)
szobak_tomb.append(szoba1)
szobak_tomb.append(szoba2)
szobak_tomb.append(szoba3)
szalloda = Szalloda('Szálloda', szobak_tomb)
szalloda.foglalas(1, datetime(2025, 5, 9), "Gyuri")
szalloda.foglalas(2, datetime(2025, 5, 9), "Tibi")
szalloda.foglalas(3, datetime(2025, 5, 9), "Feri")
szalloda.foglalas(1, datetime(2025, 5, 10), "Ákos")
szalloda.foglalas(2, datetime(2025, 5, 10), "Máté")

print("Üdvözlünk a szállodában!\nVálassza ki a kívánt műveletet(1,2,3)\n1. Foglalás\n2. Lemondás\n3. Listázás")
valasztott_opcio = input()
if valasztott_opcio == "1":
    print("Ön a foglalást válaszotta, kérem adja meg a foglaláshoz szükséges adatokat")
    bekert_nev = input("Név: ")
    bekert_szobaszam = input("Szobaszám: ")
    bekert_datum = input("Dátum: ")
    try:
        bekert_datum = datetime.strptime(bekert_datum, "%Y-%m-%d")
        bekert_szobaszam = int(bekert_szobaszam)
        print(str(szalloda.foglalas(int(bekert_szobaszam), bekert_datum, bekert_nev)))
    except ValueError:
        print("Nem megfelelő paraméter")
elif valasztott_opcio == "2":
    print("Ön a lemodnást válaszotta, kéream adja meg a lemondáshoz szükséges adatokat")
    bekert_nev = input("Név: ")
    print(szalloda.lemondas(bekert_nev))
elif valasztott_opcio == "3":
    print("Ön a listázást válaszotta")
    print(szalloda.foglalasok_list())
else:
    print("Nem megfelelő paraméter")
