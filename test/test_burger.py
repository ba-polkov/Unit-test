from praktikum.burger import *
from conftest import *


class TestBurger:
    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    def test_remove_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == mock_ingredient

    def test_get_price(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == 250

    def test_get_receipt(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        expected_receipt = (
            "(==== black bun ====)\n"
            "= filling cutlet =\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 250"
        )

        actual_receipt = burger.get_receipt()
        assert actual_receipt == expected_receipt
