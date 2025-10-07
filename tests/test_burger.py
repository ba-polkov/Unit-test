import sys
import os
import pytest
from unittest.mock import Mock
# Добавляем корень проекта в путь Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data import BunData, IngredientData, ExpectedResults
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    # Добавляем булочку к бургеру с использованием фикстуры mock_bun
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    # Добавляем ингредиент в бургер (соус) с использованием фикстуры mock_ingredient_sauce
    def test_add_ingredient_sauce(self, mock_ingredient_sauce):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_sauce)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient_sauce

    # Добавляем ингредиент в бургер (начинка) с использованием фикстуры mock_ingredient_filling
    def test_add_ingredient_filling(self, mock_ingredient_filling):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_filling)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient_filling

    # Удаляем ингредиент по индексу с использованием фикстур mock_ingredient_sauce и mock_ingredient_filling
    def test_remove_ingredient(self, mock_ingredient_sauce, mock_ingredient_filling):
        burger = Burger()
        burger.ingredients = [mock_ingredient_sauce, mock_ingredient_filling]
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient_filling

    # Меняем местами ингредиенты с использованием фикстур mock_ingredient_sauce и mock_ingredient_filling
    def test_move_ingredient(self, mock_ingredient_sauce, mock_ingredient_filling):
        burger = Burger()
        burger.ingredients = [mock_ingredient_sauce, mock_ingredient_filling]
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_ingredient_filling
        assert burger.ingredients[1] == mock_ingredient_sauce

    # Считаем цену бургера без ингредиентов с использованием фикстуры mock_bun
    def test_get_price_only_bun(self, mock_bun):
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = []
        assert burger.get_price() == ExpectedResults.BURGER_PRICE_ONLY_BUN

    # Считаем цену бургера с ингредиентами с использованием фикстур mock_bun, mock_ingredient_sauce, mock_ingredient_filling
    def test_get_price_with_ingredients(self, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient_sauce, mock_ingredient_filling]
        assert burger.get_price() == ExpectedResults.BURGER_PRICE_WITH_INGREDIENTS

    # Проверяем формирование чека для бургера с ингредиентами с использованием фикстур mock_bun, mock_ingredient_sauce, mock_ingredient_filling
    def test_get_receipt_with_ingredients_returns_correct_format(self, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient_sauce, mock_ingredient_filling]

        burger.get_price = Mock(return_value=ExpectedResults.BURGER_PRICE_WITH_INGREDIENTS)

        receipt = burger.get_receipt()
        assert receipt == ExpectedResults.RECEIPT_WITH_INGREDIENTS

    # Проверяем формирование чека для бургера без ингредиентов с использованием фикстуры mock_bun
    def test_get_receipt_without_ingredients_returns_correct_format(self, mock_bun):
        burger = Burger()
        mock_bun.get_name.return_value = BunData.WHITE_BUN[0]
        burger.bun = mock_bun
        burger.ingredients = []

        burger.get_price = Mock(return_value=ExpectedResults.BURGER_PRICE_ONLY_BUN)

        receipt = burger.get_receipt()
        assert receipt == ExpectedResults.RECEIPT_WITHOUT_INGREDIENTS

    # Удаление несуществующего ингредиента
    def test_remove_ingredient_with_invalid_index_raises_error(self):
        burger = Burger()
        burger.ingredients = []
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)

    # Меняем местами несуществующий ингредиент
    def test_move_ingredient_with_invalid_index_raises_error(self):
        burger = Burger()
        burger.ingredients = []
        with pytest.raises(IndexError):
            burger.move_ingredient(0, 1)

    # Тестируем готовый бургер из фикстуры burger_with_mocks
    def test_burger_with_mocks_fixture(self, burger_with_mocks):
        assert burger_with_mocks.bun is not None
        assert len(burger_with_mocks.ingredients) == 2
        assert burger_with_mocks.get_price() == ExpectedResults.BURGER_PRICE_WITH_INGREDIENTS

    # Параметризованный тест: расчет цены с разными комбинациями
    @pytest.mark.parametrize('bun_price, ingredient_prices, expected_total',
                             [
                                (100, [], 200),
                                (150, [50], 350),
                                (200, [100, 200], 700),
                             ]
                             )
    def test_get_price_calculates_correctly(self, bun_price, ingredient_prices, expected_total):
        burger = Burger()
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
