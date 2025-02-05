
import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


@pytest.fixture()
def mock_bun():
    mock_bun = Bun("Булка", 3)
    return mock_bun

@pytest.fixture()
def mock_ingredients():
    mock_ingredients = Ingredient('Тип', 'Имя', 100)
    return mock_ingredients

