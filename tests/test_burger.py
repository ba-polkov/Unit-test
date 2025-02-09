from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:
    def test_set_buns(self):
        mock_bun = Mock()
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self):
        mock_ingr = Mock()
        burger = Burger()
        burger.add_ingredient(mock_ingr)
        assert burger.ingredients == [mock_ingr]

    def test_remove_ingredient(self):
        mock_ingr = Mock()
        burger = Burger()
        burger.add_ingredient(mock_ingr)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self):
        burger = Burger()
        mock_ingr_1 = Mock()
        mock_ingr_2 = Mock()
        burger.add_ingredient(mock_ingr_1)
        burger.add_ingredient(mock_ingr_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_ingr_2
        assert burger.ingredients[1] == mock_ingr_1

    def test_get_price(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 99
        mock_ingr1 = Mock()
        mock_ingr2 = Mock()
        mock_ingr1.get_price.return_value = 109
        mock_ingr2.get_price.return_value = 209
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingr1, mock_ingr2]
        expected_price = mock_bun.get_price() * 2 + mock_ingr1.get_price() + mock_ingr2.get_price()
        assert expected_price == burger.get_price()

    def test_get_receipt(self):
        mock_bun = Mock()
        mock_ingr1 = Mock()
        mock_ingr2 = Mock()
        mock_bun.get_name.return_value = "Cosmic_rye"
        mock_ingr1.get_type.return_value = "Cutlet"
        mock_ingr1.get_name.return_value = "Vegan steak"
        mock_ingr2.get_type.return_value = "Sauce"
        mock_ingr2.get_name.return_value = "Cosmic lava"
        expected_receipt = "(==== Cosmic_rye ====)\n= cutlet Vegan steak =\n= sauce Cosmic lava =\n(==== Cosmic_rye ====)\n\nPrice: 1000"

        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingr1, mock_ingr2]
        burger.get_price = Mock(return_value=1000)

        assert burger.get_receipt() == expected_receipt



