import pytest

from praktikum.ingredient import Ingredient


class TestIngredient:
    list_data = [("SAUCE", "hot sauce", 100.0),
                 ("FILLING", "cutlet", 200.0),
                 ("FILLING", "", 0.0),
                 ("SAUCE", "1", 0.01),
                 ("SAUCE", "c" * 100, 999.99)]

    @pytest.mark.parametrize("types, name, price", list_data)
    def test_ingredients_properties(self, types, name, price):
        ingredient = Ingredient(types, name, price)

        assert ingredient.get_type() == types
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price
