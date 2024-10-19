import pytest
from ya_praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:

    @pytest.mark.parametrize('ingredient, expected_type, expected_name, expected_price', [
        ('sauce', INGREDIENT_TYPE_SAUCE, 'hot sauce', 100),
        ('filling', INGREDIENT_TYPE_FILLING, 'cutlet', 100)
    ])
    def test_ingredient_properties(self, request, ingredient, expected_type, expected_name, expected_price):
        ingredient_instance = request.getfixturevalue(ingredient)
        assert ingredient_instance.get_type() == expected_type
        assert ingredient_instance.get_name() == expected_name
        assert ingredient_instance.get_price() == expected_price