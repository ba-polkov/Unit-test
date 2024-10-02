import pytest
from unittest.mock import Mock
from data import BUNS, INGREDIENTS


@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = BUNS[0][0]
    mock_bun.get_price.return_value = BUNS[0][1]
    return mock_bun


@pytest.fixture
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.get_type.return_value = INGREDIENTS[0][0]
    mock_ingredient.get_name.return_value = INGREDIENTS[0][1]
    mock_ingredient.get_price.return_value = INGREDIENTS[0][2]
    return mock_ingredient


@pytest.fixture
def mock_second_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.get_type.return_value = INGREDIENTS[2][0]
    mock_ingredient.get_name.return_value = INGREDIENTS[2][1]
    mock_ingredient.get_price.return_value = INGREDIENTS[2][2]
    return mock_ingredient
