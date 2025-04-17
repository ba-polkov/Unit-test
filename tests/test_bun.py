import pytest
from bun import Bun


def test_bun_creation():
    """Проверка, что булочка создается с правильными параметрами"""
    bun = Bun("black bun", 100)

    # Проверка, что имя булочки правильно
    assert bun.get_name() == "black bun", f"Ожидалось имя 'black bun', но получено {bun.get_name()}"

    # Проверка, что цена булочки правильно
    assert bun.get_price() == 100, f"Ожидалась цена 100, но получено {bun.get_price()}"


def test_bun_get_name():
    """Проверка работы метода get_name"""
    bun = Bun("white bun", 150)
    assert bun.get_name() == "white bun", f"Ожидалось имя 'white bun', но получено {bun.get_name()}"


def test_bun_get_price():
    """Проверка работы метода get_price"""
    bun = Bun("red bun", 200)
    assert bun.get_price() == 200, f"Ожидалась цена 200, но получено {bun.get_price()}"