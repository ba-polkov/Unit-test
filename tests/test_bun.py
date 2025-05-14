import pytest
from praktikum.bun import Bun

@pytest.mark.buns
class TestBun:


    def test_set_name_for_bun(self):
        name ='Соевая булка'
        price = 10
        bun = Bun(name,price)
        assert bun.get_name() == name

    def test_set_price_for_bun(self):
        name ='Соевая булка'
        price = 10
        bun = Bun(name,price)
        assert bun.get_price() == price