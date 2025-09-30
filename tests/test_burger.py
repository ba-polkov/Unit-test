import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest  # noqa: E402
from unittest.mock import Mock  # noqa: E402
from praktikum.burger import Burger  # noqa: E402
from praktikum.bun import Bun  # noqa: E402
from praktikum.ingredient import Ingredient  # noqa: E402
from praktikum.ingredient_types import (  # noqa: E402
    INGREDIENT_TYPE_SAUCE,
    INGREDIENT_TYPE_FILLING
)


class TestBurger:
    """Тесты для класса Burger с мокированием зависимостей Bun и Ingredient."""

    def test_burger_initialization(self, empty_burger):
        """Тест инициализации пустого бургера."""
        burger = empty_burger

        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self, empty_burger, mock_bun):
        """Тест установки булки в бургер."""
        burger = empty_burger

        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_add_ingredient(self, empty_burger, mock_ingredient):
        """Тест добавления ингредиента в бургер."""
        burger = empty_burger

        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self):
        """Тест удаления ингредиента из бургера."""
        burger = Burger()
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient2 = Mock(spec=Ingredient)

        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        assert len(burger.ingredients) == 2

        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient2

    def test_remove_ingredient_invalid_index(self):
        """Тест удаления ингредиента с некорректным индексом."""
        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)
        burger.add_ingredient(mock_ingredient)

        with pytest.raises(IndexError):
            burger.remove_ingredient(5)

    def test_move_ingredient(self):
        """Тест перемещения ингредиента в бургере."""
        burger = Burger()
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient3 = Mock(spec=Ingredient)

        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.add_ingredient(mock_ingredient3)

        burger.move_ingredient(0, 2)

        assert burger.ingredients[0] == mock_ingredient2
        assert burger.ingredients[1] == mock_ingredient3
        assert burger.ingredients[2] == mock_ingredient1

    def test_move_ingredient_invalid_index(self):
        """Тест перемещения ингредиента с некорректными индексами."""
        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)
        burger.add_ingredient(mock_ingredient)

        with pytest.raises(IndexError):
            burger.move_ingredient(5, 0)

    @pytest.mark.parametrize("bun_price, ingredient_prices, expected_total", [
        (100.0, [50.0, 75.0], 325.0),  # 2 * 100 + 50 + 75 = 325
        (200.0, [100.0], 500.0),       # 2 * 200 + 100 = 500
        (0.0, [0.0, 0.0, 0.0], 0.0),   # 2 * 0 + 0 + 0 + 0 = 0
        (150.5, [25.25, 50.75], 377.0),  # 2 * 150.5 + 25.25 + 50.75 = 377.0
    ])
    def test_get_price(self, bun_price, ingredient_prices, expected_total):
        """Тест расчета цены бургера с параметризацией."""
        burger = Burger()

        # Мокаем булку
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        # Добавляем ингредиенты с указанными ценами
        for price in ingredient_prices:
            mock_ingredient = Mock(spec=Ingredient)
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == expected_total

    def test_get_price_no_bun(self):
        """Тест расчета цены бургера без булки."""
        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_price.return_value = 100.0
        burger.add_ingredient(mock_ingredient)

        # Цена должна быть только от ингредиентов (без булки)
        assert burger.get_price() == 100.0

    def test_get_price_no_ingredients(self):
        """Тест расчета цены бургера без ингредиентов."""
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = 200.0
        burger.set_buns(mock_bun)

        # Цена должна быть только от двух булок
        assert burger.get_price() == 400.0

    def test_get_receipt(self):
        """Тест получения чека бургера."""
        burger = Burger()

        # Мокаем булку
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "white bun"
        mock_bun.get_price.return_value = 100.0  # Добавляем цену для расчета
        burger.set_buns(mock_bun)

        # Мокаем ингредиенты
        mock_sauce = Mock(spec=Ingredient)
        mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_sauce.get_name.return_value = "ketchup"
        mock_sauce.get_price.return_value = 50.0

        mock_filling = Mock(spec=Ingredient)
        mock_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_filling.get_name.return_value = "cutlet"
        mock_filling.get_price.return_value = 150.0

        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        receipt = burger.get_receipt()

        assert "(==== white bun ====)" in receipt
        assert "= sauce ketchup =" in receipt
        assert "= filling cutlet =" in receipt
        assert "Price:" in receipt

    def test_get_receipt_no_bun(self):
        """Тест получения чека бургера без булки."""
        burger = Burger()

        with pytest.raises(AttributeError):
            # Должна возникнуть ошибка при обращении к get_name() None
            burger.get_receipt()

    def test_get_receipt_no_ingredients(self):
        """Тест получения чека бургера без ингредиентов."""
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 200.0  # Добавляем цену для расчета
        burger.set_buns(mock_bun)

        receipt = burger.get_receipt()

        assert "(==== black bun ====)" in receipt
        assert "Price:" in receipt
        # Должны быть верхняя булка, нижняя булка и цена
        # (с пустой строкой между ними)
        lines = receipt.strip().split('\n')
        assert len(lines) == 4  # Верхняя булка, пустая строка, нижняя булка, цена
