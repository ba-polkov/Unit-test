import pytest

from data import INGREDIENT_SAUCE_TABASCO, INGREDIENT_SAUCE_TOMATO, \
    INGREDIENT_TYPE_DEFAULT, INGREDIENT_NAME_DEFAULT, PRICE_DEFAULT, PRICE_FLOAT, PRICE_INT, PRICE_ZERO
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @pytest.mark.parametrize('ingredient_type', (INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING))
    def test_ingredient_get_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, INGREDIENT_NAME_DEFAULT, PRICE_DEFAULT)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize('ingredient_name', (INGREDIENT_SAUCE_TABASCO, INGREDIENT_SAUCE_TOMATO))
    def test_ingredient_get_name(self, ingredient_name):
        ingredient = Ingredient(INGREDIENT_TYPE_DEFAULT, ingredient_name, PRICE_DEFAULT)
        assert ingredient.get_name() == ingredient_name

    @pytest.mark.parametrize('ingredient_price', (PRICE_ZERO, PRICE_FLOAT, PRICE_INT))
    def test_ingredient_get_price(self, ingredient_price):
        ingredient = Ingredient('default', 'default', ingredient_price)
        assert ingredient.get_price() == ingredient_price
