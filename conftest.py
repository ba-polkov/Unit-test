import pytest
from data import *
from unittest.mock import Mock

@pytest.fixture(scope='function')
def mock_bun():
    mock_bun = Mock()
    mock_bun.name = bun_name_price[0]
    mock_bun.price = bun_name_price[1]
    yield mock_bun

@pytest.fixture(scope='function')
def mock_ingredient():
    ingredient = Mock()
    ingredient.type = ingredient_sauce[0]
    ingredient.name = ingredient_sauce[1]
    ingredient.price = ingredient_sauce[2]
    yield ingredient

