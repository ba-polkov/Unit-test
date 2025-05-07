import pytest

from bun import Bun
from data.test_data import BUN_PRICE, BUN_NAME

@pytest.fixture
def bun():
    return Bun(BUN_NAME, BUN_PRICE)
