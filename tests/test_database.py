from praktikum.database import Database
import pytest


class TestDatabase:

    @pytest.mark.parametrize('index, bun_name, bun_price,', [[0, "black bun", 100], [1, "white bun", 200], [2, "red bun", 300]])
    def test_init_buns_list(self, index, bun_name, bun_price):
        database = Database()
        buns = database.buns
        assert buns[index].name == bun_name and buns[index].price == bun_price

    @pytest.mark.parametrize('index, ing_type, ing_name, ing_price', [[0, 'SAUCE', "hot sauce", 100], [1, 'SAUCE', "sour cream", 200],
        [2, 'SAUCE', "chili sauce", 300], [3, 'FILLING', "cutlet", 100], [4, 'FILLING', "dinosaur", 200], [5, 'FILLING', "sausage", 300]])
    def test_init_ingredients_list(self, index, ing_type, ing_name, ing_price):
        database = Database()
        ingredients = database.ingredients
        assert ingredients[index].type == ing_type and ingredients[index].name == ing_name and ingredients[index].price == ing_price

    def test_available_buns(self):
        database = Database()
        assert len(database.available_buns()) == 3

    def test_available_ingredients(self):
        database = Database()
        assert len(database.available_ingredients()) == 6
