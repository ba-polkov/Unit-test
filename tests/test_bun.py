from praktikum.bun import Bun
from conftest import *

class TestBun:
    def test_init_bun_name_positive_result(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name

    def test_init_bun_price_positive_result(self, name, price):
        bun = Bun(name, price)
        assert bun.price == price

    def test_get_name_positive_result(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    def test_get_price_positive_result(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price