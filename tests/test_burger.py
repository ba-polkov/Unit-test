from bun import Bun
from burger import Burger
from faker import Faker

from ingredient import Ingredient

fake = Faker()

class TestBurger:
    def test_set_bun(self):
        bun = Bun("black bun", 100)
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        ingredient = Ingredient("SAUCE", "hot sauce", 100)
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    def test_remove_ingredient(self):
        ingredient = Ingredient("SAUCE", "hot sauce", 100)
        burger = Burger()
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len (burger.ingredients) == 0

    def test_move_ingredient(self):
        ingredient = Ingredient("SAUCE", "hot sauce", 100)
        ingredient_2 = Ingredient("FILLING", "cutlet", 100)
        burger = Burger()
        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == ingredient

    def test_get_price(self):
        burger = Burger()
        bun = Bun("black bun", 100)
        burger.set_buns(bun)
        ingredient = Ingredient("SAUCE", "sour cream", 200)
        burger.add_ingredient(ingredient)
        assert burger.get_price() == bun.price * 2 + ingredient.price

    def test_get_receipt(self, mock_bun, mock_ingredient):
        burger = Burger()

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        assert (burger.get_receipt() ==
f"""(==== {mock_bun.get_name()} ====)
= {mock_ingredient.get_type()} {mock_ingredient.get_name()} =
(==== {mock_bun.get_name()} ====)

Price: {burger.get_price()}""")





