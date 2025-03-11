import pytest
from bun import Bun
from database import Database
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE


class TestDatabase:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.database = Database()

    def test_available_buns(self):
        buns = self.database.available_buns()
        assert len(buns) == 3
        assert isinstance(buns[0], Bun)
        assert buns[0].get_name() == "black bun"
        assert buns[0].get_price() == 100

    def test_available_ingredients(self):
        ingredients = self.database.available_ingredients()
        assert len(ingredients) == 6
        assert isinstance(ingredients[0], Ingredient)
        assert ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[0].get_price() == 100
