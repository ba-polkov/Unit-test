import pytest
from unittest.mock import Mock
from burger import Burger

@pytest.fixture
def database():
    db = Mock(spec=["save", "load", "connect", "close"])
    return db

@pytest.fixture
def make_burger(database):
    def _make(*args, **kwargs):
        try:
            return Burger(database, *args, **kwargs)
        except TypeError:
            return Burger(*args, **kwargs)
    return _make

@pytest.fixture
def bun():
    bun_mock = Mock()
    bun_mock.get_name.return_value = "Small Bun"
    bun_mock.get_price.return_value = 100.0
    return bun_mock

@pytest.fixture
def ingredient():
    ingredient_mock = Mock()
    ingredient_mock.get_name.return_value = "Cheese"
    ingredient_mock.get_type.return_value = "FILLING"
    ingredient_mock.get_price.return_value = 50.0
    return ingredient_mock
