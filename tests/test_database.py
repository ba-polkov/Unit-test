from database import Database


class TestDatabase:
    def test_available_buns_returns_list(self):
        db = Database()
        buns = db.available_buns()
        assert buns is db.buns

    def test_available_ingredients_return_list(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert ingredients is db.ingredients
