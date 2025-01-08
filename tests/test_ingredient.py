import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    def test_get_price_get_right_price(self, mock_ingredients):
        assert mock_ingredients.get_price() == mock_ingredients.price

    def test_get_name_get_right_name(self, mock_ingredients):
        assert mock_ingredients.get_name() == mock_ingredients.name


    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            (INGREDIENT_TYPE_SAUCE, "имя_1", 100),
            (INGREDIENT_TYPE_FILLING, "имя_2", 200),
        ]
    )
    def test_get_type_get_right_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type



