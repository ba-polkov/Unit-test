import pytest
from burger import Burger

class TestBurger:
    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_ingredient1):
        burger.add_ingredient(mock_ingredient1)
        assert burger.ingredients == [mock_ingredient1]

    def test_remove_ingredient(self, burger, mock_ingredient1):
        burger.add_ingredient(mock_ingredient1)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, burger, mock_ingredient1, mock_ingredient2):
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == mock_ingredient1

    def test_get_price(self, burger, mock_bun, mock_ingredient1):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        price = burger.get_price()
        expected_price = mock_bun.get_price() * 2 + mock_ingredient1.get_price()
        assert price == expected_price

    def test_get_receipt(self, burger, mock_bun, mock_ingredient2):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient2)
        expected_receipt = (
            '(==== fluorescent bun ====)\n'
            '= filling Cheese with asteroid mold =\n'
            '(==== fluorescent bun ====)\n\n'
            'Price: 6118'
        )
        assert burger.get_receipt() == expected_receipt
