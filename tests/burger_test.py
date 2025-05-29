import pytest

from data import const
from helpers import TestTools
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


class TestBurger:

    def test_burger_set_buns_set_buns_of_burger(self):
        burger = Burger()
        burger.set_buns(bun=Bun(name=const['TESTS_DATA_BUN'][0], price=const['TESTS_DATA_BUN'][1]))
        buns = burger.bun.name, burger.bun.price
        TestTools.check_unit_test_result(expected_value=const['TESTS_DATA_BUN'], actually_value=buns)

    def test_burger_add_ingredient_add_ingredient_in_burger(self):
        burger = Burger()
        burger.add_ingredient(ingredient=Ingredient(ingredient_type=const['TESTS_DATA_INGREDIENT'][0], name=const['TESTS_DATA_INGREDIENT'][1], price=const['TESTS_DATA_INGREDIENT'][2]))
        ingredient = burger.ingredients[0].type, burger.ingredients[0].name, burger.ingredients[0].price
        TestTools.check_unit_test_result(expected_value=const['TESTS_DATA_INGREDIENT'], actually_value=ingredient)

    def test_burger_remove_ingredient_remove_ingredient_from_burger(self):
        burger = Burger()
        burger.add_ingredient(ingredient=Ingredient(ingredient_type=const['TESTS_DATA_INGREDIENT'][0], name=const['TESTS_DATA_INGREDIENT'][1], price=const['TESTS_DATA_INGREDIENT'][2]))
        burger.remove_ingredient(index=0)
        TestTools.check_unit_test_result(expected_value=[], actually_value=burger.ingredients)

    def test_burger_move_ingredient_moved_ingredient_in_new_position(self):
        burger = Burger()
        burger.add_ingredient(ingredient=Ingredient(ingredient_type=const['TESTS_DATA_INGREDIENT'][0], name=const['TESTS_DATA_INGREDIENT'][1], price=const['TESTS_DATA_INGREDIENT'][2]))
        burger.add_ingredient(ingredient=Ingredient(ingredient_type=const['TESTS_DATA_INGREDIENT_2'][0], name=const['TESTS_DATA_INGREDIENT_2'][1], price=const['TESTS_DATA_INGREDIENT_2'][2]))
        burger.move_ingredient(index=1,new_index=0)
        ingredient_0 = burger.ingredients[0].type, burger.ingredients[0].name, burger.ingredients[0].price
        TestTools.check_unit_test_result(expected_value=const['TESTS_DATA_INGREDIENT_2'], actually_value=ingredient_0)

    @pytest.mark.parametrize('ingredients', const['TESTS_DATA_BURGER'])
    def test_burger_get_price_return_price_of_burger(self, ingredients):
        burger = Burger()
        ingredients_price = 0
        burger.set_buns(bun=Bun(name=const['TESTS_DATA_BUN'][0], price=const['TESTS_DATA_BUN'][1]))
        for ingredient in ingredients:
            burger.add_ingredient(ingredient=Ingredient(ingredient_type=ingredient[0], name=ingredient[1], price=ingredient[2]))
            ingredients_price += ingredient[2]
        TestTools.check_unit_test_result(expected_value=const['TESTS_DATA_BUN'][1] * 2 + ingredients_price, actually_value=burger.get_price())

    @pytest.mark.parametrize('ingredients,results', const['TESTS_DATA_BURGER_RECEIPT'])
    def test_burger_get_receipt_return_receipt_of_burger(self, ingredients, results):
        burger = Burger()
        ingredients_price = 0
        burger.set_buns(bun=Bun(name=const['TESTS_DATA_BUN'][0], price=const['TESTS_DATA_BUN'][1]))
        for ingredient in ingredients:
            burger.add_ingredient(ingredient=Ingredient(ingredient_type=ingredient[0], name=ingredient[1], price=ingredient[2]))
            ingredients_price += ingredient[2]
        TestTools.check_unit_test_result(expected_value=results, actually_value=burger.get_receipt())


