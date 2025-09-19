import pytest
from unittest.mock import Mock

class TestBurger:
    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingridient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    def test_remove_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self, burger):
        ingredient_1 = Mock()
        ingredient_1.get_name.return_value = "Cheese"
        ingredient_2 = Mock()
        ingredient_2.get_name.return_value = "Ketchup"

        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)

        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient_2, ingredient_1]

    def test_remove_invalid_index(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        with pytest.raises(IndexError):
            burger.remove_ingredient(1)

    @pytest.mark.parametrize("ingredient_data, expected_price", [
        ([("FILLING", "Cheese", 50.0), ("Sauce", "Ketchup", 20.0)], 270.0), ([("FILLING", "lettuce", 10.0), ("FILLING", "Tomato", 15.0)], 225.0)
        ])

    def test_get_receipt(self, burger, bun, ingredient):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        expected_receipt = f'(==== {bun.get_name()} ====)\n'\
                           f'= {ingredient.get_type().lower()} {ingredient.get_name()} =\n'\
                           '\n'\
                           f'Price: {burger.get_price()}'

        assert burger.get_receipt() == expected_receipt