import pytest

from Diplom_1.data import IngredientData
from Diplom_1.praktikum.ingredient import Ingredient


# Тестирование класса Bun
class TestIngredient:
    @pytest.mark.parametrize("ingredient_type", IngredientData.INGREDIENT_TYPES)
    def test_ingredient_types(self, ingredient_type):
        index = IngredientData.INGREDIENT_TYPES.index(ingredient_type)
        ingredient = Ingredient(ingredient_type, IngredientData.INGREDIENT_NAMES[index],
                                IngredientData.INGREDIENT_PRICES[index])

        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize("name", IngredientData.INGREDIENT_NAMES)
    def test_ingredient_names(self, name):
        index = IngredientData.INGREDIENT_NAMES.index(name)
        ingredient = Ingredient(IngredientData.INGREDIENT_TYPES[index], name, IngredientData.INGREDIENT_PRICES[index])

        assert ingredient.get_name() == name

    @pytest.mark.parametrize("price", IngredientData.INGREDIENT_PRICES)
    def test_ingredient_prices(self, price):
        index = IngredientData.INGREDIENT_PRICES.index(price)
        ingredient = Ingredient(IngredientData.INGREDIENT_TYPES[index], IngredientData.INGREDIENT_NAMES[index], price)

        assert ingredient.get_price() == price