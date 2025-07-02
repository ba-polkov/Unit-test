import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

class TestIngredient:

    def test_get_price_success(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Sause", 30)
        assert ingredient.get_price() == 30


    def test_get_name_success(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Sause", 30)
        assert ingredient.get_name() == "Sause"
        

    @pytest.mark.parametrize(
        'ingredient_type, expected_type',
        [
            (INGREDIENT_TYPE_FILLING, "FILLING"),
            (INGREDIENT_TYPE_SAUCE, "SAUCE")
        ]
    )
    def test_get_type_success(self, ingredient_type, expected_type):
        ingredient = Ingredient(ingredient_type, "Sause", 30)
        assert ingredient.get_type() == expected_type


