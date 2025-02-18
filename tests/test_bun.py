import pytest

from praktikum.bun import Bun

from data.burger_data import BunsData as buns


class TestBun:

    @pytest.mark.parametrize(("name", "price"), [buns.BUN_1, buns.BUN_2, buns.BUN_3])
    def test_bun_attribute_name(self, name, price):
        bun = Bun(name, price)
        expected_name = name
        actual_name = bun.name
        assert actual_name == expected_name

    @pytest.mark.parametrize(("name", "price"), [buns.BUN_1, buns.BUN_2, buns.BUN_3])
    def test_bun_attribute_price(self, name, price):
        bun = Bun(name, price)
        expected_price = price
        actual_price = bun.price
        assert actual_price == expected_price

    @pytest.mark.parametrize(("name", "price"), [buns.BUN_1, buns.BUN_2, buns.BUN_3])
    def test_get_bun_name(self, name, price):
        bun = Bun(name, price)
        expected_name = name
        actual_name = bun.get_name()
        assert actual_name == expected_name

    @pytest.mark.parametrize(("name", "price"), [buns.BUN_1, buns.BUN_2, buns.BUN_3])
    def test_get_bun_price(self, name, price):
        bun = Bun(name, price)
        expected_price = price
        actual_price = bun.get_price()
        assert actual_price == expected_price
