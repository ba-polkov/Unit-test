from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
import pytest

class TestDatabase:
    def test_available_buns_returns_list(self, database_instance):
        buns = database_instance.available_buns()
        assert isinstance(buns, list)

    def test_available_buns_list_not_empty(self, database_instance):
        buns = database_instance.available_buns()
        assert len(buns) > 0

    def test_available_buns_contains_bun_objects(self, database_instance):
        buns = database_instance.available_buns()
        assert all(isinstance(bun, Bun) for bun in buns)

    def test_available_ingredients_returns_list(self, database_instance):
        ingredients = database_instance.available_ingredients()
        assert isinstance(ingredients, list)

    def test_available_ingredients_list_not_empty(self, database_instance):
        ingredients = database_instance.available_ingredients()
        assert len(ingredients) > 0

    def test_available_ingredients_contains_ingredient_objects(self, database_instance):
        ingredients = database_instance.available_ingredients()
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
