import pytest
from praktikum.burger import Burger


def test_set_buns(bun_mock):
    burger = Burger()
    burger.set_buns(bun_mock)
    assert burger.bun == bun_mock


def test_add_ingredient(ingredient_instance):
    ingredient, _ = ingredient_instance
    burger = Burger()
    burger.add_ingredient(ingredient)
    assert ingredient in burger.ingredients


def test_remove_ingredient(ingredient_instance):
    ingredient, _ = ingredient_instance
    burger = Burger()
    burger.add_ingredient(ingredient)
    burger.remove_ingredient(0)
    assert ingredient not in burger.ingredients


def test_move_ingredient(ingredient_instance):
    ingredient1, _ = ingredient_instance
    ingredient2, _ = ingredient_instance
    burger = Burger()
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    burger.move_ingredient(0, 1)
    assert burger.ingredients[1] == ingredient1


@pytest.mark.parametrize("extra_ingredients", [0, 1, 2])
def test_get_price(bun_mock, ingredient_instance, extra_ingredients):
    burger = Burger()
    burger.set_buns(bun_mock)

    for _ in range(extra_ingredients):
        ingredient, _ = ingredient_instance
        burger.add_ingredient(ingredient)

    expected_price = bun_mock.get_price() * 2 + sum(i.get_price() for i in burger.ingredients)
    assert round(burger.get_price(), 2) == round(expected_price, 2)


def test_get_receipt(bun_mock, ingredient_instance):
    ingredient, data = ingredient_instance

    burger = Burger()
    burger.set_buns(bun_mock)
    burger.add_ingredient(ingredient)

    receipt = burger.get_receipt()
    assert bun_mock._expected_name in receipt and data["name"] in receipt
