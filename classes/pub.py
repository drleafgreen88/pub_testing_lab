class Pub:
    def __init__(self, input_name, input_till):
        self.name = input_name
        self.till = input_till
        self.drinks = ["Jack Daniels", "Baileys", "Beer"]

    def add_money(self, price):
        self.till += price

    def check_customer_age(self, input_age):
        if input_age < 18:
            print("Sorry buddy")

    def customer_drunkenness(self, alcohol_level):
        if alcohol_level >= 10:
            print("No more tonight buddy")