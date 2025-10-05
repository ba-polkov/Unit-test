from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

class TestDatabase:
    def test_available_buns(self, database):
        buns = database.available_buns()
        assert len(buns) == 3
        assert all(isinstance(bun, Bun) for bun in buns)

    def test_available_ingredients(self, database):
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
