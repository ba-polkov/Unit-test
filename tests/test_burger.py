import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    @pytest.fixture
    def mock_bun(self):
        bun = Mock()
        bun.get_name.return_value = "black bun"
        bun.get_price.return_value = 100
        return bun

    @pytest.fixture
    def mock_sauce(self):
        ingredient = Mock()
        ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        ingredient.get_name.return_value = "hot sauce"
        ingredient.get_price.return_value = 100
        return ingredient

    @pytest.fixture
    def mock_filling(self):
        ingredient = Mock()
        ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        ingredient.get_name.return_value = "cutlet"
        ingredient.get_price.return_value = 150
        return ingredient

    # Основные тесты
    def test_set_buns_sets_bun_reference(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun is mock_bun

    def test_add_sauce_increases_count(self, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        assert len(burger.ingredients) == 1

    def test_add_filling_increases_count(self, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_filling)
        assert len(burger.ingredients) == 1

    def test_remove_ingredient_works(self, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_price_with_sauce(self, mock_bun, mock_sauce):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        assert burger.get_price() == 300

    def test_price_with_filling(self, mock_bun, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_filling)
        assert burger.get_price() == 350

    # Тесты чека
    def test_receipt_contains_bun_name(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert "black bun" in burger.get_receipt()

    def test_receipt_contains_sauce(self, mock_bun, mock_sauce):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        assert "hot sauce" in burger.get_receipt()

    def test_receipt_contains_filling(self, mock_bun, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_filling)
        assert "cutlet" in burger.get_receipt()
