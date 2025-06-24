import allure
from praktikum.bun import Bun
from data import bun_name_price
from helpers import *

class TestBun:

    @allure.title("Тест получения названия булочки")
    def test_bun_get_name(self):
        bun = Bun(name=bun_name_price[0], price=bun_name_price[1])
        TestTools.check_unit_test_result(expected_value=bun_name_price[0], actually_value=bun.get_name())

    @allure.title("Тест получения цены булочки")
    def test_bun_get_price(self):
        bun = Bun(name=bun_name_price[0], price=bun_name_price[1])
        TestTools.check_unit_test_result(expected_value=bun_name_price[1], actually_value=bun.get_price())


