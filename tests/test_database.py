class TestDataBase:

    def test_database_available_buns(self, db):
        assert len(db.available_buns()) == 3

    def test_database_available_ingredients(self, db):
        assert len(db.available_ingredients()) == 6

    def test_database_add_bun(self, db, mock_bun):
        current_available_buns = len(db.available_buns())
        db.buns.append(mock_bun)
        assert len(db.available_buns()) == current_available_buns + 1

    def test_database_add_ingredient(self, db, mock_ingredient_sauce):
        current_available_ingredients = len(db.available_ingredients())
        db.ingredients.append(mock_ingredient_sauce)
        assert len(db.available_ingredients()) == current_available_ingredients + 1
