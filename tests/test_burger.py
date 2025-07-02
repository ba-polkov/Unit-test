import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestBurger:

    def test_set_bun(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        assert burger.bun.name == "White bun" and burger.bun.price == 30


    @pytest.mark.parametrize(
    'ingredients, expected_types',
    [
        ([INGREDIENT_TYPE_FILLING], ["FILLING"]),
        ([INGREDIENT_TYPE_SAUCE], ["SAUCE"]),
        (
            [INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE],
            ["FILLING", "SAUCE"]
        ),
    ]
)
    def test_add_ingredients(self, ingredients, expected_types):
        burger = Burger()
        for ingredient_type in ingredients:
            ingredient = Ingredient(ingredient_type, name="Test", price=10.0) 
            burger.add_ingredient(ingredient)
        actual_types = [ingredient.type for ingredient in burger.ingredients]
        assert actual_types == expected_types


    def test_remove_ingredient(self, burger_with_bun_and_two_ingredients):
        burger = burger_with_bun_and_two_ingredients
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1 


    def test_move_ingredient(self, burger_with_bun_and_two_ingredients):
        #список ингредиентов изначально по фикстуре: [INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE]
        burger = burger_with_bun_and_two_ingredients
        burger.move_ingredient(1, 0)
        assert burger.ingredients == [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING]

    
    def test_get_price(self):
        bun_mock = Mock()
        ingredient_mock = Mock()
        bun_mock.get_price.return_value = 100
        ingredient_mock.get_price.return_value = 50
        burger = Burger()
        burger.bun = bun_mock
        burger.ingredients = [ingredient_mock]
        assert burger.get_price() == 250


    def test_get_receipt(self):
        burger = Burger()
        bun = Bun("White bun", 30)
        burger.set_buns(bun)
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "sauсe", 20)
        burger.add_ingredient(ingredient)
        receipt = burger.get_receipt()
        expected_receipt = (
            "(==== White bun ====)\n"
            "= sauce sauсe =\n"
            "(==== White bun ====)\n"
            "\n"
            "Price: 80"
        )
        assert receipt == expected_receipt


