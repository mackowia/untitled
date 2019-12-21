#TESTOWANIE

def splaszcz(lista):
    result = []
    for element in lista:
        if isinstance(element, list):
            #wiemy, że element jest listą
            for subelement in splaszcz(element):
                result.append(subelement)
        else:
            return.append(subelement)
    return result

def test_flat_list():
    assert splaszcz([1,2,3]) == ([1,2,3])

def test_one_embedded_list():
    assert splaszcz([1, [2,3]]) == [1,2,3]

def test_one_embedded_level2():
    assert splaszcz([1, [2,[3,43]]) == [1,2,3,4] #nie wykona tego test

def test_form_exercise():
        assert splaszcz([1,2,3,[4,5,[6]],7]) == [1,2,3,4,5,6,7]