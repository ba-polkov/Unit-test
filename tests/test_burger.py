import unittest
from unittest.mock import Mock

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from data import DataTests


class TestBurger(unittest.TestCase):

    def test_set_buns(self):
        mock = Mock()
        burger = Burger()
        mock.get_name.return_value = DataTests.BLACK_BUN
        mock.get_price.return_value = DataTests.PRICE_BLACK_BUN
        burger.set_buns(mock)
        self.assertEqual(burger.bun.get_name(), DataTests.BLACK_BUN) and self.assertEqual(burger.bun.get_price(), DataTests.PRICE_BLACK_BUN)

    def test_add_ingredient(self):
        mock = Mock()
        burger = Burger()
        mock.get_price.return_value = DataTests.PRICE_HOT_SAUSE
        mock.get_name.return_value = DataTests.HOT_SAUSE
        mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
        burger.add_ingredient(mock)
        self.assertEqual(burger.ingredients, [mock])

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, DataTests.HOT_SAUSE, DataTests.PRICE_HOT_SAUSE)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        self.assertEqual(burger.ingredients, [])

    def test_move_ingredient(self):
        burger = Burger()
        ingredient_0 = Ingredient(INGREDIENT_TYPE_SAUCE, DataTests.HOT_SAUSE, DataTests.PRICE_HOT_SAUSE)
        ingredient_1 = Ingredient(INGREDIENT_TYPE_SAUCE, DataTests.CHILI_SAUSE, DataTests.PRICE_CHILI_SAUSE)
        burger.add_ingredient(ingredient_0)
        burger.add_ingredient(ingredient_1)
        burger.move_ingredient(0, 1)
        self.assertEqual(burger.ingredients[1].name, DataTests.HOT_SAUSE)

    def test_get_price(self):
        burger = Burger()
        bun = Bun(DataTests.BLACK_BUN, DataTests.PRICE_BLACK_BUN)
        burger.set_buns(bun)
        sauce_1 = Ingredient(INGREDIENT_TYPE_SAUCE, DataTests.HOT_SAUSE, DataTests.PRICE_HOT_SAUSE)
        sauce_2 = Ingredient(INGREDIENT_TYPE_SAUCE, DataTests.CHILI_SAUSE, DataTests.PRICE_CHILI_SAUSE)
        burger.add_ingredient(sauce_1)
        burger.add_ingredient(sauce_2)
        self.assertEqual(burger.get_price(), 140)

    def test_get_receipt(self):
        mock = Mock()
        burger = Burger()
        mock.get_name.return_value = DataTests.BLACK_BUN
        mock.get_price.return_value = DataTests.PRICE_BLACK_BUN
        burger.set_buns(mock)
        sauce = Ingredient(INGREDIENT_TYPE_SAUCE, DataTests.SOUR_CREAM, DataTests.PRICE_SOUR_CREAM)
        burger.add_ingredient(sauce)
        self.assertEqual(burger.get_receipt(), DataTests.RECEIPT)

