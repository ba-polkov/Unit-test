import pytest

from data import const
from helpers import TestTools, Generators
from unittest.mock import patch
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


class TestBurger:

    @patch('praktikum.bun.Bun')
    def test_burger_set_buns_set_buns_of_burger(self, mock_bun):
        burger = Burger()
        mock_bun.name = const['TESTS_DATA_BUN'][0]
        mock_bun.price = const['TESTS_DATA_BUN'][1]
        burger.set_buns(bun=mock_bun)
        buns = burger.bun.name, burger.bun.price
        TestTools.check_unit_test_result(expected_value=const['TESTS_DATA_BUN'], actually_value=buns)

    @patch('praktikum.ingredient.Ingredient')
    def test_burger_add_ingredient_add_ingredient_in_burger(self, mock_ingredient):
        burger = Burger()
        mock_ingredient.type = const['TESTS_DATA_INGREDIENT'][0]
        mock_ingredient.name = const['TESTS_DATA_INGREDIENT'][1]
        mock_ingredient.price = const['TESTS_DATA_INGREDIENT'][2]
        burger.add_ingredient(ingredient=mock_ingredient)
        ingredient = burger.ingredients[0].type, burger.ingredients[0].name, burger.ingredients[0].price
        TestTools.check_unit_test_result(expected_value=const['TESTS_DATA_INGREDIENT'], actually_value=ingredient)

    @patch('praktikum.ingredient.Ingredient')
    def test_burger_remove_ingredient_remove_ingredient_from_burger(self, mock_ingredient):
        burger = Burger()
        mock_ingredient.type = const['TESTS_DATA_INGREDIENT'][0]
        mock_ingredient.name = const['TESTS_DATA_INGREDIENT'][1]
        mock_ingredient.price = const['TESTS_DATA_INGREDIENT'][2]
        burger.add_ingredient(ingredient=mock_ingredient)
        burger.remove_ingredient(index=0)
        TestTools.check_unit_test_result(expected_value=[], actually_value=burger.ingredients)

    @patch('praktikum.ingredient.Ingredient')
    @patch('praktikum.ingredient.Ingredient')
    def test_burger_move_ingredient_moved_ingredient_in_new_position(self, mock_ingredient, mock_ingredient_2):
        burger = Burger()
        burger.add_ingredient(ingredient=mock_ingredient)
        burger.add_ingredient(ingredient=mock_ingredient_2)
        burger.move_ingredient(index=1,new_index=0)
        ingredient_0 = burger.ingredients[0].type, burger.ingredients[0].name, burger.ingredients[0].price
        TestTools.check_unit_test_result(expected_value=const['TESTS_DATA_INGREDIENT_2'], actually_value=ingredient_0)

    @patch('praktikum.bun.Bun')
    @patch('praktikum.ingredient.Ingredient')
    @pytest.mark.parametrize('bun_price,ingredient_price', [[0, 0], [Generators.random_number(), 0], [0, Generators.random_number()], [Generators.random_number(), Generators.random_number()]])
    def test_burger_get_price_return_price_of_burger(self, mock_bun, mock_ingredient, bun_price, ingredient_price):
        mock_bun.get_price.return_value = bun_price
        mock_ingredient.get_price.return_value = ingredient_price
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients.append(mock_ingredient)
        TestTools.check_unit_test_result(expected_value=bun_price * 2 + ingredient_price, actually_value=burger.get_price())

    @patch('praktikum.bun.Bun')
    @patch('praktikum.ingredient.Ingredient')
    @patch('praktikum.ingredient.Ingredient')
    def test_burger_get_price_return_price_of_burger_vs_two_ingredients(self, mock_bun, mock_ingredient, mock_ingredient_2):
        mock_bun.get_price.return_value = 0
        mock_ingredient.get_price.return_value = Generators.random_number()
        mock_ingredient_2.get_price.return_value = Generators.random_number()
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients.append(mock_ingredient)
        burger.ingredients.append(mock_ingredient_2)
        TestTools.check_unit_test_result(expected_value=mock_ingredient.get_price()+mock_ingredient_2.get_price(), actually_value=burger.get_price())

    @pytest.mark.parametrize('ingredients,results', const['TESTS_DATA_BURGER_RECEIPT'])
    def test_burger_get_receipt_return_receipt_of_burger(self, ingredients, results):
        burger = Burger()
        ingredients_price = 0
        burger.set_buns(bun=Bun(name=const['TESTS_DATA_BUN'][0], price=const['TESTS_DATA_BUN'][1]))
        for ingredient in ingredients:
            burger.add_ingredient(ingredient=Ingredient(ingredient_type=ingredient[0], name=ingredient[1], price=ingredient[2]))
            ingredients_price += ingredient[2]
        TestTools.check_unit_test_result(expected_value=results, actually_value=burger.get_receipt())


