import pytest
from bun import Bun


@pytest.fixture
def bun():
    bun = Bun('Mike', 500)
    return bun

