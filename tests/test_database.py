import pytest

from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    @pytest.mark.parametrize(
        "index,expected_name",
        [
            (0, "black bun"),
            (1, "white bun"),
            (2, "red bun"),
        ]
    )
    def test_database_bun_names(self, index, expected_name):
        db = Database()
        assert db.available_buns()[index].get_name() == expected_name

    @pytest.mark.parametrize(
        "index,expected_price",
        [
            (0, 100),
            (1, 200),
            (2, 300),
        ]
    )
    def test_database_bun_prices(self, index, expected_price):
        db = Database()
        assert db.available_buns()[index].get_price() == expected_price

    @pytest.mark.parametrize(
        "index,expected_type",
        [
            (0, INGREDIENT_TYPE_SAUCE),
            (1, INGREDIENT_TYPE_SAUCE),
            (2, INGREDIENT_TYPE_SAUCE),
            (3, INGREDIENT_TYPE_FILLING),
            (4, INGREDIENT_TYPE_FILLING),
            (5, INGREDIENT_TYPE_FILLING),
        ]
    )
    def test_database_ingredient_types(self, index, expected_type):
        db = Database()
        assert db.available_ingredients()[index].get_type() == expected_type

    @pytest.mark.parametrize(
        "index,expected_name",
        [
            (0, "hot sauce"),
            (1, "sour cream"),
            (2, "chili sauce"),
            (3, "cutlet"),
            (4, "dinosaur"),
            (5, "sausage"),
        ]
    )
    def test_database_ingredient_names(self, index, expected_name):
        db = Database()
        assert db.available_ingredients()[index].get_name() == expected_name

    @pytest.mark.parametrize(
        "index,expected_price",
        [
            (0, 100),
            (1, 200),
            (2, 300),
            (3, 100),
            (4, 200),
            (5, 300),
        ]
    )
    def test_database_ingredient_prices(self, index, expected_price):
        db = Database()
        assert db.available_ingredients()[index].get_price() == expected_price

    def test_database_available_buns_returns_buns(self):
        db = Database()
        assert db.available_buns() == db.buns

    def test_database_available_ingredients_returns_ingredients(self):
        db = Database()
        assert db.available_ingredients() == db.ingredients
