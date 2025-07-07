from praktikum.database import *
import pytest


class TestBun:
    # проверяем название булочки и ее цену
    @pytest.mark.parametrize(
        "expected_name, expected_price",
        [
            ("black bun", 100),
            ("white bun", 200),
            ("red bun", 300),
        ],
    )
    def test_bun_name_and_price(self, expected_name, expected_price):
        bun = Bun(expected_name, expected_price)
        assert bun.get_name() == expected_name and bun.get_price() == expected_price


