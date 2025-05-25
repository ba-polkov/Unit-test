import pytest
from praktikum.bun import Bun

class TestBun:
    # Проверка создания булочки с разными параметрами

    @pytest.mark.parametrize(
        "name, price",
        [
            ("sesame seed bun", 99.99),  # булочка с дробной ценой
            ("ночная булка", 0),  # бесплатная булочка (пограничный случай)
            ("BUN_UPPERCASE", 123.45),  # имя в верхнем регистре
            ("булка с пробелом", 89.50),  # имя с пробелами
        ],
    )
    def test_bun_creation(self, name, price):
        # Создаем булочку
        bun = Bun(name, price)

        # Проверяем корректность имени булочки
        assert bun.get_name() == name

        # Проверяем корректность цены булочки
        assert bun.get_price() == price


