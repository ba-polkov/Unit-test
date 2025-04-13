import pytest

import data
from praktikum.bun import Bun
from praktikum.burger import Burger

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def bun():
    return Bun(data.BUN_NAME_COSMOBUN, data.BUN_PRICE_COSMOBUN)