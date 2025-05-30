from unittest.mock import Mock

from praktikum.burger import Burger


class TestBurger:

    # Тест проверяет начальное состояния бургера (без булочки и ингредиентов)
    def test_initial_state(self, burger):
        assert burger.bun is None
        assert len(burger.ingredients) == 0


    # Тест проверяет корректность установки булочки в бургер и сохраняет её
    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun


   # Тест проверяет успешное добавление ингредиента - соус в бургер
    def test_add_ingredient(self, burger, ingredient_sauce):
        burger.add_ingredient(ingredient_sauce)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient_sauce


    # Тест проверяет успешное удаление ингредиента из бургера
    def test_remove_ingredient(self, burger, ingredient_sauce, ingredient_filling):
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_filling)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient_filling


    # Тест проверяет успешное перемещение ингредиентов (меняется индекс ингредиента)
    def test_move_ingredient(self, burger, ingredient_sauce, ingredient_filling):
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingredient_filling
        assert burger.ingredients[1] == ingredient_sauce

    # Тест проверяет расчет стоимости бургера с учетом булочек и ингредиентов
    def test_get_price(self):
        # Создать мок-объекты
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100

        mock_sauce = Mock()
        mock_sauce.get_price.return_value = 50

        mock_filling = Mock()
        mock_filling.get_price.return_value = 80

        # Протестировать
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        # Вызвать метод, который должен использовать моки

        price = burger.get_price()
        # Проверить вызовы моков
        mock_bun.get_price.assert_called_once()
        mock_sauce.get_price.assert_called_once()
        mock_filling.get_price.assert_called_once()

        # Проверить
        assert price == 330  # Сначала проверяем результат



    # Тест проверяет формирование чека с правильным форматированием
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



    # Тест проверяет чек с моками
    def test_get_receipt_with_mocks(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Test Bun"
        mock_bun.get_price.return_value = 100

        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = "SAUCE"
        mock_ingredient.get_name.return_value = "Test Sauce"
        mock_ingredient.get_price.return_value = 50

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        receipt = burger.get_receipt()

        mock_bun.get_name.assert_called()
        mock_ingredient.get_name.assert_called()

        assert "Test Bun" in receipt
        assert "Test Sauce" in receipt


    # Тест проверяет стоимость бургера без ингредиентов
    def test_empty_burger_price(self, burger, bun):
        burger.set_buns(bun)
        assert burger.get_price() == bun.get_price() * 2


    # Тест проверяет чек для бургера без ингредиентов
    def test_empty_burger_receipt(self, burger, bun):
        burger.set_buns(bun)
        expected_receipt = (
            f'(==== {bun.get_name()} ====)\n'
            f'(==== {bun.get_name()} ====)\n\n'
            f'Price: {burger.get_price()}'
        )
        assert burger.get_receipt() == expected_receipt
