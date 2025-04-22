from praktikum.bun import Bun
import pytest

class TestBunModel:
    def test_set_valid_and_price_name_for_bun(self):
        bun = Bun(name="Ordinary Bun", price=0.5)
        assert bun.get_name() == "Ordinary Bun" and bun.get_price() == 0.5







