from praktikum.bun import Bun
from data import BUN_DATA, BUN_NAMES
import pytest

class TestBun:
    @pytest.mark.parametrize("bun_name", BUN_NAMES)
    def test_bun_get_name(self, bun_name):
        bun = Bun(bun_name, BUN_DATA[bun_name]["price"])
        assert bun.get_name() == bun_name

    @pytest.mark.parametrize("bun_name", BUN_NAMES)
    def test_bun_get_price(self, bun_name):
        bun = Bun(bun_name, BUN_DATA[bun_name]["price"])
        assert bun.get_price() == BUN_DATA[bun_name]["price"]