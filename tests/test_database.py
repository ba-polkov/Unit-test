from praktikum.database import Database


class TestDatabase:

    def test_available_buns_get_length_arr_success(self, mock_bun):
        database = Database()
        print(database.available_buns())
        assert len(database.available_buns()) == 3

    def test_available_ingredients_get_length_arr_success(self, mock_bun):
        database = Database()
        assert len(database.available_ingredients()) == 6