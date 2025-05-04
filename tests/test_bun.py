# test_bun.py

import pytest
from bun import Bun


class TestBun:
    """Тесты для класса Bun"""

    def test_bun_name_after_initialization(self, parametrized_bun, request):
        """Проверка сохранения названия"""
        name = request.node.callspec.params["parametrized_bun"][0]
        assert parametrized_bun.get_name() == name

    def test_bun_price_after_initialization(self, parametrized_bun, request):
        """Проверка сохранения цены"""
        price = request.node.callspec.params["parametrized_bun"][1]
        assert parametrized_bun.get_price() == price

    def test_int_price_converts_to_float(self):
        """Проверка конвертации int в float"""
        bun = Bun("Булка", 1000)
        assert isinstance(bun.get_price(), float)
        assert bun.get_price() == 1000.0

    def test_float_price_remains_unchanged(self):
        """Проверка сохранения float-цены"""
        bun = Bun("Булка", 999.99)
        assert isinstance(bun.get_price(), float)
        assert bun.get_price() == 999.99

    @pytest.mark.parametrize("price", [0, -100, 1e6])
    def test_unusual_prices(self, price):
        """Проверка граничных значений цен"""
        bun = Bun("Тестовая булка", price)
        assert bun.get_price() == price

    def test_bun_name_immutability(self, default_bun):
        """Проверка, что имя булочки нельзя изменить через прямое присваивание"""
        original_name = default_bun.get_name()

        with pytest.raises(AttributeError):
            default_bun.name = "Новое имя"

        assert default_bun.get_name() == original_name

    def test_bun_price_immutability(self, default_bun):
        """Проверка, что цену булочки нельзя изменить через прямое присваивание"""
        original_price = default_bun.get_price()

        with pytest.raises(AttributeError):
            default_bun.price = 1000

        assert default_bun.get_price() == original_price

    def test_bun_string_representation(self, default_bun):
        """Проверка строкового представления"""
        assert str(default_bun) == "Bun(name='Краторная булка N-200i', price=1255.0)"
