import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.mark.parametrize("type_, name, price", [
    (INGREDIENT_TYPE_SAUCE, "Sauce", 10),
    (INGREDIENT_TYPE_FILLING, "Filling", 20)
])
def test_ingredient_init(type_, name, price):
    ing = Ingredient(type_, name, price)
    assert ing.type == type_

@pytest.mark.parametrize("type_, name, price", [
    (INGREDIENT_TYPE_SAUCE, "Sauce", 10),
    (INGREDIENT_TYPE_FILLING, "Filling", 20)
])
def test_ingredient_get_type(type_, name, price):
    ing = Ingredient(type_, name, price)
    assert ing.get_type() == type_

@pytest.mark.parametrize("type_, name, price", [
    (INGREDIENT_TYPE_SAUCE, "Sauce", 10),
    (INGREDIENT_TYPE_FILLING, "Filling", 20)
])
def test_ingredient_get_name(type_, name, price):
    ing = Ingredient(type_, name, price)
    assert ing.get_name() == name

@pytest.mark.parametrize("type_, name, price", [
    (INGREDIENT_TYPE_SAUCE, "Sauce", 10),
    (INGREDIENT_TYPE_FILLING, "Filling", 20)
])
def test_ingredient_get_price(type_, name, price):
    ing = Ingredient(type_, name, price)
    assert ing.get_price() == price