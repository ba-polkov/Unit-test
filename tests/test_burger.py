import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient

from .data import BUNS, INGREDIENTS


class TestBurger:

    def test_set_buns_and_get_price(self):
        burger = Burger()
        bun = BUNS[0]
        burger.set_buns(bun)
        # Проверка базовой цены (только булки)
        assert burger.get_price() == bun.get_price() * 2

    def test_add_ingredient(self):
        burger = Burger()
        burger.set_buns(BUNS[0])
        ingredient = INGREDIENTS[0]
        burger.add_ingredient(ingredient)
        # Проверка внутреннего состояния
        assert burger.ingredients == [ingredient]

    def test_remove_ingredient(self):
        burger = Burger()
        burger.set_buns(BUNS[0])
        ingredient = INGREDIENTS[0]
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        # Проверка, что список пуст
        assert burger.ingredients == []

    def test_move_ingredient(self):
        burger = Burger()
        burger.set_buns(BUNS[0])
        i1 = INGREDIENTS[0]
        i2 = INGREDIENTS[2]
        burger.add_ingredient(i1)
        burger.add_ingredient(i2)
        burger.move_ingredient(0, 1)
        # Проверка измененного порядка
        assert burger.ingredients == [i2, i1]

    def test_get_price_with_multiple_ingredients(self):
        burger = Burger()
        bun = BUNS[0]
        burger.set_buns(bun)
        total = bun.get_price() * 2
        for ing in INGREDIENTS[:3]:
            burger.add_ingredient(ing)
            total += ing.get_price()
        # Проверка итоговой цены
        assert burger.get_price() == total

    def test_get_receipt_full_match(self):
        burger = Burger()
        bun = BUNS[0]
        burger.set_buns(bun)
        ingredients = INGREDIENTS[:2]
        for ing in ingredients:
            burger.add_ingredient(ing)
        receipt = burger.get_receipt()
        expected_lines = [
            f'(==== {bun.get_name()} ====)',
            f'= {ingredients[0].get_type().lower()} {ingredients[0].get_name()} =',
            f'= {ingredients[1].get_type().lower()} {ingredients[1].get_name()} =',
            f'(==== {bun.get_name()} ====)\n',
            f'Price: {burger.get_price()}'
        ]
        expected_receipt = '\n'.join(expected_lines)
        # Проверка чека с ингредиентами
        assert receipt == expected_receipt

    # Добавлен для полного покрытия: Проверка чека без ингредиентов
    def test_get_receipt_without_ingredients(self):
        burger = Burger()
        bun = BUNS[1]
        burger.set_buns(bun)

        expected_lines = [
            f'(==== {bun.get_name()} ====)',
            f'(==== {bun.get_name()} ====)\n',
            f'Price: {burger.get_price()}'
        ]
        expected_receipt = '\n'.join(expected_lines)

        assert burger.get_receipt() == expected_receipt

    # Добавлен для демонстрации: Тест на исключение, если нет булок при печати чека
    def test_get_receipt_raises_error_without_buns(self):
        burger = Burger()
        # Ожидаем ошибку ValueError, которую мы добавили в Burger.get_receipt()
        with pytest.raises(ValueError):
            burger.get_receipt()