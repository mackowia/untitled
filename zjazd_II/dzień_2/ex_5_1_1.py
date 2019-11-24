# silnia dla 0 oraz liczb ujemnych = 1

def silnia(n):
    print("Jesteśmy na", n)
    if n < 1:
        return 1
    return n * silnia(n-1)

    #print("Kończymy z", n)   #mozna odkomentowac, zobaczysz roznice :)
    #return result

print(silnia(5))