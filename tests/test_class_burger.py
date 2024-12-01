from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from burger import Burger
from unittest.mock import Mock

def test_burger_init():
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

def test_remove_ingredient():
    burger = Burger()
    ingredient = Mock(spec=Ingredient)
    burger.ingredients = [ingredient]
    burger.remove_ingredient(0)
    assert ingredient not in burger.ingredients

def test_move_ingredient():
    burger = Burger()
    ingredient1, ingredient2 = Mock(spec=Ingredient), Mock(spec=Ingredient)
    burger.ingredients = [ingredient1, ingredient2]
    burger.move_ingredient(0, 1)
    assert burger.ingredients == [ingredient2, ingredient1]

def test_get_price():
    burger = Burger()
    bun = Mock(spec=Bun)
    bun.get_price.return_value = 100
    burger.set_buns(bun)
    ingredient = Mock(spec=Ingredient)
    ingredient.get_price.return_value = 50
    burger.add_ingredient(ingredient)
    assert burger.get_price() == 250

def test_get_receipt():
    burger = Burger()
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "Test Bun"
    bun.get_price.return_value = 100
    burger.set_buns(bun)
    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = "Test Ingredient"
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    ingredient.get_price.return_value = 50
    burger.add_ingredient(ingredient)
    receipt = burger.get_receipt()
    assert "(==== Test Bun ====)" in receipt
    assert "= filling Test Ingredient =" in receipt
    assert "Price: 250" in receipt