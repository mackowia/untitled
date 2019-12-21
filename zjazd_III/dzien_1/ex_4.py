#TESTOWANIE

def formatuj (*args, **kwargs) :
    result = "\n".join(args)
    for nazwa, wartosc in kwargs.items():
        result = result.replace("$+nazwa", str(wartosc))
    return result

def test_formatuj_no_kwargs():
    expect =  """aa    
bb
cc"""
    assert formatuj("aa", "bb", "cc") == expected


def test_formatuj_single_line_with_kwargs():
    assert formatuj("Podróż z $miasto1 do $miasto2 zajmuje $czas h",
        miasto1="Los Angeles", miasto2="Yorktown", czas=5)

#def test_formatuj_multiple_lines_multiple_kwargs():
#    expect= "Hej!\nMam niecieski samochód\nMam też niebieski rower\nA nawet mam niebieski dom, bo niebieski to mój ulubiony kolor" \
#    " A nawet mam $kolor dom, bo $kolor to mój ulubiony kolor.",\
#    powitanie= "Hej!", kolor="niebieski")  ZLE!!!!!!!





#kwargs == ["miasto1" : "Los Angeles", ....