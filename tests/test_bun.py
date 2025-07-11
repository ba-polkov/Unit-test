from praktikum.bun import Bun
from tests.test_data import TEST_BUN_NAME, TEST_BUN_PRICE

class TestBun:
    def test_get_name(self):
        bun = Bun(TEST_BUN_NAME, TEST_BUN_PRICE)
        assert bun.get_name() == TEST_BUN_NAME

    def test_get_price(self):
        bun = Bun(TEST_BUN_NAME, TEST_BUN_PRICE)
        assert bun.get_price() == TEST_BUN_PRICE
