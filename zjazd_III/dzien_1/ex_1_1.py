class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def print_info(self):
        print(f"Produkt {self.name!r}, id: {self.id}, cena: {self.price} PLN")   #!r -> robi, że Woda jest w cudzyslowie ('Woda')


def test_product_init():
    product = Product(1, 'Woda', 10.99)
    assert product.id == 1
    assert product.name == 'Woda'
    assert product.price == 10.99

#TO POWODUJE:
def test_print_info(capsys):
    product = Product (1, 'Woda', 10.99)
    product.print_info()
    captured = capsys. readoutterr()
    assert captured.out == "Produkct 'Woda', id: 1, cena: 10.99"

if __name__ == '__main__':
    product = Product(1, 'Woda', 10.99)
    product.print_info()