import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:
    # Проверка корректного сохранения типа ингредиента
    @pytest.mark.parametrize("type, name, price",
                             [(INGREDIENT_TYPE_SAUCE, "hot sauce", 100), (INGREDIENT_TYPE_FILLING, "cutlet", 100), ], )
    def test_ingredient_get_type(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == type

    # Проверка корректного сохранения имени ингредиента
    @pytest.mark.parametrize("type, name, price",
                             [(INGREDIENT_TYPE_SAUCE, "hot sauce", 100), (INGREDIENT_TYPE_FILLING, "cutlet", 100), ], )
    def test_ingredient_get_name(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_name() == name

    # Проверка корректного сохранения цены ингредиента
    @pytest.mark.parametrize("type, name, price",
                             [(INGREDIENT_TYPE_SAUCE, "hot sauce", 100), (INGREDIENT_TYPE_FILLING, "cutlet", 100), ], )
    def test_ingredient_get_price(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_price() == price
