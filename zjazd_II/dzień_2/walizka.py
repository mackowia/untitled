#podejrzenia - gdzie mniej wiecej bylo klikane na klawiaturze
def otworz_walizke(szyfr):
    return szyfr == "dudda68"

def kolejna_literka(lista_podejrzen, czesc_hasla, krok):
    print("Funkcja wywolana z", czesc_hasla)
    if krok == len(lista_podejrzen):
        print("próbuje otworzyć walizke z hasłem", czesc_hasla)
        return False

    for literka in lista_podejrzen[krok]:
        kolejna_literka(lista_podejrzen, czesc_hasla+literka, krok+1)

def otwieracz(lista_podejrzen):
    return kolejna_literka(lista_podejrzen, "", 0)

podejrzenia = ['sdf', 'yui8j', 'sdfe', 'dscf', 'aq', '6', '89']
print("Hasło to", otwieracz(podejrzenia))