class Pojazd:
    def podaj_wlasciciela(self):
        return "ZTM"    #warszawki wlasciciel

class Tramwaj(Pojazd):
    def podnies_pantograf(self):
        return "Pantograf podniesiony"

class Autobus(Pojazd):
    def zatrab(self):
        return "Bip! Bip!"

class Trolejbus (Tramwaj, Autobus):
    def rozpocznij_prace(self):
        print(self.podnies_pantograf())
        print(self.zatrab())
        return (f"Ku chwale {self.podaj_wlasciciela()}")

t = Trolejbus()
t.rozpocznij_prace()