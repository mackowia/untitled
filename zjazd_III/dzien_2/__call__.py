#CO TO JEST __CALL__ ??

class Dodawacz:
    def __call__(self, a, b):
        return a+b
dodawacz = Dodawacz()

print(     dodawacz(1,2)         ) # spacje tylko zeby wbylo widac miejsce, nie musi ich byc



### TO SAMO CO WYZEJ
def dodawacz(a,b):
    return a+b
###
print(dodawacz(1,2))