import pytest
from praktikum.bun import Bun


class TestBun:
    list_data = [("black bun", 100.0),
                 ("white bun", 200.0),
                 ("", 0.0),
                 ("1", 0.01),
                 ("b" * 100, 999.99)]

    @pytest.mark.parametrize("name, price", list_data)
    def test_bun_properties(self, name, price):
            bun = Bun(name, price)

            assert bun.get_name() == name
            assert bun.get_price() == price
