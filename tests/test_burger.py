from unittest.mock import MagicMock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


def test_burger_init_has_no_buns_and_empty_ingredients():
    burger = Burger()
    assert burger.bun is None
    assert burger.ingredients == []

def test_set_buns_sets_bun():
    burger = Burger()
    mock_bun = MagicMock(spec=Bun)
    burger.set_buns(mock_bun)
    assert burger.bun == mock_bun

def test_add_ingredient_appends_to_list():
    burger = Burger()
    mock_ing = MagicMock(spec=Ingredient)
    burger.add_ingredient(mock_ing)
    assert burger.ingredients[-1] == mock_ing

def test_remove_ingredient_removes_by_index():
    burger = Burger()
    burger.ingredients = [1, 2, 3]
    burger.remove_ingredient(1)
    assert burger.ingredients == [1, 3]

def test_move_ingredient_moves_from_to():
    burger = Burger()
    burger.ingredients = [1, 2, 3]
    burger.move_ingredient(0, 2)
    assert burger.ingredients == [2, 3, 1]

def test_get_price_calculates_bun_and_ingredients():
    burger = Burger()
    mock_bun = MagicMock(spec=Bun)
    mock_bun.get_price.return_value = 100
    burger.set_buns(mock_bun)

    mock_ing1 = MagicMock(spec=Ingredient)
    mock_ing1.get_price.return_value = 50
    mock_ing2 = MagicMock(spec=Ingredient)
    mock_ing2.get_price.return_value = 30

    burger.add_ingredient(mock_ing1)
    burger.add_ingredient(mock_ing2)

    total = burger.get_price()
    assert total == 100 * 2 + 50 + 30

def test_get_receipt_returns_formatted_string():
    burger = Burger()
    mock_bun = MagicMock(spec=Bun)
    mock_bun.get_name.return_value = "Test Bun"
    mock_bun.get_price.return_value = 100
    burger.set_buns(mock_bun)

    mock_ing = MagicMock(spec=Ingredient)
    mock_ing.get_type.return_value = INGREDIENT_TYPE_SAUCE
    mock_ing.get_name.return_value = "Test Sauce"
    mock_ing.get_price.return_value = 50
    burger.add_ingredient(mock_ing)

    receipt = burger.get_receipt()
    lines = receipt.split('\n')
    print(receipt)
    print(lines)
    assert lines[0] == "(==== Test Bun ====)"
    assert lines[1] == "= sauce Test Sauce ="
    assert lines[2] == "(==== Test Bun ====)"
    assert lines[4] == "Price: 250"