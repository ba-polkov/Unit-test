import allure

class TestBurger:

    @allure.title('Тест проверяет начальное состояния бургера (без булочки и ингредиентов)')
    def test_initial_state(self, burger):
        assert burger.bun is None
        assert len(burger.ingredients) == 0


    @allure.title('Тест проверяет корректность установки булочки в бургер и сохраняет её')
    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun


    @allure.title('Тест проверяет успешное добавление ингредиента  - соус в бургер')
    def test_add_ingredient(self, burger, ingredient_sauce):
        burger.add_ingredient(ingredient_sauce)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient_sauce


    @allure.title('Тест проверяет успешное удаление ингредиента из бургера')
    def test_remove_ingredient(self, burger, ingredient_sauce, ingredient_filling):
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_filling)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient_filling


    @allure.title('Тест проверяет успешное перемещение ингредиентов (меняется индекс ингредиента)')
    def test_move_ingredient(self, burger, ingredient_sauce, ingredient_filling):
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingredient_filling
        assert burger.ingredients[1] == ingredient_sauce


    @allure.title('Тест проверяет расчет стоимости бургера с учетом булочек и ингредиентов')
    def test_get_price(self, burger, bun, ingredient_sauce, ingredient_filling):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_filling)
        expected_price = bun.get_price() * 2 + ingredient_sauce.get_price() + ingredient_filling.get_price()
        assert burger.get_price() == expected_price


    @allure.title('Тест проверяет формирование чека с правильным форматированием')
    def test_get_receipt(self, burger, bun, ingredient_sauce, ingredient_filling):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_filling)

        expected_receipt = (
            f'(==== {bun.get_name()} ====)\n'
            f'= {str(ingredient_sauce.get_type()).lower()} {ingredient_sauce.get_name()} =\n'
            f'= {str(ingredient_filling.get_type()).lower()} {ingredient_filling.get_name()} =\n'
            f'(==== {bun.get_name()} ====)\n\n'
            f'Price: {burger.get_price()}'
        )

        assert burger.get_receipt() == expected_receipt

    @allure.title('Тест проверяет стоимость бургера без ингредиентов')
    def test_empty_burger_price(self, burger, bun):
        burger.set_buns(bun)
        assert burger.get_price() == bun.get_price() * 2


    @allure.title('Тест проверяет чек для бургера без ингредиентов')
    def test_empty_burger_receipt(self, burger, bun):
        burger.set_buns(bun)
        expected_receipt = (
            f'(==== {bun.get_name()} ====)\n'
            f'(==== {bun.get_name()} ====)\n\n'
            f'Price: {burger.get_price()}'
        )
        assert burger.get_receipt() == expected_receipt
