import sys
import os

# Добавляем корневую директорию проекта в Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


#Фикстура создает Бургер
@pytest.fixture
def burger():
    return Burger()

#Фикстура создает булочку для тестирования методов работы с бургером
@pytest.fixture
def bun():
    return Bun("black bun", 100)

#Фикстура создает соус для тестирования добавления ингредиентов
@pytest.fixture
def ingredient_sauce():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)

#Фикстура создает начинку для тестирования добавления ингредиентов
@pytest.fixture
def ingredient_filling():
    return Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200)