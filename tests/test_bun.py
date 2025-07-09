import pytest

from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize("name, price", [
        ("Белая булка", 123.03),
        ("Бородинский хлеб", 789.25),
        ("Чиабата", 250.00),
        ("Блины", 125.25)
    ])
    def test_bun_get_name(self, name, price):
        bun = Bun(name,price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", [
        ("Белая булка", 123.03),
        ("Бородинский хлеб", 789.25),
        ("Чиабата", 250.00),
        ("Блины", 125.25)
    ])
    def test_bun_get_price(self, name, price):
        bun = Bun(name,price)
        assert bun.get_price() == price