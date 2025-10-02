import pytest
from praktikum.ingredient import Ingredient
from tests.data import TestData


class TestIngredient:

    @pytest.mark.parametrize("ingredient_type, name, price", TestData.ingredients)
    def test_get_type(self, ingredient_type, name, price):

        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize("ingredient_type, name, price", TestData.ingredients)
    def test_get_price(self, ingredient_type, name, price):

        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize("ingredient_type, name, price", TestData.ingredients)
    def test_get_name(self, ingredient_type, name, price):

        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    def test_ingredient_initialization(self):

        ingredient_type = "SAUCE"
        name = "Тестовый соус"
        price = 150

        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.type == ingredient_type
        assert ingredient.name == name
        assert ingredient.price == price
