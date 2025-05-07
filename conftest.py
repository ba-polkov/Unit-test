import pytest

from bun import Bun
from ingredient import Ingredient
from data import test_data
from ingredient_types import INGREDIENT_TYPE_FILLING


@pytest.fixture
def bun():
    return Bun(test_data.BUN_NAME, test_data.BUN_PRICE)


@pytest.fixture
def ingredient():
    return Ingredient(
        INGREDIENT_TYPE_FILLING, test_data.INGREDIENT_NAME, test_data.INGREDIENT_PRICE,
    )