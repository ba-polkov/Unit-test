from praktikum.bun import Bun
from data.Data import Data

class TestBun:
    # Проверка: метод должен возвращать корректное название булки
    def test_get_name_return_true_name(self):
        bun_info = Data.buns[0]
        bun = Bun(bun_info.get("name"), bun_info.get("price"))
        actual_name = bun.get_name()
        expected_name = bun_info.get("name")
        assert actual_name == expected_name

    # Проверка: метод должен возвращать корректную цену булки
    def test_get_price_return_true_price(self):
        bun_info = Data.buns[1]
        bun = Bun(bun_info.get("name"), bun_info.get("price"))
        actual_price = bun.get_price()
        expected_price = bun_info.get("price")
        assert actual_price == expected_price
