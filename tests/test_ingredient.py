import pytest
from praktikum.ingredient import Ingredient
from ingredient_types import *

from praktikum.database import *
from data import *


class TestIngredient:
    # проверяем соус и начинку

    @pytest.mark.parametrize(
        "expected_type,  expected_name, expected_price",
        [
            (INGREDIENT_TYPE_SAUCE, name_sause, price_sause),
            (INGREDIENT_TYPE_FILLING, name_filling, price_filling),
        ],
    )
    def test_ingredient_all_param(self, expected_type, expected_name, expected_price):
        ingredient = Ingredient(expected_type, expected_name, expected_price)
        assert (
            ingredient.get_name() == expected_name
            and ingredient.get_price() == expected_price
            and ingredient.get_type() == expected_type
        )
