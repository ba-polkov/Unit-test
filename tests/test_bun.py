import pytest
from practikum.bun import Bun

class TestBun:

    # Тестирование получения названия булочки
    @pytest.mark.parametrize("name,price", [
                        ("Plasma Bun", 25.0),
                        ("Ice Bun", 10.0),])
    def test_get_name(self, name , price):
        bun = Bun(name, price)
        assert bun.get_name() == name, "Метод get_name возвращает неверное название."

    # Тестирование получения цены булочки
    @pytest.mark.parametrize("name,price", [
                        ("Plasma Bun", 25.0),
                        ("Ice Bun", 10.0),])
    def test_get_price(self, name , price):
        bun = Bun(name, price)
        assert bun.get_price() == price, "Метод get_price возвращает неверную цену."

