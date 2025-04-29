from typing import AnyStr

import pytest
from conftest import mock, mock_bun
from mock_data import MockData
from src.burger import Burger
from src.bun import Bun
from src.ingredient import Ingredient
from src.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestBurger:

    @pytest.mark.parametrize('name, price', [
        (MockData.BLACK_BUN, MockData.WHITE_BUN_PRICE),
        (MockData.WHITE_BUN, MockData.WHITE_BUN_PRICE),
        (MockData.RED_BUN, MockData.RED_BUN_PRICE)
    ])
    def test_set_buns_selected_buns_and_added_to_burger(self, mock, name, price):
        mock.get_name.return_value = name
        mock.get_price.return_value = price
        burger = Burger()
        burger.set_buns(mock)
        assert burger.bun.get_name() == name
        assert burger.bun.get_price() == price

    @pytest.mark.parametrize('type, name, price', [
        (INGREDIENT_TYPE_SAUCE, MockData.HOT_SAUCE, MockData.HOT_SAUCE_PRICE),
        (INGREDIENT_TYPE_SAUCE, MockData.SOUR_CREAM, MockData.SOUR_CREAM_PRICE),
        (INGREDIENT_TYPE_SAUCE, MockData.CHILI_SAUCE, MockData.CHILI_SAUCE_PRICE),
        (INGREDIENT_TYPE_FILLING, MockData.CUTLET_FILLING, MockData.CUTLET_FILLING_PRICE),
        (INGREDIENT_TYPE_FILLING, MockData.DINOSAUR_FILLING, MockData.DINOSAUR_FILLING_PRICE),
        (INGREDIENT_TYPE_FILLING, MockData.SAUSAGE_FILLING, MockData.SAUSAGE_FILLING_PRICE)
    ])
    def test_add_ingredient_selected_ingredients_and_added_to_burger(self, mock, name, price, type):
        mock.get_name.return_value = name
        mock.get_price.return_value = price
        mock.get_type.return_value = type
        burger = Burger()
        burger.add_ingredient(mock)
        assert burger.ingredients == [mock]

    @pytest.mark.parametrize('type, name, price', [
        (INGREDIENT_TYPE_SAUCE, MockData.HOT_SAUCE, MockData.HOT_SAUCE_PRICE),
        (INGREDIENT_TYPE_SAUCE, MockData.SOUR_CREAM, MockData.SOUR_CREAM_PRICE),
        (INGREDIENT_TYPE_SAUCE, MockData.CHILI_SAUCE, MockData.CHILI_SAUCE_PRICE),
        (INGREDIENT_TYPE_FILLING, MockData.CUTLET_FILLING, MockData.CUTLET_FILLING_PRICE),
        (INGREDIENT_TYPE_FILLING, MockData.DINOSAUR_FILLING, MockData.DINOSAUR_FILLING_PRICE),
        (INGREDIENT_TYPE_FILLING, MockData.SAUSAGE_FILLING, MockData.SAUSAGE_FILLING_PRICE)
    ])
    def test_remove_ingredient_from_burger(self, mock, name, price, type):
        mock.get_name.return_value = name
        mock.get_price.return_value = price
        mock.get_type.return_value = type
        burger = Burger()
        burger.add_ingredient(mock)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    @pytest.mark.parametrize('type, name1, price1, name2, price2', [
        (INGREDIENT_TYPE_SAUCE, MockData.HOT_SAUCE, MockData.HOT_SAUCE_PRICE, MockData.SOUR_CREAM, MockData.SOUR_CREAM_PRICE),
        (INGREDIENT_TYPE_SAUCE, MockData.CHILI_SAUCE, MockData.CHILI_SAUCE_PRICE, MockData.HOT_SAUCE, MockData.HOT_SAUCE_PRICE),
        (INGREDIENT_TYPE_FILLING,  MockData.CUTLET_FILLING, MockData.CUTLET_FILLING_PRICE, MockData.SAUSAGE_FILLING, MockData.SAUSAGE_FILLING_PRICE),
        (INGREDIENT_TYPE_FILLING, MockData.DINOSAUR_FILLING, MockData.DINOSAUR_FILLING_PRICE, MockData.CUTLET_FILLING, MockData.CUTLET_FILLING_PRICE)
    ])
    def test_move_ingredient_in_burger(self, type, name1, price1, name2, price2):
        ingredient_1 = Ingredient(type, name1, price1)
        ingredient_2 = Ingredient(type, name2, price2)
        burger = Burger()
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1].name == ingredient_1.name
        assert burger.ingredients[0].name == ingredient_2.name

    @pytest.mark.parametrize('bun_name, bun_price', [
        (MockData.BLACK_BUN, MockData.BLACK_BUN_PRICE),
        (MockData.WHITE_BUN, MockData.WHITE_BUN_PRICE),
        (MockData.RED_BUN, MockData.RED_BUN_PRICE)
    ])
    @pytest.mark.parametrize('ingredient_type, ingredient_name, ingredient_price', [
        (INGREDIENT_TYPE_SAUCE, MockData.HOT_SAUCE, MockData.HOT_SAUCE_PRICE),
        (INGREDIENT_TYPE_SAUCE, MockData.SOUR_CREAM, MockData.SOUR_CREAM_PRICE),
        (INGREDIENT_TYPE_SAUCE, MockData.CHILI_SAUCE, MockData.CHILI_SAUCE_PRICE),
        (INGREDIENT_TYPE_FILLING, MockData.CUTLET_FILLING, MockData.CUTLET_FILLING_PRICE),
        (INGREDIENT_TYPE_FILLING, MockData.DINOSAUR_FILLING, MockData.DINOSAUR_FILLING_PRICE),
        (INGREDIENT_TYPE_FILLING, MockData.SAUSAGE_FILLING, MockData.SAUSAGE_FILLING_PRICE)
    ])
    def test_get_price_of_the_burger(
        self, mock_bun, bun_name, bun_price, ingredient_type, ingredient_name, ingredient_price):
        bun = Bun(bun_name, bun_price)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(Ingredient(ingredient_type, ingredient_name, ingredient_price))
        expected_price = bun_price * 2 + ingredient_price
        assert burger.get_price() == expected_price

    @pytest.mark.parametrize('bun_name, bun_price', [
        (MockData.BLACK_BUN, MockData.BLACK_BUN_PRICE),
        (MockData.WHITE_BUN, MockData.WHITE_BUN_PRICE),
        (MockData.RED_BUN, MockData.RED_BUN_PRICE)
    ])
    def test_get_receipt_of_burger_with_only_buns(self, bun_name, bun_price):
        bun = Bun(bun_name, bun_price)
        burger = Burger()
        burger.set_buns(bun)
        expected_receipt = f'(==== {bun.get_name()} ====)\n(==== {bun.get_name()} ====)\n\nPrice: {bun.get_price() * 2}'
        assert burger.get_receipt() == expected_receipt



