from praktikum.bun import Bun
from .data import BUNS


class TestBun:
    """Тестовый класс для проверки методов класса Bun."""

    def test_get_name_returns_correct_name(self):
        """Проверяет, что get_name() возвращает ТОЧНОЕ название."""
        bun = BUNS[0]
        assert bun.get_name() == "black bun"

    def test_get_price_returns_correct_price(self):
        """Проверяет, что get_price() возвращает ТОЧНУЮ цену."""
        bun = BUNS[0]
        assert bun.get_price() == 100