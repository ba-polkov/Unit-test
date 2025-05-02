import pytest
from data import create_mock_ingredient
from Diplom_1.practicum.burger import Burger
from Diplom_1.practicum import Database


@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def mock_sauce():
    from data import SAUCE_NAME, SAUCE_PRICE
    return create_mock_ingredient(SAUCE_NAME, SAUCE_PRICE)

@pytest.fixture
def mock_filling():
    from data import FILLING_NAME, FILLING_PRICE
    return create_mock_ingredient(FILLING_NAME, FILLING_PRICE)

@pytest.fixture
def mock_bun():
    from unittest.mock import Mock
    from Diplom_1.practicum import Bun
    from data import BUN_NAME_1, BUN_PRICE

    mock = Mock(spec=Bun)
    mock.get_name.return_value = BUN_NAME_1
    mock.get_price.return_value = BUN_PRICE
    return mock

@pytest.fixture
def database():
    return Database()