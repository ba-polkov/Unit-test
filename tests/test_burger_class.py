from typing import List
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
import pytest


class TestBurger:
    def test_set_buns_for_burger(self):
        burger = Burger()
        bun = Bun('Булочка с кунжутом', 84)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient_in_burger(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус сладкий', 41)
        burger.add_ingredient(ingredient)
        assert burger.ingredients[0] == ingredient

    @pytest.mark.parametrize(
        'ingredient_index',
        [
            0,
            1
        ]
    )
    def test_remove_ingredient_in_burger(self, ingredient_index):
        burger = Burger()
        ingredients = [
            Ingredient(INGREDIENT_TYPE_FILLING, 'Начинка сладкая', 41),
            Ingredient(INGREDIENT_TYPE_FILLING, 'Начинка острая', 41)
        ]
        for ingredient in ingredients[::-1]:
            burger.add_ingredient(ingredient)

        burger.remove_ingredient(ingredient_index)
        assert len(burger.ingredients) == 1
        assert ingredients[ingredient_index] == burger.ingredients[0]

    @pytest.mark.parametrize(
        'ingredient_index,ingredient_new_index',
        [
            [0, 1],
            [1, 2],
            [2, 0],
            [1, 0],
            [2, 1],
            [0, 2]
        ]
    )
    def test_move_ingredient_in_burger(self, ingredient_index, ingredient_new_index):
        burger = Burger()
        ingredients = [
            Ingredient(INGREDIENT_TYPE_FILLING, 'Начинка сладкая', 41),
            Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус сладкий', 41),
            Ingredient(INGREDIENT_TYPE_FILLING, 'Начинка острая', 41)
        ]

        for ingredient in ingredients:
            burger.add_ingredient(ingredient)

        burger.move_ingredient(ingredient_index, ingredient_new_index)
        assert len(burger.ingredients) == 3
        assert ingredients[ingredient_index] == burger.ingredients[ingredient_new_index]

    def test_get_price_for_burger(self):
        burger = Burger()
        bun = Bun('Булочка с кунжутом', 10)
        ingredient_1 = Ingredient(INGREDIENT_TYPE_FILLING, 'Начинка новая 1', 25)
        ingredient_2 = Ingredient(INGREDIENT_TYPE_FILLING, 'Начинка новая 2', 25)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        assert burger.get_price() == 70

    def test_get_receipt_for_burger(self):
        burger = Burger()
        bun = Bun('Булочка с кунжутом', 10)
        ingredient_1 = Ingredient(INGREDIENT_TYPE_FILLING, 'Начинка новая 1', 25)
        ingredient_2 = Ingredient(INGREDIENT_TYPE_FILLING, 'Начинка новая 2', 25)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)

        receipt: List[str] = [f'(==== {bun.get_name()} ====)']
        receipt.append(f'= {str(ingredient_1.get_type()).lower()} {ingredient_1.get_name()} =')
        receipt.append(f'= {str(ingredient_2.get_type()).lower()} {ingredient_2.get_name()} =')
        receipt.append(f'(==== {bun.get_name()} ====)\n')
        receipt.append(f'Price: {burger.get_price()}')

        receipt = "\n".join(receipt)

        assert receipt == burger.get_receipt()
