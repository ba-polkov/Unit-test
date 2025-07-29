import pytest
from unittest.mock import Mock
from praktikum.database import Database
from praktikum.burger import Burger
from praktikum.ingredient_types import *


class TestBurger:


    def setup_method(self):
        self.db = Database()
        self.burger = Burger()

    def test_set_buns(self):
        bun = self.db.available_buns()[0]
        self.burger.set_buns(bun)
        assert self.burger.bun == bun

    def test_add_ingredient(self):
        ingredient = self.db.available_ingredients()[0]
        self.burger.add_ingredient(ingredient)
        assert ingredient in self.burger.ingredients

    def test_remove_ingredient(self):
        ingredient = self.db.available_ingredients()[0]
        self.burger.add_ingredient(ingredient)
        self.burger.remove_ingredient(0)
        assert ingredient not in self.burger.ingredients

    def test_move_ingredient(self):
        ingredient1 = self.db.available_ingredients()[0]
        ingredient2 = self.db.available_ingredients()[1]
        self.burger.add_ingredient(ingredient1)
        self.burger.add_ingredient(ingredient2)
        self.burger.move_ingredient(0, 1)
        assert self.burger.ingredients[1] == ingredient1

    @pytest.mark.parametrize("bun_index, ingredient_indexes, expected_price", [
        (0, [], lambda db: db.available_buns()[0].get_price() * 2),
        (1, [0], lambda db: db.available_buns()[1].get_price() * 2 + db.available_ingredients()[0].get_price()),
        (2, [1, 4], lambda db: db.available_buns()[2].get_price() * 2 +
                              db.available_ingredients()[1].get_price() +
                              db.available_ingredients()[4].get_price())
    ])
    def test_get_price(self, bun_index, ingredient_indexes, expected_price):
        bun = self.db.available_buns()[bun_index]
        self.burger.set_buns(bun)
        for i in ingredient_indexes:
            self.burger.add_ingredient(self.db.available_ingredients()[i])
        assert self.burger.get_price() == expected_price(self.db)    

    def test_get_receipt(self):
        bun = self.db.available_buns()[0]
        ingredient = self.db.available_ingredients()[0]

        self.burger.set_buns(bun)
        self.burger.add_ingredient(ingredient)

        receipt = self.burger.get_receipt()

        assert bun.get_name() in receipt
        assert ingredient.get_name() in receipt
        assert str(self.burger.get_price()) in receipt
