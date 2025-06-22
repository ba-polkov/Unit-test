import pytest
from praktikum.bun import Bun

def test_bun_init():
    bun = Bun("Test Bun", 1.99)
    assert bun.name == "Test Bun"

def test_bun_price():
    bun = Bun("Test Bun", 1.99)
    assert bun.price == 1.99

@pytest.mark.parametrize("name, price", [("Black Bun", 100), ("White Bun", 200)])
def test_bun_get_name_returns_correct(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name

@pytest.mark.parametrize("name, price", [("Black Bun", 100), ("White Bun", 200)])
def test_bun_get_price_returns_correct(name, price):
    bun = Bun(name, price)
    assert bun.get_price() == price