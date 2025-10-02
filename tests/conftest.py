import pytest
from burger import Burger
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


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