import pytest
from unittest.mock import Mock

from praktikum.burger import Burger


class TestBurger:
    def test_burger_set_buns_setting_bun_name(self):
        burger = Burger()
        bun = Mock()
        burger.set_buns(bun)

        assert burger.bun == bun

    def test_burger_add_ingredient_item_added(self):
        burger = Burger()
        ingredient = Mock()
        burger.add_ingredient(ingredient)

        assert ingredient in burger.ingredients

    def test_burger_remove_ingredient_item_removed(self):
        burger = Burger()
        ingredient = Mock()
        ingredient1 = Mock()
        burger.ingredients = [ingredient, ingredient1]
        burger.remove_ingredient(1)

        assert ingredient in burger.ingredients and ingredient1.get_name.return_value not in burger.ingredients

    def test_burger_move_ingredient_item_index_updated(self):
        burger = Burger()
        ingredient = Mock()
        ingredient1 = Mock()
        burger.ingredients = [ingredient, ingredient1]

        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == ingredient1 and burger.ingredients[1] == ingredient

    @pytest.mark.parametrize("bun_price, ingredient_price, ingredient1_price",
                             [[3.5, 14.5, 1.5], [0, 0, 0], [-1, -99, 1]])
    def test_burger_get_price_calculate_price(self, bun_price, ingredient_price, ingredient1_price):
        burger = Burger()
        bun = Mock()
        bun.get_price.return_value = bun_price
        burger.bun = bun
        ingredient = Mock()
        ingredient.get_price.return_value = ingredient_price
        ingredient1 = Mock()
        ingredient1.get_price.return_value = ingredient1_price
        burger.ingredients = [ingredient, ingredient1]

        assert burger.get_price() == bun.get_price.return_value * 2 + ingredient.get_price.return_value + ingredient1.get_price.return_value

    def test_burger_get_receipt_return_data(self):
        burger = Burger()
        bun = Mock()
        bun.get_price.return_value = 3.5
        bun.get_name.return_value = 'yammi_bun_name'
        burger.bun = bun
        ingredient = Mock()
        ingredient.get_name.return_value = 'ketchup ingredient'
        ingredient.get_price.return_value = 14.5
        ingredient.get_type.return_value = 'yammi sauce'
        burger.ingredients = [ingredient]

        assert burger.get_receipt() == '(==== yammi_bun_name ====)\n= yammi sauce ketchup ingredient =\n(==== yammi_bun_name ====)\n\nPrice: 21.5'
