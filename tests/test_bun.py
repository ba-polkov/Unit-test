import pytest
from praktikum.bun import Bun

class TestBun:
    @pytest.mark.parametrize("name, price", [
        ("Краторная булка", 100),
        ("Сахарная булка", 200),
        ("", 0),
        (None, 10.5),
    ])
    def test_bun_initialization(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price