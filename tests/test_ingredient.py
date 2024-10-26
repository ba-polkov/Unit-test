from unittest.mock import Mock

from data import Data
from yandex import ingredient_types
from yandex.ingredient import Ingredient


class TestIngredient:

    def test_create_ingredient(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, Data.NAME_INGREDIENT_3,
                                Data.PRICE_INGREDIENT_3)

        assert (ingredient.type == ingredient_types.INGREDIENT_TYPE_FILLING and ingredient.name ==
                Data.NAME_INGREDIENT_3 and ingredient.price == Data.PRICE_INGREDIENT_3)

    def test_get_ingredient_price(self):
        mock_ingredient_price = Mock()
        mock_ingredient_price.configure_mock(price=30)

        assert Ingredient.get_price(mock_ingredient_price) == 30

    def test_get_ingredient_name(self):
        mock_ingredient_name = Mock()
        mock_ingredient_name.configure_mock(name='Тестовый ингредиент')

        assert Ingredient.get_name(mock_ingredient_name) == 'Тестовый ингредиент'

    def test_get_ingredient_type(self):
        mock_ingredient_type = Mock()
        mock_ingredient_type.configure_mock(type=ingredient_types.INGREDIENT_TYPE_SAUCE)

        assert Ingredient.get_type(mock_ingredient_type) == 'SAUCE'