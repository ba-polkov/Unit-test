from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        bun = Bun("Test Bun", 100)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_and_remove_ingredient(self):
        burger = Burger()
        ingredient = Mock(spec=Ingredient)
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients
        burger.remove_ingredient(0)
        assert ingredient not in burger.ingredients

    def test_move_ingredient(self):
        burger = Burger()
        ing1 = Mock(spec=Ingredient)
        ing2 = Mock(spec=Ingredient)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == ing1

    def test_get_price(self):
        bun = Mock(spec=Bun)
        bun.get_price.return_value = 50

        ing1 = Mock(spec=Ingredient)
        ing1.get_price.return_value = 30
        ing2 = Mock(spec=Ingredient)
        ing2.get_price.return_value = 20

        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        assert burger.get_price() == 150

    def test_get_receipt_exact_match(self):
        bun = Mock(spec=Bun)
        bun.get_name.return_value = "Test Bun"
        bun.get_price.return_value = 100

        ing = Mock(spec=Ingredient)
        ing.get_name.return_value = "Cheese"
        ing.get_type.return_value = "FILLING"
        ing.get_price.return_value = 20

        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ing)
        expected = (
            "(==== Test Bun ====)\n"
            "= filling Cheese =\n"
            "(==== Test Bun ====)\n\n"
            "Price: 220"
        )
        assert burger.get_receipt() == expected
