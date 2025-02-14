import pytest
from unittest.mock import MagicMock
from praktikum.ingredient import Ingredient
from data import Data


def test_set_buns(burger):
    assert burger.bun.get_name() == Data.BUNS[0][0]
    assert burger.bun.get_price() == Data.BUNS[0][1]


@pytest.mark.parametrize("ingredient_type, ingredient_name, price", Data.INGREDIENTS)
def test_add_ingredient(burger, ingredient_type, ingredient_name, price):
    ingredient = MagicMock(spec=Ingredient)
    ingredient.get_name.return_value = ingredient_name
    ingredient.get_price.return_value = price
    ingredient.get_type.return_value = ingredient_type  # Устанавливаем тип ингредиента

    # Добавляем ингредиент в бургер
    burger.add_ingredient(ingredient)

    # Проверяем, что ингредиент добавлен
    assert len(burger.ingredients) == 1
    assert burger.ingredients[0].get_name() == ingredient_name
    assert burger.ingredients[0].get_price() == price
    assert burger.ingredients[0].get_type() == ingredient_type  # Проверяем тип ингредиента


def test_move_ingredient(burger):
    # Добавляем два ингредиента
    ingredient1_type, ingredient1_name, ingredient1_price = Data.INGREDIENTS[0]  # hot sauce, 100, SAUCE
    ingredient2_type, ingredient2_name, ingredient2_price = Data.INGREDIENTS[1]  # cutlet, 200, FILLING
    ingredient1 = MagicMock(spec=Ingredient)
    ingredient2 = MagicMock(spec=Ingredient)
    ingredient1.get_name.return_value = ingredient1_name
    ingredient1.get_price.return_value = ingredient1_price
    ingredient1.get_type.return_value = ingredient1_type
    ingredient2.get_name.return_value = ingredient2_name
    ingredient2.get_price.return_value = ingredient2_price
    ingredient2.get_type.return_value = ingredient2_type

    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)

    # Перемещаем ингредиенты
    burger.move_ingredient(0, 1)

    # Проверяем, что ингредиенты перемещены
    assert burger.ingredients[0].get_name() == ingredient2_name
    assert burger.ingredients[1].get_name() == ingredient1_name


def test_remove_ingredient(burger):
    # Добавляем ингредиент
    ingredient_type, ingredient_name, price = Data.INGREDIENTS[1]
    ingredient = MagicMock(spec=Ingredient)
    ingredient.get_name.return_value = ingredient_name
    ingredient.get_price.return_value = price
    ingredient.get_type.return_value = ingredient_type
    burger.add_ingredient(ingredient)

    # Удаляем ингредиент
    burger.remove_ingredient(0)

    # Проверяем, что ингредиент удалён
    assert len(burger.ingredients) == 0


def test_get_price_with_ingredient(burger):
    ingredient_type, ingredient_name, price = Data.INGREDIENTS[1]
    ingredient = MagicMock(spec=Ingredient)
    ingredient.get_price.return_value = price
    ingredient.get_type.return_value = ingredient_type
    burger.add_ingredient(ingredient)

    # Проверяем общую цену
    expected_price = Data.BUNS[0][1] * 2 + price
    assert burger.get_price() == expected_price


def test_get_price_without_ingredient(burger):
    # Проверяем цену только с булочкой
    assert burger.get_price() == Data.BUNS[0][1] * 2


def test_get_receipt(burger):
    # Создаем и настраиваем ингредиенты
    ingredient1_type, ingredient1_name, ingredient1_price = Data.INGREDIENTS[0]
    ingredient2_type, ingredient2_name, ingredient2_price = Data.INGREDIENTS[1]

    ingredient1 = MagicMock(spec=Ingredient)
    ingredient1.get_name.return_value = ingredient1_name
    ingredient1.get_price.return_value = ingredient1_price
    ingredient1.get_type.return_value = ingredient1_type

    ingredient2 = MagicMock(spec=Ingredient)
    ingredient2.get_name.return_value = ingredient2_name
    ingredient2.get_price.return_value = ingredient2_price
    ingredient2.get_type.return_value = ingredient2_type

    # Добавляем ингредиенты в бургер
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)

    # Получаем чек
    receipt = burger.get_receipt()

    # Ожидаемый результат
    expected_receipt = (
        f'(==== {Data.BUNS[0][0]} ====)\n'
        f'= {Data.INGREDIENTS[0][0].lower()} {Data.INGREDIENTS[0][1]} =\n'
        f'= {Data.INGREDIENTS[1][0].lower()} {Data.INGREDIENTS[1][1]} =\n'
        f'(==== {Data.BUNS[0][0]} ====)\n'

        f'Price: {burger.get_price()}'
    )

    # Проверяем, что полученный чек соответствует ожидаемому
    assert receipt == expected_receipt