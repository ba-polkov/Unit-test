import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from data import TestData

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
        bun = Bun(TestData.BUN_NAME, TestData.BUN_PRICE)
        ingredient1 = Ingredient(TestData.INGREDIENT_TYPE, TestData.INGREDIENT_NAME, TestData.INGREDIENT_PRICE)
        ingredient2 = Ingredient(TestData.INGREDIENT_TYPE_NEXT, TestData.INGREDIENT_NAME_NEXT, TestData.INGREDIENT_PRICE_NEXT)

        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        expected_price = TestData.BUN_PRICE * 2 + TestData.INGREDIENT_PRICE + TestData.INGREDIENT_PRICE_NEXT
        assert burger.get_price() == expected_price

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
        bun.get_name.return_value = TestData.BUN_NAME
        bun.get_price.return_value = TestData.BUN_PRICE

        ingredient1 = Mock(spec=Ingredient)
        ingredient1.get_name.return_value = TestData.INGREDIENT_NAME
        ingredient1.get_type.return_value = TestData.INGREDIENT_TYPE
        ingredient1.get_price.return_value = TestData.INGREDIENT_PRICE

        ingredient2 = Mock(spec=Ingredient)
        ingredient2.get_name.return_value = TestData.INGREDIENT_NAME_NEXT
        ingredient2.get_type.return_value = TestData.INGREDIENT_TYPE_NEXT
        ingredient2.get_price.return_value = TestData.INGREDIENT_PRICE_NEXT

        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        expected_receipt = (
            f'(==== {TestData.BUN_NAME} ====)\n'
            f'= {TestData.INGREDIENT_TYPE.lower()} {TestData.INGREDIENT_NAME} =\n'
            f'= {TestData.INGREDIENT_TYPE_NEXT.lower()} {TestData.INGREDIENT_NAME_NEXT} =\n'
            f'(==== {TestData.BUN_NAME} ====)\n\n'
            f'Price: {TestData.BUN_PRICE * 2 + TestData.INGREDIENT_PRICE + TestData.INGREDIENT_PRICE_NEXT}'
        )

        assert burger.get_receipt() == expected_receipt



