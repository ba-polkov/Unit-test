import pytest
from bun import Bun
from burger import Burger
from ingredient import Ingredient
import ingredient_types


@pytest.fixture
def bun():
    bun = Bun('Mike', 500)
    return bun

@pytest.fixture
def burger(bun):
    burger = Burger()
    burger.set_buns(bun)
    ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, 'Соус', 60)
    burger.add_ingredient(ingredient)
    return burger
