import pytest
from praktikum.bun import Bun
from data import TestData

class TestBun:
    @pytest.mark.parametrize("name, price", TestData.valid_buns)
    def test_valid_bun_creation(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price

    @pytest.mark.parametrize("name, price", TestData.invalid_buns)
    def test_invalid_bun_raises_error(self, name, price):
        with pytest.raises(ValueError):
            Bun(name, price)
