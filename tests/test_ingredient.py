import unittest
from data import DataTests
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestIngredient(unittest.TestCase):

    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, DataTests.HOT_SAUSE, DataTests.PRICE_HOT_SAUSE)
        self.assertIsInstance(ingredient.get_price(), float)

    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, DataTests.SOUR_CREAM, DataTests.PRICE_SOUR_CREAM)
        self.assertEqual(ingredient.get_name(), DataTests.SOUR_CREAM)

    def test_get_name_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, DataTests.SOUR_CREAM, DataTests.PRICE_SOUR_CREAM)
        self.assertIsInstance(ingredient.get_name(), str)

    def test_get_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, DataTests.HOT_SAUSE, DataTests.PRICE_HOT_SAUSE)
        self.assertEqual(ingredient.get_type(), INGREDIENT_TYPE_SAUCE)
