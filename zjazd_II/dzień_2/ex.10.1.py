napis = "Oko za oko, ząb za ząb"

literki = {}

#opcja 1:
for literka in napis:
    literka = literka.lower()
    if literka in literki:
        literki[literka] += 1
    else:
        literki[literka]=1

#opcja 2:
    #literki[literka]=literki.get(literka, 0) + 1
#opcja 3:
#dla chętnych: poczytać o defaultdict():


print("Oto nasze literki:")
for literka, ilosc in literki.items():
    #print(f"-{literka!r:}: {ilosc}")
    print("-", repr(literka),':', ilosc) # repr() dodaje cudzyslow


