import ingredient_types
from praktikum.ingredient import Ingredient
import  data


class TestBurger:
    def test_set_buns_one_bun_bun_set(self, bun, burger):
        burger.set_buns(bun)
        assert burger.bun == bun

def test_add_ingredient_one_ingredient_ingredient_added(burger):
    ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, data.INGREDIENT_NAME_TOMATO, data.INGREDIENT_PRICE_TOMATO)
    burger.add_ingredient(ingredient)
    assert ingredient in burger.ingredients

def test_remove_ingredient_two_ingredient_one_ingredient_removed(burger):
    ingredient1 = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, data.INGREDIENT_NAME_TOMATO, data.INGREDIENT_PRICE_TOMATO)
    ingredient2 = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, data.INGREDIENT_NAME_CUCUMBER, data.INGREDIENT_PRICE_CUCUMBER)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    burger.remove_ingredient(0)
    assert ingredient1 not in burger.ingredients

def test_move_ingredient_two_ingredient_ingredient_moved(burger):
    ingredient1 = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, data.INGREDIENT_NAME_TOMATO, data.INGREDIENT_PRICE_TOMATO)
    ingredient2 = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, data.INGREDIENT_NAME_CUCUMBER, data.INGREDIENT_PRICE_CUCUMBER)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    burger.move_ingredient(0, 1)
    assert burger.ingredients == [ingredient2, ingredient1]

def test_get_price_one_complete_burger_price_received(burger, bun):
    ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, data.INGREDIENT_NAME_TOMATO, data.INGREDIENT_PRICE_TOMATO)
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)
    assert burger.get_price() == data.BUN_PRICE_COSMOBUN * 2 + data.INGREDIENT_PRICE_TOMATO

def test_get_receipt_one_complete_burger_receipt_received(burger, bun):
    ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, data.INGREDIENT_NAME_TOMATO, data.INGREDIENT_PRICE_TOMATO)
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)
    assert burger.get_receipt() == f"(==== {data.BUN_NAME_COSMOBUN} ====)\n= {ingredient_types.INGREDIENT_TYPE_FILLING.lower()} {data.INGREDIENT_NAME_TOMATO} =\n(==== {data.BUN_NAME_COSMOBUN} ====)\n\nPrice: {data.BUN_PRICE_COSMOBUN * 2 + data.INGREDIENT_PRICE_TOMATO}"
