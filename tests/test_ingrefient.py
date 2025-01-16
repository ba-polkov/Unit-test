import data as dt
from praktikum.ingredient import Ingredient

class TestIngredient:
    def test_get_type_ingredient(self):
        ingredient = Ingredient(dt.ingredients[1][0],
                                dt.ingredients[3][1],
                                dt.ingredients[5][2])

        assert ingredient.get_type() == dt.ingredients[1][0]

    def test_get_name_indrefient(self):
        ingredient = Ingredient(dt.ingredients[1][0],
                                dt.ingredients[3][1],
                                dt.ingredients[5][2])

        assert ingredient.get_name() == dt.ingredients[3][1]

    def test_get_price_ingredient(self):
        ingredient = Ingredient(dt.ingredients[1][0],
                                dt.ingredients[3][1],
                                dt.ingredients[5][2])

        assert ingredient.get_price() == dt.ingredients[5][2]