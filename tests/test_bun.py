import pytest
from pages.bun import Bun


def test_bun_constructor_sets_name_and_price():
    name = "Test Bun"
    price = 99.9
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price


@pytest.mark.parametrize("name,price", [
    ("black bun", 100),
    ("white bun", 200),
    ("red bun", 300)
])
def test_database_buns_available(name, price):
    bun = Bun(name, price)
    assert bun.name == name
    assert bun.price == price