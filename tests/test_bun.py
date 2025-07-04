import pytest
from praktikum.bun import Bun


class TestBun:
    
    @pytest.mark.parametrize("name, price", [("Japan bun", 100.0), 
                                         ("USA bun", 200.0), 
                                         ("Russia bun", 300.0)])
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", [("Japan bun", 100.0), 
                                         ("USA bun", 200.0), 
                                         ("Russia bun", 300.0)])
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
