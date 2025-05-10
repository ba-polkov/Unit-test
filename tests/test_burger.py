import pytest
from praktikum.burger import Burger
from unittest.mock import Mock
from praktikum.ingredient_types import *
from data import TestData

class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = TestData.buns[0][0]
        mock_bun.get_price.return_value = TestData.buns[0][1]
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredients = Mock()
        mock_ingredients.get_price.return_value = TestData.ingredients[9][2]
        mock_ingredients.get_name.return_value = TestData.ingredients[9][1]
        mock_ingredients.get_type.return_value = INGREDIENT_TYPE_SAUCE
        burger.add_ingredient(mock_ingredients)
        assert burger.ingredients == [mock_ingredients]

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredients = Mock()
        mock_ingredients.get_price.return_value = TestData.ingredients[0][2]
        mock_ingredients.get_name.return_value = TestData.ingredients[0][1]
        mock_ingredients.get_type.return_value = INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredients)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self):
        burger = Burger()
        mock_ingredients = Mock()
        mock_ingredients.get_price.return_value = TestData.ingredients[0][2]
        mock_ingredients.get_name.return_value = TestData.ingredients[0][1]
        mock_ingredients.get_type.return_value = INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredients)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_ingredients

    def test_get_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = TestData.buns[1][1]
        mock_ingredients = Mock()
        mock_ingredients.get_price.return_value = TestData.ingredients[1][2]
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredients]
        price = mock_bun.get_price() * 2 + mock_ingredients.get_price()
        assert burger.get_price() == price

    def test_get_receipt(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = TestData.buns[0][0]
        mock_bun.get_price.return_value = TestData.buns[0][1]
        mock_ingredient1 = Mock()
        mock_ingredient1.get_name.return_value = TestData.ingredients[0][1]
        mock_ingredient1.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient1.get_price.return_value = TestData.ingredients[0][2]
        mock_ingredient2 = Mock()
        mock_ingredient2.get_price.return_value = TestData.ingredients[9][2]
        mock_ingredient2.get_name.return_value = TestData.ingredients[9][1]
        mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_SAUCE
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient1, mock_ingredient2]
        receipt_text = ('(==== Краторная булка N-200i ====)\n= filling Биокотлета из марсианской Магнолии =\n= sauce Соус Spicy-X =\n(==== Краторная булка N-200i ====)\n\nPrice: 3024')
        assert burger.get_receipt() == receipt_text