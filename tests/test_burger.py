import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from data import TestData

class TestBurger:
    @pytest.fixture
    def burger(self):
        return Burger()

    @pytest.mark.parametrize("bun_data, ingredients_data, expected", TestData.burger_cases)
    def test_burger_price_calculation(self, burger, bun_data, ingredients_data, expected):
        try:
            # Создание объектов
            bun = Bun(*bun_data) if isinstance(bun_data, tuple) else None
            ingredients = [Ingredient(*i) for i in ingredients_data]
            
            # Настройка бургера
            burger.set_buns(bun)
            for ingredient in ingredients:
                burger.add_ingredient(ingredient)
            
            # Проверка
            if isinstance(expected, type) and issubclass(expected, Exception):
                pytest.fail("Ожидалось исключение, но тест прошёл успешно")
            assert burger.get_price() == expected
            
        except Exception as e:
            if not isinstance(expected, type) or not issubclass(expected, Exception):
                raise
            assert isinstance(e, expected)
