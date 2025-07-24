import pytest
from unittest.mock import MagicMock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

class TestBurger:
    @pytest.fixture
    def mock_bun(self):
        bun = MagicMock()
        bun.get_name.return_value = "black bun"
        bun.get_price.return_value = 100
        return bun

    @pytest.fixture
    def mock_ingredient(self):
        ingredient = MagicMock()
        ingredient.get_type.return_value = "sauce"
        ingredient.get_name.return_value = "hot sauce"
        ingredient.get_price.return_value = 50
        return ingredient

    # Тесты для set_buns()
    def test_set_buns_sets_bun_correctly(self, mock_bun):
        """Проверяем, что set_buns() устанавливает булочку"""
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    # Тесты для add_ingredient()
    def test_add_ingredient_adds_to_list(self, mock_ingredient):
        """Проверяем, что add_ingredient() добавляет ингредиент"""
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    # Тесты для remove_ingredient()
    def test_remove_ingredient_removes_correctly(self, mock_ingredient):
        """Проверяем, что remove_ingredient() удаляет по индексу"""
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    # Тесты для move_ingredient()
    def test_move_ingredient_changes_position(self, mock_ingredient):
        """Проверяем, что move_ingredient() перемещает ингредиент"""
        burger = Burger()
        second_ingredient = MagicMock()
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(second_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == mock_ingredient

    # Тесты для get_price()
    def test_get_price_calculates_correctly(self, mock_bun, mock_ingredient):
        """Проверяем расчет цены с булочкой и ингредиентами"""
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == 250  # (100*2) + 50

    # Тесты для get_receipt()
    def test_get_receipt_includes_bun_name(self, mock_bun):
        """Проверяем, что чек содержит название булочки"""
        burger = Burger()
        burger.set_buns(mock_bun)
        assert "black bun" in burger.get_receipt()