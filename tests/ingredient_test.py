import pytest
from unittest.mock import Mock
from practicum.ingredient import Ingredient
from practicum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    @pytest.mark.parametrize('ingredient_type,name,price', [
        (INGREDIENT_TYPE_SAUCE, 'hot sauce', 100),
        (INGREDIENT_TYPE_FILLING, 'cutlet', 200)
    ])
    def test_ingredient_initialization(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.type == ingredient_type
        assert ingredient.name == name
        assert ingredient.price == price

    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'sour cream', 200)
        assert ingredient.get_price() == 200

    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, 'dinosaur', 300)
        assert ingredient.get_name() == 'dinosaur'

    def test_get_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'chili sauce', 300)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE