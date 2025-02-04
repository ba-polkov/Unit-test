from unittest.mock import Mock
from praktikum.database import Database


class TestDataBase:
    def test_database_return_available_buns(self):
        database = Database()
        bun = Mock()
        bun1 = Mock()
        bun2 = Mock()
        database.buns = [bun, bun1, bun2]

        assert database.available_buns() == database.buns

    def test_database_return_available_ingredients(self):
        database = Database()
        ingredient = Mock()
        ingredient1 = Mock()
        ingredient2 = Mock()

        database.ingredients = [ingredient, ingredient1, ingredient2]

        assert database.available_ingredients() == database.ingredients
