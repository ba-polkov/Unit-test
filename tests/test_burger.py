from unittest.mock import Mock

import pytest

from praktikum.burger import Burger
from constants import Constants


class TestBurger:
    @pytest.mark.parametrize('name, price', Constants.BUN_DATA)
    def test_set_buns(self, name, price):
        burger = Burger()
        mock = Mock()
        mock.get_name.return_value = name
        mock.get_price.return_value = price
        burger.set_buns(mock)
        assert burger.bun.get_name() == name and burger.bun.get_price() == price

    @pytest.mark.parametrize('ingredient, name, price', Constants.INGREDIENT_DATA)
    def test_add_ingredient(self, ingredient, name, price):
        burger = Burger()
        mock = Mock()
        mock.get_type.return_value = ingredient
        mock.get_name.return_value = name
        mock.get_price.return_value = price
        burger.add_ingredient(mock)
        assert burger.ingredients[0].get_type() == ingredient and burger.ingredients[0].get_name() == name and \
               burger.ingredients[0].get_price() == price

    @pytest.mark.parametrize('ingredient, name, price', Constants.INGREDIENT_DATA)
    def test_remove_ingredient(self, ingredient, name, price):
        burger = Burger()
        mock = Mock()
        mock.get_type.return_value = ingredient
        mock.get_name.return_value = name
        mock.get_price.return_value = price
        burger.add_ingredient(mock)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self):
        burger = Burger()
        mock_1 = Mock()
        mock_1.get_type.return_value = Constants.INGREDIENT_DATA[0][0]
        mock_1.get_name.return_value = Constants.INGREDIENT_DATA[0][1]
        mock_1.get_price.return_value = Constants.INGREDIENT_DATA[0][2]
        burger.add_ingredient(mock_1)
        mock_2 = Mock()
        mock_2.get_type.return_value = Constants.INGREDIENT_DATA[1][0]
        mock_2.get_name.return_value = Constants.INGREDIENT_DATA[1][1]
        mock_2.get_price.return_value = Constants.INGREDIENT_DATA[1][2]
        burger.add_ingredient(mock_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_2

    @pytest.mark.parametrize('name_bun, price_bun, ingredient, name_ingredient, price_ingredient, final_price',
                             Constants.BUN_AND_INGREDIENT_DATA)
    def test_get_price(self, name_bun, price_bun, ingredient, name_ingredient, price_ingredient, final_price):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = name_bun
        mock_bun.get_price.return_value = price_bun
        burger.set_buns(mock_bun)
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = ingredient
        mock_ingredient.get_name.return_value = name_ingredient
        mock_ingredient.get_price.return_value = price_ingredient
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == final_price

    @pytest.mark.parametrize('name_bun, price_bun, final_price', Constants.BUN_AND_FINAL_PRICE_DATA)
    def test_get_receipt(self, name_bun, price_bun, final_price):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = name_bun
        mock_bun.get_price.return_value = price_bun
        burger.set_buns(mock_bun)
        mock_ingredient_first = Mock()
        mock_ingredient_first.get_type.return_value = Constants.INGREDIENT_DATA[0][0]
        mock_ingredient_first.get_name.return_value = Constants.INGREDIENT_DATA[0][1]
        mock_ingredient_first.get_price.return_value = Constants.INGREDIENT_DATA[0][2]
        burger.add_ingredient(mock_ingredient_first)
        mock_ingredient_second = Mock()
        mock_ingredient_second.get_type.return_value = Constants.INGREDIENT_DATA[1][0]
        mock_ingredient_second.get_name.return_value = Constants.INGREDIENT_DATA[1][1]
        mock_ingredient_second.get_price.return_value = Constants.INGREDIENT_DATA[1][2]
        burger.add_ingredient(mock_ingredient_second)
        result = f'(==== {name_bun} ====)\n' \
                 f'= sauce First Ingredient =\n' \
                 f'= filling Second Ingredient =\n' \
                 f'(==== {name_bun} ====)\n\n'\
                 f'Price: {final_price}'
        assert burger.get_receipt() == result
