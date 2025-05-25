import pytest

from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.database import Database
from data_for_test import TestBunsData as TBD, TestIngredientsData as TID

# Фикстура создания объекта Мок
@pytest.fixture(scope='function')
def mock():
    return Mock()

# Фикстура создания мока bun
@pytest.fixture(scope='function')
def mock_test_bun(mock):
    mock.configure_mock(**TBD.BUN)
    mock.get_name.return_value = mock.name
    mock.get_price.return_value = mock.price
    return mock

# Фикстура создания мока ingredient
@pytest.fixture(scope='function')
def mock_test_ingredient(mock):
    mock.configure_mock(**TID.INGREDIENT)
    mock.get_type.return_value = mock.type
    mock.get_name.return_value = mock.name
    mock.get_price.return_value = mock.price
    return mock

# Фикстура создания бургрера
@pytest.fixture(scope='function')
def create_test_burger():
    return Burger()

@pytest.fixture(scope='function')
def create_test_database():
    return Database()