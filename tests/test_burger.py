import pytest
import data as dt
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient

class TestBurger:
    def test_buns(self):
        burger = Burger()
        bun = Bun(dt.bun_data[0], dt.bun_data[1])
        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(dt.ingredients[1][0],
                                dt.ingredients[2][1],
                                dt.ingredients[3][2])
        burger.add_ingredient(ingredient)

        assert ingredient in burger.ingredients

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(dt.ingredients[2][0],
                                dt.ingredients[4][1],
                                dt.ingredients[3][2])
        burger.add_ingredient(ingredient)
        ingredient_index = burger.ingredients.index(ingredient)
        burger.remove_ingredient(ingredient_index)

        assert ingredient not in burger.ingredients

    def test_move_ingredient(self):
        burger = Burger()
        ingredient_1 = Ingredient(dt.ingredients[1][0],
                                  dt.ingredients[2][1],
                                  dt.ingredients[3][2])
        ingredient_2 = Ingredient(dt.ingredients[2][0],
                                  dt.ingredients[4][1],
                                  dt.ingredients[3][2])
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        ingredient_index = burger.ingredients.index(ingredient_1)
        new_index = ingredient_index + 1
        burger.move_ingredient(ingredient_index, new_index)

        assert burger.ingredients.index(ingredient_1) == new_index

    def test_get_price(self):
        bun_price = 323
        ingredient_price = 474
        bun_mock = Mock()
        ingredient_mock = Mock()
        bun_mock.get_price.return_value = bun_price
        ingredient_mock.get_price.return_value = ingredient_price
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        burger_price = (bun_price * 2) + ingredient_price

        assert burger.get_price() == burger_price

    def test_get_receipt_bun(self):
        burger = Burger()
        bun = Bun(dt.bun_data[0], dt.bun_data[1])
        burger.set_buns(bun)

        assert burger.bun.get_name() in burger.get_receipt()

    def test_get_receipt_price(self):
        burger = Burger()
        bun = Bun(dt.bun_data[0], dt.bun_data[1])
        ingridient = Ingredient(dt.ingredients[5][0],
                                dt.ingredients[4][1],
                                dt.ingredients[3][2])
        burger.set_buns(bun)
        burger.add_ingredient(ingridient)

        assert str(burger.get_price()) in burger.get_receipt()

    @pytest.mark.parametrize('index', [0, 1])
    def test_get_receipt_ingredient(self, index):
        burger = Burger()
        bun = Bun(dt.bun_data[0], dt.bun_data[1])
        ingredient_1 = Ingredient(dt.ingredients[1][0],
                                  dt.ingredients[2][1],
                                  dt.ingredients[3][2])
        ingredient_2 = Ingredient(dt.ingredients[2][0],
                                  dt.ingredients[4][1],
                                  dt.ingredients[3][2])
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)

        assert burger.ingredients[index].get_name() in burger.get_receipt()