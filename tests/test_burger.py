import pytest
from praktikum import burger
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from unittest.mock import Mock

class TestBurger:

    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, burger):
        mocked_ingredients = [
            Mock(spec=Ingredient, name="hot sauce", price=100),
            Mock(spec=Ingredient, name="sour cream", price=200),
            Mock(spec=Ingredient, name="chili sauce", price=300),
        ]
        burger.ingredients = mocked_ingredients[:]
        burger.move_ingredient(2, 0)
        assert burger.ingredients == [mocked_ingredients[2], mocked_ingredients[0], mocked_ingredients[1]]

    def test_get_price(self, burger, bun, ingredient):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        expected_price = bun.get_price() * 2 + ingredient.get_price()
        assert burger.get_price() == expected_price

    def test_get_receipt(self, burger, bun, ingredient):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        receipt = burger.get_receipt()
        assert bun.get_name() in receipt
        assert ingredient.get_name() in receipt
        assert str(burger.get_price()) in receipt