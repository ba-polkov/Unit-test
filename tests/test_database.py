import pytest
from database import Database
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:
    def test_available_buns(self, db):
        buns = db.available_buns()
        assert len(buns) == 3

    def test_available_buns_names(self, db):
        buns = db.available_buns()
        expected_names = ["black bun", "white bun", "red bun"]
        actual_names = [bun.name for bun in buns]
        assert actual_names == expected_names

    def test_available_buns_prices(self, db):
        buns = db.available_buns()
        expected_prices = [100, 200, 300]
        actual_prices = [bun.price for bun in buns]
        assert actual_prices == expected_prices


    def test_available_ingredients(self, db):
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6

    def test_available_ingredients_names(self, db):
        ingredients = db.available_ingredients()
        expected_names = ["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"]
        actual_names = [ingredient.name for ingredient in ingredients]
        assert actual_names == expected_names

    def test_available_ingredients_prices(self, db):
        ingredients = db.available_ingredients()
        expected_prices = [100, 200, 300, 100, 200, 300]
        actual_prices = [ingredient.price for ingredient in ingredients]
        assert actual_prices == expected_prices

    def test_available_ingredients_types(self, db):
        types = db.available_ingredients()
        expected_types = [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_FILLING]
        actual_types = [type.type for type in types]
        assert actual_types == expected_types
