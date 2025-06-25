import pytest
from praktikum.bun import Bun
from data import DataBun


class TestBun:

    @pytest.mark.parametrize("name, price", DataBun.BUN_CREATION_TEST_DATA)
    def test_bun_attributes(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name
        assert bun.price == price

    @pytest.mark.parametrize("name, price", DataBun.BUN_CREATION_TEST_DATA)
    def test_bun_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", DataBun.BUN_CREATION_TEST_DATA)
    def test_bun_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price

    @pytest.mark.parametrize("name, price", DataBun.BUN_CREATION_TEST_DATA)
    def test_bun_types(self, name, price):
        bun = Bun(name, price)
        assert isinstance(bun.name, str)
        assert isinstance(bun.price, float)
        assert isinstance(bun.get_name(), str)
        assert isinstance(bun.get_price(), float)

