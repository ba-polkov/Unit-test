from data import BurgerData
from praktikum.ingredient import Ingredient


class TestBurger:

    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_ingredient_1):
        burger.add_ingredient(mock_ingredient_1)
        assert burger.ingredients == [mock_ingredient_1]

    def test_remove_ingredient(self, burger, mock_ingredient_1):
        burger.add_ingredient(mock_ingredient_1)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self, burger, mock_ingredient_1, mock_ingredient_2):
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == mock_ingredient_1

    def test_get_price(self, mock_bun, mock_ingredient_1, mock_ingredient_2, burger):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        assert burger.get_price() == BurgerData.BURGER_PRICE

    def test_get_receipt(self, mock_bun, mock_ingredient_1, mock_ingredient_2, burger):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        expected_receipt = (
            f'(==== {mock_bun.get_name()} ====)\n'
            f'= {str(mock_ingredient_1.get_type()).lower()} {mock_ingredient_1.get_name()} =\n'
            f'= {str(mock_ingredient_2.get_type()).lower()} {mock_ingredient_2.get_name()} =\n'            
            f'(==== {mock_bun.get_name()} ====)\n'
            f"\n"
            f"Price: {burger.get_price()}"
        )
        assert burger.get_receipt() == expected_receipt
