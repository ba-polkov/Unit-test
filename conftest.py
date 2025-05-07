import pytest

from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from data import test_data
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING


@pytest.fixture
def bun():
    return Bun(test_data.BUN_NAME, test_data.BUN_PRICE)


@pytest.fixture
def ingredient():
    return Ingredient(
        INGREDIENT_TYPE_FILLING, test_data.INGREDIENT_NAME, test_data.INGREDIENT_PRICE,
    )

@pytest.fixture
def database():
    return Database()
