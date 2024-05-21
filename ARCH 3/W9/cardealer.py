#create a class named car
class Car:

    #create four fields (brand, model, color, price) and implement these using the init function
    def __init__(self, brand, model, color, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        # a fifth field called sold with default value False
        self.sold = False
        # by default the car is not sold yet, here its default is none
        self.sold_to = None

    #define the car selling method with its needed functions
    def sell(self, customer):
        # if car is sold, sold turns to true
        self.sold = True
        # the sold marking will show who bought it
        self.sold_to = customer

    #define a method that prints the info of called car
    def print(self):
        #assign a string to the status of a car being sold or available with an if statement
        sold_status = "Not sold yet" if not self.sold else f"Sold to: {self.sold_to.name}"
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Price: {self.price}")
        print(sold_status)

#repeat the methods in the class of motorcycle as addition
#creates two options to buy: cars and motorcycles
class motorcycle:
    def __init__(self, brand, model, color, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.sold = False
        self.sold_to = None

    def sell(self, customer):
        self.sold = True
        self.sold_to = customer

    def print(self):
        #refactor this sentence
        sold_status = "Not sold yet" if not self.sold else f"Sold to: {self.sold_to.name}"
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Price: {self.price}")
        print(sold_status)

#class customer that rules the functions related to the customers input
class Customer:

    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"Name: {self.name}")

def main():
    pass


if __name__ == "__main__":
    main()


