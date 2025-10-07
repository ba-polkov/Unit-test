from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestDatabase:
    def test_available_buns_returns_three_items(self):
        database = Database()
        assert len(database.available_buns()) == 3

    def test_first_bun_has_correct_name(self):
        database = Database()
        assert database.available_buns()[0].get_name() == "black bun"

    def test_second_bun_has_correct_price(self):
        database = Database()
        assert database.available_buns()[1].get_price() == 200

    def test_available_ingredients_returns_six_items(self):
        database = Database()
        assert len(database.available_ingredients()) == 6

    def test_first_ingredient_has_sauce_type(self):
        database = Database()
        assert database.available_ingredients()[0].get_type() == INGREDIENT_TYPE_SAUCE

    def test_fourth_ingredient_has_correct_name(self):
        database = Database()
        assert database.available_ingredients()[3].get_name() == "cutlet"
