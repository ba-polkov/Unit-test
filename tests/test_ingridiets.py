import pytest
from praktikum.ingredient import Ingredient
from data import TestData

class TestIngredient:
    @pytest.mark.parametrize("name, type_, price", [
        (TestData.INGREDIENT_NAME, TestData.INGREDIENT_TYPE, TestData.INGREDIENT_PRICE),
        (TestData.INGREDIENT_NAME_NEXT, TestData.INGREDIENT_TYPE_NEXT, TestData.INGREDIENT_PRICE_NEXT),
        ('Бекон', 'Начинка', 40.00)
    ])
    def test_ingredient_initialization_name(self, name, type_, price):
        ingredient = Ingredient(type_, name, price)
        assert ingredient.name == name

    @pytest.mark.parametrize("name, type_, price", [
        (TestData.INGREDIENT_NAME, TestData.INGREDIENT_TYPE, TestData.INGREDIENT_PRICE),
        (TestData.INGREDIENT_NAME_NEXT, TestData.INGREDIENT_TYPE_NEXT, TestData.INGREDIENT_PRICE_NEXT),
        ('Бекон', 'Начинка', 40.00)
    ])
    def test_ingredient_initialization_type(self, name, type_, price):
        ingredient = Ingredient(type_, name, price)
        assert ingredient.type == type_

    @pytest.mark.parametrize("name, type_, price", [
        (TestData.INGREDIENT_NAME, TestData.INGREDIENT_TYPE, TestData.INGREDIENT_PRICE),
        (TestData.INGREDIENT_NAME_NEXT, TestData.INGREDIENT_TYPE_NEXT, TestData.INGREDIENT_PRICE_NEXT),
        ('Бекон', 'Начинка', 40.00)
    ])
    def test_ingredient_initialization_price(self, name, type_, price):
        ingredient = Ingredient(type_, name, price)
        assert ingredient.price == price

    # Тесты для проверки методов получения имени, типа и цены
    @pytest.mark.parametrize("name, type_, price", [
        (TestData.INGREDIENT_NAME, TestData.INGREDIENT_TYPE, TestData.INGREDIENT_PRICE),
        (TestData.INGREDIENT_NAME_NEXT, TestData.INGREDIENT_TYPE_NEXT, TestData.INGREDIENT_PRICE_NEXT),
        ('Бекон', 'Начинка', 40.00)
    ])
    def test_ingredient_get_name(self, name, type_, price):
        ingredient = Ingredient(type_, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("name, type_, price", [
        (TestData.INGREDIENT_NAME, TestData.INGREDIENT_TYPE, TestData.INGREDIENT_PRICE),
        (TestData.INGREDIENT_NAME_NEXT, TestData.INGREDIENT_TYPE_NEXT, TestData.INGREDIENT_PRICE_NEXT),
        ('Бекон', 'Начинка', 40.00)
    ])
    def test_ingredient_get_type(self, name, type_, price):
        ingredient = Ingredient(type_, name, price)
        assert ingredient.get_type() == type_

    @pytest.mark.parametrize("name, type_, price", [
        (TestData.INGREDIENT_NAME, TestData.INGREDIENT_TYPE, TestData.INGREDIENT_PRICE),
        (TestData.INGREDIENT_NAME_NEXT, TestData.INGREDIENT_TYPE_NEXT, TestData.INGREDIENT_PRICE_NEXT),
        ('Бекон', 'Начинка', 40.00)
    ])
    def test_ingredient_get_price(self, name, type_, price):
        ingredient = Ingredient(type_, name, price)
        assert ingredient.get_price() == price



