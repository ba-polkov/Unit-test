from unittest.mock import Mock
from praktikum.burger import Burger
from data import BurgerData


class TestBurger:

    def test_set_buns(self):
        bun_mock = Mock()
        burger = Burger()
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    def test_add_ingredient(self):
        ing_mock = Mock()
        burger = Burger()
        burger.add_ingredient(ing_mock)
        assert len(burger.ingredients) == 1 and burger.ingredients[0] == ing_mock

    def test_remove_ingredient(self):
        ing_mock_1 = Mock()
        ing_mock_2 = Mock()
        burger = Burger()
        burger.add_ingredient(ing_mock_1)
        burger.add_ingredient(ing_mock_2)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1 and burger.ingredients[0] == ing_mock_2

    def test_move_ingredient(self):
        ing_mock_1 = Mock()
        ing_mock_2 = Mock()
        burger = Burger()
        burger.add_ingredient(ing_mock_1)
        burger.add_ingredient(ing_mock_2)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == ing_mock_2 and burger.ingredients[1] == ing_mock_1

    def test_get_price(self):
        bun_mock = Mock()
        bun_mock.get_price.return_value = BurgerData.bun.get('price')
        ing_mock_1 = Mock()
        ing_mock_1.get_price.return_value = BurgerData.ing_1.get('price')
        ing_mock_2 = Mock()
        ing_mock_2.get_price.return_value = BurgerData.ing_2.get('price')
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ing_mock_1)
        burger.add_ingredient(ing_mock_2)
        actual_price = burger.get_price()
        assert actual_price == BurgerData.total_price

    def test_get_receipt(self):
        bun_mock = Mock()
        bun_mock.get_price.return_value = BurgerData.bun.get('price')
        bun_mock.get_name.return_value = BurgerData.bun.get('name')
        ing_mock_1 = Mock()
        ing_mock_1.get_price.return_value = BurgerData.ing_1.get('price')
        ing_mock_1.get_type.return_value = BurgerData.ing_1.get('type')
        ing_mock_1.get_name.return_value = BurgerData.ing_1.get('name')
        ing_mock_2 = Mock()
        ing_mock_2.get_price.return_value = BurgerData.ing_2.get('price')
        ing_mock_2.get_type.return_value = BurgerData.ing_2.get('type')
        ing_mock_2.get_name.return_value = BurgerData.ing_2.get('name')
        expected_receipt = '\n'.join(BurgerData.receipt_model)
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ing_mock_1)
        burger.add_ingredient(ing_mock_2)
        actual_receipt = burger.get_receipt()
        assert actual_receipt == expected_receipt
