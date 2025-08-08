import pytest

import data
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient


@pytest.fixture
def bun():
    bun = Bun(data.NAME_BUN, data.PRICE_BUN)
    return bun

@pytest.fixture
def ingredient():
    ingredient = Ingredient(data.TYPE_INGREDIENT, data.NAME_INGREDIENT, data.PRICE_INGREDIENT)
    return ingredient

@pytest.fixture
def burger():
    burger = Burger()
    return burger

@pytest.fixture
def database():
    database = Database()
    return database
