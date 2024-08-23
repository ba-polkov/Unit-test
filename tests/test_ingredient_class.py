from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.ingredient import Ingredient


class TestIngredient:
    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE,'Соус', 84)
        assert ingredient.get_price() == 84

    def test_get_name(self):
        name = Ingredient(INGREDIENT_TYPE_FILLING,'Начинка', 65)
        assert name.get_name() == 'Начинка'

    def test_get_type(self):
        type_ingredient = Ingredient(INGREDIENT_TYPE_FILLING, 'Соучинка', 54)
        assert type_ingredient.get_type() == INGREDIENT_TYPE_FILLING
