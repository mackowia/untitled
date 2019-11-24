#*argumenty to *args (ang.arguments)- łapie pozycyjne
# **kwargs (od ang."keywordarguments")- łapie kluczowe

def funkcja(*argumenty):
    print(argumenty)
    #print(".....
    if argumenty:
        print("pierwszy argument to", argumenty[0])
    for argument in argumenty:
        print(argument, end=" ")
    print()
funkcja (1, 2, 3, 4)
funkcja("test", [1,5], {1:"a"})
# #funkcja(1, kupic="kota") # nie zadziała, bo * dziala na zmienne bez przypisanej wartosci/ nazwane -> kupic= "kota"

def funkcja(imie, *argumenty, kupic='nic'):
    print(argumenty)
    if argumenty:
        print("pierwszy argument to", argumenty[0])
    for argument in argumenty:
        print(argument, end=" ")
    print()
funkcja (1, 2, 3, 4)
funkcja("Azor", [1,5], {1:"a"})
funkcja(1, kupic="kota") # juz teraz zadziala bo w (*argumenty, kupic='nic')