# Тесты для инициализации
import pytest


def test_burger_initialization(burger):
    assert burger.bun is None
    assert burger.ingredients == []

# Тесты для set_buns
def test_set_buns(burger, mock_bun):
    burger.set_buns(mock_bun)
    assert burger.bun == mock_bun

# Тесты для add_ingredient
def test_add_ingredient(burger, mock_ingredients):
    burger.add_ingredient(mock_ingredients['sauce'])
    burger.add_ingredient(mock_ingredients['veggie'])
    burger.add_ingredient(mock_ingredients['meat'])
    assert len(burger.ingredients) == 3
    assert burger.ingredients == mock_ingredients['all']

# Тесты для remove_ingredient
def test_remove_ingredient(burger, mock_ingredients):
    burger.ingredients = [mock_ingredients['veggie'], mock_ingredients['sauce']]
    burger.remove_ingredient(0)
    assert len(burger.ingredients) == 1
    assert burger.ingredients[0] == mock_ingredients['sauce']

# # Тесты для move_ingredient
def test_move_ingredient(burger, mock_ingredients):
    ingredients = mock_ingredients['all']
    burger.ingredients = ingredients.copy()
    burger.move_ingredient(0, 2)
    assert burger.ingredients == [mock_ingredients['veggie'], mock_ingredients['meat'], mock_ingredients['sauce']]

# Тесты для get_price
@pytest.mark.parametrize("ingredients, price", [
(['veggie', 'meat'], 100*2 + 30 + 100),
(['meat', 'meat'], 100*2 + 100*2),
])
def test_get_price_with_bun_and_ingredients(burger, mock_bun, mock_ingredients, ingredients, price):
    burger.bun = mock_bun
    burger.ingredients = [mock_ingredients[ingredients[0]], mock_ingredients[ingredients[1]]]
    assert burger.get_price() == price

# Тесты для get_receipt
def test_get_receipt_full(burger, mock_bun, mock_ingredients):
    burger.bun = mock_bun
    burger.ingredients = [mock_ingredients['sauce']]
    expected = (
        "(==== black bun ====)\n"
        "= sauce hot sauce =\n"
        "(==== black bun ====)\n\n"
        "Price: 250"
    )
    assert burger.get_receipt() == expected