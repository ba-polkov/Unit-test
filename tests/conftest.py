import pytest
from unittest.mock import Mock
from burger import Burger
from data import BurgerElements as BE



# Создаем объект класса Burger
@pytest.fixture
def burger():
    burger = Burger()
    return burger

# Cоздаем мок красной булочки
@pytest.fixture()
def mock_red_bun():
    mock_red_bun = Mock()
    mock_red_bun.name = BE.BUN_NAME_3
    mock_red_bun.price = BE.BUN_PRICE_3
    mock_red_bun.get_name.return_value = BE.BUN_NAME_3
    mock_red_bun.get_price.return_value = BE.BUN_PRICE_3
    return mock_red_bun

# Создаем мок соуса 1 (острый соус)
@pytest.fixture
def mock_sauce_1():
    mock_sauce = Mock()
    mock_sauce.type = BE.INGREDIENT_TYPE_1
    mock_sauce.name = BE.SAUCE_NAME_1
    mock_sauce.price = BE.SAUCE_PRICE_1
    mock_sauce.get_price.return_value = BE.SAUCE_PRICE_1
    mock_sauce.get_name.return_value = BE.SAUCE_NAME_1
    mock_sauce.get_type.return_value = BE.INGREDIENT_TYPE_1
    return mock_sauce

# Создаем мок соуса 2 (сметана)
@pytest.fixture
def mock_sauce_2():
    mock_sauce = Mock()
    mock_sauce.type = BE.INGREDIENT_TYPE_1
    mock_sauce.name = BE.SAUCE_NAME_2
    mock_sauce.price = BE.SAUCE_PRICE_2
    mock_sauce.get_price.return_value = BE.SAUCE_PRICE_2
    mock_sauce.get_name.return_value = BE.SAUCE_NAME_2
    mock_sauce.get_type.return_value = BE.INGREDIENT_TYPE_1
    return mock_sauce

# Создаем мок соуса 3 (чили-соус)
@pytest.fixture
def mock_sauce_3():
    mock_sauce = Mock()
    mock_sauce.type = BE.INGREDIENT_TYPE_1
    mock_sauce.name = BE.SAUCE_NAME_3
    mock_sauce.price = BE.SAUCE_PRICE_3
    mock_sauce.get_price.return_value = BE.SAUCE_PRICE_3
    mock_sauce.get_name.return_value = BE.SAUCE_NAME_3
    mock_sauce.get_type.return_value = BE.INGREDIENT_TYPE_1
    return mock_sauce

# Создаем мок начинки 1 (котлета)
@pytest.fixture
def mock_filling_1():
    mock_filling = Mock()
    mock_filling.type = BE.INGREDIENT_TYPE_2
    mock_filling.name = BE.FILLING_NAME_1
    mock_filling.price = BE.FILLING_PRICE_1
    mock_filling.get_price.return_value = BE.FILLING_PRICE_1
    mock_filling.get_name.return_value = BE.FILLING_NAME_1
    mock_filling.get_type.return_value = BE.INGREDIENT_TYPE_2
    return mock_filling

# Создаем мок начинки 2 (динозавр)
@pytest.fixture
def mock_filling_2():
    mock_filling = Mock()
    mock_filling.type = BE.INGREDIENT_TYPE_2
    mock_filling.name = BE.FILLING_NAME_2
    mock_filling.price = BE.FILLING_PRICE_2
    mock_filling.get_price.return_value = BE.FILLING_PRICE_2
    mock_filling.get_name.return_value = BE.FILLING_NAME_2
    mock_filling.get_type.return_value = BE.INGREDIENT_TYPE_2
    return mock_filling

# Создаем мок начинки 3 (сосиска)
@pytest.fixture
def mock_filling_3():
    mock_filling = Mock()
    mock_filling.type = BE.INGREDIENT_TYPE_2
    mock_filling.name = BE.FILLING_NAME_3
    mock_filling.price = BE.FILLING_PRICE_3
    mock_filling.get_price.return_value = BE.FILLING_PRICE_3
    mock_filling.get_name.return_value = BE.FILLING_NAME_3
    mock_filling.get_type.return_value = BE.INGREDIENT_TYPE_2
    return mock_filling
