import pytest
from database import  Database
from data import Data


class TestDatabase:

    def test_available_buns(self):
        database = Database()
        list_buns = database.available_buns()
        available_names = ["black bun", "white bun","red bun"]
        assert [bun.get_name() for bun in list_buns] == available_names

    def test_available_ingredients(self):
        database = Database()
        list_ingredients = database.available_ingredients()
        available_names = ["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"]
        assert [ingredient.get_name() for ingredient in list_ingredients] == available_names