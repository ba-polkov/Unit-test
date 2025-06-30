import pytest
from unittest.mock import Mock
from practicum.bun import Bun
from practicum.ingredient import Ingredient
from practicum.burger import Burger  
from practicum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.fixture
def mock_bun():
    bun = Mock(spec=Bun)
    bun.get_price.return_value = 100
    bun.get_name.return_value = "black bun"
    return bun

@pytest.fixture
def mock_ingredient_sauce():
    ingredient = Mock(spec=Ingredient)
    ingredient.get_price.return_value = 50
    ingredient.get_name.return_value = "hot sauce"
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return ingredient

@pytest.fixture
def mock_ingredient_filling():
    ingredient = Mock(spec=Ingredient)
    ingredient.get_price.return_value = 75
    ingredient.get_name.return_value = "cutlet"
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    return ingredient

@pytest.fixture
def mock_ingredients(mock_ingredient_sauce, mock_ingredient_filling):
    return [mock_ingredient_sauce, mock_ingredient_filling]

@pytest.fixture
def empty_burger():
    return Burger()  

@pytest.fixture
def prepared_burger(mock_bun, mock_ingredients):
    burger = Burger()  
    burger.set_buns(mock_bun)
    for ingredient in mock_ingredients:
        burger.add_ingredient(ingredient)
    return burger