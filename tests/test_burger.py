from unittest.mock import Mock
from burger import Burger


class TestBurger:

    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.ingredients = [Mock(), mock_ingredient]
        burger.move_ingredient(1, 0)

        assert burger.ingredients[0] == mock_ingredient

    def test_get_price(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        expected_result = burger.get_price()
        actual_result = 277.0

        assert expected_result == actual_result

    def test_get_receipt(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        name_bun = 'test_bun'
        name_ingredient = 'test_ingredient'
        price = '277.0'
        result = burger.get_receipt()

        assert name_bun in result
        assert name_ingredient in result
        assert price in result
