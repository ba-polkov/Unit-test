from conftest import *

class TestIngredient:
    def test_get_name(self):
        ingredient = Ingredient("FILLING", "cutlet", 100)
        assert ingredient.get_name() == "cutlet"

    def test_get_price(self):
        ingredient = Ingredient("SAUCE", "sour cream", 200)
        assert ingredient.get_price() == 200

    def test_get_type(self):
        ingredient = Ingredient("SAUCE", "hot sauce", 150)
        assert ingredient.get_type() == "SAUCE"