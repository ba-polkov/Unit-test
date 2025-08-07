import pytest
from unittest.mock import MagicMock


class TestBurger:
    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun
    def test_add_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    def test_remove_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert ingredient not in burger.ingredients

    def test_move_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        burger.add_ingredient(MagicMock())
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == ingredient

    @pytest.mark.parametrize("ingredient_data, expected_price", [
        ([("SAUCE", "hot sauce", 100.0), ("FILLING", "cutlet", 100.0)], 600.0),
        ([("FILLING", "dinosaur", 200.0), ("SAUCE", "sour cream", 200.0)], 800.0)
    ])
    def test_get_price(self, burger, bun, ingredient_data, expected_price):
        burger.set_buns(bun)
        for ingredient_type, name, price in ingredient_data:
            ingredient_mock = MagicMock()
            ingredient_mock.get_name.return_value = name
            ingredient_mock.get_type.return_value = ingredient_type
            ingredient_mock.get_price.return_value = price
            burger.add_ingredient(ingredient_mock)
        assert burger.get_price() == expected_price

    def test_get_receipt(self, burger, bun, ingredient):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        receipt = burger.get_receipt()
        assert f'(==== {bun.get_name()} ====)' in receipt
        assert f'= {ingredient.get_type().lower()} {ingredient.get_name()} =' in receipt
        assert 'Price:' in receipt
