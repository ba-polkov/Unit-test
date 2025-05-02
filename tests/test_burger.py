class TestBurger:

    def test_set_buns(self, bun, burger):
        burger = burger
        burger.set_buns(bun)

        assert burger.bun.name == 'Mike'

    def test_add_ingredient(self, burger):
        burger = burger
        assert (burger.ingredients[0].type == 'SAUCE' and burger.ingredients[0].name == 'Соус'
                and burger.ingredients[0].price == 60)