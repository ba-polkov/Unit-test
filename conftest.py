import pytest
from unittest.mock import Mock


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "Sesame"
    bun.get_price.return_value = 2.5
    return bun

@pytest.fixture
def mock_ingredient_filling():
    ingredient = Mock()
    ingredient.get_name.return_value = "Beef"
    ingredient.get_price.return_value = 3.0
    ingredient.get_type.return_value = "filling"
    return ingredient

@pytest.fixture
def mock_ingredient_sauce():
    ingredient = Mock()
    ingredient.get_name.return_value = "Ketchup"
    ingredient.get_price.return_value = 1.0
    ingredient.get_type.return_value = "sauce"
    return ingredient
