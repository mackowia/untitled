# **kwargs (od ang."keywordarguments")- łapie kluczowe

def funkcja(**kwargs):
    dzien_miesiaca = kwargs.get('dzien', 1)
    for klucz, wartosc in kwargs.items():
        print("klucz", klucz, "-wartość", wartosc)
        print()

funkcja()
funkcja(dzien=24)
funkcja(dzien=24, miesiac="listopad")