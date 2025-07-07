import pytest
from unittest.mock import Mock
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:
    """Тест-кейсы для класса Ingredient"""
    
    # Параметризованный тест конструктора с разными типами ингредиентов
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "Сырный соус", 50),
        (INGREDIENT_TYPE_FILLING, "Говяжья котлета", 100),
        (INGREDIENT_TYPE_SAUCE, "Острый соус", 60),
        (INGREDIENT_TYPE_FILLING, "Салат", 20)
    ])
    def test_ingredient_creation(self, ingredient_type, name, price):
        """Тест-кейс 1: Создание ингредиента с разными параметрами"""
        ingredient = Ingredient(ingredient_type, name, price)
        
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price

    # Тест строкового представления
    def test_ingredient_string_representation(self):
        """Тест-кейс 2: Проверка строкового представления"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Сырный соус", 50)
        assert str(ingredient) == "Сырный соус"
        assert repr(ingredient) == "Сырный соус"

    # Тест с mock-объектом
    def test_mock_ingredient(self):
        """Тест-кейс 3: Проверка работы с mock-объектом"""
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient.get_name.return_value = "Котлета"
        mock_ingredient.get_price.return_value = 100
        
        assert mock_ingredient.get_type() == INGREDIENT_TYPE_FILLING
        assert mock_ingredient.get_name() == "Котлета"
        assert mock_ingredient.get_price() == 100

    # Негативные тесты
    @pytest.mark.parametrize("ingredient_type, name, price, exception", [
        (None, "Соус", 50, TypeError),          # None вместо типа
        ("UNKNOWN", "Соус", 50, ValueError),    # Неизвестный тип
        (INGREDIENT_TYPE_SAUCE, "", 50, ValueError),    # Пустое название
        (INGREDIENT_TYPE_SAUCE, None, 50, TypeError),   # None вместо названия
        (INGREDIENT_TYPE_SAUCE, "Соус", -10, ValueError),  # Отрицательная цена
        (INGREDIENT_TYPE_SAUCE, "Соус", "50", TypeError)   # Строка вместо цены
    ])
    def test_invalid_ingredient_creation(self, ingredient_type, name, price, exception):
        """Тест-кейс 4: Проверка обработки некорректных входных данных"""
        with pytest.raises(exception):
            Ingredient(ingredient_type, name, price)

    # Тест изменения цены (если функционал предусмотрен)
    def test_price_change(self):
        """Тест-кейс 5: Проверка изменения цены ингредиента"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус", 50)
        
        # Если атрибут изменяемый
        ingredient.price = 60
        assert ingredient.get_price() == 60
        
        # Если атрибут read-only
        with pytest.raises(AttributeError):
            ingredient.price = 70