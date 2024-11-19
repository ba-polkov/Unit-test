import pytest
from unittest.mock import MagicMock
from praktikum.burger import Burger


class TestBurger:
    @pytest.fixture
    def burger(self):
        return Burger()

    @pytest.fixture
    def bun(self):
        bun_mock = MagicMock()
        bun_mock.get_name.return_value = "Small Bun"
        bun_mock.get_price.return_value = 100.0
        return bun_mock

    @pytest.fixture
    def ingredient(self):
        ingredient_mock = MagicMock()
        ingredient_mock.get_name.return_value = "Cheese"
        ingredient_mock.get_type.return_value = "FILLING"
        ingredient_mock.get_price.return_value = 50.0
        return ingredient_mock

    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    def test_remove_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self, burger):
        ingredient1 = MagicMock()
        ingredient1.get_name.return_value = "Cheese"
        ingredient1.get_type.return_value = "FILLING"
        ingredient1.get_price.return_value = 50.0

        ingredient2 = MagicMock()
        ingredient2.get_name.return_value = "Ketchup"
        ingredient2.get_type.return_value = "SAUCE"
        ingredient2.get_price.return_value = 20.0

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient2, ingredient1]

    @pytest.mark.parametrize("ingredient_data, expected_price", [
        ([("FILLING", "Cheese", 50.0), ("SAUCE", "Ketchup", 20.0)], 270.0),
        ([("FILLING", "Lettuce", 10.0), ("FILLING", "Tomato", 15.0)], 225.0)
    ])
    def test_get_price(self, burger, bun, ingredient_data, expected_price):
        burger.set_buns(bun)
        for ingredient_type, name, price in ingredient_data:
            ingredient_mock = MagicMock()
            ingredient_mock.get_name.return_value = name
            ingredient_mock.get_type.return_value = ingredient_type
            ingredient_mock.get_price.re
