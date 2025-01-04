import pytest
from praktikum.ingredient import Ingredient
from data import (
    INGREDIENT_NAME, INGREDIENT_TYPE, INGREDIENT_PRICE,
    INGREDIENT_NAME_NEXT, INGREDIENT_TYPE_NEXT, INGREDIENT_PRICE_NEXT
)

@pytest.mark.parametrize("name, type_, price", [
    (INGREDIENT_NAME, INGREDIENT_TYPE, INGREDIENT_PRICE),
    (INGREDIENT_NAME_NEXT, INGREDIENT_TYPE_NEXT, INGREDIENT_PRICE_NEXT),
    ('Бекон', 'Начинка', 40.00)
])
def test_ingredient_initialization(name, type_, price):
    ingredient = Ingredient(type_, name, price)
    assert ingredient.name == name
    assert ingredient.type == type_
    assert ingredient.price == price

