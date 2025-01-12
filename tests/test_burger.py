import pytest
from conftest import *
from helpers import RandomCred
from praktikum.ingredient_types import *
from moks.mock_bun import *
from moks.mock_ingredient import *
from praktikum.burger import Burger
from data import Constants

class TestBurger:
    def test_set_buns(self, name, price):
        mock_bun = set_mock_bun(name, price)
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun.get_name() == name
        assert burger.bun.get_price() == price

    @pytest.mark.paramitrize(
        "type_ingredient",
        ([
            [INGREDIENT_TYPE_SAUCE],
            [INGREDIENT_TYPE_FILLING]
        ])
    )
    def test_add_ingredient(self, name, price, type_ingredient):
        mock_ingredient = set_mock_ingredient(name, price, type_ingredient)
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0] == mock_ingredient
        assert len(burger.ingredients) == 1

    def test_remove_ingredient(self, name, price, type_ingredient):
        mock_ingredient_1 = set_mock_ingredient(name, price, type_ingredient)
        mock_ingredient_2 = set_mock_ingredient(name, price, type_ingredient)
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient_2

    def test_move_ingredient(self, name, price, type_ingredient):
        mock_ingredient_1 = set_mock_ingredient(name, price, type_ingredient)
        mock_ingredient_2 = set_mock_ingredient(name, price, type_ingredient)
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(0, 1)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_ingredient_2
        assert burger.ingredients[1] == mock_ingredient_1

    def test_get_price(self, name, price, type_ingredient):
        price_bun = RandomCred.generate_random_float()
        price_ingredient = RandomCred.generate_random_float()
        sum_price = price_bun * 2 + price_ingredient
        mock_bun = set_mock_bun(name, price_bun)
        mock_ingredient = set_mock_ingredient(name, price_ingredient, type_ingredient)
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == sum_price

    def test_get_receipt(self):
        mock_bun = set_mock_bun(Constants.BUN_NAME, Constants.BUN_PRICE)
        mock_ingredient_1 = set_mock_ingredient(Constants.INGREDIENT_NAME_1, Constants.INGREDIENT_PRICE_1, Constants.INGREDIENT_TYPE_1)
        mock_ingredient_2 = set_mock_ingredient(Constants.INGREDIENT_NAME_2, Constants.INGREDIENT_PRICE_2, Constants.INGREDIENT_TYPE_2)
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        assert burger.get_receipt() == Constants.CREATE_RECEIPT
