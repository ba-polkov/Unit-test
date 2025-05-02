from praktikum import ingredient_types


class TestDatabase:

    def test_available_buns(self, database):

        assert database.available_buns() == database.buns

    def test_available_ingredients(self, database):

        assert database.available_ingredients() == database.ingredients