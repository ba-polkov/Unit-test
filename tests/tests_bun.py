import allure
import pytest

class TestBun:
    @allure.title('Получение названия булочки')
    def test_get_name(self, mock_bun, bun_data):
        assert mock_bun.get_name() == bun_data['name']

    @allure.title('Получение цены булочки')
    def test_get_price(self, mock_bun, bun_data):
        assert mock_bun.get_price() == bun_data['price']