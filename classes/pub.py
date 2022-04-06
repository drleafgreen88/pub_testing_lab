class Pub:
    def __init__(self, input_name, input_till, input_drinks):
        self.name = input_name
        self.till = input_till
        self.drinks = input_drinks

    def add_money(self, price):
        self.till += price

    def check_customer_age(self, input_age):
        if input_age < 18:
            print("Sorry buddy")

    def customer_drunkenness(self, alcohol_level):
        if alcohol_level >= 10:
            print("No more tonight buddy")

    # def stock_check(self)