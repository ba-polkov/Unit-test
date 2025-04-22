import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from praktikum.database import Database


@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def bun():
    return Bun(name="Булочка", price=100)

@pytest.fixture
def ingredient_sauce():
    return Ingredient('SAUCE', 'Соус', 50)

@pytest.fixture
def ingredient_filling():
    return Ingredient('FILLING', 'Начинка', 75)

@pytest.fixture
def db():
    return Database()

