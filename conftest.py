import pytest
from unittest.mock import MagicMock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


@pytest.fixture
def mocked_database():
    mock_db = MagicMock()
    mock_db.available_buns.return_value = [Bun("mock bun", 100)]
    return mock_db

@pytest.fixture
def bun():
    return Bun("white bun", 150)

@pytest.fixture
def ingredients():
    return [
        Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 100),
        Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 300),
        Ingredient(INGREDIENT_TYPE_SAUCE, "ketchup", 50),
    ]
