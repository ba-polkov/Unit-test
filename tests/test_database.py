import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    def test_database_initialization(self):
        db = Database()
        assert len(db.buns) == 3
        assert len(db.ingredients) == 6

        assert isinstance(db.buns[0], Bun)
        assert db.buns[0].get_name() == "black bun"
        assert db.buns[0].get_price() == 100

        assert isinstance(db.ingredients[0], Ingredient)
        assert db.ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
        assert db.ingredients[0].get_name() == "hot sauce"
        assert db.ingredients[0].get_price() == 100

    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()

        assert len(buns) == 3
        assert all(isinstance(bun, Bun) for bun in buns)
        assert buns[0].get_name() == "black bun"
        assert buns[1].get_name() == "white bun"
        assert buns[2].get_name() == "red bun"

    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()

        assert len(ingredients) == 6
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)

        sauces = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE]
        assert len(sauces) == 3

        fillings = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(fillings) == 3