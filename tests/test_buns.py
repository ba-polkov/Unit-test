import pytest
from practicum.bun import Bun
from data import BUN_NAME_1, BUN_NAME_2, BUN_PRICE


class TestBuns:
#Тест, правильно ли устанавливается название булочки
    @pytest.mark.parametrize("name", [BUN_NAME_1, BUN_NAME_2])
    def test_bun_name(self, name):
        bun = Bun(name, BUN_PRICE)
        assert bun.get_name() == name, f"Название булочки '{bun.get_name()}' не соответствует ожидаемому '{name}'"

#Тест, проверяет, цену на булочку
    def test_bun_price(self):
        bun = Bun(BUN_NAME_1, BUN_PRICE)
        assert bun.get_price() == BUN_PRICE, f"Цена булочки {bun.get_price()} не соответствует ожидаемой {BUN_PRICE}"