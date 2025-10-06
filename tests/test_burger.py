from unittest.mock import Mock
from burger import Burger
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE


class TestBurger:

    def test_add_bun(self):
        burger = Burger()
        bun = Bun("Сезам", 2.0)
        burger.set_buns(bun)
        assert bun == burger.bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "sychuan sauce", 100)

        burger.add_ingredient(ingredient)

        assert ingredient in burger.ingredients

    def test_remove_ingredient_first(self, get_burger_with_ingredients):
        burger, a, b, c = get_burger_with_ingredients

        burger.remove_ingredient(0)

        assert burger.ingredients == [b, c]

    def test_remove_ingredient_middle(self, get_burger_with_ingredients):
        burger, a, b, c = get_burger_with_ingredients

        burger.remove_ingredient(1)

        assert burger.ingredients == [a, c]

    def test_remove_ingredient_last(self, get_burger_with_ingredients):
        burger, a, b, c = get_burger_with_ingredients

        burger.remove_ingredient(2)

        assert burger.ingredients == [a, b]

    def test_move_ingredient(self, get_burger_with_ingredients):
        burger, a, b, c = get_burger_with_ingredients

        burger.move_ingredient(0, 1)

        assert burger.ingredients == [b, a, c]

    def test_get_price_only_bun_doubles_price(self):
        burger = Burger()
        bun = Mock()
        bun.get_price.return_value = 2.0
        burger.set_buns(bun)

        total = burger.get_price()

        assert total == 4.0
        assert bun.get_price.call_count == 1

    def test_get_price_with_one_ingredient(self):
        burger = Burger()
        bun = Mock()
        bun.get_price.return_value = 2.0
        ing = Mock()
        ing.get_price.return_value = 1.5
        burger.set_buns(bun)
        burger.add_ingredient(ing)

        total = burger.get_price()

        assert total == 5.5
        assert bun.get_price.call_count == 1
        assert ing.get_price.call_count == 1

    def test_get_price_with_multiple_ingredients(self):
        burger = Burger()
        bun = Mock()
        bun.get_price.return_value = 1.0
        ing1 = Mock()
        ing1.get_price.return_value = 0.5
        ing2 = Mock()
        ing2.get_price.return_value = 2.0
        burger.set_buns(bun)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        total = burger.get_price()

        assert total == 4.5
        assert bun.get_price.call_count == 1
        assert ing1.get_price.call_count == 1
        assert ing2.get_price.call_count == 1

    def test_get_receipt_formats_full_receipt(self):
        burger = Burger()
        bun = Mock()
        bun.get_name.return_value = "Sesame"
        bun.get_price.return_value = 2.0
        burger.set_buns(bun)

        ing1 = Mock()
        ing1.get_type.return_value = "SAUCE"
        ing1.get_name.return_value = "BBQ"
        ing1.get_price.return_value = 1.5

        ing2 = Mock()
        ing2.get_type.return_value = "FILLING"
        ing2.get_name.return_value = "Cheese"
        ing2.get_price.return_value = 3.0

        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        receipt = burger.get_receipt()

        expected_total = 2 * 2.0 + 1.5 + 3.0  # 2*булка + сумма ингредиентов
        expected_lines = [
            "(==== Sesame ====)",
            "= sauce BBQ =",
            "= filling Cheese =",
            "(==== Sesame ====)\n",
            f"Price: {expected_total}",
        ]
        expected_receipt = "\n".join(expected_lines)
        assert receipt == expected_receipt
