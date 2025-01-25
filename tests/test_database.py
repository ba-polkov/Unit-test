import pytest
from praktikum.database import Database

class TestDatabase:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.db = Database()

    def test_available_buns(self):
        available_buns = self.db.available_buns()
        expected_names = ["black bun", "white bun", "red bun"]
        assert [bun.get_name() for bun in available_buns] == expected_names

    def test_available_ingredients(self):
        available_ingredients = self.db.available_ingredients()
        expected_names = [
            "hot sauce", "sour cream", "chili sauce",
            "cutlet", "dinosaur", "sausage"
        ]
        assert [ingredient.get_name() for ingredient in available_ingredients] == expected_names



