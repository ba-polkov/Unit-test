import pytest

from data import DataForTests
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from unittest.mock import Mock



@pytest.fixture(scope='function')
def bun():
    bun = Bun(DataForTests.BLACK_BUN, DataForTests.PRICE_BLACK_BUN)
    return bun


@pytest.fixture(scope='function')
def burger():
    burger = Burger()
    return burger


@pytest.fixture(scope='function')
def ingredient():
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, DataForTests.CHILI_SAUSE, DataForTests.PRICE_CHILI_SAUSE)
    return ingredient


@pytest.fixture(scope='function')
def mock():
    mock = Mock()
    return mock
