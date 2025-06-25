import allure
import pytest
from praktikum.bun import Bun

@allure.feature('Bun')
class TestBun:

    @allure.title('Проверка создания булочки')
    def test_bun_creation(self, bun):
        assert bun.name == "white bun"
        assert bun.price == 200

    @allure.title('Проверка метода get_name')
    def test_get_name(self, bun):
        assert bun.get_name() == "white bun"

    @allure.title('Проверка метода get_price')
    def test_get_price(self, bun):
        assert bun.get_price() == 200

    @allure.title('Параметризованный тест булочек')
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

    @allure.title('Тест с отрицательной ценой')
    def test_negative_price(self):
        bun = Bun("black bun", -100)
        assert bun.get_price() == -100