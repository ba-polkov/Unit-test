import pytest
from ya_praktikum.bun import Bun

@pytest.mark.parametrize("name, price", [
    ("white", 25),
    ("wholewheat", 30),
    ("gluten-free", 40),
    ("black", 50)
])
def test_bun_initialization(name, price):
    bun = Bun(name=name, price=price)
    assert bun.name == name, f"Expected name {name}, but got {bun.name}"
    assert bun.price == price, f"Expected price {price}, but got {bun.price}"

def test_bun_get_name(sample_bun):
    assert sample_bun.get_name() == "white", f"Expected name 'white', but got {sample_bun.get_name()}"

def test_bun_get_price(sample_bun):
    assert sample_bun.get_price() == 25, f"Expected price 25, but got {sample_bun.get_price()}"
