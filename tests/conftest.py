import pytest
from unittest.mock import MagicMock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.fixture
def mock_bun():
    # Создаю мок-объект булочки с тестовыми значениями имени и цены
    bun_mock = MagicMock(spec=Bun)
    bun_mock.get_name.return_value = "test bun"
    bun_mock.get_price.return_value = 100
    return bun_mock

@pytest.fixture
def mock_sauce():
    # Создаю мок-объект соуса с тестовыми значениями имени, цены и типа
    sauce_mock = MagicMock(spec=Ingredient)
    sauce_mock.get_name.return_value = "test sauce"
    sauce_mock.get_price.return_value = 50
    sauce_mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return sauce_mock

@pytest.fixture
def mock_filling():
    # Создаю мок-объект начинки с тестовыми значениями имени, цены и типа
    filling_mock = MagicMock(spec=Ingredient)
    filling_mock.get_name.return_value = "test filling"
    filling_mock.get_price.return_value = 150
    filling_mock.get_type.return_value = INGREDIENT_TYPE_FILLING
    return filling_mock
