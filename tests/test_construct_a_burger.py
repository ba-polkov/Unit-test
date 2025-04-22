from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        bun_mock = Mock()

        assert burger.bun is None

        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    def test_add_ingredient(self):
        burger = Burger()
        ingredient_mock = Mock()

        assert len(burger.ingredients) == 0

        burger.add_ingredient(ingredient_mock)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient_mock

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient1 = Mock()
        ingredient2 = Mock()

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)


        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient2

    def test_move_ingredient(self):
        burger = Burger()
        ingredient1 = Mock()
        ingredient2 = Mock()
        ingredient3 = Mock()

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)


        burger.move_ingredient(0, 2)
        assert burger.ingredients[0] == ingredient2
        assert burger.ingredients[1] == ingredient3
        assert burger.ingredients[2] == ingredient1

    def test_get_price(self):
        burger = Burger()
        bun_mock = Mock()
        bun_mock.get_price.return_value = 100

        ingredient_mock1 = Mock()
        ingredient_mock1.get_price.return_value = 50

        ingredient_mock2 = Mock()
        ingredient_mock2.get_price.return_value = 75


        burger.set_buns(bun_mock)
        assert burger.get_price() == 200


        burger.add_ingredient(ingredient_mock1)
        assert burger.get_price() == 250


        burger.add_ingredient(ingredient_mock2)
        assert burger.get_price() == 325

    def test_get_receipt(self):
        burger = Burger()
        bun_mock = Mock()
        bun_mock.get_name.return_value = "black bun"
        bun_mock.get_price.return_value = 100

        sauce_mock = Mock()
        sauce_mock.get_type.return_value = "SAUCE"
        sauce_mock.get_name.return_value = "hot sauce"
        sauce_mock.get_price.return_value = 50

        filling_mock = Mock()
        filling_mock.get_type.return_value = "FILLING"
        filling_mock.get_name.return_value = "cutlet"
        filling_mock.get_price.return_value = 100


        burger.set_buns(bun_mock)
        receipt = burger.get_receipt()
        assert "(==== black bun ====)" in receipt
        assert "Price: 200" in receipt


        burger.add_ingredient(sauce_mock)
        receipt = burger.get_receipt()
        assert "= sauce hot sauce =" in receipt
        assert "Price: 250" in receipt


        burger.add_ingredient(filling_mock)
        receipt = burger.get_receipt()
        assert "= filling cutlet =" in receipt
        assert "Price: 350" in receipt

    def test_multiple_operations(self):
        burger = Burger()
        bun_mock = Mock()
        bun_mock.get_price.return_value = 100
        bun_mock.get_name.return_value = "bun"

        ing1 = Mock()
        ing1.get_price.return_value = 10
        ing1.get_name.return_value = "ing1"
        ing1.get_type.return_value = "SAUCE"

        ing2 = Mock()
        ing2.get_price.return_value = 20
        ing2.get_name.return_value = "ing2"
        ing2.get_type.return_value = "FILLING"


        burger.set_buns(bun_mock)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.move_ingredient(0, 1)
        burger.remove_ingredient(0)

        assert burger.get_price() == 210
        receipt = burger.get_receipt()
        assert "= sauce ing1 =" in receipt
        assert "Price: 210" in receipt