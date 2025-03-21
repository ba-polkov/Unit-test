import pytest

from praktikum.bun import Bun


@pytest.fixture
def bun():
    return Bun(name='Краторная булка', price=1255.0)

class TestBun:
    def test_get_name(self, bun):
        assert bun.get_name() == 'Краторная булка'

    def test_get_price(self, bun):
         assert bun.get_price() == 1255.0
