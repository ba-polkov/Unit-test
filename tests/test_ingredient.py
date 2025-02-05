from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import INGREDIENT_DATA, INGREDIENT_NAMES, SAUCE_NAMES, FILLING_NAMES
import pytest

class TestIngredient:
    @pytest.mark.parametrize("ingredient_name", INGREDIENT_NAMES)
    def test_ingredient_creation_and_attributes(self, ingredient_name):
        ingredient = Ingredient(
            INGREDIENT_DATA[ingredient_name]["type"],
            ingredient_name,
            INGREDIENT_DATA[ingredient_name]["price"]
        )
        assert ingredient.get_type() == INGREDIENT_DATA[ingredient_name]["type"]
        assert ingredient.get_name() == ingredient_name
        assert ingredient.get_price() == INGREDIENT_DATA[ingredient_name]["price"]

    @pytest.mark.parametrize("ingredient_name", INGREDIENT_NAMES)
    def test_ingredient_get_price(self, ingredient_name):
        ingredient = Ingredient(
            INGREDIENT_DATA[ingredient_name]["type"],
            ingredient_name,
            INGREDIENT_DATA[ingredient_name]["price"]
        )
        assert ingredient.get_price() == INGREDIENT_DATA[ingredient_name]["price"]

    @pytest.mark.parametrize("ingredient_name", INGREDIENT_NAMES)
    def test_ingredient_get_name(self, ingredient_name):
        ingredient = Ingredient(
            INGREDIENT_DATA[ingredient_name]["type"],
            ingredient_name,
            INGREDIENT_DATA[ingredient_name]["price"]
        )
        assert ingredient.get_name() == ingredient_name

    @pytest.mark.parametrize("ingredient_name", SAUCE_NAMES)
    def test_ingredient_get_type_sauce(self, ingredient_name):
        ingredient = Ingredient(
            INGREDIENT_DATA[ingredient_name]["type"],
            ingredient_name,
            INGREDIENT_DATA[ingredient_name]["price"]
        )
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE

    @pytest.mark.parametrize("ingredient_name", FILLING_NAMES)
    def test_ingredient_get_type_filling(self, ingredient_name):
        ingredient = Ingredient(
            INGREDIENT_DATA[ingredient_name]["type"],
            ingredient_name,
            INGREDIENT_DATA[ingredient_name]["price"]
        )
        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING