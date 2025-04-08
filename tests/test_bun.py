import pytest
from ..bun import Bun

class TestBun():
    @pytest.mark.parametrize(
        "name, price, expected_name",
        [
            ("black bun", 100, "black bun"),
            ("white bun", 200, "white bun"),
            ("red bun", 300, "red bun"),
        ]
    )
    def test_get_name(self, name, price, expected_name):
        bun = Bun(name, price)

        assert bun.get_name() == expected_name

    @pytest.mark.parametrize(
        "name, price, expected_price",
        [
            ("black bun", 100, 100),
            ("white bun", 200, 200),
            ("red bun", 300, 300),
        ]
    )
    def test_get_price(self, name, price, expected_price):
        bun = Bun(name, price)

        assert bun.get_price() == expected_price

    def test_price_type(self):
        bun = Bun("black bun", 100.0)
        assert isinstance(bun.get_price(), float)


    def test_name_type(self):
        bun = Bun("black bun", 100)
        assert isinstance(bun.get_name(), str)
