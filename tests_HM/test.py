import unittest
from unittest.mock import patch, Mock
from My_classes import *

class CarTest(unittest.TestCase):

    def test_car_equall(self):
        self.assertFalse(car_1== car_2)

        self.assertFalse(car_1< car_2)

        self.assertTrue(car_1> car_2)

    def test_car_change_number(self):
        number = car_1.number
        self.assertTrue(number!= car_1.change_number())

class GarageTest(unittest.TestCase):

    def test_add_car(self):
        garage_1.add(car_1)
        garage_1.add(car_2)
        self.assertEqual(len(garage_1.cars), 2)

    # def test_remove_car(self):
    #     garage_1.remove(car_1)
    #     self.assertEqual(len(garage_1.cars),1)

    def test_hit_hat(self):
        self.assertEqual(garage_2.hit_hap(), 20000)

class CollectionarTest(unittest.TestCase):

    def test_hit_hat(self):
        self.assertEqual(collectionar_1.hit_hat(),20000)
    def test_garages_count(self):
        self.assertEqual(collectionar_1.garages_count(),1)
    def test_cars_count(self):
        self.assertEqual(collectionar_2.cars_count(),3)
    def test_add_car(self):
        collectionar_2.add_car(car_2)
        self.assertEqual(len(collectionar_2.cars),2)
    def test_compare_collectionar(self):
        self.assertTrue(collectionar_1.hit_hat()>collectionar_2.hit_hat())
        self.assertFalse(collectionar_2.hit_hat()<collectionar_1.hit_hat())
        self.assertFalse(collectionar_2.hit_hat() == collectionar_1.hit_hat())

class JsoncarTest(unittest.TestCase):

    @patch('main.Car')

if __name__ == "__main__":
    unittest.main()

