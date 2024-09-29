import pytest

from Diplom_1.data import BunData
from Diplom_1.praktikum.bun import Bun


# Тестирование класса Bun
class TestBun:
    @pytest.mark.parametrize("name", BunData.BUN_NAMES)
    def test_bun_names(self, name):
        index = BunData.BUN_NAMES.index(name)
        bun = Bun(name, BunData.BUN_PRICES[index])

        assert bun.get_name() == name

    @pytest.mark.parametrize("price", BunData.BUN_PRICES)
    def test_bun_prices(self, price):
        index = BunData.BUN_PRICES.index(price)
        bun = Bun(BunData.BUN_NAMES[index], price)

        assert bun.get_price() == price
