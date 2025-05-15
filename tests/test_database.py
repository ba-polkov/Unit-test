
from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    expected_buns = [{"name": "black bun", "price": 100},
                     {"name": "white bun", "price": 200},
                     {"name": "red bun", "price": 300}]

    expected_ingredients = [{"type": INGREDIENT_TYPE_SAUCE, "name": "hot sauce", "price": 100},
                            {"type": INGREDIENT_TYPE_SAUCE, "name": "sour cream", "price": 200},
                            {"type": INGREDIENT_TYPE_SAUCE, "name": "chili sauce", "price": 300},
                            {"type": INGREDIENT_TYPE_FILLING, "name": "cutlet", "price": 100},
                            {"type": INGREDIENT_TYPE_FILLING, "name": "dinosaur", "price": 200},
                            {"type": INGREDIENT_TYPE_FILLING, "name": "sausage", "price": 300},]

    def test_buns_list_created(self):
        database = Database()

        actual_list = database.buns
        actual_values = [{"name": bun.name, "price": bun.price} for bun in actual_list]

        assert type(actual_list) == list
        assert actual_values == self.expected_buns
        assert all(type(bun) == Bun for bun in actual_list)

    def test_ingredients_list_created(self):
        database = Database()

        actual_list = database.ingredients
        actual_values = [{"type": ingredient.type, "name": ingredient.name, "price": ingredient.price} for ingredient in actual_list]

        assert type(actual_list) == list
        assert all(type(ingredient) == Ingredient for ingredient in actual_list)
        assert actual_values == self.expected_ingredients

    def test_available_buns_return_buns_list(self):
        database = Database()

        actual_list = database.available_buns()
        actual_values = [{"name": bun.name, "price": bun.price} for bun in actual_list]

        assert type(actual_list) == list
        assert actual_values == self.expected_buns
        assert all(type(bun) == Bun for bun in actual_list)


    def test_available_ingredients_return_ingredients_list(self):
        database = Database()

        actual_list = database.available_ingredients()
        actual_values = [{"type": ingredient.type, "name": ingredient.name, "price": ingredient.price} for ingredient in actual_list]

        assert type(actual_list) == list
        assert all(type(ingredient) == Ingredient for ingredient in actual_list)
        assert actual_values == self.expected_ingredients
