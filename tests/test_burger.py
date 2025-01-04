from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from data import BUN_NAME, BUN_PRICE, INGREDIENT_NAME, INGREDIENT_TYPE, INGREDIENT_PRICE

def test_burger_initialization():
    burger = Burger()
    assert burger.bun is None
    assert burger.ingredients == []

def test_set_buns():
    burger = Burger()
    bun = Mock(spec=Bun)
    burger.set_buns(bun)
    assert burger.bun == bun

def test_add_ingredient():
    burger = Burger()
    ingredient = Mock(spec=Ingredient)
    burger.add_ingredient(ingredient)
    assert ingredient in burger.ingredients

def test_get_price():
    burger = Burger()
    bun = Bun(BUN_NAME, BUN_PRICE)
    ingredient = Ingredient(INGREDIENT_TYPE, INGREDIENT_NAME, INGREDIENT_PRICE)
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)
    assert burger.get_price() == BUN_PRICE * 2 + INGREDIENT_PRICE


