import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


class TestBurger:

    def test_set_buns(self):

        burger = Burger()
        assert burger.bun is None
        bun = Bun("Sesame", 2.5)
        burger.set_buns(bun)
        assert burger.bun is not None
        assert burger.bun == bun

    def test_add_ingredient(self):

        burger = Burger()
        ingredient = Ingredient("filling", "Cheese", 1.0)
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient(self):

        burger = Burger()
        ingredient1 = Ingredient("filling", "Cheese", 1.0)
        ingredient2 = Ingredient("sauce", "Ketchup", 0.5)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient2

    def test_move_ingredient(self):

        burger = Burger()
        ingredient1 = Ingredient("filling", "Cheese", 1.0)
        ingredient2 = Ingredient("filling", "Lettuce", 0.5)
        ingredient3 = Ingredient("sauce", "Mayo", 0.3)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)
        burger.move_ingredient(2, 0)
        assert burger.ingredients[0] == ingredient3
        assert burger.ingredients[1] == ingredient1
        assert burger.ingredients[2] == ingredient2

    @pytest.mark.parametrize("bun_price, ingredients, expected_price", [
        (2.5, [("filling", "Cheese", 1.0), ("sauce", "Ketchup", 0.5)], 6.5),
        (3.0, [("filling", "Lettuce", 0.7)], 6.7),
        (1.5, [], 3.0),
    ])
    def test_get_price(self, bun_price, ingredients, expected_price):

        burger = Burger()
        bun = Bun("Test Bun", bun_price)
        burger.set_buns(bun)
        for ingredient_type, name, price in ingredients:
            ingredient = Ingredient(ingredient_type, name, price)
            burger.add_ingredient(ingredient)
        assert burger.get_price() == expected_price

    @pytest.mark.parametrize("bun_name, bun_price, ingredients, expected_receipt", [
        (
            "Sesame", 2.5, [("filling", "Cheese", 1.0), ("sauce", "Ketchup", 0.5)],
            "(==== Sesame ====)\n= filling Cheese =\n= sauce Ketchup =\n(==== Sesame ====)\n\nPrice: 6.5"
        ),
        (
            "White", 1.5, [],
            "(==== White ====)\n(==== White ====)\n\nPrice: 3.0"
        ),
    ])
    def test_get_receipt(self, bun_name, bun_price, ingredients, expected_receipt):

        burger = Burger()
        bun = Bun(bun_name, bun_price)
        burger.set_buns(bun)
        for ingredient_type, name, price in ingredients:
            ingredient = Ingredient(ingredient_type, name, price)
            burger.add_ingredient(ingredient)
        assert burger.get_receipt() == expected_receipt