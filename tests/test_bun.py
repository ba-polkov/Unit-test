import pytest
from praktikum.bun import Bun

class TestBun:
    
    @pytest.mark.parametrize("name, price", [
        ("black bun", 100.0),
        ("white bun", 250.5),
        ("seed bun", 0.0)
    ])
    def test_bun_getters(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price
