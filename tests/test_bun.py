import pytest
from praktikum.bun import Bun


@pytest.mark.parametrize("name,price", [
    ("Бородинская булка", 21),
    ("Булка с розмарином", 10000),
    ("", 50),
    ("Булка с кунжутом", None),
    ("Булка бесплатная", 0),
    ("Булка зарплатная", -20)
])
def test_bun_creation(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price

