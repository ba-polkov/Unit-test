import pytest
from praktikum.bun import *
class TestBun():

    @pytest.mark.parametrize("name, price, expected_name, expected_price", [
        ("Вкусняшка булка", 10.99, "Вкусняшка булка", 10.99),
        ("Черная булочка", 20, "Черная булочка", 20)
    ])
    def test_product_initialization_and_method_name(self, name, price, expected_name, expected_price):
        bun = Bun(name=name, price=price)
        assert bun.get_name() == expected_name


    @pytest.mark.parametrize("name, price, expected_name, expected_price", [
        ("Вкусняшка булка", 10.99, "Вкусняшка булка", 10.99),
        ("Черная булочка", 20, "Черная булочка", 20)
    ])
    def test_product_initialization_and_method_price(self, name, price, expected_name, expected_price):

        bun = Bun(name=name, price=price)
        assert bun.get_price() == expected_price