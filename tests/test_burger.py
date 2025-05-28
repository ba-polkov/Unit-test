from praktikum.burger import Burger
from tests.data import BUN_NAME1, PRICE1, INGREDIENT1, INGREDIENT2, RECEIPT, PRICE2, TYPE1
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from unittest.mock import Mock, patch


class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        burger.set_buns(BUN_NAME1)
        assert burger.bun == BUN_NAME1

    def test_add_ingredient(self):
        burger = Burger()
        burger.add_ingredient(INGREDIENT1)
        assert burger.ingredients == [INGREDIENT1]

    def test_remove_ingredient(self):
        burger = Burger()
        burger.ingredients = [INGREDIENT1, INGREDIENT2]
        burger.remove_ingredient(0)
        assert burger.ingredients == [INGREDIENT2]

    def test_move_ingredient(self):
        burger = Burger()
        burger.ingredients = [INGREDIENT1, INGREDIENT2]
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [INGREDIENT2, INGREDIENT1]

    def test_get_price(self, mock_bun, mock_ingredient):
        mock_bun.get_price.return_value = PRICE1
        mock_ingredient.get_price.return_value = PRICE2

        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]

        assert burger.get_price() == 5

    def test_get_receipt(self, mock_bun, mock_ingredient):
        mock_bun.get_price.return_value = PRICE1
        mock_bun.get_name.return_value = BUN_NAME1

        mock_ingredient.get_price.return_value = PRICE2
        mock_ingredient.get_type.return_value = TYPE1
        mock_ingredient.get_name.return_value = INGREDIENT1

        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        assert burger.get_receipt() == RECEIPT