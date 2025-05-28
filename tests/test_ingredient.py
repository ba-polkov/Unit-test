import pytest

from praktikum.ingredient import Ingredient
from tests.data import INGREDIENT1, INGREDIENT2, PRICE1, PRICE2, TYPE1, TYPE2


class TestIngredient:

    @pytest.mark.parametrize('price', [PRICE1, PRICE2])
    def test_get_price(self, price):
        ingredient = Ingredient(INGREDIENT1, INGREDIENT2, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize('custom_ingredient', ['INGREDIENT1, INGREDIENT2'])
    def test_get_name(self, custom_ingredient):
        ingredient = Ingredient(TYPE1, custom_ingredient, PRICE1)
        assert ingredient.get_name() == custom_ingredient

    @pytest.mark.parametrize('type_of_ingredient', [TYPE1, TYPE2])
    def test_get_type(self, type_of_ingredient):
        ingredient = Ingredient(type_of_ingredient, INGREDIENT1, PRICE1)
        assert ingredient.get_type() == type_of_ingredient