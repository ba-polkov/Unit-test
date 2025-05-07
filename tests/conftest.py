import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.database import Database


@pytest.fixture
def database():
    """Создаем экземпляр базы данных для тестов."""
    return Database()


@pytest.fixture
def burger():
    """Фикстура для создания пустого бургера."""
    return Burger()


@pytest.fixture
def bun():
    """Фикстура для создания булочки."""
    return Bun("black bun", 100)


@pytest.fixture
def ingredient_sauce():
    """Фикстура для создания соуса."""
    return Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50)


@pytest.fixture
def ingredient_filling():
    """Фикстура для создания начинки."""
    return Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150)