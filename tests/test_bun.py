import pytest
from praktikum.bun import Bun


@pytest.mark.parametrize("name, price", [
    ("black bun", 100),
    ("white bun", 200),
    ("red bun", 300),
    ("special bun", 0),
    ("long name bun", 999.99)
])
def test_bun_get_name_and_price(name, price):
    """
    Проверяет корректность работы геттеров для различных значений
    """
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price