from unittest.mock import patch
from data import Data
from praktikum.praktikum import Database

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
        for index, bun_data in enumerate(Data.buns):
            bun = database.buns[index]
            assert bun.name == bun_data["name"]
            assert bun.price == bun_data["price"]

    # Проверяем, что ингредиенты добавляются с правильными типами, названиями и ценами
    @patch("praktikum.ingredient.Ingredient")
    def test_database_ingredients_have_correct_attributes(self, mock_ingredient):
        database = Database()
        for index, ing_data in enumerate(Data.ingredients):
            ingredient = database.ingredients[index]
            assert ingredient.type == ing_data["type"]
            assert ingredient.name == ing_data["name"]
            assert ingredient.price == ing_data["price"]

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
