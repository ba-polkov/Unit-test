import pytest
from unittest.mock import Mock
from data import *

@pytest.fixture
def mock_bun():
    mock_buns = Mock()
    mock_buns.get_name.return_value = Data.Bun_name
    mock_buns.get_price.return_value = Data.Bun_price
    return mock_buns

