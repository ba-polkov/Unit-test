import pytest
from tests.mock_data import MockData
from src.bun import Bun
from src.ingredient import Ingredient
from unittest.mock import Mock
from src.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from src.burger import Burger


@pytest.fixture(scope='function')
def mock():
    mock = Mock()
    return mock

@pytest.fixture(scope='function')
def mock_bun():
    bun = Bun(MockData.BLACK_BUN, MockData.BLACK_BUN_PRICE)
    return bun

@pytest.fixture(scope='function')
def ingredient_sauce():
    test_ingredient_sauce = Ingredient(INGREDIENT_TYPE_SAUCE, MockData.HOT_SAUCE, MockData.HOT_SAUCE_PRICE)
    return test_ingredient_sauce

@pytest.fixture(scope='function')
def ingredient_filling():
    test_ingredient_filling = Ingredient(INGREDIENT_TYPE_FILLING, MockData.CUTLET_FILLING, MockData.CUTLET_FILLING_PRICE)
    return test_ingredient_filling

@pytest.fixture(scope='function')
def mock_burger():
    mock_burger = Burger()
    return mock_burger