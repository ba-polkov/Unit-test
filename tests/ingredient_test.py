import pytest

from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.praktikum import Ingredient


class TestIngredient:
    @pytest.mark.parametrize("ingredient_type", [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_ingredient_ingredient_type_set(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, 'super spicy sauce', 3.5)
        assert ingredient.get_type() == ingredient_type, f'Expected {ingredient_type} but got {ingredient.get_name()}'

    def test_ingredient_name_set(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'super spicy sauce', 3.5)
        assert ingredient.get_name() == 'super spicy sauce', f'Expected name but got {ingredient.get_name()}'

    def test_ingredient_price_set(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, 'super spicy sauce', 3.5)
        assert ingredient.get_price() == 3.5, f'Expected 3 but got {ingredient.get_price()}'
