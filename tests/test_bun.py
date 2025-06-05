from conftest import *
import allure

class TestBun:

    @allure.title('Проверка get_name()')
    def test_get_name_bun_positive(self, mock_bun):
        assert mock_bun.get_name() == Data1.bun_name

    @allure.title('Проверка get_price()')
    def test_get_price_bun_positive(self, mock_bun_2):
        assert mock_bun_2.get_price() == Data2.bun_price
