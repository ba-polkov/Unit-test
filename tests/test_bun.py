from praktikum.bun import Bun
from data import Data
import allure


class TestBun:
    @allure.title("Проверить инициализацию булки по названию и цене")
    def test_initial_name_price(self):
        bun = Bun(Data.bun_name, Data.bun_price)
        assert bun.name == Data.bun_name and bun.price == Data.bun_price

    @allure.title("Проверить метод get_name, возвращающий название булки")
    def test_get_bun_name(self):
        bun = Bun(Data.bun_name, Data.bun_price)
        assert bun.name == bun.get_name()

    @allure.title("Проверить метод get_price, возвращающий цену булки")
    def test_get_bun_price(self):
        bun = Bun(Data.bun_name, Data.bun_price)
        assert bun.price == bun.get_price()
