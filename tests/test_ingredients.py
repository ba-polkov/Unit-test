import pytest

from data import IngredientData
from praktikum.ingredient import Ingredient

class TestIngredient:

    @pytest.mark.parametrize('ingredient_type, name, price', [IngredientData.list_ingredient[0],
                                                              IngredientData.list_ingredient[3]])
    def test_get_price_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize('ingredient_type, name, price', [IngredientData.list_ingredient[1],
                                                              IngredientData.list_ingredient[4]])
    def test_get_name_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('ingredient_type, name, price', [IngredientData.list_ingredient[2],
                                                              IngredientData.list_ingredient[5]])
    def test_get_ingredient_type_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type