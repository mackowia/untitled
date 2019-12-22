class Pies:
    rasa = "mieszaniec"
    def __str__(self):
        return f"Pies rasy {self.rasa}"

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

azor = Pies()
print(azor)
azor.daj_glos()

dzuseppe = Lagotto()
print(dzuseppe)#dzuseppe- imie psa rasy Lagotto
dzuseppe.daj_glos()
print (dzuseppe.znajdz_trufle())

tajga = Haski()
print(tajga)    #tajga- imie psa rasy Husky
tajga.daj_glos()