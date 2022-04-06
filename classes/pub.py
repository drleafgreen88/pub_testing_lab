class Pub:
    def __init__(self, input_name, input_till):
        self.name = input_name
        self.till = input_till
        self.drinks = ["Jack Daniels", "Baileys", "Beer"]

    def add_money(self, price):
        self.till += price