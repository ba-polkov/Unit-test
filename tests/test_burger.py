from unittest.mock import Mock

from praktikum.burger import Burger
from tests.conftest import burger


class TestBurger:

    def test_bun_is_None_when_initialized(self):
        burger = Burger()

        assert burger.bun is None

    def test_ingredients_list_is_empty_when_initialized(self, bun):
        burger = Burger()

        assert burger.ingredients == []

    def test_method_set_buns_set_bun(self, bun):
        burger = Burger()

        burger.set_buns(bun)

        assert burger.bun == bun

    def test_method_add_ingredient_adds_ingredient_list(self, ingredients):
        burger = Burger()

        burger.add_ingredient(ingredients[0])
        burger.add_ingredient(ingredients[1])
        burger.add_ingredient(ingredients[2])

        expected_list = [{"type": i.type, "name": i.name, "price": i.price} for i in ingredients]
        actual_list = [{"type": i.type, "name": i.name, "price": i.price} for i in burger.ingredients]

        assert actual_list == expected_list
        assert type(actual_list) == list
        assert all(isinstance(ingredient, Mock) for ingredient in burger.ingredients)

    def test_method_remove_ingredients_removes_ingredients(self, burger, ingredients):

        initial_list = [{"type": i.type, "name": i.name, "price": i.price} for i in ingredients]

        burger.remove_ingredient(2)

        actual_list = [{"type": i.type, "name": i.name, "price": i.price} for i in burger.ingredients]

        assert actual_list == [initial_list[0], initial_list[1]]

        burger.remove_ingredient(1)
        burger.remove_ingredient(0)

        assert burger.ingredients == []

    def test_method_move_ingredients_set_new_ingredient_index(self, burger, ingredients):
        initial_list = [{"type": i.type, "name": i.name, "price": i.price} for i in ingredients]

        burger.move_ingredient(0,2)

        actual_list = [{"type": i.type, "name": i.name, "price": i.price} for i in burger.ingredients]
        expected_list = [initial_list[1], initial_list[2], initial_list[0]]

        assert actual_list == expected_list


    def test_method_get_price_return_price(self, burger):

        assert burger.get_price() == 460.5

    def test_method_get_price_without_ingredients_return_price(self, bun):

        burger = Burger()
        burger.bun = bun

        assert burger.get_price() == 200

    def test_method_get_receipt_return_receipt(self, burger):

        assert burger.get_receipt() == ('(==== Quantum Bread ====)\n'
                                    '= filling Космогриб =\n'
                                    '= filling Криодраконья котлета =\n'
                                    '= sauce Биолюминесцентный соус =\n'
                                    '(==== Quantum Bread ====)\n\n'
                                    'Price: 460.5')

