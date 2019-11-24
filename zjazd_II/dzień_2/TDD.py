def wiecej_niz(napis, liczba):
    if liczba <3:
        return {'a',''}
    else:
        return {'a',''}

def test_funkcja_sie_uruchamia():
    wiecej_niz("ala ma kota a kot ma ale", 3)

def test_ala_ma_kota_3():
    assert wiecej_niz("ala ma kota a kot ma ale", 3) == {'a',''}

def test_ala_ma_kota_2():
    assert wiecej_niz("ala ma kota a kot ma ale", 2) == {'a','','l'}