import pytest
from unittest.mock import Mock
from burger import Burger
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


def test_set_buns(bun_mock):
    burger = Burger()
    burger.set_buns(bun_mock)
    assert burger.bun == bun_mock


def test_add_ingredient(ingredient_mock):
    burger = Burger()
    burger.add_ingredient(ingredient_mock)
    assert ingredient_mock in burger.ingredients


def test_remove_ingredient(ingredient_mock):
    burger = Burger()
    burger.add_ingredient(ingredient_mock)
    burger.remove_ingredient(0)
    assert ingredient_mock not in burger.ingredients


def test_move_ingredient(ingredient_mock):
    burger = Burger()
    another_mock = Mock()
    burger.add_ingredient(ingredient_mock)
    burger.add_ingredient(another_mock)
    burger.move_ingredient(0, 1)
    assert burger.ingredients[1] == ingredient_mock


@pytest.mark.parametrize("count", [0, 1, 5])
def test_get_price(bun_mock, ingredient_mock, count):
    burger = Burger()
    burger.set_buns(bun_mock)
    for _ in range(count):
        burger.add_ingredient(ingredient_mock)
    expected = bun_mock.get_price() * 2 + count * ingredient_mock.get_price()
    assert burger.get_price() == expected


def test_get_receipt(bun_mock, ingredient_mock):
    burger = Burger()
    burger.set_buns(bun_mock)
    burger.add_ingredient(ingredient_mock)

    receipt = burger.get_receipt()
    assert bun_mock.get_name() in receipt
    assert ingredient_mock.get_name() in receipt
