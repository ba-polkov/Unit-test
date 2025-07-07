import pytest
from unittest.mock import Mock, patch
import sys
import os

# Добавляем корень проекта в PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Теперь импортируем модули
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestBurger:
    """Тест-кейсы для класса Burger"""
    
    @pytest.fixture
    def burger(self):
        return Burger()

    @pytest.fixture
    def mock_bun(self):
        bun = Mock()
        bun.get_name.return_value = "Краторная булка"
        bun.get_price.return_value = 100
        return bun

    @pytest.fixture
    def mock_ingredient(self):
        ingredient = Mock()
        ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        ingredient.get_name.return_value = "Сырный соус"
        ingredient.get_price.return_value = 50
        return ingredient

    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_ingredient):
        initial_count = len(burger.ingredients)
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == initial_count + 1

    # Тест-кейс 1: Проверка установки булочек
    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    # Тест-кейс 2: Проверка добавления ингредиента
    def test_add_ingredient(self, burger, mock_ingredient):
        initial_count = len(burger.ingredients)
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == initial_count + 1

    # Тест-кейс 3: Проверка удаления ингредиента
    def test_remove_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        initial_count = len(burger.ingredients)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == initial_count - 1

    # Тест-кейс 4: Проверка перемещения ингредиента
    def test_move_ingredient(self, burger):
        ing1 = Mock()
        ing1.get_name.return_value = "Соус"
        ing2 = Mock()
        ing2.get_name.return_value = "Начинка"
        
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.move_ingredient(1, 0)
        
        assert burger.ingredients[0].get_name() == "Начинка"
        assert burger.ingredients[1].get_name() == "Соус"

    # Тест-кейс 5: Проверка расчета цены
    def test_get_price(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        
        # Цена: (100 * 2) + (50 * 2) = 300
        assert burger.get_price() == 300

    # Тест-кейс 6: Проверка получения чека
    def test_get_receipt(self, burger, mock_bun, mock_ingredient):
        mock_bun.get_name.return_value = "Белая булка"
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient.get_name.return_value = "Котлета"
        
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        
        receipt = burger.get_receipt()
        
        assert "(==== Белая булка ====)" in receipt
        assert "= filling Котлета =" in receipt
        assert "Price: 250" in receipt

    # Тест-кейс 7: Проверка с пустым бургером
    def test_empty_burger_price(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.get_price() == 200  # Только булочки

    # Тест-кейс 8: Параметризованный тест разных комбинаций ингредиентов
    @pytest.mark.parametrize("ing_count,expected_price", [
        (0, 200),  # Только булочки
        (1, 250),  # Булочки + 1 ингредиент
        (3, 350),  # Булочки + 3 ингредиента
    ])
    def test_burger_with_different_ingredients_count(
        self, burger, mock_bun, mock_ingredient, ing_count, expected_price
    ):
        burger.set_buns(mock_bun)
        for _ in range(ing_count):
            burger.add_ingredient(mock_ingredient)
        
        assert burger.get_price() == expected_price