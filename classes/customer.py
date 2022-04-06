class Customer:
    def __init__(self, input_name, input_wallet):
        self.name = input_name
        self.wallet = input_wallet
        self.drinks = []

    def remove_money(self, price):
        self.wallet >= price

    def buy_drink(self, input_drink):
        self.drinks.append(input_drink)