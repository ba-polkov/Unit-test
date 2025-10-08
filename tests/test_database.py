import pytest

from praktikum.database import Database
from data import DATABASE_DATA


class TestDatabase:

    def test_available_buns_total_len(self):
        database = Database()
        assert len(database.available_buns()) == DATABASE_DATA["test_available_buns_total_len"]

    @pytest.mark.parametrize("index, name, price", DATABASE_DATA["test_available_buns"])
    def test_available_buns(self, index, name, price):
        database = Database()

        av_buns = database.available_buns()

        assert av_buns[index].get_name() == name and av_buns[index].get_price() == price

    def test_available_ingredients_len(self):
        database = Database()
        assert len(database.available_ingredients()) == DATABASE_DATA["test_available_ingredients_len"]

    @pytest.mark.parametrize("index, type, name, price", DATABASE_DATA["test_available_ingredients"])
    def test_available_ingredients(self, index, type, name, price):
        database = Database()

        av_ingredients = database.available_ingredients()

        assert av_ingredients[index].get_type() == type
        assert av_ingredients[index].get_name() == name
        assert av_ingredients[index].get_price() == price
