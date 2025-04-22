from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
import pytest

class TestIngredient:
    def test_get_price(self, ingredient_sauce, ingredient_filling):
        assert ingredient_sauce.get_price() == 50
        assert ingredient_filling.get_price() == 75

    def test_get_name(self, ingredient_sauce, ingredient_filling):
        assert ingredient_sauce.get_name() == 'Соус'
        assert ingredient_filling.get_name() == 'Начинка'

    def test_get_type(self,ingredient_sauce, ingredient_filling):
        assert ingredient_sauce.get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredient_filling.get_type() == INGREDIENT_TYPE_FILLING

    @pytest.mark.parametrize("ingredient_type, name, price, expected_type, expected_name, expected_price", [
        (INGREDIENT_TYPE_SAUCE, 'Соус', 50, INGREDIENT_TYPE_SAUCE, 'Соус', 50),
        (INGREDIENT_TYPE_FILLING, 'Начинка', 75, INGREDIENT_TYPE_FILLING, 'Начинка', 75)
    ])
    def test_ingredient_initialization(self, ingredient_type, name, price, expected_type, expected_name, expected_price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == expected_type
        assert ingredient.get_name() == expected_name
        assert ingredient.get_price() == expected_price