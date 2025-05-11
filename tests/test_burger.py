import pytest
from unittest.mock import MagicMock
from praktikum.burger import Burger


@pytest.fixture
def mock_bun():
    bun = MagicMock()
    bun.get_price.return_value = 100
    bun.get_name.return_value = "test bun"
    return bun


@pytest.fixture
def mock_ingredient():
    ingredient = MagicMock()
    ingredient.get_price.return_value = 50
    ingredient.get_name.return_value = "test sauce"
    ingredient.get_type.return_value = "SAUCE"
    return ingredient


def test_set_buns(mock_bun):
    burger = Burger()
    burger.set_buns(mock_bun)
    assert burger.bun == mock_bun


def test_add_ingredient(mock_ingredient):
    burger = Burger()
    burger.add_ingredient(mock_ingredient)
    assert len(burger.ingredients) == 1
    assert burger.ingredients[0] == mock_ingredient


def test_remove_ingredient(mock_ingredient):
    burger = Burger()
    burger.add_ingredient(mock_ingredient)
    burger.remove_ingredient(0)
    assert burger.ingredients == []


def test_move_ingredient(mock_ingredient):
    burger = Burger()
    burger.add_ingredient(mock_ingredient)
    burger.add_ingredient(mock_ingredient)
    burger.move_ingredient(0, 1)
    assert len(burger.ingredients) == 2  # список остался длины 2
    assert burger.ingredients[0] == mock_ingredient
    assert burger.ingredients[1] == mock_ingredient  # порядок сменился, но одинаковые объекты


def test_get_price(mock_bun, mock_ingredient):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)
    burger.add_ingredient(mock_ingredient)
    # bun price * 2 + ingredient1 + ingredient2
    expected_price = 100 * 2 + 50 + 50
    assert burger.get_price() == expected_price


def test_get_receipt(mock_bun, mock_ingredient):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)
    receipt = burger.get_receipt()

    assert "(==== test bun ====)" in receipt
    assert "= sauce test sauce =" in receipt.lower()
    assert "Price: 250" in receipt
