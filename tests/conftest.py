import pytest

from unittest.mock import Mock
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "red bun"
    bun.get_price.return_value = 300
    return bun

@pytest.fixture
def mock_ing_1():
    ingredient = Mock()
    ingredient.get_name.return_value = "dinosaur"
    ingredient.get_price.return_value = 200
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    return ingredient

@pytest.fixture
def mock_ing_2():
    ingredient = Mock()
    ingredient.get_name.return_value = "chili sauce"
    ingredient.get_price.return_value = 300
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return ingredient