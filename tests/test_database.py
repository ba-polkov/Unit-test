import pytest
from unittest.mock import patch, MagicMock
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    """Тесты для класса Database"""

    def test_initialization_and_buns(self):
        """Проверяет, что база данных создает 3 булочки с правильными именами"""
        # Arrange: Создаем базу данных
        db = Database()
        expected_buns = ["black bun", "white bun", "red bun"]

        # Act: Получаем список булочек
        buns = db.available_buns()

        # Assert: Проверяем количество и имена булочек
        assert len(buns) == 3, f"Ожидалось 3 булочки, но получено {len(buns)}"
        assert all(isinstance(bun, Bun) for bun in buns), "Не все элементы - объекты Bun"
        for i, bun in enumerate(buns):
            assert bun.get_name() == expected_buns[i], f"Ожидалось имя '{expected_buns[i]}', но получено '{bun.get_name()}'"

    def test_ingredients(self):
        """Проверяет, что база данных создает 6 ингредиентов, включая 3 соуса и 3 начинки"""
        # Arrange: Создаем базу данных
        db = Database()

        # Act: Получаем список ингредиентов
        ingredients = db.available_ingredients()

        # Assert: Проверяем количество, соусы и начинки
        assert len(ingredients) == 6, f"Ожидалось 6 ингредиентов, но получено {len(ingredients)}"
        assert all(isinstance(ing, Ingredient) for ing in ingredients), "Не все элементы - объекты Ingredient"
        sauces = [ing for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_SAUCE]
        assert len(sauces) == 3, f"Ожидалось 3 соуса, но получено {len(sauces)}"
        fillings = [ing for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(fillings) == 3, f"Ожидалось 3 начинки, но получено {len(fillings)}"

    @pytest.mark.parametrize(
        "bun_count, expected_count",
        [(0, 0), (1, 1), (2, 2)],
        ids=["no_buns", "one_bun", "two_buns"]
    )
    def test_buns_with_mock(self, mock_bun, bun_count, expected_count):
        """Проверяет метод available_buns с разным количеством булочек, используя мок"""
        # Arrange: Создаем базу данных и список из моков
        db = Database()
        buns_list = [mock_bun for _ in range(bun_count)]

        # Act: Подменяем список булочек и получаем результат
        with patch.object(db, "buns", buns_list):
            buns = db.available_buns()

        # Assert: Проверяем количество булочек
        assert len(buns) == expected_count, f"Ожидалось {expected_count} булочек, но получено {len(buns)}"

    @patch('praktikum.database.Bun')
    @patch('praktikum.database.Ingredient')
    def test_initialization_mocks(self, mock_ingredient, mock_bun):
        """Проверяет, что при создании базы данных вызывается нужное количество объектов"""
        # Arrange: Настраиваем моки
        mock_bun.return_value = MagicMock()
        mock_ingredient.return_value = MagicMock()

        # Act: Создаем базу данных
        db = Database()

        # Assert: Проверяем количество вызовов
        assert mock_bun.call_count == 3, f"Ожидалось 3 вызова Bun, но получено {mock_bun.call_count}"
        assert mock_ingredient.call_count == 6, f"Ожидалось 6 вызовов Ingredient, но получено {mock_ingredient.call_count}"