from praktikum.ingredient import Ingredient
from .data import INGREDIENTS

class TestIngredient:
    """Тестовый класс для проверки методов класса Ingredient."""

    def test_get_name_returns_correct_name(self):
        """Проверяет, что get_name() возвращает ТОЧНОЕ название."""
        ingredient = INGREDIENTS[0]
        assert ingredient.get_name() == "hot sauce"

    def test_get_price_returns_correct_price(self):
        """Проверяет, что get_price() возвращает ТОЧНУЮ цену."""
        ingredient = INGREDIENTS[0]
        assert ingredient.get_price() == 10

    def test_get_type_returns_correct_type(self):
        """Проверяет, что get_type() возвращает ТОЧНЫЙ тип."""
        ingredient = INGREDIENTS[1]
        assert ingredient.get_type() == 'FILLING'