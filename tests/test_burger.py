import pytest
from unittest.mock import Mock
from data.data import buns_name_and_price, ingredients_type_name_and_price
from praktikum.burger import Burger


class TestBurger:

    @pytest.mark.parametrize("bun_name, bun_price", buns_name_and_price)
    def test_set_buns_sets_burger_bun(self, bun_name, bun_price):
        mock_bun = Mock()
        mock_bun.name = bun_name
        mock_bun.price = bun_price
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun.name == bun_name
        assert burger.bun.price == bun_price

    def test_add_ingredient_adds_to_list(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    @pytest.mark.parametrize("ingredient_type, ingredient_name, ingredient_price", ingredients_type_name_and_price)
    def test_add_ingredient_sets_correct_data(self, ingredient_type, ingredient_name, ingredient_price):
        mock_ingredient = Mock()
        mock_ingredient.type = ingredient_type
        mock_ingredient.name = ingredient_name
        mock_ingredient.price = ingredient_price

        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        ingredient = burger.ingredients[0]
        assert ingredient.type == ingredient_type
        assert ingredient.name == ingredient_name
        assert ingredient.price == ingredient_price

    def test_remove_ingredient_removes_by_index(self):
        burger = Burger()
        ingredients1 = Mock()
        ingredients2 = Mock()
        burger.ingredients = [ingredients1, ingredients2]
        burger.remove_ingredient(0)
        assert burger.ingredients == [ingredients2]

    def test_move_ingredient_changes_order(self):
        burger = Burger()
        ingredients1 = Mock()
        ingredients2 = Mock()
        burger.ingredients = [ingredients1, ingredients2]
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredients2, ingredients1]

    def test_get_price_returns_correct_total(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100.0

        ingredients1 = Mock()
        ingredients1.get_price.return_value = 50.0
        ingredients2 = Mock()
        ingredients2.get_price.return_value = 75.0

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(ingredients1)
        burger.add_ingredient(ingredients2)

        expected = 100.0 * 2 + 50.0 + 75.0
        assert burger.get_price() == expected

    def test_get_receipt_returns_formatted_string(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Булка Тестовая"
        mock_bun.get_price.return_value = 500.0

        ingredients1 = Mock()
        ingredients1.get_type.return_value = "SAUCE"
        ingredients1.get_name.return_value = "Соус Огонь"
        ingredients1.get_price.return_value = 90.0

        ingredients2 = Mock()
        ingredients2.get_type.return_value = "FILLING"
        ingredients2.get_name.return_value = "Начинка Бургерная"
        ingredients2.get_price.return_value = 110.0

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(ingredients1)
        burger.add_ingredient(ingredients2)

        burger.get_price = Mock(return_value=1200.0)

        expected = (
            f"(==== Булка Тестовая ====)\n"
            f"= sauce Соус Огонь =\n"
            f"= filling Начинка Бургерная =\n"
            f"(==== Булка Тестовая ====)\n"
            f"\n"
            f"Price: 1200.0"
        )

        assert burger.get_receipt() == expected