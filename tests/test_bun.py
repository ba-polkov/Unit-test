from data import DataForTests
from praktikum.bun import Bun
from conftest import bun
import pytest


class TestBun:

    @pytest.mark.parametrize('name, price', [(DataForTests.BLACK_BUN, DataForTests.PRICE_BLACK_BUN),
                                             (DataForTests.RED_BUN, DataForTests.PRICE_RED_BUN),
                                             (DataForTests.WHITE_BUN, DataForTests.PRICE_WHITE_BUN)
                                             ])
    def test_get_name_successfully(self, bun, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('name, price', [
        (DataForTests.BLACK_BUN, DataForTests.PRICE_BLACK_BUN),
        (DataForTests.RED_BUN, DataForTests.PRICE_RED_BUN),
        (DataForTests.WHITE_BUN, DataForTests.PRICE_WHITE_BUN)
    ])
    def test_get_price_successfully(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price

