import pytest
from praktikum.database import Database
from praktikum.ingredient_types import *

class TestDatabase:
    
    def test_get_available_buns(self, database):
        available_buns = database.available_buns()
        assert len(available_buns) == 3

    def test_get_avaliable_ingredients(self, database):
        avaliable_ingredients = database.available_ingredients()
        assert len(avaliable_ingredients) == 6
