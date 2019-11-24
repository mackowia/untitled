
def czy_jest_pierwsza(liczba):
    if liczba <= 1: #liczby pierwsze musza byc > 1
        return False

    for x in range(2, liczba): #liczba- czego nie chcemy -> (1:2)- 1 chcemy, 2 nie chcemy np. w tuplach, listach, itd
        if liczba % x == 0:
            return False
        #else:
            #return True #bedzie tylko True dla 2
    #else: # to się wykona bo "else" jest na rowni z "for"
        #return True tez sie nie wykona boi nie jest na rowni z "for"
    return True

#print(czy_jest_pierwsza(1))
# print(czy_jest_pierwsza(9))
# print(czy_jest_pierwsza(10))
# print(czy_jest_pierwsza(2))
# print(czy_jest_pierwsza(17))

#print (czy_jest_pierwsza(1)) == False
#print (czy_jest_pierwsza(9)) == False
#print (czy_jest_pierwsza(10)) == False
#print (czy_jest_pierwsza(2)) == True
#print (czy_jest_pierwsza(17)) == True

def test_mniejszy_od_2():
    assert czy_jest_pierwsza(1) == False

def test_nie_pierwsza_parzysta():
   assert czy_jest_pierwsza(9) == False

def test_nie_pierwsza_parzysta():
    assert czy_jest_pierwsza(10) == False

def test_nie_pierwsza_parzysta():
    assert czy_jest_pierwsza(2) == True

def test_nie_pierwsza_parzysta():
    assert czy_jest_pierwsza(17) == True

