import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

test_ingredient_data = [
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    (INGREDIENT_TYPE_FILLING, "sour cream", 200),
    (INGREDIENT_TYPE_SAUCE, "chili sauce", 300)
]
@pytest.mark.parametrize("type, name, price", test_ingredient_data)
def test_get_price_ingredient(type, name, price):
    ingredient = Ingredient(type, name, price)
    assert ingredient.get_price() == price

@pytest.mark.parametrize("type, name, price", test_ingredient_data)
def test_get_name_ingredient(type, name, price):
    ingredient = Ingredient(type, name, price)
    assert ingredient.get_name() == name

@pytest.mark.parametrize("type, name, price", test_ingredient_data)
def test_get_type_ingredient(type, name, price):
    ingredient = Ingredient(type, name, price)
    assert ingredient.get_type() == type
