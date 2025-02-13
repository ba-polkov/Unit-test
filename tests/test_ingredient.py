import pytest
from praktikum.ingredient import Ingredient

class TestIngredient:

    @pytest.mark.parametrize("ingredient_type", ["filling", "sauce"])
    def test_get_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, "Тестовый ингредиент", 100)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize("name", ["Говяжий метеорит (отбивная)", "Соус фирменный Space Sauce"])
    def test_get_name(self, name):
        ingredient = Ingredient("filling", name, 100)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("price", [3000, 90])
    def test_get_price(self, price):
        ingredient = Ingredient("filling", "Тестовый ингредиент", price)
        assert ingredient.get_price() == price