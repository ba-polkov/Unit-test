import pytest

from praktikum.ingredient import Ingredient

from data.burger_data import IngredientsData as ingredients


class TestIngredient:

    @pytest.mark.parametrize(('ingredient_type, name, price'),
                             [ingredients.SAUCE_1, ingredients.SAUCE_2,
                              ingredients.FILLING_1, ingredients.FILLING_2])
    def test_ingredient_attributes(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.name == name
        assert ingredient.price == price
        assert ingredient.type == ingredient_type

    @pytest.mark.parametrize(('ingredient_type, name, price'),
                             [ingredients.SAUCE_1, ingredients.SAUCE_2,
                              ingredients.FILLING_1, ingredients.FILLING_2])
    def test_ingredient_get_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price


    @pytest.mark.parametrize(('ingredient_type, name, price'),
                         [ingredients.SAUCE_1, ingredients.SAUCE_2,
                          ingredients.FILLING_1, ingredients.FILLING_2])
    def test_ingredient_get_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize(('ingredient_type, name, price'),
                             [ingredients.SAUCE_1, ingredients.SAUCE_2,
                              ingredients.FILLING_1, ingredients.FILLING_2])
    def test_ingredient_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
