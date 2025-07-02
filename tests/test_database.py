from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    def test_available_buns(self):
        database = Database()
        list_buns = database.available_buns()
        list_result = []
        for bun in list_buns:
            list_result.append((bun.get_name(), bun.get_price()))
        expected_list = [('black bun', 100), ('white bun', 200), ('red bun', 300)]
        assert list_result == expected_list


    def test_available_ingredients(self):
        database = Database()
        list_ingredients = database.available_ingredients()
        list_result = []
        for ingredient in list_ingredients:
            list_result.append((ingredient.get_type(), ingredient.get_name(), ingredient.get_price()))
        expected_result = [
            (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            (INGREDIENT_TYPE_FILLING, "cutlet", 100),
            (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            (INGREDIENT_TYPE_FILLING, "sausage", 300)
        ] 
        assert list_result == expected_result