import pytest
from unittest.mock import Mock

from tests.conftest import burger


class TestBurger:

    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient_sauce(self, burger, ingredient_sauce):
        burger.add_ingredient(ingredient_sauce)
        assert ingredient_sauce in burger.ingredients

    def test_add_ingredient_fill(self, burger, ingredient_fill):
        burger.add_ingredient(ingredient_fill)
        assert ingredient_fill in burger.ingredients

    def test_remove_ingredient(self, burger, ingredient_sauce, ingredient_fill):
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_fill)
        burger.remove_ingredient(0)
        assert burger.ingredients == [ingredient_fill]

    def test_move_ingredient(self, burger, ingredient_sauce, ingredient_fill):
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_fill)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient_fill, ingredient_sauce]

    def test_get_price_with_ingredients(self,burger, bun, ingredient_sauce):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_sauce)
        assert burger.get_price() == bun.get_price.return_value * 2 + ingredient_sauce.get_price.return_value

    def test_get_price_without_ingredients(self,burger, bun):
        burger.set_buns(bun)
        assert burger.get_price() == bun.get_price.return_value * 2

    def test_get_receipt(self, burger, bun, ingredient_sauce, ingredient_fill):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_fill)
        receipt = burger.get_receipt()
        new_receipt = (
            '(==== Bulochka ====)\n'
             '= sauce Mayonez =\n'
             '= filling Kotletka =\n'
             '(==== Bulochka ====)\n'
             '\n'
             'Price: 50.0')
        assert receipt == new_receipt

    def test_get_receipt_without_ingredients(self, burger, bun):
        burger.set_buns(bun)
        receipt = burger.get_receipt()
        new_receipt = (
            '(==== Bulochka ====)\n'
            '(==== Bulochka ====)\n'
            '\n'
            'Price: 10.0')
        assert receipt == new_receipt




