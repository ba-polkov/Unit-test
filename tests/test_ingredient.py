import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:

    # Тест на получение цен на ингредиент
    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90)
        assert ingredient.get_price() == 90

    # Тест на получение наименования ингредиент
    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90)
        assert ingredient.get_name() == 'Соус Spicy-X'

    # Тест на получение типа ингредиент
    @pytest.mark.parametrize(
        'ingredient_type,name,price',[
            (INGREDIENT_TYPE_FILLING, 'Мясо бессмертных моллюсков Protostomia', 1337),
            (INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90)
            ])
    def test_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type