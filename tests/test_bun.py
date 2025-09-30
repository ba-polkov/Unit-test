import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest  # noqa: E402
from praktikum.bun import Bun  # noqa: E402


class TestBun:
    """Тесты для класса Bun с параметризацией различных типов булок и цен."""

    @pytest.mark.parametrize("name, price, expected_name, expected_price", [
        ("black bun", 100.0, "black bun", 100.0),
        ("white bun", 200.0, "white bun", 200.0),
        ("red bun", 300.0, "red bun", 300.0),
        ("sesame bun", 150.5, "sesame bun", 150.5),
        ("whole wheat bun", 250.75, "whole wheat bun", 250.75),
    ])
    def test_bun_initialization(
        self, name, price, expected_name, expected_price
    ):
        """Тест инициализации булки с различными параметрами."""
        bun = Bun(name, price)

        assert bun.get_name() == expected_name
        assert bun.get_price() == expected_price

    @pytest.mark.parametrize("name, price", [
        ("black bun", 100.0),
        ("white bun", 200.0),
        ("red bun", 300.0),
        ("", 0.0),  # Пустое название
        ("premium bun", -50.0),  # Отрицательная цена
    ])
    def test_bun_get_name(self, name, price):
        """Тест получения названия булки."""
        bun = Bun(name, price)

        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", [
        ("black bun", 100.0),
        ("white bun", 200.0),
        ("red bun", 300.0),
        ("budget bun", 0.0),  # Нулевая цена
        ("luxury bun", 999.99),  # Высокая цена
    ])
    def test_bun_get_price(self, name, price):
        """Тест получения цены булки."""
        bun = Bun(name, price)

        assert bun.get_price() == price

    def test_bun_attributes_access(self, sample_bun):
        """Тест доступа к атрибутам булки через геттеры."""
        bun = sample_bun

        # Проверяем, что геттеры возвращают правильные значения
        assert bun.get_name() == "test bun"
        assert bun.get_price() == 100.0

        # Проверяем, что прямое изменение атрибутов влияет на геттеры
        # (это демонстрирует отсутствие инкапсуляции в текущей реализации)
        bun.name = "modified bun"
        bun.price = 999.0

        assert bun.get_name() == "modified bun"
        assert bun.get_price() == 999.0
# Тесты для класса Bun с параметризацией различных типов булок и цен.
# Используем моки для симуляции зависимостей и параметризацию
# для тестирования различных сценариев без дублирования кода.
