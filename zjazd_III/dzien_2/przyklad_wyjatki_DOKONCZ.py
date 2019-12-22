class IncorrectUserAction(Exception):
    pass

def obsluga_kantoru():
    operacja = input("Chcesz kupić czy sprzedać? [s/k]:")
    if operacja == 'k':
        ...
    elif operacja == 's':
        ...
    else:
        #raise Exception ("Podana niepoprawna operacja")     #jeden z wyjatkow (->Exception)
    raise ValueError("Podana niepoprawna operacja")
    ...
    return 100
#jak wpisze w konsoli np X to wywali blad "raise Exception"

print("Poczatek programu")
try:
    kwota = obsluga_kantoru()
    print("Kolejna linijka w try")
except:    #obsługa wyjatku
#except ValueError("Podana niepoprawna operacja")
#    print("Podano złą wartość")
    print("Wystąpiło dzielenie przez zero")
#except ZeroDivisionError:
#print("Koniec programu, pożegnanie uzytkowanika")