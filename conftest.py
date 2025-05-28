from unittest.mock import Mock
import pytest

from tests.data import BUN_NAME1, PRICE1, TYPE1, INGREDIENT1, PRICE2


@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.name = BUN_NAME1
    mock_bun.price = PRICE1
    return mock_bun


@pytest.fixture
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.type = TYPE1
    mock_ingredient.name = INGREDIENT1
    mock_ingredient.price = PRICE2
    return mock_ingredient


@pytest.fixture
def mock_burger():
    mock_burger = Mock()
    return mock_burger
