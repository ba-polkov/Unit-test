import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def default_bun():
    return Bun("Стандартная булочка", 1.0)


@pytest.fixture
def ingredient_sauce():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "Соус фирменный", 0.5)


@pytest.fixture
def ingredient_filling():
    return Ingredient(INGREDIENT_TYPE_FILLING, "Котлета говяжья", 2.0)


@pytest.fixture
def empty_burger():
    return Burger()


@pytest.fixture
def prepared_burger(default_bun, ingredient_sauce, ingredient_filling):
    burger = Burger()
    burger.set_buns(default_bun)
    burger.add_ingredient(ingredient_sauce)
    burger.add_ingredient(ingredient_filling)
    return burger


@pytest.fixture
def database():
    return Database()
