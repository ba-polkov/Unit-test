from unittest.mock import Mock
import pytest
from practicum_burgers.bun import Bun
from practicum_burgers.burger import Burger
from practicum_burgers.ingredient import Ingredient
from tests.conftest import *
from helper import *



class TestBurger:
    def test_init_burger_bun_none(self, burger):
        assert burger.bun is None


    def test_init_burger_ingredients_list(self, burger):
        assert burger.ingredients == []


    def test_set_bun(self, burger):
        bun_mock = create_and_set_bun_mock(burger)
        assert burger.bun is bun_mock


    def test_add_ingredient_successful_addition(self, burger):
        ingredient_mock = create_and_add_ingredients_mock(burger)
        assert len (burger.ingredients) == 1
        assert burger.ingredients[0] is ingredient_mock


    def test_add_ingredients_multiple_successful_addition(self,burger):
        ingredient_1 = create_and_add_ingredients_mock(burger)
        ingredient_2 = create_and_add_ingredients_mock(burger)
        assert len (burger.ingredients) == 2
        assert burger.ingredients == [ingredient_1, ingredient_2]


    def test_remove_ingredient_successful_remove(self, burger):
        ingredient_1 = create_and_add_ingredients_mock(burger)
        ingredient_2 = create_and_add_ingredients_mock(burger)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients [0] is ingredient_2
        assert ingredient_1 is not burger.ingredients


    def test_remove_ingredient_invalid_index(self, burger):
        create_and_add_ingredients_mock(burger)
        with pytest.raises(IndexError):
            burger.remove_ingredient(1)


    def test_move_ingredient_successful_move(self, burger):
        create_and_set_bun_mock(burger)
        ingredient_1 = create_and_add_ingredients_mock(burger)
        ingredient_2 = create_and_add_ingredients_mock(burger)
        burger.move_ingredient(0,1)
        assert burger.ingredients[0] is ingredient_2
        assert burger.ingredients[1] is ingredient_1


    @pytest.mark.parametrize(
        "bun_price, ingredient_prices, expected_total",
        [
            (0, [20, 30], 50),
            (50, [10], 110),
            (100, [], 200),
        ]
    )
    def test_get_price_param(self, burger, bun_price, ingredient_prices, expected_total):
        create_and_set_bun_mock(burger, price=bun_price)
        for price in ingredient_prices:
            create_and_add_ingredients_mock(burger, price=price)
        result = burger.get_price()
        assert result == expected_total


    def test_get_price_without_bun_raises_attributeerror(self, burger):
        create_and_add_ingredients_mock(burger, price=20)
        with pytest.raises(AttributeError):
            burger.get_price()


    def test_get_receipt(self, burger):
        create_and_set_bun_mock(burger, name = 'Вкусная булочка')
        create_and_add_ingredients_mock(burger, ingredient_type = 'SAUCE', name = 'Чесночный')
        create_and_add_ingredients_mock(burger, ingredient_type= 'FILLING', name='Сыр')

        burger.get_price = Mock(return_value=100.0)
        receipt = burger.get_receipt()
        expected = (
            "(==== Вкусная булочка ====)\n"
            "= sauce Чесночный =\n"
            "= filling Сыр =\n"
            "(==== Вкусная булочка ====)\n"
            "\n"
            "Price: 100.0"
        )
        assert expected in receipt
