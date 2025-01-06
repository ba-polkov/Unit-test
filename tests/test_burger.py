from praktikum.burger import Burger


class TestBurger:

    def test_set_buns_set_buns_success(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun.name == 'name'

    def test_add_ingredient_add_success(self):
        burger = Burger()
        burger.add_ingredient('ингридиент')
        assert  'ингридиент' in burger.ingredients