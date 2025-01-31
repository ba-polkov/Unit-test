from praktikum.bun import Bun
from data import Data
import allure


class TestBun:
    @allure.title('Проверка инициализации модели булки')
    def test_initial_name_price(self):
        bun = Bun(Data.bun_name, Data.bun_price)
        assert bun.name == Data.bun_name and bun.price == Data.bun_price

    @allure.title('Проверка метода get_name, возвращающего название булки')
    def test_get_bun_name(self):
        bun = Bun(Data.bun_name, Data.bun_price)
        assert bun.name == bun.get_name()

    @allure.title('Проверка метода get_price, возвращающего цены булки')
    def test_get_bun_price(self):
        bun = Bun(Data.bun_name, Data.bun_price)
        assert bun.price == bun.get_price()

    @allure.title('Проверка инициализации булки с пустым именем')
    def test_empty_name(self):
        bun = Bun("", Data.bun_price)
        assert bun.get_name() == "", "Имя булки должно быть пустым"

    @allure.title('Проверка инициализации булки с ценой ноль')
    def test_zero_price(self):
        bun = Bun(Data.bun_name, Data.bun_zero_price)
        assert bun.get_price() == Data.bun_zero_price, "Цена булки должна быть 0.0"

    @allure.title('Проверка, что цена может быть отрицательной')
    def test_price_negative(self):
        bun = Bun(Data.bun_name, Data.bun_negative_price)
        assert bun.get_price() == Data.bun_negative_price, "Цена космической булки должна быть отрицательной"
