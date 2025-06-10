import pytest
from unittest.mock import MagicMock
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

def test_burger_with_mocks_and_parametrize(sample_bun, sample_ingredients):
    burger = Burger()

    burger.set_buns(sample_bun)

    ing1 = MagicMock()
    ing1.get_name.return_value = "mocked sauce"
    ing1.get_price.return_value = 50
    ing1.get_type.return_value = INGREDIENT_TYPE_SAUCE

    ing2 = MagicMock()
    ing2.get_name.return_value = "mocked filling"
    ing2.get_price.return_value = 100
    ing2.get_type.return_value = INGREDIENT_TYPE_FILLING

    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)

    expected_price = sample_bun.get_price() * 2 + 50 + 100
    assert burger.get_price() == expected_price

    receipt = burger.get_receipt()
    assert sample_bun.get_name() in receipt
    assert "mocked sauce" in receipt
    assert "mocked filling" in receipt
    assert f"Price: {expected_price}" in receipt


def test_add_and_remove_ingredient():
    burger = Burger()
    bun = Bun("Bun", 100)
    ing = Ingredient(INGREDIENT_TYPE_SAUCE, "Sauce", 50)

    burger.set_buns(bun)
    burger.add_ingredient(ing)
    assert len(burger.ingredients) == 1

    burger.remove_ingredient(0)
    assert len(burger.ingredients) == 0