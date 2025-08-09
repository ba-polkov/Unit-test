import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:
        
    @pytest.mark.parametrize("ingredient_type, expected_type", [
    (INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_SAUCE),
    (INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_FILLING),
    ("UNKNOWN", "UNKNOWN")
    ])
    def test_ingredient_get_type(self, ingredient_type, expected_type):
        """
        Проверяет корректность работы метода get_type()
        """
        ingredient = Ingredient(ingredient_type, "test", 100)
        assert ingredient.get_type() == expected_type


    @pytest.mark.parametrize("name", [
        "hot sauce",
        "sour cream",
        "chili sauce",
        "cutlet",
        "dinosaur",
        "sausage",
        "mystery",
        ""
    ])
    def test_ingredient_get_name(self, name):
        """
        Проверяет корректность работы метода get_name()
        """
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, 100)
        assert ingredient.get_name() == name


    @pytest.mark.parametrize("price", [
        0,
        100,
        200,
        300,
        999.99,
        -50
    ])
    def test_ingredient_get_price(self, price):
        """
        Проверяет корректность работы метода get_price()
        """
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "test", price)
        assert ingredient.get_price() == pytest.approx(price, 0.01)