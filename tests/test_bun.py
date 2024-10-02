import pytest
import data
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize("name, price", ((data.BUNS[0][0], data.BUNS[0][1]), (data.BUNS[1][0], data.BUNS[1][1])))
    def test_bun_get_name(self, name, price):
        bun = Bun(name, price)
        bun_name = bun.get_name()
        assert bun_name == name

    @pytest.mark.parametrize("name, price", ((data.BUNS[0][0], data.BUNS[0][1]), (data.BUNS[1][0], data.BUNS[1][1])))
    def test_bun_get_price(self, name, price):
        bun = Bun(name, price)
        actual_price = bun.get_price()
        assert actual_price == price
