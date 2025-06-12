import pytest
from praktikum.bun import Bun
from data import BUN_TEST_CASES

@pytest.mark.parametrize("name, price", BUN_TEST_CASES)
def test_bun_creation(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price


def test_bun_with_zero_price():
    bun = Bun("ZeroPrice", 0)
    assert bun.get_name() == "ZeroPrice"
    assert bun.get_price() == 0


def test_bun_with_empty_name():
    bun = Bun("", 10)
    assert bun.get_name() == ""
    assert bun.get_price() == 10