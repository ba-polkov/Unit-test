import pytest

from unittest.mock import Mock

from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.bun import Bun


class TestBurger:
    """Тесты для класса Burger.
    Проверяется корректность работы всех методов:
    инициализация, установка булочки, добавление/удаление/перемещение ингредиентов,
    расчёт цены и формирование чека.
    """
    def test_burger_initialization(self):
        """Проверяем, что при создании бургер не содержит булочку и ингредиенты."""
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_bun(self):
        """Проверяем, что метод set_buns устанавливает переданную булочку."""
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        burger.set_buns(mock_bun)
        assert burger.bun is mock_bun

    def test_add_ingredient(self):
        """Проверяем, что метод add_ingredient добавляет ингредиент в список."""
        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    def test_remove_ingredient_by_index(self):
        """Проверяем, что метод remove_ingredient удаляет ингредиент по индексу."""
        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert mock_ingredient not in burger.ingredients

    def test_move_ingredient_from_to_index(self):
        """Проверяем, что метод move_ingredient перемещает ингредиент в списке по индексу."""
        burger = Burger()
        mock_ing1 = Mock(spec=Ingredient)
        mock_ing2 = Mock(spec=Ingredient)
        burger.add_ingredient(mock_ing1)
        burger.add_ingredient(mock_ing2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_ing2, mock_ing1]


    @pytest.mark.parametrize('bun_price, ingredients_price, expected_price',
                      [(100, [100, 100], 400),
                       (200, [200, 200], 800),
                       (300, [300, 300], 1200),
                       (200, [300, 200], 900),
                       (300, [300, 100], 1000)])
    def test_get_price_burger(self, bun_price, ingredients_price, expected_price):
        """Проверяем, что метод get_price корректно рассчитывает итоговую цену.
        Цена = 2 * цена булочки + сумма цен ингредиентов.
        Тест параметризован для проверки разных комбинаций.
        """
        burger = Burger()

        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        for price in ingredients_price:
            mock_ing = Mock(spec=Ingredient)
            mock_ing.get_price.return_value = price
            burger.add_ingredient(mock_ing)

        assert burger.get_price() == expected_price


    @pytest.mark.parametrize('bun_name, bun_price, ingredients_data, expected_parts',
                             [('black bun', 100, [('FILLING', 'cutlet', 100)], ['(==== black bun ====)',
                                                                           '= filling cutlet =',
                                                                           'Price: 300']),
                              ('white bun', 200, [('SAUCE', 'sour cream', 200)], ['(==== white bun ====)',
                                                                             '= sauce sour cream =',
                                                                             'Price: 600']),
                              ('red bun', 300, [('FILLING', 'sausage', 300), ('SAUCE', 'chili sauce', 300)], ['(==== red bun ====)',
                                                                                                         '= filling sausage =',
                                                                                                         '= sauce chili sauce =',
                                                                                                         'Price: 1200'])])
    def test_get_receipt(self, bun_name, bun_price, ingredients_data, expected_parts):
        """Проверяем, что метод get_receipt формирует корректный чек.
        В чеке должны быть:
        - Название булочки (сверху и снизу)
        - Строки с типом и названием каждого ингредиента
        - Итоговая цена
        Тест параметризован для проверки разных комбинаций.
        """
        burger = Burger()
        bun_mock = Mock(spec=Bun)
        bun_mock.get_price.return_value = bun_price
        bun_mock.get_name.return_value = bun_name
        burger.set_buns(bun_mock)

        for ing_data in ingredients_data:
            mock_ing = Mock(spec=Ingredient)
            mock_ing.get_type.return_value = ing_data[0]
            mock_ing.get_name.return_value = ing_data[1]
            mock_ing.get_price.return_value = ing_data[2]
            burger.add_ingredient(mock_ing)

        receipt = burger.get_receipt()
        for part in expected_parts:
            assert part in receipt












