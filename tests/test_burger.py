import pytest
from unittest.mock import MagicMock

class TestBurger:
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
        ingredient2 = MagicMock()
        ingredient1.get_name.return_value = "Cheese sauce"
        ingredient2.get_name.return_value = "Ketchup"

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient2, ingredient1]

    @pytest.mark.parametrize("ingredient, expected_total", [
        ([("FILLING", "Cheese", 30.0), ("SAUCE", "Сheese sauce", 20.0)], 250.0),
        ([("FILLING", "Tomato", 10.0), ("FILLING", "Ketchup", 20.0)], 230.0)
    ])
    def test_get_price(self, burger, bun, ingredient, expected_total):
        burger.set_buns(bun)
        for ingredient_type, name, price in ingredient:
            ingredient_mock = MagicMock()
            ingredient_mock.get_name.return_value = name
            ingredient_mock.get_type.return_value = ingredient_type
            ingredient_mock.get_price.return_value = price
            burger.add_ingredient(ingredient_mock)
        assert burger.get_price() == expected_total

    def test_get_receipt(self, burger, bun, ingredient):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        expected_receipt = f'(==== {bun.get_name()} ====)\n'\
                           f'= {ingredient.get_type().lower()} {ingredient.get_name()} =\n'\
                           f'(==== {bun.get_name()} ====)\n'\
                           '\n'\
                           f'Price: {burger.get_price()}'

        assert burger.get_receipt() == expected_receipt
