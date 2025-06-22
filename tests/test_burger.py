import pytest
from unittest.mock import Mock
from pages.burger import Burger
from pages.bun import Bun
from pages.ingredient import Ingredient
from pages.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


def create_mock_bun(name, price):
    mock_bun = Mock(spec=Bun)
    mock_bun.get_name.return_value = name
    mock_bun.get_price.return_value = price
    return mock_bun


def create_mock_ingredient(ingredient_type, name, price):
    mock_ingredient = Mock(spec=Ingredient)
    mock_ingredient.get_type.return_value = ingredient_type
    mock_ingredient.get_name.return_value = name
    mock_ingredient.get_price.return_value = price
    return mock_ingredient


def test_burger_set_buns():
    burger = Burger()
    mock_bun = create_mock_bun("mock bun", 100)
    burger.set_buns(mock_bun)
    assert burger.bun is mock_bun


def test_burger_add_remove_ingredient():
    burger = Burger()
    mock_ingredient = create_mock_ingredient(INGREDIENT_TYPE_SAUCE, "mock sauce", 100)

    burger.add_ingredient(mock_ingredient)
    assert len(burger.ingredients) == 1
    assert mock_ingredient in burger.ingredients

    burger.remove_ingredient(0)
    assert len(burger.ingredients) == 0


def test_burger_move_ingredient():
    burger = Burger()
    ingredients = [
        create_mock_ingredient(INGREDIENT_TYPE_SAUCE, "sauce1", 100),
        create_mock_ingredient(INGREDIENT_TYPE_FILLING, "filling1", 200),
        create_mock_ingredient(INGREDIENT_TYPE_SAUCE, "sauce2", 150),
    ]

    for i in ingredients:
        burger.add_ingredient(i)

    burger.move_ingredient(0, 2)
    assert burger.ingredients[0].get_name() == "filling1"
    assert burger.ingredients[2].get_name() == "sauce1"


@pytest.mark.parametrize("bun_price, ingredient_prices, expected_total", [
    (100, [100], 300),  # 100*2 + 100 = 300
    (200, [100, 200], 700),  # 200*2 + 100 + 200 = 700
    (300, [], 600),  # 300*2 = 600
])
def test_burger_get_price(bun_price, ingredient_prices, expected_total):
    burger = Burger()
    mock_bun = create_mock_bun("mock bun", bun_price)
    burger.set_buns(mock_bun)

    for price in ingredient_prices:
        mock_ingredient = create_mock_ingredient(INGREDIENT_TYPE_FILLING, "mock ingredient", price)
        burger.add_ingredient(mock_ingredient)

    total = burger.get_price()
    assert total == expected_total