import pytest
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:


    def test_database_initialization_bun_count(self):

        db = Database()
        assert len(db.buns) == 3

    def test_database_initialization_ingredient_count(self):

        db = Database()
        assert len(db.ingredients) == 6

    @pytest.mark.parametrize("index, name, price", [
        (0, "black bun", 100),
        (1, "white bun", 200),
        (2, "red bun", 300)
    ])
    def test_database_initialization_bun_properties(self, index, name, price):

        db = Database()
        assert db.buns[index].get_name() == name
        assert db.buns[index].get_price() == price

    @pytest.mark.parametrize("index, ing_type, name, price", [
        (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (5, INGREDIENT_TYPE_FILLING, "sausage", 300)
    ])
    def test_database_initialization_ingredient_properties(self, index, ing_type, name, price):

        db = Database()
        assert db.ingredients[index].get_type() == ing_type
        assert db.ingredients[index].get_name() == name
        assert db.ingredients[index].get_price() == price

    def test_available_buns_count(self):

        db = Database()
        assert len(db.available_buns()) == 3

    @pytest.mark.parametrize("index, name, price", [
        (0, "black bun", 100),
        (1, "white bun", 200),
        (2, "red bun", 300)
    ])
    def test_available_buns_properties(self, index, name, price):

        db = Database()
        buns = db.available_buns()
        assert buns[index].get_name() == name
        assert buns[index].get_price() == price

    def test_available_ingredients_count(self):
        db = Database()
        assert len(db.available_ingredients()) == 6

    @pytest.mark.parametrize("index, ing_type, name, price", [
        (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (5, INGREDIENT_TYPE_FILLING, "sausage", 300)
    ])
    def test_available_ingredients_properties(self, index, ing_type, name, price):
        db = Database()
        ingredients = db.available_ingredients()
        assert ingredients[index].get_type() == ing_type
        assert ingredients[index].get_name() == name
        assert ingredients[index].get_price() == price