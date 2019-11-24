def pole_trapezu(wysokosc, podstawa1, podstawa2):
    return wysokosc * (podstawa1+podstawa2)/2

def test_argumenty_pozycyjne():
    assert pole_trapezu(10,3,6) == 45

def test_argumenty_nazwane():
    assert pole_trapezu(wysokosc=10, podstawa1=3, podstawa2=6) == 45

# def test_argumenty_nazwane():
#    assert pole_trapezu(podstawa1=3, wysokosc=10, podstawa2=6) == 45 # przypisujac wartosc w funkcji mozna wartosci wpisywac w obojetnie jakiej kolejnosci;
#    wartosci to nie zmienne, nalezy pisac je bez spacji tzn wartosc=9 (w zmiennej wartosc = 9- przypisuje "wasrtosci" liczbe 9)

#def test_argumenty_nie_nazwane_w_kolejnosci():
    #assert pole_trapezu(podstawa2=6, wysokosc=10, podstawa1=3) == 45

#def test_argumenty_nazwane_i_nie_nazwane():
    #assert pole_trapezu(10,3, podstawa2=6) == 45   # nie trzeba podawac nazwy kazdej wasrtosci (tu brakuje wysokosc i podstawa1)
    #assert pole_trapezu(10,podstawa2=6, podstawa1=3) == 45 # nie trzeba podawac kazdej wartosci+ mozna zmieniac miejsce innych wastosci;
# (brakuje wysokosc i podsatwa1 i podstawa2 sa zamienione kolejnosci)



def pole_elipsy(promien, rozciagniecie):
    return(3.14 * promien **2) * rozciagniecie

def test_pole_elipsy_z_rozciagnieciem():
    assert pole_elipsy(1,2) == 3.14 * 2
    assert pole_elipsy(promien=1,rozciagniecie=2) == 3.14 * 2
    assert pole_elipsy(rozciagniecie=2, promien=1) == 3.14 * 2

def test_pole_elipsy_bez_rozciagniecia():
    assert pole_elipsy(1) == pole_elipsy(1,1) ==3.14
    assert pole_elipsy(promien=1) == pole_elipsy(1,1) == 3.14
    #assert pole_elipsy(rozciagniecie=1_ -> błąd