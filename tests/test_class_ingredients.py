import pytest
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:
    @pytest.mark.parametrize("ingredient_type, name, price, expected_type", [
        (INGREDIENT_TYPE_SAUCE, "sauce", 50, INGREDIENT_TYPE_SAUCE),
        (INGREDIENT_TYPE_FILLING, "meat", 100, INGREDIENT_TYPE_FILLING)
    ])
    def test_get_type(self, ingredient_type, name, price, expected_type):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == expected_type

    @pytest.mark.parametrize("ingredient_type, name, price, expected_name", [
        (INGREDIENT_TYPE_SAUCE, "sauce", 50, "sauce"),
        (INGREDIENT_TYPE_FILLING, "meat", 100, "meat")
    ])
    def test_get_name(self, ingredient_type, name, price, expected_name):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == expected_name

    @pytest.mark.parametrize("ingredient_type, name, price, expected_price", [
        (INGREDIENT_TYPE_SAUCE, "sauce", 50, 50),
        (INGREDIENT_TYPE_FILLING, "meat", 100, 100)
    ])
    def test_get_price(self, ingredient_type, name, price, expected_price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == expected_price