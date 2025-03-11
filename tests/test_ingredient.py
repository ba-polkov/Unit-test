import pytest
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:

    @pytest.mark.parametrize(
        "ingredient_type, name, price, expected_type, expected_name, expected_price",
        [
            (INGREDIENT_TYPE_SAUCE, "Соус фирменный Space Sauce", 80, INGREDIENT_TYPE_SAUCE, "Соус фирменный Space Sauce", 80),
            (INGREDIENT_TYPE_FILLING, "Мини-салат Экзо-Плантаго", 4400, INGREDIENT_TYPE_FILLING, "Мини-салат Экзо-Плантаго", 4400),
        ]
    )
    def test_ingredient(self, ingredient_type, name, price, expected_type, expected_name, expected_price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == expected_type
        assert ingredient.get_name() == expected_name
        assert ingredient.get_price() == expected_price
