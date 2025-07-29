from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    def setup_method(self):
        self.db = Database()
        self.buns = self.db.available_buns()
        self.ingredients = self.db.available_ingredients()

    def test_available_buns_returns_list(self):
        assert isinstance(self.buns, list)

    def test_all_buns_are_instances(self):
        assert all(isinstance(b, Bun) for b in self.buns)

    def test_buns_count(self):
        assert len(self.buns) == 3

    def test_first_bun_name(self):
        assert self.buns[0].get_name() == "black bun"

    def test_last_bun_price(self):
        assert self.buns[-1].get_price() == 300


    def test_available_ingredients_returns_list(self):
        assert isinstance(self.ingredients, list)

    def test_all_ingredients_are_instances(self):
        assert all(isinstance(i, Ingredient) for i in self.ingredients)

    def test_ingredients_count(self):
        assert len(self.ingredients) == 6

    def test_sauce_count(self):
        sauces = [i for i in self.ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE]
        assert len(sauces) == 3

    def test_filling_count(self):
        fillings = [i for i in self.ingredients if i.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(fillings) == 3

    def test_first_ingredient_name(self):
        assert self.ingredients[0].get_name() == "hot sauce"

    def test_last_ingredient_price(self):
        assert self.ingredients[-1].get_price() == 300
