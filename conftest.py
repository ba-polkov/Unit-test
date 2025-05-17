import pytest
from data import create_mock_ingredient
from practicum.burger import Burger
from practicum.database import Database
from data import SAUCE_NAME, SAUCE_PRICE
from data import FILLING_NAME, FILLING_PRICE
from unittest.mock import Mock
from practicum.bun import Bun
from data import BUN_NAME_1, BUN_PRICE


@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def mock_sauce():
    mock = create_mock_ingredient(SAUCE_NAME, SAUCE_PRICE)
    mock.get_type.return_value = "sauce"
    return mock


@pytest.fixture
def mock_filling():
    return create_mock_ingredient(FILLING_NAME, FILLING_PRICE)

@pytest.fixture
def mock_bun():
    mock = Mock(spec=Bun)
    mock.get_name.return_value = BUN_NAME_1
    mock.get_price.return_value = BUN_PRICE
    return mock

@pytest.fixture
def database():
    return Database()