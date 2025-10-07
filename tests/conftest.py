import sys
import os
import pytest
from unittest.mock import Mock
# Добавляем корень проекта в путь Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data import BunData, IngredientData
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


# Фикстура создает мок-булочку для тестирования методов работы с бургером
@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = BunData.BLACK_BUN[0]
    bun.get_price.return_value = BunData.BLACK_BUN[1]
    return bun


# Фикстура создает мок-начинку для тестирования добавления ингредиентов
@pytest.fixture
def mock_ingredient_filling():
    ingredient = Mock()
    ingredient.get_name.return_value = IngredientData.CUTLET[1]
    ingredient.get_price.return_value = IngredientData.CUTLET[2]
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    return ingredient


# Фикстура создает мок-соус для тестирования добавления ингредиентов
@pytest.fixture
def mock_ingredient_sauce():
    ingredient = Mock()
    ingredient.get_name.return_value = IngredientData.HOT_SAUCE[1]
    ingredient.get_price.return_value = IngredientData.HOT_SAUCE[2]
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return ingredient


# Фикстура создает готовый бургер с булочкой и ингредиентами для комплексного тестирования
@pytest.fixture
def burger_with_mocks(mock_bun, mock_ingredient_filling, mock_ingredient_sauce):
    from praktikum.burger import Burger
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_filling)
    burger.add_ingredient(mock_ingredient_sauce)
    return burger