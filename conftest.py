import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


@pytest.fixture
def burger():
    '''Пустой бургер'''
    return Burger()

@pytest.fixture
def burger_ready():
    '''Готовый бургер'''
    burger = Burger()
    burger.set_buns(Bun('Корж ржаной', 1.50))
    burger.add_ingredient(Ingredient(INGREDIENT_TYPE_SAUCE, 'Кетчуп Джой', 1.00))
    burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING, 'Лук Порей', 0.25))
    burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING, 'Рыба Лупо', 9.00))
    burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING, 'Томат Ост', 1.75))
    burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING, 'Салат Айс', 0.99))
    return burger
