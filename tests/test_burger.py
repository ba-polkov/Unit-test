import pytest
from unittest.mock import Mock

from data.burger_data import BunsData as buns
from data.burger_data import IngredientsData as ingredients


class TestBurger:
    # в классе TestBurger используются моки для того, чтобы сделать проверки класса Burger
    # независимыми от классов Bun и Ingredient

    @pytest.mark.parametrize(("bun_name", "bun_price"), [buns.BUN_1, buns.BUN_2, buns.BUN_3])
    def test_set_buns(self, burger, bun_name, bun_price):
        bun = Mock()
        bun.get_name.return_value = bun_name
        bun.get_price.return_value = bun_price
        burger.set_buns(bun)
        assert burger.bun == bun
        assert burger.bun.get_name() == bun_name
        assert burger.bun.get_price() == bun_price

    @pytest.mark.parametrize(("ingredient_type", "ingredient_name", "ingredient_price"),
                             [ingredients.SAUCE_1, ingredients.SAUCE_2, ingredients.FILLING_1, ingredients.FILLING_2])
    def test_add_ingredient_one_ingredient(self, burger, ingredient_type, ingredient_name, ingredient_price):
        ingredient = Mock()
        ingredient.get_type.return_value = ingredient_type
        ingredient.get_name.return_value = ingredient_name
        ingredient.get_price.return_value = ingredient_price
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1 and burger.ingredients[0] == ingredient

    def test_add_ingredient_several_ingredients(self, burger, mock_ingredient_sauce, mock_ingredient_filling):
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        assert len(burger.ingredients) == 2

    def test_remove_ingredient(self, burger, mock_ingredient_sauce):
        burger.add_ingredient(mock_ingredient_sauce)
        assert len(burger.ingredients) == 1 and burger.ingredients[0] == mock_ingredient_sauce
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_remove_ingredient_by_index_if_several_ingredients(self, burger_with_mock_ingredients):
        burger_with_mock_ingredients.remove_ingredient(1)
        assert len(burger_with_mock_ingredients.ingredients) == 2
        assert burger_with_mock_ingredients.ingredients[0].get_name() == ingredients.SAUCE_1[1]
        assert burger_with_mock_ingredients.ingredients[1].get_name() == ingredients.FILLING_1[1]

    def test_move_ingredient(self, burger_with_mock_ingredients):
        burger_with_mock_ingredients.move_ingredient(2, 0)
        assert burger_with_mock_ingredients.ingredients[0].get_name() == ingredients.FILLING_1[1]
        assert burger_with_mock_ingredients.ingredients[2].get_name() == ingredients.SAUCE_1[1]

    def test_get_price(self, burger_with_mock_ingredients):
        ingredients_price = 0
        bun_price = burger_with_mock_ingredients.bun.get_price() * 2
        for item in burger_with_mock_ingredients.ingredients:
            ingredients_price += item.get_price()
        expected_price = bun_price + ingredients_price
        price = burger_with_mock_ingredients.get_price()
        assert price == expected_price

    @pytest.mark.parametrize("ingredient_count", [0, 1, 2, 3, 4])
    def test_get_price_depending_on_ing_count(self, burger, mock_bun, mock_ingredient_filling, ingredient_count):
        burger.set_buns(mock_bun)
        for _ in range(ingredient_count):
            burger.add_ingredient(mock_ingredient_filling)
        expected_price = mock_bun.get_price() * 2 + mock_ingredient_filling.get_price() * ingredient_count
        price = burger.get_price()
        assert price == expected_price

    def test_get_receipt_check_bun(self, burger_with_mock_ingredients):
        receipt = burger_with_mock_ingredients.get_receipt()
        bun_name = burger_with_mock_ingredients.bun.get_name.return_value
        assert f"(==== {bun_name} ====)" in receipt

    def test_get_receipt_check_sauce(self, burger_with_mock_ingredients):
        receipt = burger_with_mock_ingredients.get_receipt()
        sauce_name = burger_with_mock_ingredients.ingredients[0].get_name.return_value
        assert f"= sauce {sauce_name} =" in receipt

    def test_get_receipt_check_filling(self, burger_with_mock_ingredients):
        receipt = burger_with_mock_ingredients.get_receipt()
        filling_name = burger_with_mock_ingredients.ingredients[2].get_name.return_value
        assert f"= filling {filling_name} =" in receipt

    def test_get_receipt_check_price(self, burger_with_mock_ingredients):
        receipt = burger_with_mock_ingredients.get_receipt()
        price = burger_with_mock_ingredients.get_price()
        assert f"Price: {price}" in receipt

