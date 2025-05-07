import pytest
import allure
from praktikum.bun import Bun


@allure.feature("Булочка")
@allure.story("Проверка работы с булочками")
class TestBun:
    """Тесты для проверки работы с булочками"""

    @allure.title("Проверка, что булочка создается с правильными параметрами")
    def test_bun_creation(self):
        """Проверка, что булочка создается с правильными параметрами"""
        with allure.step("Создаем булочку с именем 'black bun' и ценой 100"):
            bun = Bun("black bun", 100)

        with allure.step("Проверяем, что имя булочки правильно"):
            assert bun.get_name() == "black bun", f"Ожидалось имя 'black bun', но получено {bun.get_name()}"

        with allure.step("Проверяем, что цена булочки правильно"):
            assert bun.get_price() == 100, f"Ожидалась цена 100, но получено {bun.get_price()}"

    @allure.title("Проверка работы метода get_name")
    def test_bun_get_name(self):
        """Проверка работы метода get_name"""
        with allure.step("Создаем булочку с именем 'white bun' и ценой 150"):
            bun = Bun("white bun", 150)

        with allure.step("Проверяем имя булочки"):
            assert bun.get_name() == "white bun", f"Ожидалось имя 'white bun', но получено {bun.get_name()}"

    @allure.title("Проверка работы метода get_price")
    def test_bun_get_price(self):
        """Проверка работы метода get_price"""
        with allure.step("Создаем булочку с именем 'red bun' и ценой 200"):
            bun = Bun("red bun", 200)

        with allure.step("Проверяем цену булочки"):
            assert bun.get_price() == 200, f"Ожидалась цена 200, но получено {bun.get_price()}"