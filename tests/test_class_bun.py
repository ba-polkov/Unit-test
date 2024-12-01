import pytest
from bun import Bun

class TestBun:
    def test_bun_init(self):
        bun = Bun("test bun", 100)
        assert bun.name == "test bun"
        assert bun.price == 100

    @pytest.mark.parametrize("name, price, expected_name", [
        ("white bun", 200, "white bun"),
        ("black bun", 150, "black bun")
    ])
    def test_get_name(self, name, price, expected_name):
        bun = Bun(name, price)
        assert bun.get_name() == expected_name

    @pytest.mark.parametrize("name, price, expected_price", [
        ("white bun", 200, 200),
        ("black bun", 150, 150)
    ])
    def test_get_price(self, name, price, expected_price):
        bun = Bun(name, price)
        assert bun.get_price() == expected_price