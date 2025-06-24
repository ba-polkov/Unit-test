import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from data import *
from helpers import *


class TestBurger:

    def test_burger_init(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []


    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(bun=mock_bun)
        assert burger.bun.name == bun_name_price[0], f"Ожидаемая булка: {bun_name_price[0]}, получена булка: {burger.bun.name}"
        assert burger.bun.price == bun_name_price[1], f"Ожидаемая цена: {bun_name_price[1]}, получена цена: {burger.bun.price}"

    def test_add_ingredient_to_list(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    def test_burger_add_ingredient_in_burger(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient=mock_ingredient)
        added_ingredient_sauce = burger.ingredients[0].type, burger.ingredients[0].name, burger.ingredients[0].price
        TestTools.check_unit_test_result(expected_value=ingredient_sauce, actually_value=added_ingredient_sauce)

    def test_burger_remove_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.ingredients.append(mock_ingredient)
        burger.remove_ingredient(index=0)
        TestTools.check_unit_test_result(expected_value=[], actually_value=burger.ingredients)

    def test_move_ingredient_and_swap_them_by_index(self):
        burger = Burger()
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger.ingredients.append(mock_ingredient_1)
        burger.ingredients.append(mock_ingredient_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_ingredient_2, mock_ingredient_1]

    @pytest.mark.parametrize("bun_price, ingredient_price, expected_value",[(500, 300, 1300), (800, 400, 2000), (1200, 600, 3000)])
    def test_get_price_burger(self, mock_bun, mock_ingredient, bun_price, ingredient_price, expected_value):
        mock_bun.get_price.return_value = bun_price
        mock_ingredient.get_price.return_value = ingredient_price
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients.append(mock_ingredient)
        TestTools.check_unit_test_result(expected_value=expected_value, actually_value=burger.get_price())

    def test_get_receipt(self, mock_bun, mock_ingredient):
        mock_bun.get_name.return_value = bun_name_price[0]
        mock_bun.get_price.return_value = bun_name_price[1]
        mock_ingredient.get_type.return_value =  ingredient_sauce[0]
        mock_ingredient.get_name.return_value = ingredient_sauce[1]
        mock_ingredient.get_price.return_value = ingredient_sauce[2]

        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients.append(mock_ingredient)

        receipt = burger.get_receipt()

        expected_receipt = (
            f'(==== {bun_name_price[0]} ====)\n'
            '= sauce hot sauce =\n'
            f'(==== {bun_name_price[0]} ====)\n'
            f"\n"
            f'Price: {bun_name_price[1] * 2 + ingredient_sauce[2]}'
        )

        assert receipt == expected_receipt
