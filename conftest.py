import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "КосмоБулка"
    bun.get_price.return_value = 100

    return bun

@pytest.fixture
def mock_burger():
    burger = Mock()
    burger.get_bun.return_value = "Булка"
    burger.get_ingredients.return_value = "Салат"

    return Burger()

@pytest.fixture
def mock_ingredients_sauce():
    ingredients = Mock()
    ingredients.get_type.return_value = 'SAUCE'
    ingredients.get_name.return_value = "Чили"
    ingredients.get_price.return_value = 20

    return ingredients

@pytest.fixture
def mock_ingredients_filling():
    ingredients = Mock()
    ingredients.get_type.return_value = 'FILLING'
    ingredients.get_name.return_value = "cucumber"
    ingredients.get_price.return_value = 100

    return ingredients