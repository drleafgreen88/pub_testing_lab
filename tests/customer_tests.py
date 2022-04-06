import unittest
from classes.customer import Customer
from classes.drink import Drink
from classes.pub import Pub

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Stuart", 100)
        self.drink =  Drink("Jack Daniels", 1.50)
        self.pub = Pub("Prancing Pony", 1000)

    def test_customer_has_name(self):
        self.assertEqual("Stuart", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(100, self.customer.wallet)

    def test_customer_has_enough_money(self):
        self.customer.remove_money(1.50)
        self.customer.wallet >= self.drink.price

    def test_money_added_to_till(self):
        self.pub.add_money(1.50)
        self.assertEqual(1001.50, self.pub.till)

    #could replace the list with a dictionary and remove a drink with each transaction
    def test_customer_buys_drink(self):
        self.customer.buy_drink("Jack Daniels")
        self.assertEqual(1, len(self.customer.drinks))

    #
    def test_customer_orders_drink(self):
        customer = Customer("Stuart", 100)
        self.customer.buy_drink("Jack Daniels")
        self.customer.remove_money(1.50)
        self.pub.add_money(1.50)

        # self.assertEqual()
        # self.customer.buy_drink("Jack Daniels")
        # self.customer.remove_money(1.50)
        # self.pub.add_money(1.50)
