from classes.drink import *

class Customer:
    def __init__(self, input_name, input_wallet, input_age):
        self.name = input_name
        self.wallet = input_wallet
        self.age = input_age
        self.drinks = []
        self.drunk_lvl = 0

    def remove_money(self, price):
        self.wallet >= price

    def buy_drink(self, input_drink, input_pub):
        self.drinks.append(input_drink.name)
        self.drunk_lvl += input_drink.alcohol_level
        print(input_pub.stock[input_drink.name][0])
        # for drink in input_pub.stock:
        #     if drink == input_drink.name:

        # for choice in self.drinks:
        #     if choice == input_drink:
        #         self.drunk_lvl += choice.alcohol_level


        # for choice in Drink.drink_dict:
        #     if input_drink == input_drink:
        #         self.drunk_lvl += choice
    def buy_food(self, input_food):
        self.drunk_lvl -= input_food.rejuvenation_level
        print(self.drunk_lvl)
