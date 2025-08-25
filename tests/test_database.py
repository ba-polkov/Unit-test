from praktikum.database import Database


class TestDatabase:

    def test_set_buns(self):
        data = Database()
        assert data.available_buns() == data.buns

    def test_set_ingredients(self):
        data = Database()
        assert data.available_ingredients() == data.ingredients