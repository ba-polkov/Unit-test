import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    params_price = [
        (100.5, 100.5),
        (0.01, 0.01),
        (0.0, 0.0)
    ]

    @pytest.mark.parametrize("actual_price, expected_price", params_price)
    def test_get_price(self, actual_price, expected_price):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Цезарь", actual_price)
        assert ingredient.get_price() == pytest.approx(expected_price) and isinstance(ingredient.get_price(), float)

    params_name = [
        ("Цезарь", "Цезарь"),
        ("", ""),
        ("Цезарь123", "Цезарь123"),
        ("цезарь", "цезарь"),
        ("Cesar", "Cesar"),
        ("!.'-&|\\:", "!.'-&|\\:"),
        ("Ц", "Ц"),
        (" ", " ")
    ]

    @pytest.mark.parametrize("actual_name, expected_name", params_name)
    def test_get_name(self, actual_name, expected_name):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, actual_name, 100.3)
        assert ingredient.get_name() == expected_name and isinstance(ingredient.get_name(), str)

    params_type = [
        (INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_SAUCE),
        (INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_FILLING),
        ("", ""),
        ("Соус123", "Соус123"),
        ("котлета", "котлета"),
        ("!.'-&|\\:", "!.'-&|\\:"),
        ("С", "С"),
        (" ", " ")
    ]

    @pytest.mark.parametrize("actual_type, expected_type", params_type)
    def test_get_type(self, actual_type, expected_type):
        ingredient = Ingredient(actual_type, "Цезарь", 100.3)
        assert ingredient.get_type() == expected_type and isinstance(ingredient.get_type(), str)