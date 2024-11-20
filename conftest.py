import pytest
from unittest.mock import Mock
from data import BUN_NAME, BUN_PRICE, INGREDIENT_NAME, INGREDIENT_PRICE, INGREDIENT2_NAME, INGREDIENT2_PRICE
from practicum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.fixture()
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = BUN_NAME
    mock_bun.get_price.return_value = BUN_PRICE
    return mock_bun

@pytest.fixture()
def mock_ingredient1():
    mock_ingredient1 = Mock()
    mock_ingredient1.name = INGREDIENT_NAME
    mock_ingredient1.price = INGREDIENT_PRICE
    mock_ingredient1.type = INGREDIENT_TYPE_SAUCE
    mock_ingredient1.get_price.return_value = INGREDIENT_PRICE
    mock_ingredient1.get_name.return_value = INGREDIENT_NAME
    mock_ingredient1.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock_ingredient1

@pytest.fixture()
def mock_ingredient2():
    mock_ingredient2 = Mock()
    mock_ingredient2.name = INGREDIENT2_NAME
    mock_ingredient2.price = INGREDIENT2_PRICE
    mock_ingredient2.type = INGREDIENT_TYPE_FILLING
    mock_ingredient2.get_price.return_value = INGREDIENT2_PRICE
    mock_ingredient2.get_name.return_value = INGREDIENT2_NAME
    mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_FILLING
    return mock_ingredient2






