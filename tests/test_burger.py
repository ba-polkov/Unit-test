from praktikum.burger import Burger


class TestBurger:

    def test_set_buns(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    def test_add_ingredient(self, ingredient_mock):
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        assert ingredient_mock in burger.ingredients

    def test_remove_ingredient(self, ingredient_mock):
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        burger.remove_ingredient(0)
        assert ingredient_mock not in burger.ingredients

    def test_move_ingredient(self, ingredient_mock, other_ingredient_mock):
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        burger.add_ingredient(other_ingredient_mock)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == other_ingredient_mock

    def test_get_price_ingredient(self, bun_mock, ingredient_mock, other_ingredient_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        burger.add_ingredient(other_ingredient_mock)
        expected_price = bun_mock.get_price() * 2 + ingredient_mock.get_price() + other_ingredient_mock.get_price() # 55*2+22+42
        assert burger.get_price() == expected_price

    def test_get_receipt(self, bun_mock, ingredient_mock, other_ingredient_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        receipt = [
            '(==== hot bun ====)',
            '(==== hot bun ====)\n',
            'Price: 110.0'
        ]
        assert burger.get_receipt() == '\n'.join(receipt)