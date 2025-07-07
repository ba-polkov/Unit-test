import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "Булочка"
    bun.get_price.return_value = 100
    return bun


@pytest.fixture
def mock_ingredient_one():
    mock_ingredient_one = Mock()
    mock_ingredient_one.get_type.return_value = INGREDIENT_TYPE_FILLING
    mock_ingredient_one.get_name.return_value = 'Курица'
    mock_ingredient_one.get_price.return_value = 150

    return mock_ingredient_one

@pytest.fixture
def mock_ingredient_two():
    mock_ingredient_two = Mock()
    mock_ingredient_two.get_type.return_value = INGREDIENT_TYPE_SAUCE
    mock_ingredient_two.get_name.return_value = 'Кетчуп'
    mock_ingredient_two.get_price.return_value = 90
    return mock_ingredient_two

