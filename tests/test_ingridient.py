import pytest
from praktikum.ingredient import Ingredient
from data import INGREDIENTS

@pytest.mark.parametrize("ingredient_data", INGREDIENTS)
class TestIngredient():
    def test_get_ingredient_type(self, ingredient_data):
        ing = Ingredient(ingredient_data["type"], ingredient_data["name"], ingredient_data["price"])

        assert ing.get_type() == ingredient_data["type"]

    def test_get_ingredient_name(self, ingredient_data):
        ing = Ingredient(ingredient_data["type"], ingredient_data["name"], ingredient_data["price"])

        assert ing.get_name() == ingredient_data["name"]

    def test_get_ingredient_price(self, ingredient_data):
        ing = Ingredient(ingredient_data["type"], ingredient_data["name"], ingredient_data["price"])

        assert ing.get_price() == ingredient_data["price"]
