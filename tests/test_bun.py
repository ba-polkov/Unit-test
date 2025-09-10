import pytest

from praktikum.bun import Bun
from data.fooditems import buns


class TestBun:
    """Класс для тестирования функциональности булочек."""

    @pytest.mark.parametrize(
        'name, price',
        buns,
        ids=[f'bun-{i}' for i in range(len(buns))]
    )
    def test_bun_get_name(
        self,
        name: str,
        price: float
    ) -> None:
        """Проверяет получение названия булочки."""
        bun = Bun(name, price)
        assert bun.get_name() == name, (
            f"Неверное название булочки: {name}"
        )

    @pytest.mark.parametrize(
        'name, price',
        buns,
        ids=[f'bun-{i}' for i in range(len(buns))]
    )
    def test_bun_get_price(
        self,
        name: str,
        price: float
    ) -> None:
        """Тест проверки получения цены булочки."""
        bun = Bun(name, price)
        assert bun.get_price() == price, (
            f"Неверная цена булочки: {price}"
        )
