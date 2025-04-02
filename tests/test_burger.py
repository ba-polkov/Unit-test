import pytest
from praktikum.burger import Burger


class TestBurger:
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_sauce

    def test_remove_ingredient(self, prepared_burger):
        initial_count = len(prepared_burger.ingredients)
        prepared_burger.remove_ingredient(0)
        assert len(prepared_burger.ingredients) == initial_count - 1

    def test_move_ingredient(self, prepared_burger):
        first_ingredient = prepared_burger.ingredients[0]
        second_ingredient = prepared_burger.ingredients[1]

        prepared_burger.move_ingredient(0, 1)

        assert prepared_burger.ingredients[0] == second_ingredient
        assert prepared_burger.ingredients[1] == first_ingredient

    def test_get_price(self, prepared_burger, mock_bun, mock_sauce, mock_filling):
        expected_price = mock_bun.get_price() * 2 + mock_sauce.get_price() + mock_filling.get_price()
        assert prepared_burger.get_price() == expected_price

    def test_get_receipt(self, prepared_burger, mock_bun, mock_sauce, mock_filling):
        receipt = prepared_burger.get_receipt()
        assert mock_bun.get_name() in receipt
        assert mock_sauce.get_name() in receipt
        assert mock_filling.get_name() in receipt
        assert str(prepared_burger.get_price()) in receipt

    def test_move_ingredient_invalid_index(self, prepared_burger):
        with pytest.raises(IndexError):
            prepared_burger.move_ingredient(10, 0)

    def test_remove_nonexistent_ingredient(self, prepared_burger):
        with pytest.raises(IndexError):
            prepared_burger.remove_ingredient(10)