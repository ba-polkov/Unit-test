import pytest
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

TEST_INGREDIENTS_DATA = [
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    (INGREDIENT_TYPE_FILLING, "cutlet", 100)]

class TestForIngredient:

    @pytest.mark.parametrize('ingredient_type, name, price', TEST_INGREDIENTS_DATA)
    def test_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize('ingredient_type, name, price', TEST_INGREDIENTS_DATA)
    def test_get_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('ingredient_type, name, price', TEST_INGREDIENTS_DATA)
    def test_get_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price
