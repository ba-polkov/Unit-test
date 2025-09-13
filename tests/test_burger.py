import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


@pytest.mark.parametrize(
    "bun_price, ingredients_prices, expected_total",
    [
        (50, [10, 20], 50 * 2 + 10 + 20),
        (60, [], 60 * 2),
        (70, [15], 70 * 2 + 15)
    ]
)
def test_get_price(bun_price, ingredients_prices, expected_total, mocker):
    bun = Bun("Test Bun", bun_price)
    burger = Burger()
    burger.set_buns(bun)

    for idx, price in enumerate(ingredients_prices):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, f"ingredient_{idx}", price)
        burger.add_ingredient(ingredient)

    assert burger.get_price() == expected_total


def test_add_and_remove_ingredient():
    burger = Burger()
    burger.set_buns(Bun("Bun", 50))
    ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Cutlet", 100)

    burger.add_ingredient(ingredient)
    assert burger.ingredients[0] == ingredient

    burger.remove_ingredient(0)
    assert burger.ingredients == []


def test_move_ingredient():
    burger = Burger()
    burger.set_buns(Bun("Bun", 50))
    i1 = Ingredient(INGREDIENT_TYPE_FILLING, "Cutlet", 100)
    i2 = Ingredient(INGREDIENT_TYPE_SAUCE, "Ketchup", 10)

    burger.add_ingredient(i1)
    burger.add_ingredient(i2)
    burger.move_ingredient(0, 1)

    assert burger.ingredients[0] == i2
    assert burger.ingredients[1] == i1


def test_get_receipt():
    burger = Burger()
    bun = Bun("Bun", 50)
    burger.set_buns(bun)
    i1 = Ingredient(INGREDIENT_TYPE_FILLING, "Cutlet", 100)
    burger.add_ingredient(i1)

    receipt = burger.get_receipt()
    assert "Bun" in receipt
    assert "cutlet" in receipt.lower()
    assert str(burger.get_price()) in receipt
