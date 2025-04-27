import allure
from data import *


class TestIngridientSauce:

    @allure.title('Проверка получения имени соуса через метод get_name')
    def test_get_name_sauce(self, mock_sauce):
        assert mock_sauce.get_name == Data.Sauce_name

    @allure.title('Проверка получения стоимости соуса через метод get_price')
    def test_get_price_sauce(self, mock_sauce):
        assert mock_sauce.get_price == Data.Sauce_price

    @allure.title('Проверка получения подтверждения типа данных "str" через метод get_type')
    def test_get_type_sauce(self, mock_sauce):
        assert mock_sauce.get_type == Data.Sauce_type


class TestIngridientFilling:

