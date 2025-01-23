from praktikum.database import Database
from helpers import get_bun_names, get_ingredient_names

class TestDatabase:
    def setup_method(self):
        self.db = Database()

    def test_available_buns(self):
        available_buns = self.db.available_buns()
        expected_result = ['black bun', 'white bun', 'red bun']
        bun_names_list = get_bun_names(available_buns)
        assert expected_result == bun_names_list

    def test_available_ingredients(self):
        available_ingredients = self.db.available_ingredients()
        expected_result = ['hot sauce', 'sour cream', 'chili sauce', 'cutlet', 'dinosaur', 'sausage']
        ingredient_name_list = get_ingredient_names(available_ingredients)
        assert expected_result == ingredient_name_list

