import sys
sys.path.append('C:\\Cygwin\\home\\user\\Diplom\\Diplom_1')
from Diplom_1.burger import Burger
from unittest.mock import Mock, patch

class TestBurger():

    def test_set_buns(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"

        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun


    def test_add_ingredient(self):
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = "hot sauce"

        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert mock_ingredient in burger.ingredients


    def test_remove_ingredient(self):
        mock_ingredient1 = Mock()
        mock_ingredient1.get_name.return_value = "hot sauce"

        mock_ingredient2 = Mock()
        mock_ingredient2.get_name.return_value = "sour cream"

        burger = Burger()
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        burger.remove_ingredient(0)

        assert mock_ingredient1 not in burger.ingredients
        assert mock_ingredient2 in burger.ingredients


    def test_move_ingredient(self):
        mock_ingredient1 = Mock()
        mock_ingredient1.get_name.return_value = "hot sauce"

        mock_ingredient2 = Mock()
        mock_ingredient2.get_name.return_value = "sour cream"

        burger = Burger()
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        burger.move_ingredient(0, 1)

        assert burger.ingredients == [mock_ingredient2, mock_ingredient1]


    def test_get_price(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100

        mock_ingredient1 = Mock()
        mock_ingredient1.get_price.return_value = 150

        mock_ingredient2 = Mock()
        mock_ingredient2.get_price.return_value = 200

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        assert burger.get_price()==550

    def test_get_receipt(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100

        mock_ingredient1 = Mock()
        mock_ingredient1.get_type.return_value = 'sauce'
        mock_ingredient1.get_name.return_value = "hot sauce"
        mock_ingredient1.get_price.return_value = 100

        mock_ingredient2 = Mock()
        mock_ingredient2.get_type.return_value = 'filling'
        mock_ingredient2.get_name.return_value = "dinosaur"
        mock_ingredient2.get_price.return_value = 200

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        expected_receipt = """(==== black bun ====)
= sauce hot sauce =
= filling dinosaur =
(==== black bun ====)

Price: 500"""

        assert burger.get_receipt()==expected_receipt

