from unittest.mock import MagicMock
from praktikum.ingredient import Ingredient


class TestIngredient:
    def test_get_price(self):
        mock_ingredient = MagicMock(spec=Ingredient)
        mock_ingredient.get_price.return_value = 5.99

        assert mock_ingredient.get_price() == 5.99, f'Ожидалось, что цена будет 5.99, но получено {mock_ingredient.get_price()}'
