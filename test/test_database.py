from database import Database
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    def test_add_buns(self):
        db = Database()

        expected_count = 3
        actual_count = len(db.buns)
        assert actual_count == expected_count

        names = [bun.name for bun in db.buns]
        expected_names = ["black bun", "white bun", "red bun"]
        assert names == expected_names

    def test_add_ingredients(self):
        db = Database()

        expected_count = 6
        actual_count = len(db.ingredients)
        assert actual_count == expected_count

        sauce_ingredients = [ingredient for ingredient in db.ingredients if ingredient.type == INGREDIENT_TYPE_SAUCE]
        filling_ingredients = [ingredient for ingredient in db.ingredients if
                               ingredient.type == INGREDIENT_TYPE_FILLING]

        assert len(sauce_ingredients) == 3
        assert len(filling_ingredients) == 3

    def test_get_all_ingredients(self):
        db = Database()

        count = len(db.ingredients)
        assert count == 6


    def test_available_ingredients(self):
        db = Database()

        ingredients = db.available_ingredients()

        expected_count = 6
        actual_count = len(ingredients)
        assert actual_count == expected_count

        sauce_ingredients = [ingredient for ingredient in ingredients if ingredient.type == INGREDIENT_TYPE_SAUCE]
        filling_ingredients = [ingredient for ingredient in ingredients if ingredient.type == INGREDIENT_TYPE_FILLING]

        assert len(sauce_ingredients) == 3
        assert len(filling_ingredients) == 3
