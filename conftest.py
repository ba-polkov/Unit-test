import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.database import Database


# метод создает и возвращает новый экземпляр класса Burger
@pytest.fixture
def burger():
    return Burger()


# метод создает и возвращает новый экземпляр класса Bun
@pytest.fixture
def bun():
    return Bun("Булка смерти", 405)


# метод создает и возвращает новый экземпляр класса Ingredient - соус
@pytest.fixture
def ingredient_sauce():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "Соус звездной пыли", 150)


# метод создает и возвращает новый экземпляр класса Ingredient - начинка
@pytest.fixture
def ingredient_filling():
    return Ingredient(INGREDIENT_TYPE_FILLING, "Начинка - антиматерия", 560)


# метод создает и возвращает новый экземпляр класса Database
@pytest.fixture
def database():
    return Database()