import pytest
from praktikum.bun import Bun

bun_test_data = [
    ("blue bun", 100),
    ("purple bun", 200),
    ("black bun", 300)
]

@pytest.mark.parametrize("name, price", bun_test_data)
def test_bun_get_name(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name


@pytest.mark.parametrize("name, price", bun_test_data)
def test_bun_get_price(name, price):
    bun = Bun(name, price)
    assert bun.get_price() == price

