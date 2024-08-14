from praktikum.database import Database


class TestDatabase:
    def test_available_buns(self):
        database = Database()
        first_bun = database.available_buns()[0].get_name()
        second_bun = database.available_buns()[1].get_name()
        third_bun = database.available_buns()[2].get_name()
        assert len(database.available_buns()) == 3 and first_bun == 'black bun' and second_bun == 'white bun' and third_bun == 'red bun'

    def test_available_ingredients(self):
        database = Database()
        first_ingredient = database.available_ingredients()[0].get_name()
        second_ingredient = database.available_ingredients()[1].get_name()
        last_ingredient = database.available_ingredients()[5].get_name()
        assert len(database.available_ingredients()) == 6 and first_ingredient == 'hot sauce' and second_ingredient == 'sour cream' and last_ingredient == 'sausage'