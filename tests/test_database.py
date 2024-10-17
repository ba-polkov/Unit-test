import unittest
from data import DataTests
from praktikum.database import Database


class TestDatabase(unittest.TestCase):

    def test_available_buns(self):
        data = Database()
        buns = data.available_buns()
        self.assertEqual(buns[0].name, DataTests.BLACK_BUN)

    def test_available_ingredients(self):
        data = Database()
        ingredients = data.available_ingredients()
        self.assertEqual(ingredients[0].name, DataTests.HOT_SAUSE)
