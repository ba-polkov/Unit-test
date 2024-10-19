import pytest
from praktikum.ingredient import Ingredient
from data import Ingredients

class TestIngredient:

    @pytest.mark.parametrize('ingredient_type, name, price',
                             [
                                 (Ingredients.ingredient_type_1, Ingredients.ingredient_name_1, Ingredients.ingredient_price_1),
                                 (Ingredients.ingredient_type_1, Ingredients.ingredient_name_2, Ingredients.ingredient_price_2),
                                 (Ingredients.ingredient_type_2, Ingredients.ingredient_name_3, Ingredients.ingredient_price_3),
                                 (Ingredients.ingredient_type_2, Ingredients.ingredient_name_4, Ingredients.ingredient_price_4)
                             ]
                            )
    def test_get_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('ingredient_type, name, price',
                             [
                                 (Ingredients.ingredient_type_1, Ingredients.ingredient_name_1, Ingredients.ingredient_price_1),
                                 (Ingredients.ingredient_type_1, Ingredients.ingredient_name_2, Ingredients.ingredient_price_2),
                                 (Ingredients.ingredient_type_2, Ingredients.ingredient_name_3, Ingredients.ingredient_price_3),
                                 (Ingredients.ingredient_type_2, Ingredients.ingredient_name_4, Ingredients.ingredient_price_4)
                             ]
                            )
    def test_get_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize('ingredient_type, name, price',
                             [
                                 (Ingredients.ingredient_type_1, Ingredients.ingredient_name_1, Ingredients.ingredient_price_1),
                                 (Ingredients.ingredient_type_1, Ingredients.ingredient_name_2, Ingredients.ingredient_price_2),
                                 (Ingredients.ingredient_type_2, Ingredients.ingredient_name_3, Ingredients.ingredient_price_3),
                                 (Ingredients.ingredient_type_2, Ingredients.ingredient_name_4, Ingredients.ingredient_price_4)
                             ]
                            )
    def test_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

