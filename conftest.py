import pytest

from data import const
from unittest.mock import Mock

@pytest.fixture(scope='function')
def mock_bun():
    mock_bun = Mock()
    mock_bun.name = const['TESTS_DATA_BUN'][0]
    mock_bun.price = const['TESTS_DATA_BUN'][1]
    return mock_bun

@pytest.fixture(scope='function')
def mock_ingredient():
    ingredient = Mock()
    ingredient.type = const['TESTS_DATA_INGREDIENT'][0]
    ingredient.name = const['TESTS_DATA_INGREDIENT'][1]
    ingredient.price = const['TESTS_DATA_INGREDIENT'][2]
    return ingredient

@pytest.fixture(scope='function')
def mock_ingredient_2():
    ingredient_2 = Mock()
    ingredient_2.type = const['TESTS_DATA_INGREDIENT_2'][0]
    ingredient_2.name = const['TESTS_DATA_INGREDIENT_2'][1]
    ingredient_2.price = const['TESTS_DATA_INGREDIENT_2'][2]
    return ingredient_2