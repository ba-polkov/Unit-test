import pytest
from bun import Bun


class TestBun:

    class TestBun:
        @pytest.mark.parametrize(
            "name, price",[
                ("black bun", 100.0),
                ("white bun", 200.0),
                ("", 0.0),
                ("1", 0.01),
                ("b" * 100, 999.99)
            ]
        )
        def test_bun_properties(self, name, price):
            bun = Bun(name, price)
            assert bun.get_name() == name
            assert bun.get_price() == price
