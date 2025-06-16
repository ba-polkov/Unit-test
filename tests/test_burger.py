from unittest.mock import Mock
import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from data import DataBurger, DataReceipt


class TestBurger:

    def test_burger_initialization(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun is mock_bun
        assert burger.bun.get_name() == DataBurger.BUN_NAME
        assert burger.bun.get_price() == 1255.0

    def test_add_ingredient(self, mock_sauce, mock_main):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        assert burger.ingredients == [mock_sauce]
        burger.add_ingredient(mock_main)
        assert burger.ingredients == [mock_sauce, mock_main]

    @pytest.mark.parametrize(
        "index_to_remove, expected_remaining",
        DataBurger.REMOVE_INGREDIENT_TEST_DATA
    )
    def test_remove_ingredient(self, mock_sauce, mock_main, index_to_remove, expected_remaining):
        burger = Burger()
        burger.add_ingredient(mock_sauce)  # Индекс 0
        burger.add_ingredient(mock_main)  # Индекс 1
        burger.add_ingredient(mock_sauce)  # Индекс 2

        burger.remove_ingredient(index_to_remove)

        actual_remaining = [ing.get_name() for ing in burger.ingredients]
        assert actual_remaining == expected_remaining

    def test_remove_ingredient_invalid_index(self):
        burger = Burger()
        burger.ingredients = ["ingredient1"]

        with pytest.raises(IndexError):
            burger.remove_ingredient(5)

    # Тестирование перемещения ингредиентов
    @pytest.mark.parametrize(
        "original_index, new_index, expected_order",
        DataBurger.MOVE_INGREDIENT_TEST_DATA
    )
    def test_move_ingredient(self, original_index, new_index, expected_order):

        burger = Burger()
        burger.ingredients = ["ingredient1", "ingredient2", "ingredient3"]

        burger.move_ingredient(original_index, new_index)
        assert burger.ingredients == expected_order

    # Тестирование расчета цены
    @pytest.mark.parametrize(
        "bun_price, ingredient_prices, expected_total",
        DataBurger.GET_PRICE_TEST_DATA
    )
    def test_get_price(self, bun_price, ingredient_prices, expected_total):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.bun = mock_bun

        mock_ingredients = []
        for price in ingredient_prices:
            mock_ing = Mock()
            mock_ing.get_price.return_value = price
            mock_ingredients.append(mock_ing)
            burger.add_ingredient(mock_ing)

        assert burger.get_price() == expected_total
        mock_bun.get_price.assert_called_once()

    # Тестирование формирования чека
    def test_get_receipt(self, mock_bun, mock_sauce, mock_main):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_main)

        expected_lines = DataReceipt.RECEIPT
        assert burger.get_receipt() == "\n".join(expected_lines)