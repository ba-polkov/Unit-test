from praktikum.bun import Bun
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from unittest.mock import Mock, patch


class TestDatabase:

    @patch('praktikum.database.Database.available_buns')
    def test_available_buns(self, mock_available_buns):
        database = Database()
        bun_white = Bun("white bun", 200)
        bun_red = Bun("red bun", 300)
        mock_available_buns.return_value = [bun_white, bun_red]
        buns = database.available_buns()
        assert bun_white in buns and bun_red in buns

    @patch('praktikum.database.Database.available_ingredients')
    def test_available_ingredients(self, mock_available_ingredients):
        database = Database()
        sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300)
        filling = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)
        mock_available_ingredients.return_value = [sauce, filling]
        ingredients = database.available_ingredients()
        assert sauce in ingredients and filling in ingredients
