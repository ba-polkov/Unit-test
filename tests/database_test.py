from praktikum.database import Database


class TestDatabase:

    def test_available_buns(self):
        database = Database()
        assert database.available_buns() == database.buns

    def test_available_ingredients(self):
        database = Database()
        assert database.available_ingredients() == database.ingredients