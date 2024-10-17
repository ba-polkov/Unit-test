import pytest


from data import DataTests
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize('name, price', [(DataTests.BLACK_BUN, DataTests.PRICE_BLACK_BUN),
                                             (DataTests.RED_BUN, DataTests.PRICE_RED_BUN),
                                             (DataTests.WHITE_BUN, DataTests.PRICE_WHITE_BUN)
                                             ])
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    def test_get_price(self):
        bun = Bun(DataTests.BLACK_BUN, DataTests.PRICE_BLACK_BUN)
        assert bun.get_price() == DataTests.PRICE_BLACK_BUN

    def test_price_type(self):
        bun = Bun(DataTests.BLACK_BUN, 10.0)
        assert type(bun.get_price()) == float
