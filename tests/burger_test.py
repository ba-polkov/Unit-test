from praktikum.burger import Burger


class TestBurger:

    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun.name == mock_bun.name

    def test_add_ingredient(self, mock_ingredient_1):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        assert burger.ingredients[0] == mock_ingredient_1

    def test_remove_ingredient(self, mock_ingredient_1):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_1)
        burger.remove_ingredient(1)
        assert burger.ingredients[0] == mock_ingredient_1

    def test_move_ingredient(self, mock_ingredient_1, mock_ingredient_2):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == mock_ingredient_2

    def test_get_price(self, bun_object, ingredient_object):
        burger = Burger()
        burger.set_buns(bun_object)
        burger.add_ingredient(ingredient_object)
        assert burger.get_price() == bun_object.price * 2 + ingredient_object.get_price()

    def test_get_receipt(self, bun_object, ingredient_object):
        burger = Burger()
        burger.set_buns(bun_object)
        burger.add_ingredient(ingredient_object)
        assert burger.get_receipt() == f'(==== {bun_object.get_name()} ====)\n= {(ingredient_object.get_type()).lower()} {ingredient_object.get_name()} =\n(==== {bun_object.get_name()} ====)\n\nPrice: {burger.get_price()}'
