import pytest
from unittest.mock import MagicMock
from praktikum.burger import Burger
from praktikum.bun import Bun
from data import Data


@pytest.fixture
def burger():
    burger = Burger()
    bun = MagicMock(spec=Bun)
    bun.get_name.return_value = Data.BUNS[0][0]
    bun.get_price.return_value = Data.BUNS[0][1]
    burger.set_buns(bun)
    return burger