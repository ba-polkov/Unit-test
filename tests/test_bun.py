import pytest

from praktikum.bun import Bun
from tests.data import BUN_NAME1, BUN_NAME2, PRICE1, PRICE2


class TestBun:

    @pytest.mark.parametrize('bun', [BUN_NAME1, BUN_NAME2])
    def test_get_name(self, bun):
        my_bun = Bun(bun, PRICE1)
        assert my_bun.get_name() == bun

    @pytest.mark.parametrize('price', [PRICE1, PRICE2])
    def test_get_price(self, price):
        my_bun = Bun(BUN_NAME1, price)
        assert my_bun.get_price() == price