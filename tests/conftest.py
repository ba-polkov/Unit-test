import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def bun_mock():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "Белая булочка"
    bun.get_price.return_value = 100
    return bun


@pytest.fixture
def ingredient_mock():
    ingredient = Mock(spec=Ingredient)
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    ingredient.get_name.return_value = "Соус острый"
    ingredient.get_price.return_value = 50
    return ingredient


@pytest.fixture
def filling_mock():
    filling = Mock(spec=Ingredient)
    filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    filling.get_name.return_value = "Котлета"
    filling.get_price.return_value = 200
    return filling


@pytest.fixture
def sample_bun():
    return Bun("Классическая булочка", 150)


@pytest.fixture
def sample_sauce():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "Кетчуп", 75)


@pytest.fixture
def sample_filling():
    return Ingredient(INGREDIENT_TYPE_FILLING, "Сыр", 120)