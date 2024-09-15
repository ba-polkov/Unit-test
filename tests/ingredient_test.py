from praktikum.ingredient import Ingredient



class TestIngredient:

    def test_get_price(self):
        ingredient = Ingredient("соус", "горчица", 15)
        assert ingredient.get_price() == 15

    def test_get_name(self):
        ingredient = Ingredient("соус", "горчица", 15)
        assert ingredient.get_name() == "горчица"

    def test_get_type(self):
        ingredient = Ingredient("соус", "горчица", 15)
        assert ingredient.get_type() == "соус"
