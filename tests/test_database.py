import sys
sys.path.append('C:\\Cygwin\\home\\user\\Diplom\\Diplom_1')
from Diplom_1.database import Database
from unittest.mock import Mock, patch


class MockBun:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class MockIngredient:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price

class TestDatabase():
    @patch('Diplom_1.database.Database.available_buns')
    def test_available_buns(self, mock_available_buns):
        expected_buns = [
            MockBun("black bun", 100),
            MockBun("white bun", 200),
            MockBun("red bun", 300)
        ]
        mock_available_buns.return_value = expected_buns
        database = Database()
        buns = database.available_buns()

        assert buns==expected_buns

    @patch('Diplom_1.database.Database.available_ingredients')
    def test_available_ingredients(self, mock_available_ingredients):
        # Создаем список ожидаемых ингредиентов
        expected_ingredients = [
            MockIngredient("SAUCE", "hot sauce", 100),
            MockIngredient("SAUCE", "sour cream", 200),
            MockIngredient("SAUCE", "chili sauce", 300),
            MockIngredient("FILLING", "cutlet", 100),
            MockIngredient("FILLING", "dinosaur", 200),
            MockIngredient("FILLING", "sausage", 300)
        ]

        mock_available_ingredients.return_value = expected_ingredients
        database = Database()
        assert database.available_ingredients()==expected_ingredients