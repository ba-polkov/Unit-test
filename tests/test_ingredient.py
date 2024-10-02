import pytest
from praktikum.ingredient import Ingredient
import data


class TestIngredient:
    @pytest.mark.parametrize("ingredient_type, name, price", data.INGREDIENTS)
    def test_ingredients_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize("ingredient_type, name, price", data.INGREDIENTS)
    def test_ingredients_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("ingredient_type, name, price", data.INGREDIENTS)
    def test_ingredients_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price



