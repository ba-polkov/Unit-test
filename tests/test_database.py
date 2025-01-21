import pytest

from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestDatabase:

    @pytest.mark.parametrize(
        'expected_bun',
        [
            'black bun',
            'white bun',
            'red bun'
        ])
    def test_available_buns_list(self, expected_bun):
        database = Database()
        buns = database.available_buns()
        available_buns_names = [bun.name for bun in buns]
        assert expected_bun in available_buns_names and all(
            isinstance(bun, Bun) for bun in buns), "Список доступных булок пуст"

    @pytest.mark.parametrize(
        'expected_ingredient',
        [
            'hot sauce',
            'sour cream',
            'chili sauce',
            'cutlet',
            'dinosaur',
            'sausage'

        ])
    def test_available_ingredients_list(self, expected_ingredient):
        database = Database()
        ingredients = database.available_ingredients()
        available_ingredients_names = [ingredient.name for ingredient in ingredients]
        assert expected_ingredient in available_ingredients_names and all(
            isinstance(ingredient, Ingredient) for ingredient in ingredients)

    def test_buns_initialization(self):
        database = Database()
        buns = database.buns
        assert len(buns) == 3 and all(isinstance(bun, Bun) for bun in buns)

    def test_ingredients_initialization(self):
        database = Database()
        ingredients = database.ingredients
        assert len(ingredients) == 6 and all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
