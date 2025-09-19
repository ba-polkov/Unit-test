import pytest
from burger import Burger
from unittest.mock import Mock
from database import Database

@pytest.fixture
def database():
    return Database()

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def bun():
    bun_mock = Mock()
    bun_mock.get_name.return_value = "Small Bun"
    bun_mock.get_price.return_value = 100.0
    return bun_mock

@pytest.fixture
def ingridient():
    ingridient_mock = Mock()
    ingridient_mock.get_name.return_value = "Cheese"
    ingridient_mock.get_type.return_value = "FILLING"
    ingridient_mock.get_price.return_value = 50.0
    return ingridient_mock