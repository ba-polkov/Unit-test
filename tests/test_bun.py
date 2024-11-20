import allure
import pytest
from practicum.bun import Bun
from data import BUN_NAME, BUN_PRICE, BUN_PRICE_ZERO, BUN_PRICE_NEGATIVE

class TestBun:
    @pytest.mark.parametrize("name, price, expected", [
        (BUN_NAME, BUN_PRICE, BUN_PRICE),
        (BUN_NAME, BUN_PRICE_NEGATIVE, BUN_PRICE_NEGATIVE),
        (BUN_NAME, BUN_PRICE_ZERO, 0.0)])

    @allure.title("Проверка разных цен булки")
    def test_bun_price(self, name, price, expected):
        bun = Bun(name, price)
        assert bun.get_price() == expected

    @allure.title("Проверка имени булки")
    def test_bun_name(self):
        bun = Bun(BUN_NAME, BUN_PRICE)
        assert bun.get_name() == BUN_NAME

    @allure.title("Проверка типа данных цены булки")
    def test_bun_type_price(self):
        bun = Bun(BUN_NAME, BUN_PRICE)
        assert isinstance(bun.get_price(), float)

    @allure.title("Проверка типа данных названия булки")
    def test_bun_name_type(self):
        bun = Bun(BUN_NAME, BUN_PRICE)
        assert isinstance(bun.get_name(), str)

    @allure.title("Проверка возможности сменить имя булки")
    def test_bun_set_name(self):
        bun = Bun(BUN_NAME, BUN_PRICE)
        bun.name = "Glutten"
        assert bun.get_name() == "Glutten"

    @allure.title("Проверка возможности сменить цену булки")
    def test_bun_set_price(self):
        bun = Bun(BUN_NAME, BUN_PRICE)
        bun.price = 109.9
        assert bun.get_price() == 109.9
