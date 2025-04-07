import pytest
from Diplom_1.praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
from Diplom_1.praktikum.ingredient import Ingredient
from Diplom_1.praktikum.database import Database
from Diplom_1.praktikum.bun import Bun
from Diplom_1.praktikum.burger import Burger


@pytest.fixture
def burgers():
    burgers = Burger()
    return burgers

def buns():
    bun = Bun()
    return bun

def database():
    database = Database()
    return database

def ingredient():
    ingredient = Ingredient()
    return ingredient

def ingredient_types_one():
    ingredient_types_one = INGREDIENT_TYPE_SAUCE()
    return ingredient_types_one

def ingredient_types_two():
    ingredient_types_two = INGREDIENT_TYPE_FILLING()
    return ingredient_types_two
