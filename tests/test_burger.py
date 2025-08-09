import pytest

from conftest import make_mock_bun, make_mock_ingredient
from data import buns_name_price, ingredients_type_name_price
from praktikum.burger import Burger


class TestBurger:
    @pytest.mark.parametrize("bun_name, bun_price", buns_name_price)
    def test_set_buns_sets_burger_bun_name(self, bun_name, bun_price):
        burger = Burger()
        burger.set_buns(make_mock_bun(name=bun_name, price=bun_price))
        assert burger.bun.get_name() == bun_name

    @pytest.mark.parametrize("bun_name, bun_price", buns_name_price)
    def test_set_buns_sets_burger_bun_price(self, bun_name, bun_price):
        burger = Burger()
        burger.set_buns(make_mock_bun(name=bun_name, price=bun_price))
        assert burger.bun.get_price() == bun_price

    @pytest.mark.parametrize("ingredient_type, ingredient_name, ingredient_price", ingredients_type_name_price)
    def test_add_ingredient_sets_type(self, ingredient_type, ingredient_name, ingredient_price):
        burger = Burger()
        burger.add_ingredient(make_mock_ingredient(type_=ingredient_type, name=ingredient_name, price=ingredient_price))
        assert burger.ingredients[0].get_type() == ingredient_type

    @pytest.mark.parametrize("ingredient_type, ingredient_name, ingredient_price", ingredients_type_name_price)
    def test_add_ingredient_sets_name(self, ingredient_type, ingredient_name, ingredient_price):
        burger = Burger()
        burger.add_ingredient(make_mock_ingredient(type_=ingredient_type, name=ingredient_name, price=ingredient_price))
        assert burger.ingredients[0].get_name() == ingredient_name

    @pytest.mark.parametrize("ingredient_type, ingredient_name, ingredient_price", ingredients_type_name_price)
    def test_add_ingredient_sets_price(self, ingredient_type, ingredient_name, ingredient_price):
        burger = Burger()
        burger.add_ingredient(make_mock_ingredient(type_=ingredient_type, name=ingredient_name, price=ingredient_price))
        assert burger.ingredients[0].get_price() == ingredient_price

    def test_remove_ingredient_removes_by_index(self):
        burger = Burger()
        ing1 = make_mock_ingredient(name="one")
        ing2 = make_mock_ingredient(name="two")
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.remove_ingredient(0)
        assert burger.ingredients[0].get_name() == "two"

    def test_move_ingredient_moves_correctly(self):
        burger = Burger()
        ing1 = make_mock_ingredient(name="one")
        ing2 = make_mock_ingredient(name="two")
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ing2, ing1]

    def test_get_price_counts_buns_and_ingredients(self):
        burger = Burger()
        burger.set_buns(make_mock_bun(price=20))
        ing1 = make_mock_ingredient(price=10)
        ing2 = make_mock_ingredient(price=15)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        assert burger.get_price() == 20 * 2 + 10 + 15

    def test_get_receipt_contains_bun_and_ingredients(self):
        burger = Burger()
        burger.set_buns(make_mock_bun(name="Булка"))
        burger.add_ingredient(make_mock_ingredient(type_="соус", name="Кетчуп"))
        burger.get_price = lambda: 999
        receipt = burger.get_receipt()
        assert "Булка" in receipt
