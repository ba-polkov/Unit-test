import pytest
from unittest.mock import Mock


class TestBurger:
    def test_set_buns_success(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient_success(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    def test_remove_ingredient_success(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient_success(self, burger):
        ingredient1 = Mock()
        ingredient1.get_name.return_value = "chili"
        ingredient2 = Mock()
        ingredient2.get_name.return_value = "barbecue"

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient2, ingredient1]

    @pytest.mark.parametrize("ingredient_data, expected_price", [
        ([("FILLING", "tomato", 20.0), ("SAUCE", "chili", 30.0)], 70.0),
        ([("FILLING", "pepper", 10.0), ("SAUCE", "barbecue", 20.0)], 50.0)
    ])
    def test_get_price_success(self, burger, bun, ingredient_data, expected_price):
        burger.set_buns(bun)
        for ingredient_type, name, price in ingredient_data:
            ingredient_mock = Mock()
            ingredient_mock.get_name.return_value = name
            ingredient_mock.get_type.return_value = ingredient_type
            ingredient_mock.get_price.return_value = price
            burger.add_ingredient(ingredient_mock)
        assert burger.get_price() == expected_price

    def test_get_receipt_success(self, burger, bun, ingredient):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        expected_receipt = f'(==== {bun.get_name()} ====)\n'\
                           f'= {ingredient.get_type().lower()} {ingredient.get_name()} =\n'\
                           f'(==== {bun.get_name()} ====)\n'\
                           '\n'\
                           f'Price: {burger.get_price()}'

        assert burger.get_receipt() == expected_receipt
