import pytest
from praktikum.bun import Bun
from data import BUN_NAME, BUN_PRICE

class TestBunInitialization:
    @pytest.mark.parametrize("name, price", [
        (BUN_NAME, BUN_PRICE),
        ('Сырная булочка', 30.00),
        ('Острая булочка', 25.50)
    ])
    def test_bun_initialization_name(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name


    @pytest.mark.parametrize("name, price", [
        (BUN_NAME, BUN_PRICE),
        ('Сырная булочка', 30.00),
        ('Острая булочка', 25.50)
    ])

    def test_bun_initialization_price(self, name, price):
        bun = Bun(name, price)
        assert bun.price == price

    @pytest.mark.parametrize("name, price", [
        (BUN_NAME, BUN_PRICE),
        ('Сырная булочка', 30.00),
        ('Острая булочка', 25.50)
    ])

    def test_bun_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", [
        (BUN_NAME, BUN_PRICE),
        ('Сырная булочка', 30.00),
        ('Острая булочка', 25.50)
    ])

    def test_bun_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price


