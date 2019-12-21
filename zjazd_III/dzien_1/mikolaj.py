#1
class SwietyMikolaj:
    def przywitaj_sie(self):
        print("HoHoho!")

mikolaj = SwietyMikolaj()
print(type(mikolaj))
print(mikolaj)
mikolaj.przywitaj_sie()


#2
mikolaj1 = SwietyMikolaj()
mikolaj2 = SwietyMikolaj()
mikolaj1.przywitaj_sie()
mikolaj2.przywitaj_sie()



#3
mikolaj1 = SwietyMikolaj()
mikolaj2 = SwietyMikolaj()
inni_mikolajowie = [SwietyMikolaj(),SwietyMikolaj(), SwietyMikolaj()]

mikolaj1.przywitaj_sie()
mikolaj2.przywitaj_sie()
for mikolaj in inni_mikolajowie:
    mikolaj.przywitaj_sie()


#4
class SwietyMikolaj:

    def przywitaj_sie(self):
        print("HoHoho!")

    def daj_prezent(self, dla_kogo):
        return f"Prezent dla {dla_kogo}"

mikolaj1.przywitaj_sie()
mikolaj2.przywitaj_sie()
for mikolaj in inni_mikolajowie:
    mikolaj.przywitaj_sie()

print(mikolaj1.daj_prezent("Agaty")) #dlaczego blad??


#5
class SwietyMikolaj:
    def __init__(self, imie):
        self.imie = "Mikołaj"

    def przywitaj_sie(self):
        print(f"HoHoHo! Jestem {self.imie}")

    def daj_prezent(self, dla_kogo):
        return f"Prezent dla {dla_kogo}"

mikolaj1 = SwietyMikolaj("Mikołajek")
print("Ten SwietyMikolaj nazywa się", mikolaj1.imie)
inni_mikolajowie = [SwietyMikolaj("Andrzej"), SwietyMikolaj("Baltazar"), SwietyMikolaj("")]