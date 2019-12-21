class Basket:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def print_info(self):
        print(f"Produkty w koszyku: {self.name!r}, ilość: {self.id}, cena: {self.price} PLN. W sumie {...} PLN ")





#basket = Basket ()
#product = Product (1, 'Woda', 10.00)
#basket.add_product(product, 5)
#basket.count+total_price()
#basket.generate_report()
