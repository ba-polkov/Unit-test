import pytest

import data
import ingredient_types
from praktikum.ingredient import Ingredient


class TestIngredient():

    @pytest.mark.parametrize(
       'type, name, price, is_param',
        [[ingredient_types.INGREDIENT_TYPE_SAUCE, data.DEF_INGREDIENT_NAME, data.DEF_INGREDIENT_PRICE, "name"],
         [ingredient_types.INGREDIENT_TYPE_SAUCE, data.DEF_INGREDIENT_NAME, data.DEF_INGREDIENT_PRICE, "type"],
         [ingredient_types.INGREDIENT_TYPE_SAUCE, data.DEF_INGREDIENT_NAME, data.DEF_INGREDIENT_PRICE, "price"]]
    )
    def test_get_mame_positive_value(self, mock_ingredient, type, name, price, is_param):
        testingredient = Ingredient(mock_ingredient.type, mock_ingredient.name, mock_ingredient.price)
        if is_param == "name":
            assert testingredient.get_name() == name, "name"
        elif is_param == "type":
            assert testingredient.get_type() == type, "type"
        else:
            assert testingredient.get_price() == price, "price"
