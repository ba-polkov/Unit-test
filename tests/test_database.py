from unittest.mock import patch
from praktikum.database import Database


class TestDataBase:
    @patch('praktikum.database.Bun', autospec=True)
    def test_available_buns_return_buns(self, mockbun):
        mock_bun1 = mockbun.return_value
        mock_bun1.get_name.return_value = 'Mock бутофория'
        mock_bun1.get_price.return_value = 100.0
        database = Database()
        database.buns = [mock_bun1]
        buns = database.available_buns()

        assert buns == [mock_bun1], f'Метод "available_buns" должен возвращать булочку.'

    @patch('praktikum.database.Ingredient', autospec=True)
    def test_available_ingredients_return_ingredients(self, mockingredient):
        mock_ingredient1 = mockingredient.return_value
        mock_ingredient1.get_name.return_value = 'Mock салат'
        mock_ingredient1.get_type.return_value = 'Кетчуп'
        database = Database()
        database.ingredients = [mock_ingredient1]
        ingredients = database.available_ingredients()

        assert ingredients == [mock_ingredient1], f'Метод "available_ingredients" должен возвращать ингредиенты.'
