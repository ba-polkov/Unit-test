import pytest
from data import BurgerData
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from unittest.mock import Mock


@pytest.fixture()
def bun():
    bun = Bun(name=BurgerData.BUNS_NAME, price=BurgerData.BUNS_PRICE)
    return bun


@pytest.fixture()
def burger():
    burger = Burger()
    return burger


@pytest.fixture()
def ingredient():
    ingredient = Ingredient(ingredient_type=BurgerData.SAUCES_TYPE, name=BurgerData.SAUCES_NAME,
                            price=BurgerData.SAUCES_PRICE)
    return ingredient


@pytest.fixture()
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = BurgerData.BUNS_NAME
    mock_bun.get_price.return_value = BurgerData.BUNS_PRICE
    return mock_bun


@pytest.fixture()
def mock_ingredient_1():
    mock_ingredient_1 = Mock()
    mock_ingredient_1.get_type.return_value = BurgerData.FILLINGS_TYPE
    mock_ingredient_1.get_name.return_value = BurgerData.FILLINGS_NAME
    mock_ingredient_1.get_price.return_value = BurgerData.FILLINGS_PRICE
    return mock_ingredient_1

@pytest.fixture()
def mock_ingredient_2():
    mock_ingredient_2 = Mock()
    mock_ingredient_2.get_type.return_value = BurgerData.SAUCES_TYPE
    mock_ingredient_2.get_name.return_value = BurgerData.SAUCES_NAME
    mock_ingredient_2.get_price.return_value = BurgerData.SAUCES_PRICE
    return mock_ingredient_2