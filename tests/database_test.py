import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.database import Database


class TestDatabase:

    def test_available_buns(self):
        database = Database()
        expected_buns = [
            Bun("black bun", 100),
            Bun("white bun", 200),
            Bun("red bun", 300)
        ]
        actual_buns = database.available_buns()

        assert [(bun.get_name(), bun.get_price()) for bun in actual_buns] == [(bun.get_name(), bun.get_price()) for bun in expected_buns]

    def test_available_ingredients(self):
        database = Database()
        expected_ingredients = [
            Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
            Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)
        ]

        actual_ingredients = database.available_ingredients()

        assert [(ingredient.get_type(), ingredient.get_name(), ingredient.get_price()) for ingredient in
                actual_ingredients] == [
                   (ingredient.get_type(), ingredient.get_name(), ingredient.get_price()) for ingredient in
                   expected_ingredients
               ]


    @pytest.mark.parametrize("bun_name, expected_price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300)
    ])
    def test_bun_prices(self, bun_name, expected_price):
        database = Database()
        buns = database.available_buns()
        found_bun = None
        for bun in buns:
            if bun.get_name() == bun_name:
                found_bun = bun
                break
        assert found_bun is not None
        assert found_bun.get_price() == expected_price

    @pytest.mark.parametrize("ingredient_name, ingredient_type, expected_price", [
        ("hot sauce", INGREDIENT_TYPE_SAUCE, 100),
        ("sour cream", INGREDIENT_TYPE_SAUCE, 200),
        ("chili sauce", INGREDIENT_TYPE_SAUCE, 300),
        ("cutlet", INGREDIENT_TYPE_FILLING, 100),
        ("dinosaur", INGREDIENT_TYPE_FILLING, 200),
        ("sausage", INGREDIENT_TYPE_FILLING, 300)
    ])
    def test_ingredient_prices(self, ingredient_name, ingredient_type, expected_price):
        database = Database()
        ingredients = database.available_ingredients()
        found_ingredient = None
        for ingredient in ingredients:
            if ingredient.get_name() == ingredient_name and ingredient.get_type() == ingredient_type:
                found_ingredient = ingredient
                break
        assert found_ingredient is not None
        assert found_ingredient.get_price() == expected_price


