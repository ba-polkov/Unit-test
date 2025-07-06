import pytest

class TestDatabase:
    def test_database_initialization(self, db):
        assert len(db.buns) == 3
        assert len(db.ingredients) == 6

    @pytest.mark.parametrize("index,name,price", [
        (0, "black bun", 100),
        (1, "white bun", 200),
        (2, "red bun", 300)
    ])
    def test_available_buns(self, db, index, name, price):
        buns = db.available_buns()
        assert buns[index].get_name() == name
        assert buns[index].get_price() == price

    @pytest.mark.parametrize("index,ingredient_type,name,price", [
        (0, "SAUCE", "hot sauce", 100),
        (3, "FILLING", "cutlet", 100)
    ])
    def test_available_ingredients(self, db, index, ingredient_type, name, price):
        ingredients = db.available_ingredients()
        assert ingredients[index].get_type() == ingredient_type
        assert ingredients[index].get_name() == name
        assert ingredients[index].get_price() == price