import allure
import pytest
from praktikum.bun import Bun
import allure
import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@allure.feature('Bun')
class TestBun:

    @allure.title('Проверка создания булочки (мок)')
    def test_bun_creation(self, mock_bun):
        assert mock_bun.get_name() == "black bun"
        assert mock_bun.get_price() == 100.0

    @allure.title('Проверка метода get_name (мок)')
    def test_get_name(self, mock_bun):
        assert mock_bun.get_name() == "black bun"

    @allure.title('Проверка метода get_price (мок)')
    def test_get_price(self, mock_bun):
        assert mock_bun.get_price() == 100.0

    @allure.title('Параметризованный тест булочек (реальные экземпляры)')
    @pytest.mark.parametrize('name, price', [
        ("black bun", 150),
        ("red bun", 180),
        ("", 0),
        ("a", 0.01),
        ("Очень длинное название булочки", 999.99),
    ])
    def test_bun_params(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price

    @allure.title('Тест с отрицательной ценой (реальный экземпляр)')
    def test_negative_price(self):
        bun = Bun("black bun", -100)
        assert bun.get_price() == -100