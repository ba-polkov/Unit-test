import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import BUN_DATA, BUN_NAMES, INGREDIENT_DATA, INGREDIENT_NAMES

class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        bun_name = BUN_NAMES[0]
        bun = Bun(bun_name, BUN_DATA[bun_name]["price"])
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient_name = INGREDIENT_NAMES[0]
        ingredient = Ingredient(
            INGREDIENT_DATA[ingredient_name]["type"],
            ingredient_name,
            INGREDIENT_DATA[ingredient_name]["price"]
        )
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient1_name = INGREDIENT_NAMES[0]
        ingredient2_name = INGREDIENT_NAMES[1]
        ingredient1 = Ingredient(
            INGREDIENT_DATA[ingredient1_name]["type"],
            ingredient1_name,
            INGREDIENT_DATA[ingredient1_name]["price"]
        )
        ingredient2 = Ingredient(
            INGREDIENT_DATA[ingredient2_name]["type"],
            ingredient2_name,
            INGREDIENT_DATA[ingredient2_name]["price"]
        )
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.remove_ingredient(0)
        assert ingredient1 not in burger.ingredients
        assert ingredient2 in burger.ingredients
        assert len(burger.ingredients) == 1

    def test_move_ingredient(self):
        burger = Burger()
        ingredient1_name = INGREDIENT_NAMES[0]
        ingredient2_name = INGREDIENT_NAMES[1]
        ingredient3_name = INGREDIENT_NAMES[2]
        ingredient1 = Ingredient(
            INGREDIENT_DATA[ingredient1_name]["type"],
            ingredient1_name,
            INGREDIENT_DATA[ingredient1_name]["price"]
        )
        ingredient2 = Ingredient(
            INGREDIENT_DATA[ingredient2_name]["type"],
            ingredient2_name,
            INGREDIENT_DATA[ingredient2_name]["price"]
        )
        ingredient3 = Ingredient(
            INGREDIENT_DATA[ingredient3_name]["type"],
            ingredient3_name,
            INGREDIENT_DATA[ingredient3_name]["price"]
        )
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)
        burger.move_ingredient(0, 2)
        assert burger.ingredients == [ingredient2, ingredient3, ingredient1]

    def test_get_price_no_ingredients(self):
        burger = Burger()
        bun_name = BUN_NAMES[0]
        bun = Bun(bun_name, BUN_DATA[bun_name]["price"])
        burger.set_buns(bun)
        assert burger.get_price() == bun.get_price() * 2

    def test_get_price_with_ingredients(self):
        burger = Burger()
        bun_name = BUN_NAMES[0]
        bun = Bun(bun_name, BUN_DATA[bun_name]["price"])
        burger.set_buns(bun)
        ingredient1_name = INGREDIENT_NAMES[0]
        ingredient2_name = INGREDIENT_NAMES[1]
        ingredient1 = Ingredient(
            INGREDIENT_DATA[ingredient1_name]["type"],
            ingredient1_name,
            INGREDIENT_DATA[ingredient1_name]["price"]
        )
        ingredient2 = Ingredient(
            INGREDIENT_DATA[ingredient2_name]["type"],
            ingredient2_name,
            INGREDIENT_DATA[ingredient2_name]["price"]
        )
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        expected_price = bun.get_price() * 2 + ingredient1.get_price() + ingredient2.get_price()
        assert burger.get_price() == expected_price

    def test_get_receipt_no_ingredients(self):
        burger = Burger()
        bun_name = BUN_NAMES[0]
        bun = Bun(bun_name, BUN_DATA[bun_name]["price"])
        burger.set_buns(bun)
        expected_receipt_lines = [
            f'(==== {bun_name} ====)',
            f'(==== {bun_name} ====)\n',
            f'Price: {burger.get_price()}'
        ]
        expected_receipt = '\n'.join(expected_receipt_lines)
        assert burger.get_receipt() == expected_receipt

    def test_get_receipt_with_ingredients(self):
        burger = Burger()
        bun_name = BUN_NAMES[0]
        bun = Bun(bun_name, BUN_DATA[bun_name]["price"])
        burger.set_buns(bun)
        ingredient1_name = INGREDIENT_NAMES[0]
        ingredient2_name = INGREDIENT_NAMES[1]
        ingredient1 = Ingredient(
            INGREDIENT_DATA[ingredient1_name]["type"],
            ingredient1_name,
            INGREDIENT_DATA[ingredient1_name]["price"]
        )
        ingredient2 = Ingredient(
            INGREDIENT_DATA[ingredient2_name]["type"],
            ingredient2_name,
            INGREDIENT_DATA[ingredient2_name]["price"]
        )
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        expected_receipt_lines = [
            f'(==== {bun_name} ====)',
            f'= {INGREDIENT_DATA[ingredient1_name]["type"].lower()} {ingredient1_name} =',
            f'= {INGREDIENT_DATA[ingredient2_name]["type"].lower()} {ingredient2_name} =',
            f'(==== {bun_name} ====)\n',
            f'Price: {burger.get_price()}'
        ]
        expected_receipt = '\n'.join(expected_receipt_lines)
        assert burger.get_receipt() == expected_receipt