from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
import pytest

class TestDatabase:

    def test_buns_are_loaded(self, db):
        buns = db.available_buns()
        assert len(buns) == 3
        assert all(isinstance(bun, Bun) for bun in buns)

    def test_ingredients_are_loaded(self, db):
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6
        assert all(isinstance(ing, Ingredient) for ing in ingredients)

    def test_sauce_ingredients_exist(self, db):
        sauces = [ing for ing in db.available_ingredients() if ing.get_type() == INGREDIENT_TYPE_SAUCE]
        assert len(sauces) == 3

    def test_filling_ingredients_exist(self, db):
        fillings = [ing for ing in db.available_ingredients() if ing.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(fillings) == 3
