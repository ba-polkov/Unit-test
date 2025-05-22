import pytest
from praktikum.bun import Bun

@pytest.fixture
def bun_factory():
    def _create_bun(name="default bun", price=100):
        return Bun(name, price)
    return _create_bun

import pytest
from unittest.mock import MagicMock


@pytest.fixture
def mock_bun():
    bun = MagicMock()
    bun.get_price.return_value = 100
    bun.get_name.return_value = "test bun"
    return bun


@pytest.fixture
def mock_ingredient():
    ingredient = MagicMock()
    ingredient.get_price.return_value = 50
    ingredient.get_name.return_value = "test sauce"
    ingredient.get_type.return_value = "SAUCE"
    return ingredient


@pytest.fixture
def db():
    from praktikum.database import Database
    return Database()
