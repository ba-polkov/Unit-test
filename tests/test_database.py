import pytest
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    def test_get_available_buns(self):
        database = Database()
        available_buns = database.available_buns()
        assert len(available_buns) == 3

    def test_get_available_ingredients(self):
        database = Database()
        available_ingredients = database.available_ingredients()
        assert len(available_ingredients) == 6

    def test_get_quantity_available_sauces(self):
        database = Database()
        ingredients = database.available_ingredients()
        type_sauce = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE]
        assert len(type_sauce) == 3

    def test_get_quantity_available_fillings(self):
        database = Database()
        ingredients = database.available_ingredients()
        type_fillings = [
            i for i in ingredients if i.get_type() == INGREDIENT_TYPE_FILLING
        ]
        assert len(type_fillings) == 3

    def test_get_available_ingredients_prices(self):
        database = Database()
        ingredients = database.available_ingredients()
        price = {i.get_name(): i.get_price() for i in ingredients}
        assert price["hot sauce"] == 100
        assert price["sour cream"] == 200
        assert price["chili sauce"] == 300

    def test_get_available_buns_names(self):
        database = Database()
        buns = database.available_buns()
        names = [bun.get_name() for bun in buns]
        expected_names = ["black bun", "white bun", "red bun"]
        assert names == expected_names

    def test_get_available_buns_prices(self):
        database = Database()
        buns = database.available_buns()
        prices = [bun.get_price() for bun in buns]
        expected_prices = [100, 200, 300]
        assert prices == expected_prices

    def test_sauce_ingredients_types(self):
        database = Database()
        ingredients = database.available_ingredients()
        sauces = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE]

        for sauce in sauces:
            assert sauce.get_type() == INGREDIENT_TYPE_SAUCE

    def test_filling_ingredients_types(self):
        database = Database()
        ingredients = database.available_ingredients()
        fillings = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_FILLING]

        for filling in fillings:
            assert filling.get_type() == INGREDIENT_TYPE_FILLING

    def test_sauce_ingredients_names(self):
        database = Database()
        ingredients = database.available_ingredients()
        sauces = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE]
        sauce_names = [sauce.get_name() for sauce in sauces]
        expected_sauce_names = ["hot sauce", "sour cream", "chili sauce"]
        assert sauce_names == expected_sauce_names

    def test_filling_ingredients_names(self):
        database = Database()
        ingredients = database.available_ingredients()
        fillings = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_FILLING]
        filling_names = [filling.get_name() for filling in fillings]
        expected_filling_names = ["cutlet", "dinosaur", "sausage"]
        assert filling_names == expected_filling_names

    def test_database_structure(self):
        database = Database()

        buns = database.available_buns()
        assert len(buns) == 3

        ingredients = database.available_ingredients()
        assert len(ingredients) == 6

        sauces = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE]
        fillings = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(sauces) == 3
        assert len(fillings) == 3
