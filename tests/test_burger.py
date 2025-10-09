import sys
import os
import pytest
from unittest.mock import Mock

current_dir = os.path.dirname(__file__)
project_root = os.path.dirname(current_dir)
sys.path.insert(0, project_root)

from praktikum.burger import Burger


class TestBurger:
    def test_burger_initialization(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self):
        burger = Burger()
        bun_mock = Mock()
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    def test_add_ingredient(self):
        burger = Burger()
        ingredient_mock = Mock()
        burger.add_ingredient(ingredient_mock)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient_mock

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient_mock = Mock()
        burger.add_ingredient(ingredient_mock)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_remove_ingredient_invalid_index(self):
        burger = Burger()
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)

    def test_move_ingredient(self):
        burger = Burger()
        ingredient1, ingredient2, ingredient3 = Mock(), Mock(), Mock()
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)
        
        burger.move_ingredient(1, 2)
        assert burger.ingredients == [ingredient1, ingredient3, ingredient2]

    def test_move_ingredient_invalid_index(self):
        burger = Burger()
        ingredient_mock = Mock()
        burger.add_ingredient(ingredient_mock)
        with pytest.raises(IndexError):
            burger.move_ingredient(1, 0)

    @pytest.mark.parametrize("bun_price,ingredient_prices,expected_total", [
        (100, [50, 75], 325),
        (50, [25, 25, 25], 175),
        (200, [], 400),
        (0, [10, 20], 30),
    ])
    def test_get_price(self, bun_price, ingredient_prices, expected_total):
        burger = Burger()
        bun_mock = Mock()
        bun_mock.get_price.return_value = bun_price
        burger.set_buns(bun_mock)
        
        for price in ingredient_prices:
            ingredient_mock = Mock()
            ingredient_mock.get_price.return_value = price
            burger.add_ingredient(ingredient_mock)
        
        assert burger.get_price() == expected_total

    def test_get_price_no_bun(self):
        burger = Burger()
        with pytest.raises(AttributeError):
            burger.get_price()

    def test_get_receipt(self):
        burger = Burger()
        bun_mock = Mock()
        bun_mock.get_name.return_value = "black bun"
        bun_mock.get_price.return_value = 100
        burger.set_buns(bun_mock)
        
        sauce = Mock()
        sauce.get_type.return_value = "SAUCE"
        sauce.get_name.return_value = "hot sauce"
        sauce.get_price.return_value = 100
        
        filling = Mock()
        filling.get_type.return_value = "FILLING"
        filling.get_name.return_value = "cutlet"
        filling.get_price.return_value = 100
        
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        
        receipt = burger.get_receipt()
        
        assert "(==== black bun ====)" in receipt
        assert "= sauce hot sauce =" in receipt
        assert "= filling cutlet =" in receipt
        assert "Price: 400" in receipt

    def test_get_receipt_no_bun(self):
        burger = Burger()
        with pytest.raises(AttributeError):
            burger.get_receipt()