class TestBurger:

# Тест установки булки
    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun
        assert burger.bun.get_name() == 'Булочка'
        assert burger.bun.get_price() == 100

# Тест добавления ингредиента
    def test_add_ingredient(self, burger, mock_ingredient_one):
        burger.add_ingredient(mock_ingredient_one)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient_one
        assert burger.ingredients[-1].get_name() == 'Курица'
        assert burger.ingredients[-1].get_price() == 250

# Тест удаления ингредиента
    def test_remove_ingredient(self, burger, mock_ingredient_one):
        burger.add_ingredient(mock_ingredient_one)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

# Тест перемещения ингредиента
    def test_move_ingredient(self, burger, mock_ingredient_one, mock_ingredient_two):
        burger.add_ingredient(mock_ingredient_one)
        burger.add_ingredient(mock_ingredient_two)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_ingredient_two
        assert burger.ingredients[1] == mock_ingredient_one

# Тест расчета цены бургера
    def test_get_price(self, burger, mock_bun, mock_ingredient_one, mock_ingredient_two):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_one)
        burger.add_ingredient(mock_ingredient_two)
        # Цена булочки (100) * 2 + курица (250) + кетчуп (90) = 540
        assert burger.get_price() == 540

# Тест формирования чека
    def test_get_receipt(self, burger, mock_bun, mock_ingredient_one, mock_ingredient_two):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_one)
        burger.add_ingredient(mock_ingredient_two)
        receipt = burger.get_receipt()
        expected_receipt = (
            '(==== Булочка ====)\n'
            '= filling Курица =\n'
            '= sauce Кетчуп =\n'
            '(==== Булочка ====)\n'
            '\n'
            'Price: 540'
            )
        assert receipt == expected_receipt
       # print(burger.get_receipt())
