class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, amount):
        items_bought = []
        for item in self.amount:
            if item not in items_bought:
                items_bought.append(item)

        pass
        #receives numbers of items bought and returns total cost

    def make_purchase(self):
        items_bought = self.get_price
        inventory_total = []


        #receives number of items to be bought and decreases the amount by that much

    def add_discount(self, amount, price):
        regular_price = self.price
        discounted_10 = regular_price / 10
        discounted_20 = regular_price / 5
        new_price = 0.0
        if amount < 10:
            return regular_price
        elif amount >= 10 and amount <= 99:
            new_price = regular_price - discounted_10
            return new_price
        elif amount > 100:
            new_price = regular_price - discounted_20
            return new_price
        else:
            return regular_price


if __name__ == "__main__":
    pass