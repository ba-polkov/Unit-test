import pytest
from unittest.mock import Mock


class TestBurger:

    def test_set_buns(self, burger, bun_mock): # тест добавления булочки
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    def test_add_ingredient(self, burger, sauce_mock): # тест добавления ингредиента в бургер
        burger.add_ingredient(sauce_mock)
        assert sauce_mock in burger.ingredients
        assert len(burger.ingredients) == 1

    def test_remove_ingredient(self, burger, sauce_mock, filling_mock): # тест удаления ингредиента
        burger.ingredients = [sauce_mock, filling_mock]
        burger.remove_ingredient(0)
        assert burger.ingredients.count(sauce_mock) == 0
        assert burger.ingredients.count(filling_mock) == 1

    def test_remove_invalid_index(self, burger, sauce_mock): # тест невалидных индексов при удалении ингредиента
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)

        burger.add_ingredient(sauce_mock)
        with pytest.raises(IndexError):
            burger.remove_ingredient(1)

    def test_move_ingredient(self, burger, sauce_mock, filling_mock): # тест перемещения ингредиента в бургере
        burger.add_ingredient(sauce_mock)
        burger.add_ingredient(filling_mock)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == filling_mock
        assert burger.ingredients[1] == sauce_mock

    @pytest.mark.parametrize("bun_price, ingredients_prices, expected", [
        (100, [], 200),
        (200, [50], 450),
        (150, [100, 200], 600),
        (0, [0, 0], 0),
        (300, [150, 250, 100], 1100)
    ])
    def test_get_price(self, burger, bun_mock, bun_price, ingredients_prices, expected): # тест расчета цены с использованием параметризации
        bun_mock.get_price.return_value = bun_price
        ingredients = []
        for price in ingredients_prices:
            ingredient = Mock()
            ingredient.get_price.return_value = price
            ingredients.append(ingredient)

        burger.set_buns(bun_mock)
        for ingredient in ingredients:
            burger.add_ingredient(ingredient)

        assert burger.get_price() == expected

    def test_get_receipt(self, burger, bun_mock, sauce_mock, filling_mock): # тест получения чека
        burger.set_buns(bun_mock)
        burger.add_ingredient(sauce_mock)
        burger.add_ingredient(filling_mock)

        expected = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "= filling cutlet =\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 400"
        )
        assert burger.get_receipt() == expected

