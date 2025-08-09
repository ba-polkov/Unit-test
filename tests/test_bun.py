import pytest
from praktikum.bun import Bun

class TestBun:

    @pytest.mark.parametrize("name", [
    "black bun",
    "white bun",
    "red bun",
    "special bun",
    "long name bun",
    ""
    ])
    def test_bun_get_name(self, name):
        """
        Проверяет корректность работы метода get_name()
        """
        bun = Bun(name, 100)
        assert bun.get_name() == name


    @pytest.mark.parametrize("price", [
        0,
        100,
        200,
        999.99,
        -50
    ])
    def test_bun_get_price(self, price):
        """
        Проверяет корректность работы метода get_price()
        """
        bun = Bun("test bun", price)
        assert bun.get_price() == pytest.approx(price, 0.01)