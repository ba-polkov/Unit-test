import pytest
from unittest.mock import Mock, patch
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100
    return bun


@pytest.fixture
def mock_ingredient():
    ingredient = Mock()
    ingredient.get_type.return_value = "SAUCE"
    ingredient.get_name.return_value = "hot sauce"
    ingredient.get_price.return_value = 100
    return ingredient


def test_set_buns(burger, mock_bun):
    burger.set_buns(mock_bun)
    assert burger.bun == mock_bun


def test_add_ingredient(burger, mock_ingredient):
    burger.add_ingredient(mock_ingredient)
    assert len(burger.ingredients) == 1
    assert burger.ingredients[0] == mock_ingredient


def test_remove_ingredient(burger, mock_ingredient):
    burger.add_ingredient(mock_ingredient)
    burger.remove_ingredient(0)
    assert len(burger.ingredients) == 0


def test_move_ingredient(burger, mock_ingredient):
    second_ingredient = Mock()
    second_ingredient.get_name.return_value = "sour cream"

    burger.add_ingredient(mock_ingredient)
    burger.add_ingredient(second_ingredient)
    burger.move_ingredient(0, 1)

    assert burger.ingredients[0].get_name() == "sour cream"
    assert burger.ingredients[1].get_name() == "hot sauce"


def test_get_price(burger, mock_bun, mock_ingredient):
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)
    assert burger.get_price() == 300  


def test_get_receipt(burger, mock_bun, mock_ingredient):
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)
    receipt = burger.get_receipt()

    assert "(==== black bun ====)" in receipt
    assert "= sauce hot sauce =" in receipt
    assert "Price: 300" in receipt