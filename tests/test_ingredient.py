import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import INGREDIENT_TEST_CASES

@pytest.mark.parametrize("name, type, price", INGREDIENT_TEST_CASES)
def test_ingredient_creation(name, type, price):
    ingredient = Ingredient(type, name, price)
    assert ingredient.get_name() == name
    assert ingredient.get_price() == price
    assert ingredient.get_type() == type
