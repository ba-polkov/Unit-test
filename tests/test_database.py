from database import Database


class TestDatabase:
    def test_available_buns(self):
        database = Database()
        buns_to_search = ['black bun', 'white bun', 'red bun']
        bun_not_found = False
        for bun in database.available_buns():
            if bun.get_name() not in buns_to_search:
                bun_not_found = True

        assert bun_not_found == False

    def test_available_ingredients(self):
        database = Database()
        ingredients_to_search = ['hot sauce', 'sour cream', 'chili sauce', 'cutlet', 'dinosaur', 'sausage']
        ingredients_not_found = False
        for ingredient in database.available_ingredients():
            if ingredient.get_name() not in ingredients_to_search:
                ingredients_not_found = True

        assert ingredients_not_found == False

