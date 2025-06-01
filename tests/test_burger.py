import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    def setup_method(self):
        self.burger = Burger()
        self.mock_bun = Mock(spec=Bun)
        self.mock_bun.get_name.return_value = "test bun"
        self.mock_bun.get_price.return_value = 100

        self.sauce_mock = Mock(spec=Ingredient)
        self.sauce_mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
        self.sauce_mock.get_name.return_value = "test sauce"
        self.sauce_mock.get_price.return_value = 50

        self.filling_mock = Mock(spec=Ingredient)
        self.filling_mock.get_type.return_value = INGREDIENT_TYPE_FILLING
        self.filling_mock.get_name.return_value = "test filling"
        self.filling_mock.get_price.return_value = 150

    def test_set_buns(self):
        self.burger.set_buns(self.mock_bun)
        assert self.burger.bun == self.mock_bun

    def test_add_ingredient(self):
        self.burger.add_ingredient(self.sauce_mock)
        assert len(self.burger.ingredients) == 1
        assert self.burger.ingredients[0] == self.sauce_mock

        self.burger.add_ingredient(self.filling_mock)
        assert len(self.burger.ingredients) == 2
        assert self.burger.ingredients[1] == self.filling_mock

    def test_remove_ingredient(self):
        self.burger.add_ingredient(self.sauce_mock)
        self.burger.add_ingredient(self.filling_mock)
        assert len(self.burger.ingredients) == 2

        self.burger.remove_ingredient(0)
        assert len(self.burger.ingredients) == 1
        assert self.burger.ingredients[0] == self.filling_mock

    def test_move_ingredient(self):
        self.burger.add_ingredient(self.sauce_mock)
        self.burger.add_ingredient(self.filling_mock)
        assert self.burger.ingredients[0] == self.sauce_mock
        assert self.burger.ingredients[1] == self.filling_mock

        self.burger.move_ingredient(0, 1)
        assert self.burger.ingredients[0] == self.filling_mock
        assert self.burger.ingredients[1] == self.sauce_mock

    def test_get_price(self):
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.sauce_mock)
        self.burger.add_ingredient(self.filling_mock)

        expected_price = 2 * self.mock_bun.get_price() + self.sauce_mock.get_price() + self.filling_mock.get_price()
        assert self.burger.get_price() == expected_price

        self.mock_bun.get_price.assert_called()
        self.sauce_mock.get_price.assert_called()
        self.filling_mock.get_price.assert_called()

    def test_get_receipt(self):
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.sauce_mock)
        self.burger.add_ingredient(self.filling_mock)

        receipt = self.burger.get_receipt()

        assert "(==== test bun ====)" in receipt
        assert "= sauce test sauce =" in receipt
        assert "= filling test filling =" in receipt
        assert "Price: " in receipt

        self.mock_bun.get_name.assert_called()
        self.sauce_mock.get_type.assert_called()
        self.sauce_mock.get_name.assert_called()
        self.filling_mock.get_type.assert_called()
        self.filling_mock.get_name.assert_called()