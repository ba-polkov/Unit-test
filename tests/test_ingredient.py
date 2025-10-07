from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestIngredient:

    def test_get_name(self):
        ingredient_name = 'Соус Джо'
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, ingredient_name, 1.50)
        assert ingredient_name == ingredient.get_name()

    def test_get_price(self):
        ingredient_price = 10.75
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, 'Рыба Йоу', ingredient_price)
        assert ingredient_price == ingredient.get_price()

    def test_get_type(self):
        ingredient_type = INGREDIENT_TYPE_FILLING
        ingredient = Ingredient(ingredient_type, 'Салат Айс', 0.45)
        assert ingredient_type == ingredient.get_type()
