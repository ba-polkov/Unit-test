from src.bun import Bun
from src.burger import Burger
from src.ingredient import Ingredient
from src.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestBurger:
    def test_burger_initialization(self):
        burger = Burger()
        assert burger.ingredients == []
        assert burger.bun is None

    def test_burger_set_buns_to_burger(self):
        black_bun = Bun("black bun", 100)
        burger = Burger()
        burger.set_buns(black_bun)
        assert burger.bun == black_bun

    def test_burger_add_ingredient(self):
        burger = Burger()
        hot_sauce_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50)
        burger.add_ingredient(hot_sauce_ingredient)
        assert hot_sauce_ingredient in burger.ingredients

    def test_burger_remove_ingredient(self):
        burger = Burger()
        hot_sauce_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50)
        burger.add_ingredient(hot_sauce_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_burger_move_ingredient(self):
        burger = Burger()
        sour_cream_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200)
        hot_sauce_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50)
        burger.add_ingredient(sour_cream_ingredient)
        burger.add_ingredient(hot_sauce_ingredient)
        burger.move_ingredient(1, 0)
        assert burger.ingredients == [hot_sauce_ingredient, sour_cream_ingredient]

    def test_burger_get_price(self):
        burger = Burger()
        sour_cream_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200)
        hot_sauce_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50)
        black_bun = Bun("black bun", 100)
        burger.set_buns(black_bun)
        burger.add_ingredient(sour_cream_ingredient)
        burger.add_ingredient(hot_sauce_ingredient)
        expected_price = black_bun.get_price() * 2 + sour_cream_ingredient.get_price() + hot_sauce_ingredient.get_price()
        assert burger.get_price() == expected_price

    def test_burger_get_receipt(self):
        burger = Burger()
        hot_sauce_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50)
        black_bun = Bun("black bun", 100)
        burger.set_buns(black_bun)
        burger.add_ingredient(hot_sauce_ingredient)
        receipt = burger.get_receipt()
        expected_receipt = (f'(==== {black_bun.get_name()} ====)\n'
                            f'= sauce {hot_sauce_ingredient.get_name()} =\n'
                            f'(==== {black_bun.get_name()} ====)\n'
                            '\n'
                            f'Price: {burger.get_price()}')
        assert receipt == expected_receipt
