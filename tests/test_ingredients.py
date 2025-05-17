import pytest

from data import SAUCE_PRICE, FILLING_NAME, FILLING_PRICE, SAUCE_NAME
from practicum.ingredient import Ingredient
from practicum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.mark.parametrize("ingredient_types, name, price",[
        (INGREDIENT_TYPE_SAUCE, SAUCE_NAME, SAUCE_PRICE),
        (INGREDIENT_TYPE_FILLING, FILLING_NAME, FILLING_PRICE)
    ])

class TestIngredients:

    def test_ingredient_types(self,ingredient_types, name, price):
        ingredient = Ingredient(ingredient_types, name, price)
        assert ingredient.get_type() == ingredient_types, f"Тип ингредиента '{ingredient.get_type()}' не соответствует '{ingredient_types}' "

    def test_ingredient_name(self, ingredient_types, name, price):
        ingredient = Ingredient(ingredient_types, name, price)
        assert ingredient.get_name() == name , f"Название ингредиента '{ingredient.get_name()}' не соответствует '{name}'"


    def test_ingredient_price(self, ingredient_types, name, price):
        ingredient = Ingredient(ingredient_types, name, price)
        assert ingredient.get_price() == price, f"Цена ингредиента ' {ingredient.get_price()}' не соответствует '{[price]}'"