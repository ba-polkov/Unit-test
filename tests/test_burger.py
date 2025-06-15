from praktikum.burger import Burger

class TestBurger:

    def test_burger_price(self, bun, ingredients):
        burger = Burger()
        burger.set_buns(bun)
        for ing in ingredients:
            burger.add_ingredient(ing)

        expected_price = bun.get_price() * 2 + sum(i.get_price() for i in ingredients)
        assert burger.get_price() == expected_price

    def test_burger_receipt_format(self, bun, ingredients):
        burger = Burger()
        burger.set_buns(bun)
        for ing in ingredients:
            burger.add_ingredient(ing)
        
        receipt = burger.get_receipt()
        assert bun.get_name() in receipt
        for ing in ingredients:
            assert ing.get_name() in receipt
        assert "Price:" in receipt

    def test_remove_ingredient(self, ingredients, bun):
        burger = Burger()
        burger.set_buns(bun)
        for ing in ingredients:
            burger.add_ingredient(ing)

        burger.remove_ingredient(1)
        assert len(burger.ingredients) == 2
        assert ingredients[1] not in burger.ingredients

    def test_move_ingredient(self, ingredients, bun):
        burger = Burger()
        burger.set_buns(bun)
        for ing in ingredients:
            burger.add_ingredient(ing)

        burger.move_ingredient(0, 2)
        assert burger.ingredients[2].get_name() == ingredients[0].get_name()
