import allure

from praktikum.bun import Bun
from data_for_test import TestBunsData as TBD


class TestClassBun:
    @allure.title('Возвращение названия булки')
    def test_return_bun_name(self):
        bun_name = Bun(**TBD.BUN).get_name()
        assert bun_name == TBD.BUN['name']

    @allure.title('Возвращение стоимости булки')
    def test_return_bun_price(self):
        bun_price = Bun(**TBD.BUN).get_price()
        assert bun_price == TBD.BUN['price']

    @allure.title('Возвращение нужного типа названия булки')
    def test_return_valid_bun_name_type(self):
        bun_name = Bun(**TBD.BUN).name
        assert isinstance(bun_name, str)

    @allure.title('Возвращение нужного типа стоимости булки')
    def test_return_valid_bun_price_type(self):
        bun_price = Bun(**TBD.BUN).price
        assert isinstance(bun_price, int)