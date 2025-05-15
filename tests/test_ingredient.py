import sys

import pytest

from praktikum.ingredient import Ingredient

class TestIngredient:
    test_name = ['Чёрная Дырка', '', '1',
                 'Cosmic MegaBurger Bun Featuring Nanostructured Dough Matrix, '
                 'Probiotic Enrichment, and Galactic Spectrum of Vitamins',
                 '*', '{Nebula_Stars}']

    test_price = [1000, 1, 10.50, 0, -1, sys.maxsize]

    test_ingredient_type = ['test_FILLING', '', '0', 'Всеобъемлющая Булочка для Бургера «Млечный Путь» с Наноструктурированным Тестом, Звёздными Специями и Межгалактическим Обогащением Вкуса']

    @pytest.mark.parametrize('name', test_name)
    def test_ingredient_name_is_set(self, name):
        ingredient = Ingredient('SAUCE', name, 100)

        assert ingredient.name == name

    @pytest.mark.parametrize('price', test_price)
    def test_ingredient_price_is_set(self, price):
        ingredient = Ingredient('SAUCE','Galaxy Bun', price)

        assert ingredient.price == price

    @pytest.mark.parametrize('ingredient_type', test_ingredient_type)
    def test_ingredient_type_is_set(self, ingredient_type):
        ingredient = Ingredient(ingredient_type,'Galaxy Bun', 100)

        assert ingredient.type == ingredient_type

    @pytest.mark.parametrize('name', test_name)
    def test_get_ingredient_name_return_name(self, name):
        ingredient = Ingredient('SAUCE', name, 100)

        assert ingredient.get_name() == name

    @pytest.mark.parametrize('price', test_price)
    def test_get_ingredient_price_return_price(self, price):
        ingredient = Ingredient('SAUCE','Galaxy Sauce', price)

        assert ingredient.get_price() == price

    @pytest.mark.parametrize('ingredient_type', test_ingredient_type)
    def test_get_ingredient_type_return_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type,'Galaxy Sauce', 100)

        assert ingredient.get_type() == ingredient_type