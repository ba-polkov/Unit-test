import pytest
import allure
from praktikum.burger import Burger


class TestBurger:
    @allure.title('Добавление булочки в бургер')
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    @allure.title('Добавление ингредиентов в бургер')
    @pytest.mark.parametrize('ingredient', ['sauce', 'filling'])
    def test_add_ingredient(self, ingredient, request):
        burger = Burger()
        mock_ingredient = request.getfixturevalue(f'mock_{ingredient}')
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    @allure.title('Удаление ингредиента из бургера')
    def test_remove_ingredient(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(0)
        assert mock_sauce not in burger.ingredients
        assert len(burger.ingredients) == 1

    @allure.title('Перемещение ингредиента в бургере')
    def test_move_ingredient(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_filling, mock_sauce]

    @allure.title('Расчет стоимости бургера')
    def test_get_price(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        expected_price = (
                mock_bun.get_price() * 2 +
                mock_sauce.get_price() +
                mock_filling.get_price()
        )

        assert burger.get_price() == expected_price

    @allure.title('Формирование чека')
    def test_get_receipt(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        receipt = burger.get_receipt()

        assert f'(==== {mock_bun.get_name()} ====)' in receipt
        assert f'= {mock_sauce.get_type().lower()} {mock_sauce.get_name()} =' in receipt
        assert f'= {mock_filling.get_type().lower()} {mock_filling.get_name()} =' in receipt
        assert f'Price: {burger.get_price()}' in receipt