import pytest
from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize("name", ["Флюоресцентная булка R2-D3", "Краторная булка N-200i"])
    def test_get_name(self, name):
        bun = Bun(name, 988)
        assert bun.get_name() == name

    @pytest.mark.parametrize("price", ["988", "1255"])
    def test_get_price(self, price):
        bun = Bun("Флюоресцентная булка R2-D3", price)
        assert bun.get_price() == price

    @pytest.mark.parametrize("price", [98.0, 1255.0])
    def test_price_typ(self, price):
        bun = Bun("Флюоресцентная булка R2-D3", price)
        assert type(bun.get_price()) is float

    @pytest.mark.parametrize("name", ["Флюоресцентная булка R2-D3", "Краторная булка N-200i"])
    def test_name_type(self, name):
        bun = Bun(name, 988)
        assert type(bun.get_name()) is str