class SwietyMikolaj:
    def __init__(self,imie="Mikołaj"):
        self.imie = imie

    def przywitaj_sie(self):
        print(f"HoHoHo! Jestem {self.imie}")

    def daj_prezent(self, dla_kogo):
        return f"Prezent dla {dla_kogo}"

mikolaj1 = SwietyMikolaj("Mikołajek")
print("Ten SwietyMikolaj nazywa się", mikolaj1.imie)
inni_mikolajowie = [SwietyMikolaj("Andrzej"), SwietyMikolaj("Baltazar"), SwietyMikolaj()] #COS POSZLO NIE TAK :)