import pytest
from unittest.mock import Mock

from praktikum.bun import Bun
from praktikum.burger import Burger
from ingredient_types import *


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def bun_mock():
    mock = Mock()
    mock.get_price.return_value = 100
    mock.get_name.return_value = "black bun"
    return mock


@pytest.fixture
def ingredient_mock():
    mock = Mock()
    mock.get_name.return_value = "sour cream"
    mock.get_price.return_value = 100
    mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock
