import pytest
from unittest.mock import Mock

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from praktikum.database import Database

from data.burger_data import BunsData as buns
from data.burger_data import IngredientsData as ingredients


@pytest.fixture
def burger():
    burger = Burger()
    return burger


@pytest.fixture
def bun(name=buns.BUN_1[0], price=buns.BUN_1[1]):
    bun = Bun(name, price)
    return bun


@pytest.fixture()
def ingredient(ing_type=ingredients.SAUCE_1[0], name=ingredients.SAUCE_1[1], price=ingredients.SAUCE_1[2]):
    ingredient = Ingredient(ing_type, name, price)
    return ingredient

@pytest.fixture()
def db():
    db = Database()
    return db


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = 'Mock Bun'
    bun.get_price.return_value = 2.5
    return bun


@pytest.fixture()
def mock_ingredient_sauce():
    ingredient = Mock()
    ingredient.get_type.return_value = ingredients.SAUCE_1[0]
    ingredient.get_name.return_value = ingredients.SAUCE_1[1]
    ingredient.get_price.return_value = ingredients.SAUCE_1[2]
    return ingredient


@pytest.fixture()
def mock_ingredient_filling():
    ingredient = Mock()
    ingredient.get_type.return_value = ingredients.FILLING_1[0]
    ingredient.get_name.return_value = ingredients.FILLING_1[1]
    ingredient.get_price.return_value = ingredients.FILLING_1[2]
    return ingredient







@pytest.fixture
def burger_with_mock_ingredients(mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
    my_burger = Burger()
    my_burger.set_buns(mock_bun)
    my_burger.add_ingredient(mock_ingredient_sauce)
    my_burger.add_ingredient(mock_ingredient_sauce)
    my_burger.add_ingredient(mock_ingredient_filling)
    return my_burger
