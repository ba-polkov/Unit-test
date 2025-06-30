import pytest
from unittest.mock import Mock
from practicum.bun import Bun


class TestBun:
    @pytest.mark.parametrize('name,price', [
        ('black bun', 100),
        ('white bun', 200),
        ('red bun', 300)
    ])
    def test_bun_initialization(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name
        assert bun.price == price

    def test_get_name(self):
        bun = Bun('test bun', 100)
        assert bun.get_name() == 'test bun'

    def test_get_price(self):
        bun = Bun('test bun', 150)
        assert bun.get_price() == 150