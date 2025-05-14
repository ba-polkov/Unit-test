import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.mark.ingredients
class TestIngredient:
    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            ('SAUCE', 'Сок лимона', 20),
            ('FILLING', 'Фирменный ', 40)
        ]
    )
    def test_get_type(self, ingredient_type, name, price):
        ingredient =Ingredient(ingredient_type, name, price)
        assert ingredient.get_type()  == INGREDIENT_TYPE_SAUCE or INGREDIENT_TYPE_FILLING

    def test_name_ingredient(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Сок лимона', 20)
        assert ingredient.get_name() == 'Сок лимона'

    def test_price_ingredient(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Сок лимона', 20)
        assert ingredient.get_price() == 20

