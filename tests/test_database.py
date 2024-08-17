import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    @pytest.mark.parametrize("type_of_bun, price", [["черная булочка", 100], ["белая булочка", 200], ["красная булочка", 300]])
    def test_available_buns_true(self, type_of_bun, price):
        bun = Bun(type_of_bun, price)
        database = Database()
        database.buns.append(bun)
        assert bun in database.available_buns()


    @pytest.mark.parametrize("ingredient_type, name, amount", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (INGREDIENT_TYPE_FILLING, "sausage", 300)
    ])
    def test_available_ingredients(self, ingredient_type, name, amount):
        ingredient = Ingredient(ingredient_type, name, amount)
        database = Database()
        database.ingredients.append(ingredient)
        assert ingredient in database.available_ingredients()
