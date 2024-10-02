import data
from praktikum.burger import Burger


class TestBurger:
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    def test_remove_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self, mock_ingredient, mock_second_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_second_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_second_ingredient, mock_ingredient]

    def test_get_price(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == (mock_bun.get_price() * 2) + (mock_ingredient.get_price())

    def test_get_receipt(self, mock_bun, mock_ingredient, mock_second_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_second_ingredient)
        assert burger.get_receipt() == data.TEST_BURGER_RECEIPT
