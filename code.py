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
            output += "Szobaszám: "+str(foglalas.szoba.szobaszam) + '\n'
            output += "Név: "+foglalas.nev + '\n'
            output += "Dátum: "+foglalas.datum + '\n\n'


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

print("Üdvözlünk a szállodában!\nVálassza ki a kívánt műveletet(1,2,3)\n1. Foglalás\n2. Lemondás\n3. Listázás")
valasztott_opcio=input()
if valasztott_opcio=="1":
    print("Ön a foglalást válaszotta, kérem adja meg a foglaláshoz szükséges adatokat")
    nev=input("Név: ")
    szobaszam=input("Szobaszám: ")
    datum=input("Dátum: ")
    try:
        szobaszam = int(szobaszam)
        print("A foglalás megtörtént, az összeg pedig: " + str(szalloda.foglalas(int(szobaszam), datum, nev)) + " Ft")
    except ValueError:
        print(szalloda.foglalas(szobaszam, datum, nev))
elif valasztott_opcio=="2":
    print("Ön a lemodnást válaszotta, kéream adja meg a lemondáshoz szükséges adatokat")
    nev=input("Név: ")
    print(szalloda.lemondas(nev))
elif valasztott_opcio=="3":
    print("Ön a listázást válaszotta")
    print(szalloda.foglalasok_list())
else:
    print("Nem megfelelő paraméter")
