import pytest

from bun import Bun


class TestBun:
    TEST_DATA = [
            ("Булчичка", 1.0),  # кириллица + float
            ("little bun", 2.5),  # латиница + дробная
            ("Bun 2", 0),  # с числом + ноль (int)
            ("Булчичка №1", 3.75),  # символ № + дробная
            ("  Вкуснявая  ", 10),  # пробелы по краям + int
            ("O'bun", 1_000_000),  # апостроф + большое число
            ("Вкуснявая-цельнозерновая", 1.25),  # дефис
            ("x" * 10, 0.99),  # очень длинное имя
    ]

    @pytest.mark.parametrize(
        "name, price",
        TEST_DATA,
    )
    def test_get_bun_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize(
        "name, price",
        TEST_DATA,
    )
    def test_get_bun_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
