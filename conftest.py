import pytest
from unittest.mock import MagicMock
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.fixture
def mock_bun():
    bun = MagicMock()
    bun.get_name.return_value = "mocked bun"
    bun.get_price.return_value = 123
    return bun

@pytest.fixture
def mock_ingredient():
    def _create(name, type, price):
        ingredient = MagicMock()
        ingredient.get_name.return_value = name
        ingredient.get_price.return_value = price
        ingredient.get_type.return_value = type
        return ingredient
    return _create

@pytest.fixture
def sample_bun():
    from praktikum.bun import Bun
    return Bun("sample bun", 150)

@pytest.fixture
def sample_ingredients():
    from praktikum.ingredient import Ingredient
    return [
        Ingredient(INGREDIENT_TYPE_SAUCE, "sauce1", 50),
        Ingredient(INGREDIENT_TYPE_FILLING, "filling1", 100),
    ]
