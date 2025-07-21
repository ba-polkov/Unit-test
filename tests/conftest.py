import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def mock_bun():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100
    return bun

@pytest.fixture
def mock_ingredients():
    ingredient1 = Mock(spec=Ingredient)
    ingredient1.get_type.return_value = "SAUCE"
    ingredient1.get_name.return_value = "hot sauce"
    ingredient1.get_price.return_value = 50

    ingredient2 = Mock(spec=Ingredient)
    ingredient2.get_type.return_value = "VEGGIE"
    ingredient2.get_name.return_value = "lettuce"
    ingredient2.get_price.return_value = 30

    ingredient3 = Mock(spec=Ingredient)
    ingredient3.get_type.return_value = "MEAT"
    ingredient3.get_name.return_value = "beef"
    ingredient3.get_price.return_value = 100

    return {
        'sauce': ingredient1,
        'veggie': ingredient2,
        'meat': ingredient3,
        'all': [ingredient1, ingredient2, ingredient3]
    }