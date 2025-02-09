from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    def test_get_name_shows_correct_ingredient_name(self):
        ingr = Ingredient(INGREDIENT_TYPE_SAUCE, "cosmic_soy", 99)
        result = ingr.get_name()
        print(result)
        assert result == "cosmic_soy"

    def test_get_price_shows_correct_ingredient_price(self):
        ingr = Ingredient(INGREDIENT_TYPE_SAUCE, "cosmic_soy", 99)
        result = ingr.get_price()
        print(result)
        assert result == 99

    def test_get_type_shows_correct_type(self):
        ingr = Ingredient(INGREDIENT_TYPE_FILLING, 'vegan_cutlet', 999)
        result = ingr.get_type()
        print(result)
        assert result == 'FILLING'