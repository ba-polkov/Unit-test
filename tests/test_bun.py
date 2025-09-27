from praktikum.bun import Bun
from data import BUN_DATA


class TestBun:

    def test_bun_name(self):
        name, price = BUN_DATA["test_bun_name"]
        bun = Bun(name=name, price=price)
        assert bun.get_name() == name

    def test_bun_price_positive(self):
        name, price = BUN_DATA["test_bun_price_positive"]
        bun = Bun(name=name, price=price)
        assert bun.get_price() == price

    def test_bun_price_float(self):
        name, price = BUN_DATA["test_bun_price_float"]
        bun = Bun(name=name, price=price)
        assert bun.get_price() == price
