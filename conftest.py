import pytest
from unittest.mock import Mock

from bun import Bun
from ingredient import Ingredient


@pytest.fixture()
def mock_bun():
    mock = Mock(spec=Bun)
    mock.get_name.return_value = "black bun"
    mock.get_price.return_value = 100
    return mock

@pytest.fixture()
def mock_ingredient():
    mock = Mock(spec=Ingredient)
    mock.get_name.return_value = 'hot sauce'
    mock.get_type.return_value = 'sauce'
    mock.get_price.return_value = 200
    return mock