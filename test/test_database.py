from praktikum.burger import *
from conftest import *
from praktikum.database import Database

class TestDatabase:
    def setup_method(self):
        self.database = Database()

    def test_available_buns_is_list(self):
        buns = self.database.available_buns()
        assert isinstance(buns, list)

    def test_available_buns_has_expected_length(self):
        buns = self.database.available_buns()
        assert len(buns) == 3

    def test_available_buns_are_bun_instances(self):
        buns = self.database.available_buns()
        assert all(isinstance(bun, Bun) for bun in buns)

    def test_available_ingredients_is_list(self):
        ingredients = self.database.available_ingredients()
        assert isinstance(ingredients, list)

    def test_available_ingredients_has_expected_length(self):
        ingredients = self.database.available_ingredients()
        assert len(ingredients) == 6

    def test_available_ingredients_are_ingredient_instances(self):
        ingredients = self.database.available_ingredients()
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
