import pytest
import random
from praktikum.bun import Bun
from unittest.mock import Mock
from praktikum import ingredient_types
from praktikum.ingredient import Ingredient


@pytest.fixture
def bun_object():
    bun_name = ['Гордость и предубеждение и зомби', 'Гарри Поттер и кубок огня', 'Ведьмак', 'Последнее желание',
                'Сталкер']
    bun_price = [0, 11, 100, 1000]
    bun = Bun(random.choice(bun_name), random.choice(bun_price))
    return bun


@pytest.fixture()
def ingredient_object():
    ingredient_type = [ingredient_types.INGREDIENT_TYPE_SAUCE, ingredient_types.INGREDIENT_TYPE_FILLING]
    ingredient = Ingredient(ingredient_type=random.choice(ingredient_type), name="горчица", price=15)
    return ingredient


@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.return_value.get_name = "Ржаная"
    mock_bun.return_value.get_price = 15
    return mock_bun


@pytest.fixture()
def mock_ingredient_1():
    mock_ingredient_1 = Mock()
    mock_ingredient_1.return_value.get_price = 15
    mock_ingredient_1.return_value.get_name = "майонез"
    mock_ingredient_1.return_value.get_type = "соус"
    return mock_ingredient_1


@pytest.fixture()
def mock_ingredient_2():
    mock_ingredient_2 = Mock()
    mock_ingredient_2.return_value.get_price = 15
    mock_ingredient_2.return_value.get_name = "горчица"
    mock_ingredient_2.return_value.get_type = "соус"
    return mock_ingredient_2



