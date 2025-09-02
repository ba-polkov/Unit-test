import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.mark.parametrize(
    "itype, name, price",
    [
        (INGREDIENT_TYPE_SAUCE, "ketchup", 10),
        (INGREDIENT_TYPE_SAUCE, "chili", 30),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "cheese", 40.5)
    ]
)
# проверка название, начинка, цена
def test_test_ingredient_getters(itype, name, price):
    ingredient = Ingredient(itype, name, price)
    assert ingredient.get_type() == itype
    assert ingredient.get_name() == name
    assert ingredient.get_price() == price
