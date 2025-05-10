from praktikum.database import Database
from praktikum.ingredient import Ingredient

class TestDatabase:
    def test_available_buns(self):
        db = Database()
        available_buns = db.available_buns()
        expected_buns = ['black bun', 'white bun', 'red bun']
        real_buns = [bun.get_name() for bun in available_buns]
        assert expected_buns == real_buns

    def test_available_ingredients(self):
        db = Database()
        available_ingredients = db.available_ingredients()
        expected_ingredients = ["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"]
        real_ingredients = [ingredient.get_name() for ingredient in available_ingredients]
        assert expected_ingredients == real_ingredients