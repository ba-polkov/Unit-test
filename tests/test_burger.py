import pytest
from Diplom_1.praktikum.burger import Burger
from unittest.mock import Mock

@pytest.fixture
def burger():
    return Burger()

bun = Mock()
bun.get_name.return_value = "black"
bun.get_price.return_value = 100

ingredient = Mock()
ingredient.get_type.return_value = "SAUCE"
ingredient.get_name.return_value = "hot sauce"
ingredient.get_price.return_value = 100

def test_set_buns_return_correct_buns(burger):
    burger.set_buns(bun)
    assert burger.bun == bun

def test_add_ingredient(burger):
    burger.add_ingredient(ingredient)
    assert len(burger.ingredients) == 1

def test_remove_ingredients(burger):
    burger.add_ingredient(ingredient)
    burger.remove_ingredient(0)
    assert len(burger.ingredients) == 0

def test_move_ingredients(burger):
    burger.add_ingredient(ingredient)
    burger.add_ingredient(Mock())
    burger.move_ingredient(0, 1)
    assert burger.ingredients[1] == ingredient

def test_get_price_burger(burger):
    burger.add_ingredient(ingredient)
    burger.set_buns(bun)
    assert burger.get_price() == 300

def test_get_reciept(burger):
    burger.add_ingredient(ingredient)
    burger.set_buns(bun)
    receipt = burger.get_receipt()
    assert "= sauce hot sauce =" in receipt
    assert "==== black ====" in receipt
    assert "300" in receipt
