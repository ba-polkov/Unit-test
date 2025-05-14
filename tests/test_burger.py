import pytest

from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.burger import Bun
from praktikum.ingredient_types import *

@pytest.mark.burger
class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        bun = Bun('Зерновая', 120)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name='сок лимона', price=10)
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name='сок лимона', price=10)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0


    def test_move_ingredient(self):
        burger = Burger()
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, name='сок лимона', price=10)
        ingredient2= Ingredient(INGREDIENT_TYPE_FILLING,name='сироп клюквы', price=15)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0,1)
        assert burger.ingredients[1] == ingredient1

    def test_get_price(self):
        burger = Burger()
        bun = Mock()
        bun.get_price.return_value = 20
        ingredient = Mock()
        ingredient.get_price.return_value = 30
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        final_price = 70
        actual_price = burger.get_price()
        assert final_price == actual_price


    def test_get_receipt(self):
        bun= Bun ('Соевая булка', 50)
        ingredient1 = Ingredient('соус', 'сироп клюквы', 10)
        ingredient2 = Ingredient('соус', 'сырный', 15)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        expected_receipt = (
            "(==== Соевая булка ====)\n"
            "= соус сироп клюквы =\n"
            "= соус сырный =\n"
            "(==== Соевая булка ====)\n\n"
            "Price: 125"
        )
        actual_receipt = burger.get_receipt()
        assert expected_receipt== actual_receipt







