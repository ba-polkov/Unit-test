import pytest
from praktikum.bun import Bun
from data import BUN_NAME, BUN_PRICE

@pytest.mark.parametrize("name, price", [
    (BUN_NAME, BUN_PRICE),
    ('Сырная булочка', 30.00),
    ('Острая булочка', 25.50)
])
def test_bun_initialization(name, price):
    bun = Bun(name, price)
    assert bun.name == name
    assert bun.price == price


