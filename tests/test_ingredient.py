import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.mark.parametrize("ingredient_type, name, price, expected_type, expected_name, expected_price", [
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    (INGREDIENT_TYPE_SAUCE, "sour cream", 200, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
    (INGREDIENT_TYPE_FILLING, "cutlet", 150, INGREDIENT_TYPE_FILLING, "cutlet", 150),
    (INGREDIENT_TYPE_FILLING, "sausage", 250, INGREDIENT_TYPE_FILLING, "sausage", 250),
])
class TestIngredient:

    def test_ingredient(self, ingredient_type, name, price, expected_type, expected_name, expected_price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_name() == expected_name

        assert ingredient.get_type() == expected_type

        assert ingredient.get_price() == expected_price
