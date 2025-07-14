import pytest
from unittest.mock import MagicMock
from praktikum.burger import Burger
from praktikum.database import *

@pytest.fixture
def database():
    return Database()

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def bun(database):
    bun = database.available_buns()[1]
    return bun

@pytest.fixture
def ingredient_from_db(database):
    ingredient_from_db = database.available_ingredients()[1]
    return ingredient_from_db

@pytest.fixture
def ingredient_from_class():
    ingradient_from_class = Ingredient(INGREDIENT_TYPE_SAUCE, "Горчичный", 500)
    return ingradient_from_class

@pytest.fixture
def ingredient_mock():
    ingredient_mock = MagicMock()
    ingredient_mock.get_type.return_value = "Наполнитель"
    ingredient_mock.get_name.return_value = "Сосика"
    ingredient_mock.get_price.return_value = 300
    return ingredient_mock


