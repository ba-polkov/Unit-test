import pytest

from burger import Burger
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def get_burger_with_ingredients():
    burger = Burger()
    a = Ingredient(INGREDIENT_TYPE_SAUCE, "A", 123)
    b = Ingredient(INGREDIENT_TYPE_FILLING, "B", 345)
    c = Ingredient(INGREDIENT_TYPE_FILLING, "C", 678)
    burger.add_ingredient(a)
    burger.add_ingredient(b)
    burger.add_ingredient(c)

    yield burger, a, b, c
