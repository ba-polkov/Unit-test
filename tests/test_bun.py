import pytest
import allure
from praktikum.bun import Bun
from data import *
from helpers import *

class TestBun:

    @allure.title("Тест получения названия булочки")
    @pytest.mark.parametrize("bun_name, bun_price", buns_name_price)
    def test_get_name(self, bun_name, bun_price):
        bun = Bun(name=bun_name, price=bun_price)
        TestTools.check_unit_test_result(expected_value=bun_name, actually_value=bun.get_name())

    @allure.title("Тест получения цены булочки")
    @pytest.mark.parametrize("bun_name, bun_price", buns_name_price)
    def test_get_price(self, bun_name, bun_price):
        bun = Bun(name=bun_name, price=bun_price)
        TestTools.check_unit_test_result(expected_value=bun_price, actually_value=bun.get_price())


