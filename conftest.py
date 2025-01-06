from unittest.mock import Mock

import pytest


@pytest.fixture()
def mock_bun():
    mock_bun = Mock()
    mock_bun.name = 'name'
    mock_bun.price = 1.1
    return mock_bun