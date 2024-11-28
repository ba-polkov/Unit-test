import allure
from bun import Bun
from data import BurgerConsist as bc


class TestBun:
    @allure.title('проверка получения названия булки - метод get_name')
    def test_get_name(self):
        bun = Bun(bc.SECOND_BUN_NAME, bc.SECOND_BUN_PRICE)
        assert bun.get_name() == bc.SECOND_BUN_NAME


    @allure.title('проверка получения стоимости булки - метод get_price')
    def test_get_price(self):
        bun = Bun(bc.SECOND_BUN_NAME, bc.SECOND_BUN_PRICE)
        assert bun.get_price() == bc.SECOND_BUN_PRICE
