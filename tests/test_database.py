import pytest
from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    def test_check_bun_list_length(self):
        database = Database()
        buns = database.available_buns()
        assert len(buns) == 3

    def test_check_bun_type_list(self):
        database = Database()
        buns = database.available_buns()
        assert isinstance(buns, list)

    def test_check_bun_object(self):
        database = Database()
        buns = database.available_buns()
        for bun in buns:
            assert isinstance(bun, Bun)

    @pytest.mark.parametrize("index, name", [
        (0, "black bun"),
        (1, "white bun"),
        (2, "red bun")
    ])
    def test_check_bun_name(self, index, name):
        database = Database()
        bun = database.available_buns()[index]
        assert isinstance(bun, Bun) and bun.get_name() == name

    @pytest.mark.parametrize("index, price", [
        (0, 100),
        (1, 200),
        (2, 300)
    ])
    def test_check_bun_price(self, index, price):
        database = Database()
        bun = database.available_buns()[index]
        assert isinstance(bun, Bun) and bun.get_price() == price

    def test_check_ingredients_list_length(self):
        database = Database()
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6

    def test_check_ingredients_type(self):
        database = Database()
        ingredients = database.available_ingredients()
        assert isinstance(ingredients, list)

    def test_check_ingredients_object(self):
        database = Database()
        ingredients = database.available_ingredients()
        for ingredient in ingredients:
            assert isinstance(ingredient, Ingredient)

    @pytest.mark.parametrize("index, expected_type", [
        (0, INGREDIENT_TYPE_SAUCE),
        (1, INGREDIENT_TYPE_SAUCE),
        (2, INGREDIENT_TYPE_SAUCE),
        (3, INGREDIENT_TYPE_FILLING),
        (4, INGREDIENT_TYPE_FILLING),
        (5, INGREDIENT_TYPE_FILLING)
    ])
    def test_check_ingredients_type_list(self, index, expected_type):
        database = Database()
        ingredient = database.available_ingredients()[index]
        assert isinstance(ingredient, Ingredient) and ingredient.get_type() == expected_type

    @pytest.mark.parametrize("index, expected_name", [
        (0, "hot sauce"),
        (1, "sour cream"),
        (2, "chili sauce"),
        (3, "cutlet"),
        (4, "dinosaur"),
        (5, "sausage")
    ])
    def test_check_ingredients_name(self, index, expected_name):
        database = Database()
        ingredient = database.available_ingredients()[index]
        assert isinstance(ingredient, Ingredient) and ingredient.get_name() == expected_name

    @pytest.mark.parametrize("index, expected_price", [
        (0, 100),
        (1, 200),
        (2, 300),
        (3, 100),
        (4, 200),
        (5, 300)
    ])
    def test_check_ingredients_price(self, index, expected_price):
        database = Database()
        ingredient = database.available_ingredients()[index]
        assert isinstance(ingredient, Ingredient) and ingredient.get_price() == expected_price
