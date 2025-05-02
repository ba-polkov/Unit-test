import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum import ingredient_types


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

@pytest.fixture
def ingredient():
    ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, 'Соус', 60)
    return ingredient