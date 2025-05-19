from praktikum.burger import *
from conftest import *
from praktikum.database import Database

class TestDatabase:
    def setup_method(self):
        self.database = Database()

    def test_available_buns(self):
        buns = self.database.available_buns()
        assert isinstance(buns, list)
        assert all(isinstance(bun, Bun) for bun in buns)
        assert len(buns) == 3

    def test_available_ingredients(self):
        ingredients = self.database.available_ingredients()
        assert isinstance(ingredients, list)
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
        assert len(ingredients) == 6