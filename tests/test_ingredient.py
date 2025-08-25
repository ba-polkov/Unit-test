import random

from praktikum.ingredient import Ingredient
from praktikum import ingredient_types as types
from data_for_tests import constants as const


class TestIngredient:
    ingredient_types = [types.INGREDIENT_TYPE_SAUCE, types.INGREDIENT_TYPE_FILLING]

    def test_get_type(self):
        ingredient_type = random.choice(self.ingredient_types)
        ingredient = Ingredient(ingredient_type, random.choice(const.sauces),
                                random.uniform(const.min_sauces_price, const.max_sauces_price))
        assert ingredient.get_type() == ingredient_type

    def test_get_name(self):
        ingredient_name = random.choice(const.fillings)
        ingredient = Ingredient(random.choice(self.ingredient_types), ingredient_name,
                                random.uniform(const.min_filling_price, const.max_filling_price))
        assert ingredient.get_name() == ingredient_name

    def test_get_price(self):
        ingredient_price = random.uniform(1, 10000)
        ingredient = Ingredient(random.choice(self.ingredient_types), random.choice(const.sauces), ingredient_price)
        assert ingredient.get_price() == ingredient_price