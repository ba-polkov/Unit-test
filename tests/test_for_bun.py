import pytest
from bun import Bun


BUN_TEST_DATA = [
    ('black bun', 356.9),
    ('white bun', 590),
    ('red bun', 1200.80)]

class TestForBun:
    @pytest.mark.parametrize('name, price',BUN_TEST_DATA)
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('name, price',BUN_TEST_DATA)
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
