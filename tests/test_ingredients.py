from praktikum.ingredient import Ingredient
from data import INGREDIENTS_DATA


class TestIngredients:

    def test_ingredients_type(self):
        ingredient_type, name, price = INGREDIENTS_DATA["test_ingredients_type"]
        ingredient = Ingredient(ingredient_type=ingredient_type, name=name, price=price)
        assert ingredient.get_type() == ingredient_type

    def test_ingredients_name(self):
        ingredient_type, name, price = INGREDIENTS_DATA["test_ingredients_name"]
        ingredient = Ingredient(ingredient_type=ingredient_type, name=name, price=price)
        assert ingredient.get_name() == name

    def test_ingredients_price_positive(self):
        ingredient_type, name, price = INGREDIENTS_DATA["test_ingredients_price_positive"]
        ingredient = Ingredient(ingredient_type=ingredient_type, name=name, price=price)
        assert ingredient.get_price() == price

    def test_ingredients_price_float(self):
        ingredient_type, name, price = INGREDIENTS_DATA["test_ingredients_price_float"]
        ingredient = Ingredient(ingredient_type=ingredient_type, name=name, price=price)
        assert ingredient.get_price() == price
