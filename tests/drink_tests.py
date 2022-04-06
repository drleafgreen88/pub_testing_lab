import unittest

from classes.customer import Customer
from classes.drink import Drink
from classes.pub import Pub

class TestDrink(unittest.TestCase):
    def setUp(self):
        drink_dict = {"Jack Daniels" : [1.50, 3],
        "Baileys": [2.00, 2.5],
        "Beer": [1, 2]
        }


        # self.customer = Customer("Stuart", 100)
        # self.drink =  Drink("Jack Daniels", 1.50)
        # self.pub = Pub("Prancing Pony", 1000)