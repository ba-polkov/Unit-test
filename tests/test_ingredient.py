from unittest.mock import MagicMock
from praktikum.ingredient import Ingredient


class TestIngredient:
    def test_get_price_return_price(self):
        mock_ingredient = MagicMock(spec=Ingredient)
        mock_ingredient.get_price.return_value = 5.99

        assert mock_ingredient.get_price() == 5.99, f'Ожидалось, что цена будет 5.99, но получено {mock_ingredient.get_price()}'

    def test_get_price_zero_price(self):
        mock_ingredient = MagicMock(spec=Ingredient)

        # Устанавливаем цену 0
        mock_ingredient.get_price.return_value = 0.0

        # Проверка, что метод возвращает 0.0
        assert mock_ingredient.get_price() == 0.0, f'Ожидалось, что цена будет 0.0, но получено {mock_ingredient.get_price()}'

    def test_get_name_return_name(self):
        mock_ingredient = MagicMock(spec=Ingredient)
        mock_ingredient.get_name.return_value = 'Кетчуп'

        assert mock_ingredient.get_name() == 'Кетчуп', f'Ожидалось, что название будет "Кетчуп", но получено {mock_ingredient.get_name()}'

    def test_get_type_return_type(self):
        mock_ingredient = MagicMock(spec=Ingredient)
        mock_ingredient.get_type.return_value = 'Соус'

        assert mock_ingredient.get_type() == 'Соус', f'Ожидалось, что тип будет "Соус", но получено {mock_ingredient.get_type()}'
