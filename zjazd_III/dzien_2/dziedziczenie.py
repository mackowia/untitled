class Pies:
    rasa = "mieszaniec"
    def __init__(self):
        self.x = 0
        self.y = 0

    def __str__(self):
        return f"Pies rasy {self.rasa}, x={self.x}, y={self.y}"

    def biegnij(self):
        self.x += 1
        self.y += 1

    def zjedz_karme(self, karma):
        pass

    def daj_glos(self):
        print("Hau Hau!")

class Lagotto(Pies):    #to jest rasa psów, które znajduja trufle
    rasa = "Lagotto"
    def znajdz_trufle(self):
        return "Trufla"

class Haski(Pies):
    rasa = "Haski"
    def daj_glos(self):
        print("Uuuola!")

class Hart(Pies):
    rasa = "Hart"
    def biegnij(self):
        super().biegnij()
        #self._super_biegnij()
        super().biegnij()
        #self._super_biegnij()
        super().biegnij()
        #self._super_biegnij()

azor = Pies()
print(azor)
azor.biegnij()
print(azor)
azor.daj_glos()

dzuseppe = Lagotto()
print(dzuseppe)#dzuseppe- imie psa rasy Lagotto
dzuseppe.daj_glos()
print (dzuseppe.znajdz_trufle())

tajga = Haski()
print(tajga)    #tajga- imie psa rasy Husky
tajga.daj_glos()

szybki = Hart()
print(szybki)    #szybki- imie psa rasy Hart
szybki.biegnij()
print(szybki)