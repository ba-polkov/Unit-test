import pytest
from praktikum.bun import Bun

#тест  гетеров
def test_bun_getters_return_values():
    bun = Bun("red bun", 450)
    assert bun.get_name() == "red bun"
    assert bun.get_price() == 450

@pytest.mark.parametrize(
    "name, price",
    [
        ("white bun", 0),
        ("red bun", 300),
        ("yellow bun", 10.99)
    ]
)

#разные булки и цены
def test_bun_parametrized(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price





