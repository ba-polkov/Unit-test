from data import Data
from praktikum.praktikum import Bun


class TestBun:
    def test_get_name_correct_name(self):
        new_bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)
        assert new_bun.get_name() == Data.BUN_NAME


    def test_get_price_correct_price(self):
        new_price = Bun(Data.BUN_NAME, Data.BUN_PRICE)
        assert new_price.get_price() == Data.BUN_PRICE

