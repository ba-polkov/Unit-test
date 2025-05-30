from unittest.mock import patch, Mock
from praktikum.database import Database
from ingredient_types import INGREDIENT_TYPE_SAUCE


class TestDatabase:
    @patch('praktikum.database.Database')
    def test_available_buns(self, mock_database_class):
        mock_buns = [
            Mock(get_name=Mock(return_value="black bun"), get_price=Mock(return_value=100))
        ]
        mock_database = Mock()
        mock_database.buns = mock_buns
        mock_database.available_buns.return_value = mock_buns
        mock_database_class.return_value = mock_database
        db = Database()
        result = db.available_buns()

        assert result[0].get_name() == "black bun"
        assert result[0].get_price() == 100

    @patch('praktikum.database.Database')
    def test_available_ingredients(self, mock_database_class):
        mock_ingredients = [
            Mock(get_type=Mock(return_value=INGREDIENT_TYPE_SAUCE), get_name=Mock(return_value="hot sauce"))
        ]
        mock_database = Mock()
        mock_database.ingredients = mock_ingredients
        mock_database.available_ingredients.return_value = mock_ingredients
        mock_database_class.return_value = mock_database
        db = Database()
        result = db.available_ingredients()

        assert result[0].get_type() == INGREDIENT_TYPE_SAUCE
        assert result[0].get_name() == "hot sauce"
