from unittest.mock import Mock

import pytest

from praktikum.burger import Burger
from praktikum.database import Database


@pytest.fixture()
def burger():
    return Burger()

@pytest.fixture()
def bun_mock():
    bun_mock = Mock()
    bun_mock.get_name.return_value ='hot bun'
    bun_mock.get_price.return_value = 55.0
    return bun_mock

@pytest.fixture()
def ingredient_mock():
    ingredient_mock = Mock()
    ingredient_mock.get_type.return_value = 'SAUCE'
    ingredient_mock.get_name.return_value = 'test sause'
    ingredient_mock.get_price.return_value = 22.0
    return ingredient_mock
@pytest.fixture()
def other_ingredient_mock():
    other_ingredient_mock = Mock()
    other_ingredient_mock.get_type.return_value = 'FILLING'
    other_ingredient_mock.get_name.return_value = 'test filling'
    other_ingredient_mock.get_price.return_value = 42.0
    return other_ingredient_mock

@pytest.fixture()
def database():
    return Database()