from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
import pytest
from ingredient_types import *
from data import *
from unittest.mock import Mock
from praktikum.database import *


class TestBurger:
    # тест на добавляние ингредиент соус или начинку
    @pytest.mark.parametrize(
        "_type,name,price",
        [
            (INGREDIENT_TYPE_SAUCE, name_sause, price_sause),
            (INGREDIENT_TYPE_FILLING, name_filling, price_filling),
        ],
    )
    def test_ingredient(self, burger: Burger, _type, name, price):
        ingredient = Ingredient(_type, name, price)
        burger.add_ingredient(ingredient)
        assert (
            ingredient in burger.ingredients
            and len(burger.ingredients) == 1
            and burger.ingredients[0].get_name() == name
        )

    # тест на удаление соуса из ингредиентов
    def test_delete_ingredient(self, burger: Burger):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name_sause, price_sause)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert ingredient not in burger.ingredients and len(burger.ingredients) == 0

    # тест на проверку цены бургера
    def test_get_burger_price(self, burger, bun_mock, ingredient_mock):
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        assert burger.get_price() == 300

    # тест на проверку перемещение ингридиента
    def test_move_ingredient(self, burger: Burger):
        ingredient_sause = Ingredient(INGREDIENT_TYPE_SAUCE, name_sause, price_sause)
        ingredient_filling = Ingredient(
            INGREDIENT_TYPE_FILLING, name_filling, price_filling
        )
        burger.add_ingredient(ingredient_sause)
        burger.add_ingredient(ingredient_filling)
        burger.move_ingredient(1, 0)
        assert (
            burger.ingredients[0].get_name() == name_filling
            and burger.ingredients[1].get_name() == name_sause
            and len(burger.ingredients) == 2
        )

    # проверяем получение чека
    def test_get_receipt(self, burger, bun_mock, ingredient_mock):
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)

        # Ожидаемый текст рецепта
        expected_receipt = """(==== black bun ====)
= sauce sour cream =
(==== black bun ====)

Price: 300"""

        # реальный результат
        actual_receipt = burger.get_receipt()

        # Сравниваем
        assert actual_receipt == expected_receipt
