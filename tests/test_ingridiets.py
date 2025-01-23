import pytest
from praktikum.ingredient import Ingredient
from data import (
    INGREDIENT_NAME, INGREDIENT_TYPE, INGREDIENT_PRICE,
    INGREDIENT_NAME_NEXT, INGREDIENT_TYPE_NEXT, INGREDIENT_PRICE_NEXT
)

class TestIngredient:
    @pytest.mark.parametrize("name, type_, price", [
        (INGREDIENT_NAME, INGREDIENT_TYPE, INGREDIENT_PRICE),
        (INGREDIENT_NAME_NEXT, INGREDIENT_TYPE_NEXT, INGREDIENT_PRICE_NEXT),
        ('Бекон', 'Начинка', 40.00)
    ])
    def test_ingredient_initialization_name(self, name, type_, price):
        ingredient = Ingredient(type_, name, price)
        assert ingredient.name == name

    @pytest.mark.parametrize("name, type_, price", [
        (INGREDIENT_NAME, INGREDIENT_TYPE, INGREDIENT_PRICE),
        (INGREDIENT_NAME_NEXT, INGREDIENT_TYPE_NEXT, INGREDIENT_PRICE_NEXT),
        ('Бекон', 'Начинка', 40.00)
    ])
    def test_ingredient_initialization_type(self, name, type_, price):
        ingredient = Ingredient(type_, name, price)
        assert ingredient.type == type_

    @pytest.mark.parametrize("name, type_, price", [
        (INGREDIENT_NAME, INGREDIENT_TYPE, INGREDIENT_PRICE),
        (INGREDIENT_NAME_NEXT, INGREDIENT_TYPE_NEXT, INGREDIENT_PRICE_NEXT),
        ('Бекон', 'Начинка', 40.00)
    ])
    def test_ingredient_initialization_price(self, name, type_, price):
        ingredient = Ingredient(type_, name, price)
        assert ingredient.price == price

    # Тесты для проверки методов получения имени, типа и цены
    @pytest.mark.parametrize("name, type_, price", [
        (INGREDIENT_NAME, INGREDIENT_TYPE, INGREDIENT_PRICE),
        (INGREDIENT_NAME_NEXT, INGREDIENT_TYPE_NEXT, INGREDIENT_PRICE_NEXT),
        ('Бекон', 'Начинка', 40.00)
    ])
    def test_ingredient_get_name(self, name, type_, price):
        ingredient = Ingredient(type_, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("name, type_, price", [
        (INGREDIENT_NAME, INGREDIENT_TYPE, INGREDIENT_PRICE),
        (INGREDIENT_NAME_NEXT, INGREDIENT_TYPE_NEXT, INGREDIENT_PRICE_NEXT),
        ('Бекон', 'Начинка', 40.00)
    ])
    def test_ingredient_get_type(self, name, type_, price):
        ingredient = Ingredient(type_, name, price)
        assert ingredient.get_type() == type_

    @pytest.mark.parametrize("name, type_, price", [
        (INGREDIENT_NAME, INGREDIENT_TYPE, INGREDIENT_PRICE),
        (INGREDIENT_NAME_NEXT, INGREDIENT_TYPE_NEXT, INGREDIENT_PRICE_NEXT),
        ('Бекон', 'Начинка', 40.00)
    ])
    def test_ingredient_get_price(self, name, type_, price):
        ingredient = Ingredient(type_, name, price)
        assert ingredient.get_price() == price


