import pytest
from unittest.mock import Mock

from data import DataOne, DataTwo


@pytest.fixture()
def mock_bun_one():
    mock_bun = Mock()
    mock_bun.get_name.return_value = DataOne.BUN_NAME
    mock_bun.get_price.return_value = DataOne.BUN_PRICE
    return mock_bun

@pytest.fixture()
def mock_bun_two():
    mock_bun_2 = Mock()
    mock_bun_2.get_name.return_value = DataTwo.BUN_NAME
    mock_bun_2.get_price.return_value = DataTwo.BUN_PRICE
    return mock_bun_2

@pytest.fixture()
def mock_sauce_one():
    mock_sauce = Mock()
    mock_sauce.get_name.return_value = DataOne.SAUCE_NAME
    mock_sauce.get_price.return_value = DataOne.SAUCE_PRICE
    mock_sauce.get_type.return_value = DataOne.SAUCE_TYPE
    return mock_sauce

@pytest.fixture()
def mock_sauce_two():
    mock_sauce_2 = Mock()
    mock_sauce_2.get_name.return_value = DataTwo.SAUCE_NAME
    mock_sauce_2.get_price.return_value = DataTwo.SAUCE_PRICE
    mock_sauce_2.get_type.return_value = DataTwo.SAUCE_TYPE
    return mock_sauce_2














