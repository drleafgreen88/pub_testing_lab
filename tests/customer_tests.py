import unittest
from classes.customer import Customer
from classes.drink import Drink
from classes.pub import Pub
from classes.food import Food

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Stuart", 100, 18)
        self.drink =  Drink("Jack Daniels", 1.50, 3)
        self.pub = Pub("Prancing Pony", 1000, {"Jack Daniels" : [1.50, 3],
        "Baileys": [2.00, 2.5],
        "Beer": [1, 2]
        })
        self.food = Food("Pie", 5, 2)

    def test_customer_has_name(self):
        self.assertEqual("Stuart", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(100, self.customer.wallet)

    def test_customer_has_enough_money(self):
        self.customer.remove_money(self.drink.price)
        self.customer.wallet >= self.drink.price

    #could replace the list with a dictionary and remove a drink with each transaction
    def test_customer_buys_drink(self):
        self.customer.buy_drink(self.drink, self.pub)
        self.assertEqual(1, len(self.customer.drinks))

    #
    def test_customer_orders_drink(self):

        self.customer.buy_drink(self.drink)
        self.customer.remove_money(self.drink.price)
        self.pub.add_money(self.drink.price)

        # self.assertEqual()
        # self.customer.buy_drink("Jack Daniels")
        # self.customer.remove_money(1.50)
        # self.pub.add_money(1.50)

    def test_customer_buys_food(self):
        self.customer.buy_food(self.food)
