import pytest
from unittest.mock import Mock


@pytest.fixture
def bun_mock():
    bun = Mock()
    bun.get_price.return_value = 100
    bun.get_name.return_value = "Булка"
    return bun


@pytest.fixture
def ingredient_mock():
    ingredient = Mock()
    ingredient.get_price.return_value = 50
    ingredient.get_name.return_value = "Котлета"
    ingredient.get_type.return_value = "SAUCE"
    return ingredient
