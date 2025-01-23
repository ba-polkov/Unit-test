import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from data import BUN_NAME, BUN_PRICE, INGREDIENT_NAME, INGREDIENT_TYPE, INGREDIENT_PRICE

class TestBurger:
    @pytest.fixture
    def burger(self):
        return Burger()

    def test_burger_initialization(self, burger):
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self, burger):
        bun = Mock(spec=Bun)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self, burger):
        ingredient = Mock(spec=Ingredient)
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    def test_get_price(self, burger):
        bun = Bun(BUN_NAME, BUN_PRICE)
        ingredient = Ingredient(INGREDIENT_TYPE, INGREDIENT_NAME, INGREDIENT_PRICE)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        assert burger.get_price() == BUN_PRICE * 2 + INGREDIENT_PRICE

    def test_remove_ingredient(self, burger):
        ingredient1 = Mock(spec=Ingredient)
        ingredient2 = Mock(spec=Ingredient)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.remove_ingredient(0)
        assert ingredient1 not in burger.ingredients
        assert ingredient2 in burger.ingredients

    def test_move_ingredient(self, burger):
        ingredient1 = Mock(spec=Ingredient)
        ingredient2 = Mock(spec=Ingredient)
        ingredient3 = Mock(spec=Ingredient)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)
        burger.move_ingredient(0, 2)
        assert burger.ingredients == [ingredient2, ingredient3, ingredient1]

    def test_get_receipt(self, burger):
        bun = Mock(spec=Bun)
        bun.get_name.return_value = BUN_NAME
        bun.get_price.return_value = BUN_PRICE
        ingredient = Mock(spec=Ingredient)
        ingredient.get_name.return_value = INGREDIENT_NAME
        ingredient.get_type.return_value = INGREDIENT_TYPE
        ingredient.get_price.return_value = INGREDIENT_PRICE
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        expected_receipt = (
            f'(==== {BUN_NAME} ====)\n'
            f'= {INGREDIENT_TYPE.lower()} {INGREDIENT_NAME} =\n'
            f'(==== {BUN_NAME} ====)\n\n'
            f'Price: {BUN_PRICE * 2 + INGREDIENT_PRICE}'
        )
        assert burger.get_receipt() == expected_receipt


