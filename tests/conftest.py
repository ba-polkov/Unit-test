import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum import ingredient_types
from praktikum.database import Database


@pytest.fixture
#Создаем ингредиент
def ingredient():
    ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, 'Соус', 60)
    return ingredient

@pytest.fixture
#Создаем базу
def database():
    database = Database()
    return database
