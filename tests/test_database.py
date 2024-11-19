import pytest
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE

@pytest.fixture
def database():
    return Database()

class TestDatabase:
    def test_available_buns(self, database):
        buns = database.available_buns()

        assert len(buns) == 3

        assert buns[0].get_name() == "black bun"
        assert buns[1].get_name() == "white bun"
        assert buns[2].get_name() == "red bun"

        assert buns[0].get_price() == 100
        assert buns[1].get_price() == 200
        assert buns[2].get_price() == 300

    def test_available_ingredients(self, database):

        ingredients = database.available_ingredients()

        assert len(ingredients) == 6

        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[1].get_name() == "sour cream"
        assert ingredients[2].get_name() == "chili sauce"
        assert ingredients[3].get_name() == "cutlet"
        assert ingredients[4].get_name() == "dinosaur"
        assert ingredients[5].get_name() == "sausage"

        assert ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[1].get_type() == INGREDIENT_TYPE_SAUCE
