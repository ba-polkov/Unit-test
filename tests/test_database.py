from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from .data import BUNS, INGREDIENTS


class TestDatabase:
    """Тестовый класс для проверки методов класса Database."""

    # Инициализация DB в setup_class для использования во всех тестах
    @classmethod
    def setup_class(cls):
        cls.db = Database()

    def test_available_buns_returns_correct_count(self):
        """Проверяет, что available_buns() возвращает ожидаемое количество булок (3)."""
        available_buns = self.db.available_buns()
        assert len(available_buns) == 3
        assert available_buns[0].get_name() == "black bun"  # Проверка первого элемента на точное соответствие

    def test_available_ingredients_returns_correct_count(self):
        """Проверяет, что available_ingredients() возвращает ожидаемое количество ингредиентов (6)."""
        available_ingredients = self.db.available_ingredients()
        assert len(available_ingredients) == 6
        assert available_ingredients[0].get_name() == "hot sauce"  # Проверка первого элемента на точное соответствие