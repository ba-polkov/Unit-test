import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import (
    INGREDIENT_TYPE_SAUCE,
    INGREDIENT_TYPE_FILLING,
)

@pytest.mark.unit
@pytest.mark.parametrize(
    "t, name, price",
    [
        (INGREDIENT_TYPE_SAUCE, "ketchup", 10.0),
        (INGREDIENT_TYPE_FILLING, "beef", 100.0),
    ],
)
def test_ingredient_getters(t, name, price):
    ing = Ingredient(t, name, price)
    assert ing.get_type() == t
    assert ing.get_name() == name
    assert ing.get_price() == price
