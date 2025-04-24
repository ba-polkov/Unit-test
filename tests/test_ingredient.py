import pytest
from ..ingredient import Ingredient
from ..ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

# Проверяем инициализацию объекта Ingredient
@pytest.mark.parametrize("ingredient_type, name, price", [
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    (INGREDIENT_TYPE_FILLING, "cutlet", 150),
])
def test_ingredient_init(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.type == ingredient_type
    assert ingredient.name == name
    assert ingredient.price == price

# Проверяем работу get_type
@pytest.mark.parametrize("ingredient_type", [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
def test_ingredient_get_type(ingredient_type):
    ingredient = Ingredient(ingredient_type, "Test", 10)
    assert ingredient.get_type() == ingredient_type

# Проверяем работу get_name
def test_ingredient_get_name():
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "TestSauce", 10)
    assert ingredient.get_name() == "TestSauce"

# Проверяем работу get_price
def test_ingredient_get_price():
    ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "TestFilling", 42)
    assert ingredient.get_price() == 42
