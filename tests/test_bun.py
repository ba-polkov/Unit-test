import pytest
from ..bun import Bun

# Тестируем инициализацию и геттеры Bun
@pytest.mark.parametrize("name, price", [
    ("black bun", 100),
    ("white bun", 200),
    ("red bun", 300),
])
def test_bun_init_and_getters(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price

# Проверяем, что поля инициализируются корректно
def test_bun_init():
    bun = Bun("Test", 123.45)
    assert bun.name == "Test"
    assert bun.price == 123.45

# Проверяем работу get_name
def test_bun_get_name():
    bun = Bun("Test", 123.45)
    assert bun.get_name() == "Test"

# Проверяем работу get_price
def test_bun_get_price():
    bun = Bun("Test", 123.45)
    assert bun.get_price() == 123.45
