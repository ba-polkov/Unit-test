import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum import ingredient_types
from praktikum.database import Database


@pytest.fixture
#Булочке даем название и назначаем цену.
def bun():
    bun = Bun('Mike', 500)
    return bun

@pytest.fixture
#Создаем бургер, он состоит из булочки и ингредиента(соус).
#Создаем ингредиент.
#Добавляем ингредиент к бургеру.
def burger(bun):
    burger = Burger()
    burger.set_buns(bun)
    ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, 'Соус', 60)
    burger.add_ingredient(ingredient)
    return burger

@pytest.fixture
#Создаем ингридиент
def ingredient():
    ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, 'Соус', 60)
    return ingredient

@pytest.fixture
#Создаем базу
def database():
    database = Database()
    return database