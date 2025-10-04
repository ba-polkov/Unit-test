import pytest
import random
import string
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def ingredient_instance():
    return generate_random_ingredient()

@pytest.fixture
def bun_mock() -> Mock:
    """Мок булочки с рандомными данными"""
    name = ''.join(random.choices(string.ascii_letters, k=6))
    price = round(random.uniform(50, 300), 2)

    mock = Mock(Bun)
    mock.get_name.return_value = name
    mock.get_price.return_value = price
    mock._expected_name = name
    mock._expected_price = price
    return mock

@pytest.fixture
def db():
    """Фикстура для Database"""
    return Database()

def generate_random_ingredient():
    """Генерация случайного ингредиента"""
    ingredient_type = random.choice([INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    name = ''.join(random.choices(string.ascii_letters, k=8))
    price = round(random.uniform(10, 500), 2)
    ingredient = Ingredient(ingredient_type, name, price)
    return ingredient, {"type": ingredient_type, "name": name, "price": price}