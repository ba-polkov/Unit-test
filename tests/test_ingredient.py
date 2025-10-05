import pytest
from praktikum.ingredient import Ingredient
from data import TestData

class TestIngredient:
    @pytest.mark.parametrize("ingredient_type, name, price", TestData.valid_ingredients)
    def test_valid_ingredient_creation(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price

    @pytest.mark.parametrize("ingredient_type, name, price", TestData.invalid_ingredients)
    def test_invalid_ingredient_raises_error(self, ingredient_type, name, price):
        with pytest.raises(ValueError):
            Ingredient(ingredient_type, name, price)
