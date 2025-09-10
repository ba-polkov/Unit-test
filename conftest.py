import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING


@pytest.fixture
def bun() -> Bun:
    """Фиксатура для создания булочки."""
    return Bun('Космобулочка', 45.78)


@pytest.fixture
def burger() -> Burger:
    """Фиксатура для создания пустого бургера."""
    return Burger()


@pytest.fixture
def ingredient() -> Ingredient:
    """Фиксатура для создания ингредиента."""
    return Ingredient(
        INGREDIENT_TYPE_FILLING,
        'халапеньо',
        22.33
    )
