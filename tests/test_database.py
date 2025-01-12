from praktikum.database import Database

class TestDatabase:
    def test_available_buns(self):
        database = Database()
        available_buns = database.available_buns()
        assert available_buns == database.buns

    def test_available_ingredients(self):
        database = Database()
        available_ingredients = database.available_ingredients()
        assert available_ingredients == database.ingredients
