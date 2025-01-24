from unittest.mock import Mock
import pytest
from data import TestData

@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = TestData.BUN_NAME
    mock_bun.get_price.return_value = TestData.BUN_PRICE
    return mock_bun

@pytest.fixture
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.get_name.return_value = TestData.INGREDIENT_NAME
    mock_ingredient.get_price.return_value = TestData.INGREDIENT_PRICE
    mock_ingredient.get_type.return_value = TestData.INGREDIENT_TYPE
    return mock_ingredient

@pytest.fixture
def mock_ingredient_next():
    mock_ingredient_next = Mock()
    mock_ingredient_next.get_name.return_value = TestData.INGREDIENT_NAME_NEXT
    mock_ingredient_next.get_price.return_value = TestData.INGREDIENT_PRICE_NEXT
    mock_ingredient_next.get_type.return_value = TestData.INGREDIENT_TYPE_NEXT
    return mock_ingredient_next
