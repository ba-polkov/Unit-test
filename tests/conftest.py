import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from bun import Bun
from ingredient import Ingredient
from database import Database
from burger import Burger
from unittest.mock import Mock


@pytest.fixture
def bun(name, price):
    bun = Bun(name, price)
    return bun

@pytest.fixture
def ingredient(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    return ingredient

@pytest.fixture
def db():
    db = Database()
    return db

@pytest.fixture
def burger():
    burger = Burger()
    return burger

@pytest.fixture
def mock_bun():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "fluorescent bun"
    bun.get_price.return_value = 988
    return bun

@pytest.fixture
def mock_ingredient1():
    ingredient1 = Mock(spec=Ingredient)
    ingredient1.get_name.return_value = "Traditional Galactic Sauce"
    ingredient1.get_price.return_value = 15
    ingredient1.get_type.return_value = "SAUCE"
    return ingredient1

@pytest.fixture
def mock_ingredient2():
    ingredient2 = Mock(spec=Ingredient)
    ingredient2.get_name.return_value = "Cheese with asteroid mold"
    ingredient2.get_price.return_value = 4142
    ingredient2.get_type.return_value = "FILLING"
    return ingredient2
