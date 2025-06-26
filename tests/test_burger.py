import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    def test_empty_burger(self):
        burger = Burger()
        assert burger.bun is None and burger.ingredients == []

    def test_set_buns(self):
        burger = Burger()
        bun = Bun("Булка", 100.3)
        burger.set_buns(bun)
        assert burger.bun.get_name() == "Булка" and burger.ingredients == []

    @pytest.mark.parametrize("bun_price, burger_price", [
        (0.0, 0.0),
        (100.0, 200.0),
        (100.3, 200.6)
    ])
    def test_burger_price_without_ingredients(self, bun_price, burger_price):
        burger = Burger()
        bun = Bun("Булка", bun_price)
        burger.set_buns(bun)
        assert burger.get_price() == pytest.approx(burger_price)

    def test_add_one_ingredient(self):
        burger = Burger()
        ingredient_sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "Цезарь", 100.3)
        burger.add_ingredient(ingredient_sauce)
        assert burger.bun is None and burger.ingredients == [ingredient_sauce]

    def test_burger_price_with_one_ingredient(self):
        burger = Burger()
        bun = Bun("Булка", 100.3)
        ingredient_sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "Цезарь", 100.3)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_sauce)
        assert burger.get_price() == 300.9

    def test_add_more_than_one_ingredients(self):
        burger = Burger()
        ingredient_sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "Цезарь", 100.3)
        ingredient_filling = Ingredient(INGREDIENT_TYPE_FILLING, "Котлета", 200.3)
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_filling)
        assert burger.bun is None and burger.ingredients == [ingredient_sauce, ingredient_filling]

    def test_burger_price_with_more_than_one_ingredients(self):
        burger = Burger()
        bun = Bun("Булка", 100.3)
        ingredient_sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "Цезарь", 100.3)
        ingredient_filling = Ingredient(INGREDIENT_TYPE_FILLING, "Котлета", 200.3)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_filling)
        assert burger.get_price() == 501.2

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient_sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "Цезарь", 100.3)
        burger.add_ingredient(ingredient_sauce)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_remove_invalid_index_ingredient(self):
        burger = Burger()
        with pytest.raises(IndexError):
            burger.remove_ingredient(5)

    def test_burger_price_after_remove_ingredient(self):
        burger = Burger()
        bun = Bun("Булка", 100.3)
        ingredient_sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "Цезарь", 100.3)
        ingredient_filling = Ingredient(INGREDIENT_TYPE_FILLING, "Котлета", 200.3)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_filling)
        burger.remove_ingredient(0)
        assert burger.get_price() == 400.9

    def test_move_ingredient(self):
        burger = Burger()
        ingredient_sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "Цезарь", 100.3)
        ingredient_filling = Ingredient(INGREDIENT_TYPE_FILLING, "Котлета", 200.3)
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_filling)
        burger.move_ingredient(0,1)
        assert burger.ingredients == [ingredient_filling, ingredient_sauce]

    def test_move_invalid_index_ingredient(self):
        burger = Burger()
        with pytest.raises(IndexError):
            burger.move_ingredient(0, 5)

    def test_burger_price_after_move_ingredients(self):
        burger = Burger()
        bun = Bun("Булка", 100.3)
        ingredient_sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "Цезарь", 100.3)
        ingredient_filling = Ingredient(INGREDIENT_TYPE_FILLING, "Котлета", 200.3)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_filling)
        burger.move_ingredient(0, 1)
        assert burger.get_price() == 501.2

    def test_get_receipt_without_ingredients(self):
        burger = Burger()
        bun = Bun("Булка", 100.3)
        burger.set_buns(bun)
        expected_result = (
            f"(==== {bun.get_name()} ====)\n"
            f"(==== {bun.get_name()} ====)\n\n"
            f"Price: {burger.get_price()}"
        )
        assert burger.get_receipt() == expected_result

    def test_get_receipt_with_ingredients(self):
        burger = Burger()
        bun = Bun("Булка", 100.3)
        ingredient_sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "Цезарь", 100.3)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_sauce)
        expected_result = (
            f"(==== {bun.get_name()} ====)\n"
            f"= {ingredient_sauce.get_type().lower()} {ingredient_sauce.get_name()} =\n"
            f"(==== {bun.get_name()} ====)\n\n"
            f"Price: {burger.get_price()}"
        )
        assert burger.get_receipt() == expected_result