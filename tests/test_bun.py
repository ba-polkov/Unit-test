import pytest
from praktikum.bun import Bun


class TestBun:
    
    def test_get_name(self):
        bun = Bun("Красная булочка", 150)
        assert bun.get_name() == "Красная булочка"
    
    def test_get_price(self):
        bun = Bun("Красная булочка", 150)
        assert bun.get_price() == 150
    
    def test_create_bun_with_different_data(self):
        bun = Bun("Черная булочка", 200.5)
        assert bun.get_name() == "Черная булочка"
        assert bun.get_price() == 200.5