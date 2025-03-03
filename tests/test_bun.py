import pytest
from unittest.mock import Mock
from praktikum.bun import Bun

class TestBun:
    @pytest.mark.parametrize("name, price", [     # Параметризацию для проверки различных значений имени и цены
        ("Булочка 1", 50.0),
        ("Булочка 2", 75.5),
        ("Булочка 3", 100.0),
    ])
    def test_bun(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price

    def test_get_name(self): # Проверяем, что метод возвращает правильное имя
        bun = Bun("Булочка", 30.0)
        assert bun.get_name() == "Булочка"

    def test_get_price(self): # Проверяем, что метод возвращает правильную цену
        bun = Bun("Булочка", 30.0)
        assert bun.get_price() == 30.0

    def test_price_type(self): # Проверяем, что цена возвращается как float
        bun = Bun("Булочка", 30.0)
        assert isinstance(bun.get_price(), float)

    def test_name_type(self): # Проверяем, что имя возвращается как str
        bun = Bun("Булочка", 30.0)
        assert isinstance(bun.get_name(), str)

    def test_bun_with_mock(self): # Mок для класса Bun и проверяет, что методы возвращают ожидаемые значения
        # Создаем мок для класса Bun
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "Сдобная булочка"
        mock_bun.get_price.return_value = 25.0

        assert mock_bun.get_name() == "Сдобная булочка"
        assert mock_bun.get_price() == 25.0

