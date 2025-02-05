from praktikum.burger import Burger


class TestBurger:

    def test_set_buns_set_buns_success(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun.name == mock_bun.name

    def test_add_ingredient_add_success(self, mock_ingredients):
        burger = Burger()
        burger.add_ingredient(mock_ingredients)
        assert  mock_ingredients in burger.ingredients

    def test_remove_ingredient_remove_success(self):
        burger = Burger()
        burger.ingredients = ['ингридиент', 'ингридиент2']
        burger.remove_ingredient(0)
        assert burger.ingredients == ['ингридиент2']

    def test_move_ingredient_move_success(self):
        burger = Burger()
        burger.ingredients = ['ингридиент', 'ингридиент2']
        burger.move_ingredient(0,1 )
        print(burger.ingredients)
        assert burger.ingredients == ['ингридиент2', 'ингридиент']

    def test_get_price_get_price_success(self, mock_bun, mock_ingredients):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredients)
        assert burger.get_price() == mock_bun.price * 2 + mock_ingredients.price

    def test_get_receipt_get_receipt_success(self, mock_bun, mock_ingredients):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredients)

        assert (burger.get_receipt() == f'(==== {burger.bun.name} ====)\n' 
                                        f'= {mock_ingredients.type.lower()} {mock_ingredients.name} =\n(==== {burger.bun.name} '
                                        f'====)\n\nPrice: {burger.get_price()}')

