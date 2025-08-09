import pytest

from data import test_buns
from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize("name, price", test_buns)
    def test_initialization(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name and bun.price == price

    @pytest.mark.parametrize("name, price", test_buns)
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", test_buns)
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
