from praktikum.bun import Bun
import pytest


class TestBun:

    @pytest.mark.parametrize('name,price', [
            ('Космобулка', 100000),
            ('Космобулка', 20.5),
            ('Космобулка', 222)
        ])
    def test_get_price_bun_three_bun_price_geted(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price

    @pytest.mark.parametrize('name,price', [
            ('Космобулка', 100),
            ('BLACK BUN', 100),
            ('', 100)
        ])
    def test_get_name_bun_three_bun_name_geted(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name