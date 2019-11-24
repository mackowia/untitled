def funkcja(**kwargs):
    dzien_miesiaca = kwargs.get('dzien', 1)
    print(kwargs)

funkcja()
funkcja(dzien=24)
funkcja(dzien=24, miesiac="listopad")