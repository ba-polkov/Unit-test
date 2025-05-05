# test_burger.py

import pytest
from Diplom_1.bun import Bun
from Diplom_1.ingredient import Ingredient


class TestBurger:
    # --- Тест для set_buns ---
    def test_set_buns(self, empty_burger):
        """Проверка корректности установки булок в бургере"""
        bun = Bun("Краторная булка N-200i", 1255)
        empty_burger.set_buns(bun)
        assert empty_burger.bun == bun

    # --- Тест для add_ingredient ---
    @pytest.mark.parametrize("ingredient", [
        Ingredient("SAUCE", "Соус фирменный Space Sauce", 80),
        Ingredient("FILLING", "Биокотлета из марсианской Магнолии", 424)
    ], ids=["sauce", "filling"])
    def test_add_ingredient(self, empty_burger, ingredient):
        """Проверка добавления разных типов ингредиентов"""
        empty_burger.add_ingredient(ingredient)
        assert ingredient in empty_burger.ingredients

    def test_add_duplicate_ingredient(self, empty_burger):
        """Проверка на повторное добавление одинаковых ингредиентов"""
        ingredient = Ingredient("SAUCE", "Соус", 90)
        empty_burger.add_ingredient(ingredient)
        empty_burger.add_ingredient(ingredient)
        assert len(empty_burger.ingredients) == 2

    # --- Тест для remove_ingredient ---
    def test_remove_ingredient(self, prepared_burger):
        """Проверка удаления ингредиента по индексу"""
        initial_count = len(prepared_burger.ingredients)
        removed = prepared_burger.ingredients[0]
        prepared_burger.remove_ingredient(0)
        assert len(prepared_burger.ingredients) == initial_count - 1
        assert removed not in prepared_burger.ingredients

    # --- Тесты для move_ingredient ---
    def test_move_ingredient(self, prepared_burger):
        """Проверка перемещения ингредиента на новую позицию"""
        first, second = prepared_burger.ingredients
        prepared_burger.move_ingredient(0, 1)
        assert prepared_burger.ingredients == [second, first]

    # --- Тесты для get_price ---
    @pytest.mark.parametrize("bun_price, ingr_prices, expected", [
        (988, [], 1976),
        (988, [90], 2066),
        (1255, [15, 88], 2613),
        (1255, [80, 424], 3014)
    ], ids=["only bun", "bun + sauce", "bun + cheap ingredients", "full burger"])
    def test_get_price(self, empty_burger, bun_price, ingr_prices, expected):
        """Проверка расчета цены для разных комбинаций булок и ингредиентов"""
        empty_burger.set_buns(Bun("Булка", bun_price))
        for price in ingr_prices:
            empty_burger.add_ingredient(Ingredient("FILLING", "Начинка", price))
        assert empty_burger.get_price() == expected

    def test_get_price_no_bun_raises_error(self, empty_burger):
        """Проверка вызова ошибки при расчете цены без булки"""
        with pytest.raises(AttributeError):
            empty_burger.get_price()

    # --- Тест для get_receipt ---
    @pytest.mark.parametrize("component", [
        "Краторная булка N-200i",
        "Соус фирменный Space Sauce",
        "Биокотлета из марсианской Магнолии",
        "Price: 3014"
    ], ids=["bun name", "sauce name", "filling name", "total price"])
    def test_receipt_contains_components(self, prepared_burger, component):
        """Проверяет наличие всех компонентов в чеке."""
        receipt = prepared_burger.get_receipt()
        assert component in receipt
        assert isinstance(receipt, str)