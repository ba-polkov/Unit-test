from unittest.mock import Mock

import pytest

from data import INGREDIENT_SAUCE_TOMATO, MOCK_BUN_PRICE, MOCK_INGREDIENT_FILLING_PRICE, MOCK_INGREDIENT_SAUCE_PRICE, \
    INGREDIENT_CHEESE, BUN_CIABATTA
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def mock_ingredient_sauce():
    ingredient = Mock()
    ingredient.type = INGREDIENT_TYPE_SAUCE
    ingredient.price = MOCK_INGREDIENT_SAUCE_PRICE
    ingredient.name = INGREDIENT_SAUCE_TOMATO
    ingredient.get_name.return_value = ingredient.name
    ingredient.get_price.return_value = ingredient.price
    ingredient.get_type.return_value = ingredient.type
    return ingredient


@pytest.fixture
def mock_ingredient_filling():
    ingredient = Mock()
    ingredient.type = INGREDIENT_TYPE_FILLING
    ingredient.price = MOCK_INGREDIENT_FILLING_PRICE
    ingredient.name = INGREDIENT_CHEESE
    ingredient.get_name.return_value = ingredient.name
    ingredient.get_price.return_value = ingredient.price
    ingredient.get_type.return_value = ingredient.type
    return ingredient


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.name = BUN_CIABATTA
    bun.price = MOCK_BUN_PRICE
    bun.get_price.return_value = bun.price
    bun.get_name.return_value = bun.name
    return bun


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def burger_with_ingredients(burger, mock_ingredient_sauce, mock_ingredient_filling):
    burger.add_ingredient(mock_ingredient_sauce)
    burger.add_ingredient(mock_ingredient_filling)
    return burger


@pytest.fixture
def burger_with_price(burger, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_sauce)
    burger.add_ingredient(mock_ingredient_filling)
    price = mock_bun.price * 2 + mock_ingredient_sauce.price + mock_ingredient_filling.price
    return burger, price


@pytest.fixture
def db():
    return Database()
