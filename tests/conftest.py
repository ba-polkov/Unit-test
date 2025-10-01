import pytest
from unittest.mock import Mock

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from burger import Burger


@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def bun():
    bun_mock = Mock()
    bun_mock.get_name.return_value = "white bun"
    bun_mock.get_price.return_value = 10.0
    return bun_mock

@pytest.fixture
def ingredient():
    ingredient_mock = Mock()
    ingredient_mock.get_name.return_value = "fish"
    ingredient_mock.get_type.return_value = "FILLING"
    ingredient_mock.get_price.return_value = 20.0
    return ingredient_mock