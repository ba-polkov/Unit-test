import pytest
from unittest.mock import Mock
from data import *

@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = Data.Bun_name
    mock_bun.get_price.return_value = Data.Bun_price
    return mock_bun

