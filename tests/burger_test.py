from unittest.mock import Mock
from praktikum.burger import Burger

class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self):
        burger = Burger()
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_ingredient2
        assert burger.ingredients[1] == mock_ingredient1

    def test_get_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 120
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == 320

    def test_get_receipt(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'new bun'
        mock_bun.get_price.return_value = 100

        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = 'new cream'
        mock_ingredient.get_type.return_value = 'cream'
        mock_ingredient.get_price.return_value = 120

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        expected_receipt = (
            '(==== new bun ====)\n'
            '= cream new cream =\n'
            '(==== new bun ====)\n'
            '\nPrice: 320'
        )

        assert burger.get_receipt() == expected_receipt