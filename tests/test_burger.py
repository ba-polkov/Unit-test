import pytest
from unittest.mock import MagicMock

#Тест добавления булочки
def test_set_buns(burger, mock_bun):
    burger.set_buns(mock_bun)
    assert burger.bun == mock_bun

#тест добавление ингредиентов
def test_add_ingredient(burger, mock_ingredient):
    burger.add_ingredient(mock_ingredient)
    assert mock_ingredient in burger.ingredients

#тест удаление ингредиента
def test_remove_ingredient(burger, mock_ingredient):
    burger.add_ingredient(mock_ingredient)
    burger.remove_ingredient(0)
    assert len(burger.ingredients) == 0

#тест перемещение ингредиента
def test_move_ingredient_changes_position_correctly(burger, mock_ingredient):
    second_ingredient = MagicMock()
    second_ingredient.get_name.return_value = "Соус"
    burger.add_ingredient(mock_ingredient)
    burger.add_ingredient(second_ingredient)
    burger.move_ingredient(1, 0)
    assert burger.ingredients[0] == second_ingredient

#тест получение цены
@pytest.mark.parametrize("bun_price,ingredient_prices,expected", [
    (100, [50], 250),  # 100*2 + 50 = 250
    (200, [100, 50], 550),  # 200*2 + 100 + 50 = 550
    (150, [], 300),  # 150*2 + 0 = 300
], ids=[
    "single ingredient",
    "multiple ingredients",
    "no ingredients"
])
#тест получения цены
def test_get_price(burger, mock_bun, mock_ingredient, bun_price, ingredient_prices, expected):
    mock_bun.get_price.return_value = bun_price
    burger.ingredients = []

    for price in ingredient_prices:
        ing = MagicMock()
        ing.get_price.return_value = price
        burger.add_ingredient(ing)

    burger.set_buns(mock_bun)
    assert burger.get_price() == expected

#тест получение рецепта
def test_get_receipt(burger, mock_bun, mock_ingredient):
    mock_bun.get_name.return_value = "Краторная булка"
    mock_ingredient.get_name.return_value = "Сыр"
    mock_ingredient.get_type.return_value = "FILLING"

    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)

    receipt = burger.get_receipt()

    assert "(==== Краторная булка ====)" in receipt
    assert "= filling Сыр =" in receipt
    assert "Price: 250" in receipt