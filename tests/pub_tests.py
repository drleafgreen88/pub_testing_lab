import unittest

from classes.customer import Customer
from classes.drink import Drink
from classes.pub import Pub

class TestPub(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Stuart", 100, 18)
        self.drink =  Drink("Jack Daniels", 1.50, 3)
        self.pub = Pub("Prancing Pony", 1000)

    def test_money_added_to_till(self):
        self.pub.add_money(self.drink.price)
        self.assertEqual(1001.50, self.pub.till)

    def test_check_customer_age(self):
        self.pub.check_customer_age(self.customer.age)

    def test_check_customer_alcohol_level(self):
        self.pub.customer_drunkenness(self.customer.drunk_lvl)