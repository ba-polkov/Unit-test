import pytest

from praktikum.database import Database


@pytest.mark.databases
class TestDatabase:

    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3

    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6

    def test_quantity_available_sauces(self):
        data_buns = Database()
        ingredients = data_buns.available_ingredients()
        sauces = []
        for i in ingredients:
            if i.type == 'SAUCE':
                sauces.append(i)
        assert len(sauces) == 3

    def test_quantity_available_fillings(self):
        data_buns = Database()
        ingredients = data_buns.available_ingredients()
        fillings = []
        for i in ingredients:
            if i.type == 'FILLING':
                fillings.append(i)
        assert len(fillings) == 3