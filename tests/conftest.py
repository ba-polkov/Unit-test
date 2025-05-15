from copy import deepcopy
from unittest.mock import Mock

import pytest

from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


@pytest.fixture
def bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = 'Quantum Bread'
    mock_bun.get_price.return_value = 100
    return mock_bun

@pytest.fixture
def ingredients():
    ingredient_mock1 = Mock()
    ingredient_mock1.type = INGREDIENT_TYPE_FILLING
    ingredient_mock1.name = "Космогриб"
    ingredient_mock1.price = 50

    ingredient_mock2 = Mock()
    ingredient_mock2.type = INGREDIENT_TYPE_FILLING
    ingredient_mock2.name = "Криодраконья котлета"
    ingredient_mock2.price = 200

    ingredient_mock3 = Mock()
    ingredient_mock3.type = INGREDIENT_TYPE_SAUCE
    ingredient_mock3.name = "Биолюминесцентный соус"
    ingredient_mock3.price = 10.5

    return [ingredient_mock1, ingredient_mock2, ingredient_mock3]

@pytest.fixture
def burger(ingredients, bun):

    burger = Burger()

    burger.ingredients = deepcopy(ingredients)
    burger.bun = bun

    return burger
