import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *
from conftest import *

class TestIngredient:

    def test_get_price(self, type_ingredient, name, price):
        ingredient = Ingredient(type_ingredient, name, price)
        price_ingredient = ingredient.price
        assert ingredient.get_price() == price_ingredient

    def test_init_ingredient_price(self, type_ingredient, name, price):
        ingredient = Ingredient(type_ingredient, name, price)
        price_ingredient = ingredient.price
        assert ingredient.price == price_ingredient

    def test_get_name(self, type_ingredient, name, price):
        ingredient = Ingredient(type_ingredient, name, price)
        name_ingredient = ingredient.name
        assert ingredient.get_name() == name_ingredient

    def test_init(self, type_ingredient, name, price):
        ingredient = Ingredient(type_ingredient, name, price)
        name_ingredient = ingredient.name
        assert ingredient.name == name_ingredient

    @pytest.mark.parametrize(
        "type_ingredient",
        ([
            [INGREDIENT_TYPE_SAUCE],
            [INGREDIENT_TYPE_FILLING]
        ])
    )
    def test_ingredient_types(self, type_ingredient, name, price):
        ingredient = Ingredient(type_ingredient, name, price)
        type_ingredient = ingredient.type
        assert type_ingredient == type_ingredient
        assert ingredient.get_type() == type_ingredient
