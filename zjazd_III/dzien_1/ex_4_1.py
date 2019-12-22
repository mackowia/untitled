#PORÓWNAJ Z KODEM KONRADA, COS TU JEST ZLE (50.000000- trzeba skrocic) :)

class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}({self.id}), cena: {self.price:.2f}"

    def print_info(self):
        print(f"Produkt {self.name!r}, id: {self.id}, cena: {self.price} PLN ")

class Basket:
    def __init__(self):
        self.products = {}
        #self._total_price = 0

    def add_product (self, produkt, quantity):
        if produkt in self.products:
            #key == produkt
            self.products[produkt] += quantity
        else:
            self.products[produkt] = quantity

    def count_total_price(self):
        total_price = 0
        for product, quantity in self.products.items():
            total_price += product.price * quantity
        return total_price

    def generate_report(self):
        result = "Produkty w koszyku:\n"
        for product, quantity in self.products.items():
            result += f"-{product.name}({product.id}), cena: {product.price:.2f} x {quantity}\n"
           #result += f"-{product} x {quantity}\n" (to samo co wiersz wyżej, działa bo w wierszu 8 (self. ...)
        result += f"W sumie: {self.count_total_price():2f}"
        return result

def test_basket_empty_price():
    b = Basket()
    assert b.count_total_price() == 0


def test_basket_one_product_price():
    b = Basket()
    p = Product(1, 'Woda', 10.00)
    b.add_product(p, 3)
    assert b.count_total_price() == 3 * 10

def test_basket_multiple_products_price():
    b = Basket()
    woda = Product(1, 'Woda', 10.00)
    chleb= Product(2, 'Chleb', 20.00)
    b.add_product(woda, 3)
    b.add_product(chleb, 1)
    b.add_product(woda, 1)
    assert b.count_total_price() == 4 * 10 + 1 * 20

def test_basket_one_product_report():
    b = Basket()
    p = Product(1, 'Woda', 10.00)
    b.add_product(p, 3)
    expected = """Produkty w koszyku:
-Woda(1), cena: 10.00 x 3
W sumie: 30.00"""
    assert b.generate_report() == expected

def test_basket_multiple_product_report():
    b = Basket()
    p1 = Product(1, 'Pierogi', 10.00)
    p2 = Product(1, 'Choinka', 20.00)
    p3 = Product(1, 'Prezenty', 30.00)
    b.add_product(p1, 10)
    b.add_product(p2, 1)
    b.add_product(p3, 4)
    assert len (b.generate_report().splitlines()) == 2 + 3

if __name__ == '__main__':
    b = Basket()
    woda = Product(1, 'Woda', 10.00)
    chleb = Product(2, 'Chleb', 20.00)
    b.add_product(woda, 3)
    b.add_product(chleb, 1)
    print(b.generate_report())


#def generate_report(self)

#basket = Basket ()
#product = Product (1, 'Woda', 10.00)
#basket.add_product(product, 5)
#basket.count+total_price()
#basket.generate_report()
