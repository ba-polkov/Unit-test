import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 49.99),
        (INGREDIENT_TYPE_FILLING, "sausage", 399.99)
    ])
    def test_init_method_true(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.type == ingredient_type
        assert ingredient.name == name
        assert ingredient.price == price


    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 49.99)
        assert ingredient.get_price() == 49.99
        assert isinstance(ingredient.get_price(), float)


    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 399.99)
        assert ingredient.get_name() == "sausage"
        assert isinstance(ingredient.get_name(), str)


    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 49.99),
        (INGREDIENT_TYPE_FILLING, "sausage", 399.99)
    ])
    def test_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
        assert isinstance(ingredient.get_type(), str)
