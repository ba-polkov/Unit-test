import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestIngredient:
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 50),
        (INGREDIENT_TYPE_FILLING, "cutlet", 60.5),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 20),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 30),
    ])
    def test_ingredient_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 50),
        (INGREDIENT_TYPE_FILLING, "cutlet", 60.5),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 20),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 30),
    ])
    def test_ingredient_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price
    @pytest.mark.parametrize("ingredient_type, name, price", [
        ("начинка", "Курица", 100.0),
        ("соус", "Майонез", 20.5),
        ("начинка", "Сыр", 50.0),
        ("соус", "Томатный", 30.0),
    ])
    def test_ingredient_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type