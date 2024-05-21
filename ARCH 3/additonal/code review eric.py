#code is clean and strong
# could use comments
# erg duidelijk en kort gevat

class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, amount):
        if amount < 10:
            total_price = self.price * amount

        elif 10 <= amount <= 99:
            total_price = (self.price * amount) * 0.9

        else:
            total_price = (self.price * amount) * 0.8
        return total_price

    def make_purchase(self, amount):
        self.amount -= amount