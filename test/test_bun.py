from praktikum.burger import *
from conftest import *


class TestBun:
    @pytest.mark.parametrize("name", ["black bun", "white bun", "red bun"])
    def test_get_name(self, name):
        bun = Bun(name, 123)
        assert bun.get_name() == name

    @pytest.mark.parametrize("price", [100, 200, 300])
    def test_get_price(self, price):
        bun = Bun("test bun", price)
        assert bun.get_price() == price
