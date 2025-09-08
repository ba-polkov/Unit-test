import pytest
from praktikum.bun import Bun

@pytest.mark.parametrize(
    "name, price",
    [
        ("black bun", 100),
        ("white bun", 200.5),
    ],
)
def test_bun_init_and_getters(name, price):
    bun = Bun(name, price)
    assert bun.name == name
    assert bun.price == price

    assert bun.get_name() == name
    assert bun.get_price() == price


def test_bun_multiple_instances_independent():
    a = Bun("a", 10)
    b = Bun("b", 20)
    assert a.get_name() == "a" and a.get_price() == 10
    assert b.get_name() == "b" and b.get_price() == 20
