import pytest
from praktikum.bun import Bun

class TestBun:

    # Проверяем, что get_name() возвращает корректное название булочки
    @pytest.mark.parametrize('name,price', [
        ('Флюоресцентная булка R2-D3', 988),
        ('', 100),
        ('Б', 100)
        ])
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    # Проверяем, что get_price() возвращает корректную цену
    @pytest.mark.parametrize('name,price', [
        ('Флюоресцентная булка R2-D3', 988),
        ('Краторная булка N-200i', 125.5),
        ('Без цены', 0),
        ('Большая цена', 9999999),
        ])
    def test_get_bun_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price

