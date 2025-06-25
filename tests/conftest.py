import pytest
from unittest.mock import Mock

@pytest.fixture
def bun_mock():
    mock = Mock()
    mock.get_name.return_value = "Test Bun"
    mock.get_price.return_value = 2.5
    return mock


@pytest.fixture
def ingredient_mock():
    def _create(type_, name, price):
        mock = Mock()
        mock.get_type.return_value = type_
        mock.get_name.return_value = name
        mock.get_price.return_value = price
        return mock
    return _create