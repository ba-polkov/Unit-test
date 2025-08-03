import pytest
import allure
from praktikum.bun import Bun
from data import BUN_BAP, BUN_BAGEL, BUN_CIABATTA, PRICE_DEFAULT, PRICE_ZERO, PRICE_FLOAT, PRICE_INT


class TestBun:

    @pytest.mark.parametrize('name', (BUN_CIABATTA, BUN_BAGEL, BUN_BAP))
    def test_burger_name(self, name):
        bun = Bun(name, PRICE_DEFAULT)
        assert bun.name == name

    @pytest.mark.parametrize('price', [PRICE_ZERO, PRICE_FLOAT, PRICE_INT])
    def test_burger_price(self, price):
        bun = Bun('default', price)
        assert bun.price == price

    def test_get_name(self):
        bun = Bun(BUN_CIABATTA, PRICE_DEFAULT)
        assert bun.get_name() == BUN_CIABATTA

    def test_get_price(self):
        bun = Bun(BUN_CIABATTA, PRICE_INT)
        assert bun.get_price() == PRICE_INT
