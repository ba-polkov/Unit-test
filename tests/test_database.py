from unittest.mock import patch
from data.data import Data
from praktikum.database import Database
from data.helpers import compare_buns, compare_ingredients

class TestDatabase:
    # Проверяем, что при инициализации БД создается 3 булки и 6 ингредиентов
    @patch("praktikum.bun.Bun")
    @patch("praktikum.ingredient.Ingredient")
    def test_database_initializes_with_three_buns_and_six_ingredients(self, mock_bun, mock_ingredient):
        database = Database()
        assert len(database.buns) == 3
        assert len(database.ingredients) == 6

    # Проверяем, что булки добавляются с корректными названиями и ценами
    @patch("praktikum.bun.Bun")
    def test_database_buns_have_correct_name_and_price(self, mock_bun):
        database = Database()
        success, error_message = compare_buns(database, Data.buns)
        assert success, error_message

    # Проверяем, что ингредиенты добавляются с правильными типами, названиями и ценами
    @patch("praktikum.ingredient.Ingredient")
    def test_database_ingredients_have_correct_attributes(self, mock_ingredient):
        database = Database()
        success, error_message = compare_ingredients(database, Data.ingredients)
        assert success, error_message

    # Проверяем, что метод возвращает ровно 3 доступные булки
    @patch("praktikum.bun.Bun")
    def test_available_buns_returns_three_items(self, mock_bun):
        database = Database()
        buns = database.available_buns()
        assert len(buns) == 3

    # Проверяем, что метод возвращает ровно 6 доступных ингредиентов
    @patch("praktikum.ingredient.Ingredient")
    def test_available_ingredients_returns_six_items(self, mock_ingredient):
        database = Database()
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6
