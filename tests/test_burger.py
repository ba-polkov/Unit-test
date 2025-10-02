import pytest
from unittest.mock import Mock


class TestBurger:


    # Добавляем булочку к бургеру
    def test_sets_bun_correctly(self, burger, bun):
        burger.set_buns(bun)
        assert burger.buns == bun

    # Добавляем ингредиент в бургер (соус)
    def test_ingredient_adds_to_list(self, burger, ingredient_sauce):
        burger.add_ingredient(ingredient_sauce)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient_sauce

    # Удаляем ингредиент по индексу
    def test_ingredient_removes_by_index(self, burger):
        ingredient1 = Mock()
        ingredient2 = Mock()
        burger.ingredients = [ingredient1, ingredient2]
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient2

    # Меняем местами ингредиенты
    def test_move_ingredient_changes_position(self, burger):
        ingredient1 = Mock()
        ingredient2 = Mock()
        burger.ingredients = [0, 1]
        assert burger.ingredients[0] == ingredient2
        assert burger.ingredients[1] == ingredient1

    # Считаем цену бургера без ингредиентов
    def test_get_price_with_only_bun(self, burger):
        mock_bun = Mock()
        mock_bun.get_price = Mock(return_value=100)
        burger.bun = mock_bun
        burger.ingredients = []
        assert burger.get_price() == 200

    # Считаем цену бургера с ингредиентами
    def test_get_price_with_ingredients(self, burger):
        mock_bun = Mock()
        mock_bun.get_price = Mock(return_value=100)

        mock_ingredients1 = Mock()
        mock_ingredients1.get_price = Mock(return_value=50)
        mock_ingredients2 = Mock()
        mock_ingredients2.get_price = Mock(return_value=75)

        burger.bun = mock_bun
        burger.ingredients = [mock_ingredients1, mock_ingredients2]
        assert burger.get_price() == 325

    # Проверяем формирование чека для бургера с ингредиентами
    def test_get_receipt_with_ingredients_returns_correct_format(self, burger):
        mock_bun = Mock()
        mock_bun.get_price = Mock(return_value= 'black bun')

        mock_ingredients1 = Mock()
        mock_ingredients1.get_type.return_value = 'SAUCE'
        mock_ingredients1.get_name.return_value = 'hot sauce'

        mock_ingredients2 = Mock()
        mock_ingredients2.get_type.return_value = 'FILLING'
        mock_ingredients2.get_name.return_value = 'cutlet'

        burger.bun = mock_bun
        burger.ingredients = [mock_ingredients1, mock_ingredients2]

        burger.get_price = Mock(return_value=400)

        receipt = burger.get_receipt()

        assert '(==== black bun ====)' in receipt
        assert '= sauce hot sauce =' in receipt
        assert '= filling cutlet =' in receipt
        assert 'Price: 400' in receipt

    # Проверяем формирование чека для бургера без ингредиентов
    def test_get_receipt_without_ingredients_returns_correct_format(self, burger):
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'white bun'
        burger.bun = mock_bun
        burger.ingredients = []

        burger.get_price = Mock(return_value=200)

        receipt = burger.get_receipt()

        lines = receipt.split('\n')
        assert lines[0] == '(==== white bun ====)'
        assert lines[1] == '(==== white bun ====)'
        assert lines[3] == 'Price: 200'

    # Удаление несуществующего ингредиента
    def test_remove_ingredient_with_invalid_index_raises_error(self, burger):
        burger.ingredients = []
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)

    # Меняем местами несуществующий ингредиент
    def test_move_ingredient_with_invalid_index_raises_error(self, burger):
        burger.ingredients = []
        with pytest.raises(IndexError):
            burger.move_ingredient(0, 1)

    #  Параметризованный тест: расчет цены с разными комбинациями
    @pytest.mark.parametrize('bun_price, ingredient_prices, expected_total',
                             [
                                (100, [], 200),
                                (150, [50], 350),
                                (200, [100, 200], 700),
                             ]
                             )
    def test_get_price_calculates_correctly(self, burger, bun_price, ingredient_prices, expected_total):
        mock_bun = Mock()
        mock_bun.get_price = Mock(return_value=bun_price)

        mock_ingredients = []
        for price in ingredient_prices:
            mock_ingredient = Mock()
            mock_ingredient.get_price.return_value = price
            mock_ingredients.append(mock_ingredient)

        burger.bun = mock_bun
        burger.ingredients = mock_ingredients

        assert burger.get_price() == expected_total
