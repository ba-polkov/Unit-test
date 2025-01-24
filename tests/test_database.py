from praktikum.database import Database
from helpers import Helpers
from data import TestData

class TestDatabase:
    def setup_method(self):
        self.db = Database()

    def test_available_buns(self):
        available_buns = self.db.available_buns()
        expected_result = TestData.AVAILABLE_BUNS
        bun_names_list = Helpers.get_bun_names(available_buns)
        assert set(expected_result) == set(bun_names_list)

    def test_available_ingredients(self):
        available_ingredients = self.db.available_ingredients()
        expected_result = TestData.AVAILABLE_INGREDIENTS  #
        ingredient_name_list = Helpers.get_ingredient_names(available_ingredients)
        assert set(expected_result) == set(ingredient_name_list)


