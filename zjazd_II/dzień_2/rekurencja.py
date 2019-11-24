#python broni przed nieskonczona rekurencja( w tym przypadku broni przed wywalaniem wszystkich liczb w nieskonczonosc, tu sie konczy na 996)

def funkcja(n):
    print(n)
    funkcja(n+1)

funkcja(1)
