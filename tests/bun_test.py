import pytest
from praktikum.bun import Bun
class TestBun:

    @pytest.mark.parametrize('name, price', [
        ('Bun 1', 50.0),
        ('Bun 2', 65.5),
        ('Bun 3', None),
        ('Bun 4', -1),
        (1, '100'),
        (None, 0.0),
        (None, None),
    ])
    def test_bun_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('name, price', [
        ('Bun 1', 50.0),
        ('Bun 2', 65.5),
        ('Bun 3', None),
        ('Bun 4', -1),
        (1, '100'),
        (None, 0.0),
        (None, None),
    ])
    def test_bun_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
