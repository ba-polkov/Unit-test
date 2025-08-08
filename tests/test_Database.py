

class TestDatabase:

    def test_available_buns(self, database):
        assert len(database.available_buns()) == 3

    def test_available_ingredients(self, database):
        assert len(database.available_ingredients()) == 6